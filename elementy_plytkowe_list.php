<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `nazwa`, `ilosc_pin`, `plytka_id`, `pnazwa`, `miejsce_id`, `mnazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, ";
$query .= "`kod`, `polaczenie`, `pomieszczenie` FROM `UrzadzeniaPlytkoweView` WHERE 1";

$urzadzenia = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    array_push($urzadzenia, array(
        "id" => $row["id"],
        "nazwa" => $row["nazwa"],
        "plytka_id" => $row["plytka_id"],
        "plytka" => $row["pnazwa"],
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

$opt = array(
    'urzadzenia' => $urzadzenia,
    'miejsce' => $miejscearray,
    'plytki' => $plytkiarray
);

echo json_encode($opt);
mysqli_close($con);


?>