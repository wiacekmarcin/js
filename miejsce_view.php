<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con, "utf8");

$mid = -1;

if (isset($_GET['mid'])) {
    $mid = $_GET['mid'];
}
$query = "SELECT `id`, `nazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` ";
$query .=" FROM `MiejsceView` WHERE `id` = " . $mid;

$result = mysqli_query($con, $query);
$miejsce = array();
while($row = mysqli_fetch_array($result)) {
    $miejsce = array(
        "id" => $row['id'],
        "nazwa" => $row['nazwa'],
        "opis" => $row['opis'],
        "zb" => $row["zbiorcze"],
        "id_p" => $row['id_pomieszczenie'],
        "kod" => $row['kod'],
        "pol" => $row['polaczenie'],
        "pomieszczenie" => $row['pomieszczenie']
    );
}

$przewodyid = '(';
$query = "SELECT `przewod_id` FROM `ZewnetrzneKableView` WHERE `miejsce_id` = " . $mid;
$result = mysqli_query($con, $query);
$zewnetrzne = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zewnetrzne, $row['przewod_id']);
    $przewodyid .= $row['przewod_id'] . ",";
}


$query = "SELECT `przewod_id` FROM `WewnetrzneKableView` WHERE `miejsce_id` = " . $mid;
$result = mysqli_query($con, $query);
$wewnetrzne = array();
while($row = mysqli_fetch_array($result)) {
    array_push($wewnetrzne, $row['przewod_id']);
    $przewodyid .= $row['przewod_id'] . ",";
}

$przewodyid .= "-1)";

$query = "SELECT `id`, `opis`, `ilosc_zyl` FROM `przewod` WHERE `id` in" . $przewodyid;
$result = mysqli_query($con, $query);
$przewody = array();
while($row = mysqli_fetch_array($result)) {
    $przewody[$row['id']] = array("opis" => $row["opis"], "ilosc_zyl" => $row["ilosc_zyl"]);
}

$query = "SELECT `id`, `kolor_id`, `przewod_id`, `opis`, `kolor`, `html` FROM `ZylaWidok` WHERE `przewod_id` in " . $przewodyid . " ORDER by `przewod_id`, `kolor`";

$result = mysqli_query($con, $query);
$prevprzew = -1;
$zyly = array();
while($row = mysqli_fetch_array($result)) {
    if ($prevprzew != $row['przewod_id']) {
        $prevprzew = $row['przewod_id'];
        $zyly[$row['przewod_id']] = array();
    }
    array_push($zyly[$row['przewod_id']], array(
        "zid" => $row['id'],
        "cid" => $row['kolor_id'],
        "pid" => $row['przewod_id'],
        "opis" => $row['opis'],
        "kolor" => $row['kolor'],
        "html" => $row['html']
    ));
    
}

$query = "SELECT `zid`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `przewod_id`, `miejsce_id`, `nazwa`, `kod` FROM `PrzewodMiejsceZakonczenieView`";
$query .= " WHERE `przewod_id` in " . $przewodyid . " AND `miejsce_id` = " . $mid . "  ORDER by `przewod_id`, `rodzaj_zakonczenia`, `etykieta` ";

$result = mysqli_query($con, $query);
$zakonczenie = array();
while($row = mysqli_fetch_array($result)) {
    if ($prevprzew != $row['przewod_id']) {
        $prevprzew = $row['przewod_id'];
        $zakonczenie[$row['przewod_id']] = array();
    }
    array_push($zakonczenie[$row['przewod_id']], array(
        "etykieta" => $row['etykieta'],
        "kod" => $row['kod']
    ));
    
}

$opt = array(
    'miejsce' => $miejsce,
    'zewnetrzne' => $zewnetrzne,
    'wewnetrzne' => $wewnetrzne,
    'przewody' => $przewody,
    'zyly' => $zyly,
    'zakonczenia' => $zakonczenie
);

echo json_encode($opt);
mysqli_close($con);


?>