<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$plytkiarray = array();
$query = "SELECT `id`, `nazwa`, `miejsce_id`, `mnazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, ";
$query.= "`polaczenie`, `pomieszczenie` FROM `PlytkaMiejsceView` WHERE 1";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $plytkiarray[$row['id']] = array(
        "nazwa" => $row['nazwa'],
        "miejsce" => $row['mnazwa'],
        "pomie" => $row['pomieszczenie'],
    );
}

$plytkilist = array();
$query = "SELECT `id`, `nazwa`, `miejsce_id`, `mnazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, ";
$query.= "`polaczenie`, `pomieszczenie` FROM `PlytkaMiejsceView` WHERE 1 ORDER BY `pomieszczenie`, `mnazwa`, `nazwa` ";
$result = mysqli_query($con, $query);
$prevpomieszczenie = "";
$prevmiejse = "";
while($row = mysqli_fetch_array($result)) {
    if ($prevpomieszczenie != $row["pomieszczenie"]) {
        $prevpomieszczenie = $row["pomieszczenie"];
        $plytkilist[$row["pomieszczenie"]] = array(
            $row["mnazwa"] => array()
        );
        array_push($plytkilist[$row["pomieszczenie"]][$row["mnazwa"]], $row["id"]);
        $prevmiejse = $row["mnazwa"];
    } else {
        if ($prevmiejse != $row["mnazwa"]) {
            $prevmiejse = $row["mnazwa"];
            $plytkilist[$row["pomieszczenie"]][$row["mnazwa"]] = array();
            array_push($plytkilist[$row["pomieszczenie"]][$row["mnazwa"]], $row["id"]);
        } else {
            array_push($plytkilist[$row["pomieszczenie"]][$row["mnazwa"]], $row["id"]);
        }
    }
}


$polaczeniaarray = array();
$query = "SELECT `id`, `nazwa`, `plytka_id` FROM `polaczenie_plytka` WHERE 1 ORDER BY `plytka_id`";
$prevplytkaid = -1;
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($prevplytkaid != $row["plytka_id"]) {
        $prevplytkaid = $row["plytka_id"];
        $polaczeniaarray[$row["plytka_id"]] = array();
    }
    array_push($polaczeniaarray[$row["plytka_id"]],
        array(
            "id" => $row["id"],
            "nazwa" => $row["nazwa"]
    ));
}

$query = "SELECT `plytka_id`, count(`plytka_id`) as `cnt` FROM `polaczenie_plytka` WHERE 1 GROUP BY `plytka_id` ";
$result = mysqli_query($con, $query);
$polaczeniapincntarray = array();
while($row = mysqli_fetch_array($result)) {
    $polaczeniapincntarray[$row["plytka_id"]] = $row["cnt"];
}

$opt = array(
    'plytki' => $plytkiarray,
    'plytkilist' => $plytkilist,
    'polaczenia' => $polaczeniaarray,
    'ilosc_pin' => $polaczeniapincntarray
);

echo json_encode($opt);
mysqli_close($con);


?>