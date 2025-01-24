<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con, "utf8");


$pid = -1;

if (isset($_GET['pid'])) {
    $pid = $_GET['pid'];
}

$query = "SELECT `id`, `kolor_id`, `przewod_id`, `opis`, `kolor`, `html` FROM `ZylaWidok` WHERE `przewod_id` = $pid ORDER by `id`";
$result = mysqli_query($con, $query);
$zyly = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zyly, array(
            'id' => $row['id'],
            'cid' => $row['kolor_id'],
            'opis' => $row['opis'],
            'cname' => $row['kolor'],
            'html' => $row['html']
    ));
}    

$opt = array(
    "zyly" => $zyly
);
echo json_encode ($opt);
mysqli_close($con);
?>