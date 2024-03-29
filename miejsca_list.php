<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con, "utf8");

$mid = $_GET["pid"];

$query = "SELECT `id`, `nazwa` FROM `pomieszczenie` WHERE 1 ORDER BY `nazwa`";
$result = mysqli_query($con, $query);
$pomieszczenia = array();
while($row = mysqli_fetch_array($result)) {
    array_push($pomieszczenia, array(
        "id" => $row["id"],
        "nazwa" => $row["nazwa"]
    ));
}

$query = "SELECT `id`, `nazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` ";
$query .= "FROM `MiejsceView` WHERE 1 ORDER BY `nazwa`";

$result = mysqli_query($con, $query);
$miejsca = array();

while($row = mysqli_fetch_array($result)) {
    $ins = False;
    if (($mid > 0 && $row["id_pomieszczenie"] == $mid) || 
        $mid == 0 ||
        ($mid == -1 && $row["zbiorcze"] == 1) ||
        ($mid == -2 && $row["polaczenie"] == 1) ) {
        
        array_push($miejsca, array(
            "id" => $row["id"],
            "nazwa" => $row["nazwa"],
            "kod" => $row["kod"],
            "opis" => $row["opis"],
            "zbiorcze" => $row["zbiorcze"],
            "polaczenie" => $row["polaczenie"],
            "pomieszczenie" => $row["pomieszczenie"],
            "id_pomieszczenie" => $row["id_pomieszczenie"],
        ));
    }
}

$query = "SELECT DISTINCT `przewod_id`, `miejsce_id` FROM `przewod_miejsce` WHERE 1 order by `miejsce_id`, `przewod_id` ";
$previdmiejsca = -1;
$result = mysqli_query($con, $query);
$przewody = array();
while($row = mysqli_fetch_array($result)) {
    if ($previdmiejsca != $row["miejsce_id"]) {
        $previdmiejsca = $row["miejsce_id"];
        $przewody[$row["miejsce_id"]] = array();
    }
    array_push($przewody[$row["miejsce_id"]], $row["przewod_id"]);
}

$query = "SELECT DISTINCT `etykieta`, `rodzaj_zakonczenia`, `miejsce_id` FROM ";
$query .= "`ZakonczenieView` WHERE 1 ORDER BY `miejsce_id`, `rodzaj_zakonczenia` ";

$previdmiejsca = -1;
$result = mysqli_query($con, $query);
$zakonczenia = array();
while($row = mysqli_fetch_array($result)) {
    if ($previdmiejsca != $row["miejsce_id"]) {
        $previdmiejsca = $row["miejsce_id"];
        $zakonczenia[$row["miejsce_id"]] = array(
            "1" => array(),
            "2" => array(),
            "3" => array(),
            "4" => array(),
            "5" => array(),
            "6" => array(),
            "7" => array(),
            "8" => array(),
            "9" => array(),
        );
    }
    array_push($zakonczenia[$row["miejsce_id"]][$row["rodzaj_zakonczenia"]], $row["etykieta"]);
}

$query = "SELECT `id`, `nazwa`  FROM `rodzaj_zakonczenia` WHERE 1";
$result = mysqli_query($con, $query);
$rodzaj = array();
while($row = mysqli_fetch_array($result)) {
    $rodzaj[$row["id"]] = $row["nazwa"];
}


$opt = array(
    "miejsca" => $miejsca,
    "pomieszczenia" => $pomieszczenia,
    "przewody" => $przewody,
    "zakonczenia" => $zakonczenia,
    "rodzaj" => $rodzaj
);
echo json_encode ($opt);
mysqli_close($con);
?> 
