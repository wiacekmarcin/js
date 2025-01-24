<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = db_connect();
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
$query = "SELECT `id`, `nazwa`, `plytka_id` FROM `polaczenie_plytka` WHERE 1 ORDER BY `plytka_id`, `nazwa`";
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

$query = "SELECT `id`, `polaczenie_plytka_id`, `elementy_plytkowe_piny_id`, `pinnazwa`, `pos`, `element_plytkowy_id`, `elemnazwa`, ";
$query .= "`ilosc_pin`, `plytka_id`, `rodzaj_urzadzenia`, `rodznazwa`, `kod`, `przewod`, `plytka` ";
$query .= "FROM `ElementyPlytkowePolaczeniaPinView` WHERE 1";

$prev_polaczenie_id = 0;
$result = mysqli_query($con, $query);
$polaczenienazwane = array();
while($row = mysqli_fetch_array($result)) {
    if ($prev_polaczenie_id != $row["polaczenie_plytka_id"]) {
        $prev_polaczenie_id = $row["polaczenie_plytka_id"];
        $polaczenienazwane[$row["polaczenie_plytka_id"]] = array();
    }
    array_push($polaczenienazwane[$row["polaczenie_plytka_id"]],
        array(
            "id" => $row["id"],
            "pinpid" => $row["elementy_plytkowe_piny_id"],
            "pinnazwa" => $row["pinnazwa"],
            "pos" => $row["pos"],
            "elemnazwa" => $row["elemnazwa"],
            "rodznazwa" => $row["rodznazwa"],
            "rodz_kod" => $row["kod"]
    ));
}

$query = "SELECT `id`, `pinnazwa`, `pos`, `element_plytkowy_id`, `elementnazwa`, `ilosc_pin`, `plytka_id`, `rodzaj_urzadzenia` ";
$query .= "FROM `ElementyPlytkowePinView` WHERE 1";
$prevplytkaid = -1;
$result = mysqli_query($con, $query);
$pins = array();
while($row = mysqli_fetch_array($result)) {
    if ($prevplytkaid != $row["plytka_id"]) {
        $prevplytkaid = $row["plytka_id"];
        $pins[$row["plytka_id"]] = array();
    }
    array_push($pins[$row["plytka_id"]],
        array(
            "id" => $row["id"],
            "pinnazwa" => $row["pinnazwa"],
            "elementnazwa" => $row["elementnazwa"],
            "pos" => $row["pos"]
    ));
}



$opt = array(
    'plytki' => $plytkiarray,
    'plytkilist' => $plytkilist,
    'polaczenia' => $polaczeniaarray,
    'ilosc_pin' => $polaczeniapincntarray,
    'polaczenienazwane' => $polaczenienazwane,
    'pins' => $pins 
);

echo json_encode($opt);
mysqli_close($con);


?>