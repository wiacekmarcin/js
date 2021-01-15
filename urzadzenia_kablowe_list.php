<?php
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `zid`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `przewod_id`, `miejsce_id`, `znazwa`, `zkod`, ";
$query.= "`mnazwa`, `mopis`, `zbiorcze`, `mkod`, `polaczenie`, `pomieszczenie`, `popis`, `ilosc_zyl`, `ilosc_pin` ";
$query.= "FROM `ZakonczePrzewodMiejsce` WHERE 1 ORDER BY `mnazwa`, `etykieta`";
$result = mysqli_query($con, $query);

$urzadzenia = array();
while($row = mysqli_fetch_array($result)) {
    array_push($urzadzenia , array(
        'id' => $row['zid'], 
        'nazwa' => $row['etykieta'],
        'przewod_id' => $row['przewod_id'],
        'urzadzenie' => $row['znazwa'],
        'zkod' => $row['zkod'],
        'miejsce' => $row['mnazwa'],
        'pomieszczenie' => $row['pomieszczenie'],
        'opis' => $row['popis'],
        "ilosc_zyl" => $row['ilosc_zyl'],
        "ilosc_pin" => $row['ilosc_pin'],
    ));
}


$opt = array(
    'urzadzenia' => $urzadzenia,
);

echo json_encode($opt);
mysqli_close($con);
?>