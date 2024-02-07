<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$pmid=$_GET["pmid"];

$con = db_connect();
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `nazwa`, `kod` FROM `rodzaj_zakonczenia` WHERE 1";
$result = mysqli_query($con, $query);
$rodzajzakonczeniaarray = array();
while($row = mysqli_fetch_array($result)) {
    array_push($rodzajzakonczeniaarray, array(
            'id' => $row['id'],
            'nazwa' => $row['nazwa'],
            'kod' => $row['kod'],
    ));
}    

$query = "SELECT `id`, `pid`, `mid`, `nazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, ";
$query .= "`kod`, `polaczenie`, `pomieszczenie`, `ppid`, `popis`, `ilosc_zyl` ";
$query .= "FROM `MiejscePrzewodView` WHERE `id` = " . $pmid;
$result = mysqli_query($con, $query);
$zakonczenie = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zakonczenie, array(
            'id' => $row['id'],
            'przewod' => $row['pid'],
            'miejsce' => $row['pomieszczenie'] . ":" . $row['nazwa'] ,
            'popis' => $row['popis'],
            'ilosc' => $row['ilosc_zyl']
    ));
} 

$opt = array(
    'rodzaj_zakonczenia' => $rodzajzakonczeniaarray,
    'zakonczenie' => $zakonczenie
);

echo json_encode($opt);
mysqli_close($con);

?>