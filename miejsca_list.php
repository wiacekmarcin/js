<?php
require_once "db.php";

$pid = get_int('pid', 0);

$pomieszczenia = q_all("SELECT `id`, `nazwa` FROM `pomieszczenie` ORDER BY `nazwa`");

$cols = "`id`, `nazwa`, `kod`, `opis`, `zbiorcze`, `polaczenie`, `pomieszczenie`, `id_pomieszczenie`";
if ($pid > 0) {
    $miejsca = q_all("SELECT $cols FROM `MiejsceView` WHERE `id_pomieszczenie` = ? ORDER BY `nazwa`", [$pid]);
} elseif ($pid == 0) {
    $miejsca = q_all("SELECT $cols FROM `MiejsceView` ORDER BY `nazwa`");
} elseif ($pid == -1) {
    $miejsca = q_all("SELECT $cols FROM `MiejsceView` WHERE `zbiorcze` = 1 ORDER BY `nazwa`");
} elseif ($pid == -2) {
    $miejsca = q_all("SELECT $cols FROM `MiejsceView` WHERE `polaczenie` = 1 ORDER BY `nazwa`");
} else {
    $miejsca = [];
}

$przewody = [];
foreach (q_all("SELECT DISTINCT `przewod_id`, `miejsce_id` FROM `przewod_miejsce` ORDER BY `miejsce_id`, `przewod_id`") as $row) {
    $przewody[$row["miejsce_id"]][] = $row["przewod_id"];
}

$zakonczenia = [];
$rows = q_all("SELECT DISTINCT `etykieta`, `rodzaj_zakonczenia`, `miejsce_id` FROM `ZakonczenieView` ORDER BY `miejsce_id`, `rodzaj_zakonczenia`");
foreach ($rows as $row) {
    $mid = $row["miejsce_id"];
    if (!isset($zakonczenia[$mid])) {
        $zakonczenia[$mid] = array_fill_keys(array_map('strval', range(1, 9)), []);
    }
    $zakonczenia[$mid][$row["rodzaj_zakonczenia"]][] = $row["etykieta"];
}

$rodzaj = array_column(q_all("SELECT `id`, `nazwa` FROM `rodzaj_zakonczenia`"), "nazwa", "id");

json_out([
    "miejsca" => $miejsca,
    "pomieszczenia" => $pomieszczenia,
    "przewody" => $przewody,
    "zakonczenia" => $zakonczenia,
    "rodzaj" => $rodzaj,
]);
