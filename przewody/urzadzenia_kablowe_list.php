<?php
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = db_connect();
mysqli_set_charset($con, "utf8");

$query = "SELECT `zid`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `przewod_id`, `miejsce_id`, `znazwa`, `zkod`, ";
$query.= "`mnazwa`, `mopis`, `zbiorcze`, `mkod`, `polaczenie`, `pomieszczenie`, `popis`, `ilosc_zyl`, `ilosc_pin` ";
$query.= "FROM `ZakonczePrzewodMiejsce` WHERE 1 ORDER BY `etykieta`";
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
        "przewod_miejsce_id" => $row["przewod_miejsce_id"],
        'opis' => $row['popis'],
        "ilosc_zyl" => $row['ilosc_zyl'],
        "ilosc_pin" => $row['ilosc_pin'],
        "rodzaj_zakonczenia" => $row["rodzaj_zakonczenia"]
    ));
}

$rodzajarray = array();
$query = "SELECT `id`, `nazwa`  FROM `rodzaj_zakonczenia` WHERE `przewod` = 1";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $rodzajarray[$row['id']] = array(
        "nazwa" => $row['nazwa'],
    );
}

$przewodmiejscearray = array();
$query =  "SELECT `p`.`zid`, `p`.`etykieta`, `p`.`przewod_miejsce_id_zlacze`, `p`.`rodzaj_zakonczenia`, `p`.`przewod_id`, ";
$query .= "`p`.`miejsce_id`, `p`.`przewod_miejsce_id`, `p`.`nazwa`, `p`.`kod` ,";
$query .= "`m`.`nazwa`, `m`.`opis`, `m`.`zbiorcze`, `m`.`id_pomieszczenie`, `m`.`polaczenie`, `m`.`pomieszczenie` ";
$query .= "FROM `PrzewodMiejsceZakonczenieView` `p` ";
$query .= "LEFT JOIN `MiejsceView` `m` ON `m`.`id` = `p`.`miejsce_id` ";
$query .= "WHERE 1";

$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {

    $etykieta = $row["przewod_id"];
    if ($row["kod"]) {
        $etykieta = $etykieta . ' - ' . $row["kod"] . ":" . $row["etykieta"];
    }
    if ($row["zid"]) {
        $zid = $row["zid"];
    } else {
        $zid = "-". $row["przewod_miejsce_id"];
    }

    array_push($przewodmiejscearray, array(
        "zid" => $zid,
        "etykieta" => $etykieta,
        "przewod_miejsce_id" => $row["przewod_miejsce_id"],
        "zakonczenie_id" => $row["zid"],
        "miejsce" => $row["pomieszczenie"] . ":" . $row["nazwa"],
    ));
}

$query = "SELECT `id`, `zakonczenie_id`, `zyla_id`, `pos`, `opis` FROM `zakonczenie_zyly` WHERE 1";
$result = mysqli_query($con, $query);
$pins = array();
$prevuid = -1;
while($row = mysqli_fetch_array($result)) {
    $uid = $row["zakonczenie_id"];
    if ($uid != $prevuid) {
        $prevuid = $uid;
        $pins[$uid] = array();   
    }
    array_push($pins[$uid], array(
        'id' => $row['id'],
        'zyla_id' => $row['zyla_id'],
        'pos' => $row['pos'],
        'opis' => $row['opis']   
    ));
}


$opt = array(
    'urzadzenia' => $urzadzenia,
    "rodzaj" => $rodzajarray,
    "przewodmiejsce" => $przewodmiejscearray,
    "pins" => $pins

);

echo json_encode($opt);
mysqli_close($con);
?>