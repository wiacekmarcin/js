
<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = db_connect();
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `nazwa`, `mnazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, ";
$query .= "`miejsce_id`, `pomieszczenie` FROM `PlytkaMiejsceView` WHERE 1";

$plytki = array();
$result = mysqli_query($con, $query);


$urzadzenie = array();
while($row = mysqli_fetch_array($result)) {
    array_push($plytki, array(
        "id" => $row["id"],
        "nazwa" => $row["nazwa"],
        "miejsce_id" => $row["miejsce_id"],
        "miejsce_nazwa" => $row["mnazwa"],
        "pomieszczenie" => $row["pomieszczenie"],
    ));
    $elementy[$row["id"]] = array();
}


$query = "SELECT `id`, `nazwa`, `ilosc_pin`, `plytka_id` FROM `elementy_plytkowe` WHERE 1";
$result = mysqli_query($con, $query);

while($row = mysqli_fetch_array($result)) {
    array_push($elementy[$row["plytka_id"]], 
        array(
            "id" => $row["id"],
            "nazwa" => $row["nazwa"],
            "ilosc_pin" => $row["ilosc_pin"],
        )
    );    
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

$opt = array(
    'plytki' => $plytki,
    'miejsce' => $miejscearray,
    'elementy' => $elementy
);

echo json_encode($opt);
mysqli_close($con);


?>