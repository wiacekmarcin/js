<?php
// Wspólna obsługa bazy: połączenie, prepared statements, transakcje, odpowiedzi JSON.
require_once __DIR__ . "/database.php";

ini_set('display_errors', '0');
ini_set('log_errors', '1');
// Kompresja tylko, gdy nic jeszcze nie wyszło (inaczej odpowiedź byłaby pomieszana).
if (!headers_sent() && !ob_get_length()) {
    ini_set('zlib.output_compression', '1');
}
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
header("Content-Type: application/json; charset=UTF-8");

function db(): mysqli
{
    static $con = null;
    if ($con === null) {
        global $username, $password, $database, $host;
        $con = new mysqli($host ?? "127.0.0.1", $username, $password, $database);
        try {
            $con->set_charset("utf8mb4");
        } catch (mysqli_sql_exception $e) {
            // Starsze serwery MySQL/MariaDB nie znają utf8mb4.
            $con->set_charset("utf8");
        }
    }
    return $con;
}

function json_out($data, int $code = 200): void
{
    http_response_code($code);
    header("Content-Type: application/json; charset=UTF-8");
    echo json_encode($data, JSON_UNESCAPED_UNICODE);
    exit;
}

function fail(string $msg, int $code = 400): void
{
    json_out(["status" => "ERR", "error" => $msg], $code);
}

set_exception_handler(function (Throwable $e) {
    error_log("[przewody] " . $e->getMessage() . " @ " . $e->getFile() . ":" . $e->getLine());
    if ($e instanceof mysqli_sql_exception) {
        // Sam kod MySQL (np. 1045 = złe hasło, 2002 = brak serwera, 1146 = brak tabeli) nie ujawnia danych.
        json_out(["status" => "ERR", "error" => "Błąd bazy danych", "code" => $e->getCode()], 500);
    }
    fail($e->getMessage(), 500);
});

function q(string $sql, array $params = []): mysqli_stmt
{
    $stmt = db()->prepare($sql);
    if ($params) {
        $types = "";
        foreach ($params as $p) {
            $types .= is_int($p) ? "i" : (is_float($p) ? "d" : "s");
        }
        $stmt->bind_param($types, ...$params);
    }
    $stmt->execute();
    return $stmt;
}

// Zwracamy wartości jako stringi (jak dawne mysqli_query), bo szablony porównują np. z '0'/'1'.
function stringify_row(array $row): array
{
    foreach ($row as $k => $v) {
        if ($v !== null && !is_string($v)) {
            $row[$k] = (string)$v;
        }
    }
    return $row;
}

function q_all(string $sql, array $params = []): array
{
    return array_map('stringify_row', q($sql, $params)->get_result()->fetch_all(MYSQLI_ASSOC));
}

function q_one(string $sql, array $params = []): ?array
{
    $row = q($sql, $params)->get_result()->fetch_assoc();
    return $row ? stringify_row($row) : null;
}

function tx(callable $fn)
{
    $con = db();
    $con->begin_transaction();
    try {
        $res = $fn($con);
        $con->commit();
        return $res;
    } catch (Throwable $e) {
        $con->rollback();
        throw $e;
    }
}

function in_int(array $src, string $name, ?int $default = null): int
{
    // toparams() w JS wysyła brakujące pola jako "undefined"/"null".
    if (!isset($src[$name]) || in_array($src[$name], ['', 'undefined', 'null'], true)) {
        if ($default !== null) {
            return $default;
        }
        fail("Brak parametru: $name");
    }
    $v = filter_var($src[$name], FILTER_VALIDATE_INT);
    if ($v === false) {
        fail("Niepoprawna liczba: $name");
    }
    return $v;
}

function in_str(array $src, string $name, string $default = ''): string
{
    if (!isset($src[$name]) || in_array($src[$name], ['undefined', 'null'], true)) {
        return $default;
    }
    return trim((string)$src[$name]);
}

function in_bool(array $src, string $name): int
{
    $v = strtolower(in_str($src, $name));
    return in_array($v, ['1', 'true', 'on', 'yes'], true) ? 1 : 0;
}

function post_int(string $n, ?int $d = null): int { return in_int($_POST, $n, $d); }
function post_str(string $n, string $d = ''): string { return in_str($_POST, $n, $d); }
function post_bool(string $n): int { return in_bool($_POST, $n); }
function get_int(string $n, ?int $d = null): int { return in_int($_GET, $n, $d); }

function require_post(): void
{
    if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
        fail("Wymagana metoda POST", 405);
    }
}
