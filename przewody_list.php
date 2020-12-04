<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `zid`, `etykieta`, `przewod_miejsce_id_zlacze`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `przewod_id`, `miejsce_id`, `nazwa`, `kod` ";
$query.= "FROM `PrzewodMiejsceZakonczenieView` ORDER by `przewod_id`";
$prevpprzew = -1;
$przemiejscarr = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($row["przewod_id"] != $prevpprzew) {
        $przemiejscarr[$row["przewod_id"]] = array();
        $prevpprzew = $row["przewod_id"];
    }
    array_push($przemiejscarr[$row["przewod_id"]], array(
        "przewod_miejsce_id" => $row["przewod_miejsce_id"],
        "przewod_miejsce_id_zlacze" => $row["przewod_miejsce_id_zlacze"],
        "miejsce_id" => $row["miejsce_id"],
        "etykieta" => $row["etykieta"],
        "nazwa" => $row["nazwa"],
        "kod" => $row["kod"],

    ));
}

$query = "SELECT `id`, `nazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` FROM `MiejsceView` WHERE 1";
$miejscearr = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $miejscearr[$row['id']] = array(
        "id" => $row["id"],
        "nazwa" => $row["nazwa"],
        "opis" => $row["opis"],
        "zbiorcze" => $row["zbiorcze"],
        "kod" => $row["kod"],
        "polaczenie" => $row["polaczenie"],
        "pomieszczenie" => $row["pomieszczenie"],
        "kod" => $row["kod"]
    );
}

$query = "SELECT `id`, `opis`, `ilosc_zyl` FROM `przewod` WHERE 1";
$przewodyarr = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    array_push($przewodyarr, array(
        "id" => $row["id"],
        "opis" => $row["opis"],
        "ilosc_zyl" => "" . $row["ilosc_zyl"],
    ));
}

$query = "SELECT `id`, `kolor_id`, `przewod_id`, `opis`, `kolor`, `html` FROM `ZylaWidok` WHERE 1 order by `przewod_id`";
$prevpprzew = -1;
$zylyarr = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($row["przewod_id"] != $prevpprzew) {
        $zylyarr[$row["przewod_id"]] = array();
        $prevpprzew = $row["przewod_id"];
    }
    array_push($zylyarr[$row["przewod_id"]], array(
        "zyla_id" => $row["id"],
        "opis" => $row["opis"],
        "kolor" => $row["kolor"],
        "html" => $row["html"]
    ));
}


$opt = array(
    'miejsca_przewody' => $przemiejscarr,
    'przewody' => $przewodyarr,
    'zyly' => $zylyarr,
    'miejsca' => $miejscearr
);

echo json_encode($opt);
mysqli_close($con);
?>