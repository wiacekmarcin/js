<?php
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$zid=$_GET["zid"];

$query = "SELECT `zid`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `przewod_id`, ";
$query .= "`miejsce_id`, `znazwa`, `zkod`, `ilosc_pin`, `mnazwa`, `mopis`, `zbiorcze`, `mkod`, ";
$query .= "`polaczenie`, `pomieszczenie`, `popis`, `ilosc_zyl` ";
$query .= "FROM `ZakonczePrzewodMiejsce` WHERE `zid` = " . $zid;

$result = mysqli_query($con, $query);
$zakonczenie = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zakonczenie, array(
            'id' => $row['zid'],
            'przewod' => $row['przewod_id'],
            'etykieta' => $row['znazwa'] . ": ". $row['etykieta'],
            'zkod' => $row['zkod'],
            'miejsce' => $row['pomieszczenie'] . ":" . $row['mnazwa'] ,
            'popis' => $row['popis'],
            'ilosc' => $row['ilosc_zyl']
    ));
}

$query = "SELECT `id`, `zakonczenie_id`, `zyla_id`, `pos`, `opis` ";
$query .= "FROM `zakonczenie_zyly` WHERE `zakonczenie_id` = $zid";
$result = mysqli_query($con, $query);
$zakonczeniazyly = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zakonczeniazyly, array(
        'id' => $row['id'],
        'zyla_id' => $row['zyla_id'],
        'pos' => $row['pos'],
        'opis' => $row['opis'],
    ));
}

$query = "SELECT `ZylaWidok`.`id`, `ZylaWidok`.`kolor_id`, `ZylaWidok`.`przewod_id`, ";
$query .= "`ZylaWidok`.`opis`, `ZylaWidok`.`kolor`, `ZylaWidok`.`html`, `przewod_miejsce`.`id` AS `pmid`, ";
$query .= "`przewod_miejsce`.`miejsce_id` AS `mid`, `zakonczenie`.`id` AS `zid`, `zakonczenie`.`etykieta`, ";
$query .= " `zakonczenie`.`rodzaj_zakonczenia`, `zakonczenie`.`ilosc_pin` FROM `ZylaWidok` ";
$query .= "LEFT JOIN `przewod_miejsce` ON `przewod_miejsce`.`przewod_id` = `ZylaWidok`.`przewod_id` ";
$query .= "LEFT JOIN `zakonczenie` ON `zakonczenie`.`przewod_miejsce_id` = `przewod_miejsce`.`id` ";
$query .= "WHERE `zakonczenie`.`id` = $zid ";

$result = mysqli_query($con, $query);
$zyly = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zyly, array(
        'id' => $row['id'],
        'kolor_id' => $row['kolor_id'],
        'opis' => $row['opis'],
        'kolor' => $row['kolor'],
        'html' => $row['html'],
    ));
}



$opt = array(
    'zakonczenie' => $zakonczenie,
    "zyly" => $zyly,
    "zakonczeniaz_zyly" => $zakonczeniazyly,
);

echo json_encode($opt);
mysqli_close($con);
?>