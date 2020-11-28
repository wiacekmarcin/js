<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

require_once "database.php";
$con = mysqli_connect("127.0.0.1",$username,$password,$database);
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

$query = "SELECT count(*) FROM `zlacze` WHERE 1 ";
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

$outp = "{";
$outp .= '"przewod":"'  . $cntPrz . '",';
$outp .= '"zyla":"'      . $cntZyla        . '",';
$outp .= '"zlacze":"'    . $cntZlacze     . '",';
$outp .= '"zewn_przew":"'    . $cntPzew     . '",';
$outp .= '"wewn_przew":"'    . $cntPwew     . '",';
$outp .= '"zyla_all":"'     . $cntAllZyl .  '"}';
$con->close();

echo($outp);
?>

