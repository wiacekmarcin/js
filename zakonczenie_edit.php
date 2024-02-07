<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = db_connect();
mysqli_set_charset($con, "utf8");

$zid = $_GET["zid"];

$query = "SELECT `zid`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `przewod_id`, `miejsce_id`, ";
$query .= "`znazwa`, `zkod`, `mnazwa`, `mopis`, `zbiorcze`, `mkod`, `polaczenie`, `pomieszczenie`, `popis`, `ilosc_zyl` ";
$query .= "FROM `ZakonczePrzewodMiejsce` WHERE `zid` = $zid";
$result = mysqli_query($con, $query);
$row = mysqli_fetch_array($result);
$zakonczeniearray = array(
    "zid" => $row["zid"],
    "etykieta" => $row["etykieta"],
    "pmid" => $row["przewod_miejsce_id"],
    "rodzaj_zakonczenia" => $row["rodzaj_zakonczenia"],
    "przewod_id" => $row["przewod_id"],
    "znazwa" => $row["znazwa"],
    "zkod" => $row["zkod"],
    "mnazwa" => $row["mnazwa"],
    "mopis" => $row["mopis"],
    "zbiorcze" => $row["zbiorcze"],
    "mkod" => $row["mkod"],
    "polaczenie" => $row["polaczenie"],
    "pomieszczenie" => $row["pomieszczenie"],
    "popis" => $row["popis"],
    "ilosc_zyl" => $row["ilosc_zyl"],
);

$pid = $row["przewod_id"];
$query = "SELECT `id`, `kolor_id`, `przewod_id`, `opis`, `kolor`, `html` FROM `ZylaWidok` WHERE `przewod_id` = $pid";
$result = mysqli_query($con, $query);
$zyly = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zyly, array(
            'id' => $row['id'],
            'opis' => $row['opis'],
            'kolor' => $row['kolor'],
            'html' => $row['html']
    ));
}    
$query = "SELECT `id`, `nazwa`, `html` FROM `KolorView` WHERE 1";
$result = mysqli_query($con, $query);
$colors = array();
while($row = mysqli_fetch_array($result)) {
    array_push($colors, array(
            'id' => $row['id'],
            'kolor' => $row['nazwa'],
            'html' => $row['html']
    ));
}  

$opt = array(
    'zakonczenie' => $zakonczeniearray,
    'zyly' => $zyly,
    'kolory' => $colors,
);

echo json_encode($opt);
mysqli_close($con);

?>