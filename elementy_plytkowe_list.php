<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `nazwa`, `ilosc_pin`, `plytka_id`, `pnazwa`, `urzadzenie_nazwa`, `miejsce_id`, `mnazwa`, `opis`, `zbiorcze`, ";
$query .= "`id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie`, `urzadzenie_rodzaj_id`, `urzadzenie_rodzaj_kod` FROM `ElementyPlytkoweView` WHERE 1";

$elementy = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    array_push($elementy, array(
        "id" => $row["id"],
        "nazwa" => $row["nazwa"],
        "plytka_id" => $row["plytka_id"],
        "plytka" => $row["pnazwa"],
        "urzadzenie" => $row["urzadzenie_nazwa"],
        "element_rodzaj_id" => $row["urzadzenie_rodzaj_id"],
        "miejsce_id" => $row["miejsce_id"],
        "miejsce_nazwa" => $row["mnazwa"],
        "ilosc_pin" => $row["ilosc_pin"],
        "pomieszczenie" => $row["pomieszczenie"],
        "pins" => array()
    ));
}

$miejscearray = array();
$query = "SELECT `id`, `nazwa`, `opis`, `zbiorcze`, `polaczenie`, `pomieszczenie` FROM `MiejsceView` WHERE 1";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $miejscearray[$row['id']] = array(
        "nazwa" => $row['nazwa'],
        "opis" => $row['opis'],
        "zbior" => $row['zbiorcze'],
        "polac" => $row['polaczenie'],
        "pomie" => $row['pomieszczenie'],
    );
}
$plytkiarray = array();
$query = "SELECT `id`, `nazwa`, `miejsce_id`, `mnazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, ";
$query.= "`polaczenie`, `pomieszczenie` FROM `PlytkaMiejsceView` WHERE 1";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $plytkiarray[$row['id']] = array(
        "plytka" => $row['nazwa'],
        "nazwa" => $row['mnazwa'],
        "pomie" => $row['pomieszczenie'],
    );
}

$rodzajarray = array();
$query = "SELECT `id`, `nazwa`  FROM `rodzaj_zakonczenia` WHERE `plytka` = 1";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $rodzajarray[$row['id']] = array(
        "nazwa" => $row['nazwa'],
    );
}


$opt = array(
    'elementy' => $elementy,
    'miejsce' => $miejscearray,
    'plytki' => $plytkiarray,
    'rodzaj' => $rodzajarray
);

echo json_encode($opt);
mysqli_close($con);


?>