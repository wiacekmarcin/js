<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

require_once "database.php";
$con = db_connect();
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

$outp = "{";
$outp .= '"przewod":"'  . $cntPrz . '",';
$outp .= '"zyla":"'      . $cntZyla        . '",';
$outp .= '"zlacze":"'    . $cntZlacze     . '",';
$outp .= '"zewn_przew":"'    . $cntPzew     . '",';
$outp .= '"wewn_przew":"'    . $cntPwew     . '",';
$outp .= '"zyla_all":"'     . $cntAllZyl .  '",';
$outp .= '"przewod_opis":"'     . $cntDescrPrzew .  '",';
$outp .= '"zakonczenia":' . json_encode($zakoarray) . ",";
$outp .= '"kolory":' . json_encode($kolory);
$outp .= "}";
$con->close();

echo($outp);
?>

