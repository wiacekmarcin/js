<?php

require_once "db.php";
$con = db();
mysqli_set_charset($con, "utf8");

$query = "SELECT count(*) FROM `przewod` WHERE 1 ";
$result = mysqli_query($con, $query);
$clrarr = array();
$cntPrz = $result->fetch_array()[0];

$query = "SELECT count(*) FROM `zyla` WHERE 1 ";
$result = mysqli_query($con, $query);
$cntZyla = $result->fetch_array()[0];

$query = "SELECT count(*) FROM `zyla` WHERE 1 ";
$result = mysqli_query($con, $query);
$cntZyla = $result->fetch_array()[0];

$query = "SELECT count(*) FROM `zakonczenie` WHERE 1 ";
$result = mysqli_query($con, $query);
$cntZlacze = $result->fetch_array()[0];

$query = "SELECT CAST(count(*) AS UNSIGNED) FROM `WewnetrzneKableView` WHERE 1";
$result = mysqli_query($con, $query);
$cntPwew = $result->fetch_array()[0];

$query = "SELECT CAST(count(*)/2 AS UNSIGNED) FROM `ZewnetrzneKableView` WHERE 1";
$result = mysqli_query($con, $query);
$cntPzew = $result->fetch_array()[0];

$query = "SELECT sum(`ilosc_zyl`) FROM `przewod` WHERE 1 ";
$result = mysqli_query($con, $query);
$cntAllZyl = $result->fetch_array()[0];

$query = "select count(r.id) from (SELECT `z`.`przewod_id` as id, count(`z`.`przewod_id` ) as `cnt` ";
$query .= "FROM `zyla` `z` WHERE 1 GROUP BY `z`.`przewod_id`) as r";
$result = mysqli_query($con, $query);
$cntDescrPrzew = $result->fetch_array()[0];

$query = "SELECT `nazwa`, count(`nazwa`) as ilosc FROM `ZakonczenieView` WHERE 1 GROUP by `nazwa` ";
$zakoarray = array();
$result = mysqli_query($con, $query);
while($row = $result->fetch_array()) {
    array_push($zakoarray, array(
        "nazwa" => $row["nazwa"],
        "ilosc" => $row["ilosc"]
    ));
}

$query = "SELECT kolor, count(kolor) as cnt FROM `ZylaWidok` WHERE 1 GROUP BY kolor ORDER BY cnt DESC ";
$kolory = array();

$result = mysqli_query($con, $query);
while($row = $result->fetch_array()) {
    array_push($kolory, array(
        "nazwa" => $row["kolor"],
        "ilosc" => $row["cnt"],
    ));
}

$con->close();

echo json_encode([
    "przewod" => (string)$cntPrz,
    "zyla" => (string)$cntZyla,
    "zlacze" => (string)$cntZlacze,
    "zewn_przew" => (string)$cntPzew,
    "wewn_przew" => (string)$cntPwew,
    "zyla_all" => (string)$cntAllZyl,
    "przewod_opis" => (string)$cntDescrPrzew,
    "zakonczenia" => $zakoarray,
    "kolory" => $kolory,
], JSON_UNESCAPED_UNICODE);
?>

