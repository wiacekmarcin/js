<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$index = 0;
$przewody = array();
$isrow = true;
while($isrow) {
    $tmp = array();
    $query = "SELECT `id`, `description`, `ilosc_zyl` FROM `przewod` LIMIT " . 50*$index . ",  50";
    $result = mysqli_query($con, $query);
    $isrow = false;
    while($row = mysqli_fetch_array($result)) {
        $isrow = true;
        array_push($tmp, array(
            'id' => $row['id'],
            'descr' => $row['description'],
            'ilosc_zyl' => $row['ilosc_zyl']
        ));
    }    
    $index += 1;
    array_push($przewody, $tmp);
}

$query = "SELECT `id`, `name`, `html` FROM `KolorView` WHERE 1";
$result = mysqli_query($con, $query);
$colors = array();
while($row = mysqli_fetch_array($result)) {
    array_push($colors, array(
            'id' => $row['id'],
            'cname' => $row['name'],
            'html' => $row['html']
    ));
}    

$opt = array(
    "przewody" => $przewody,
    "colors" => $colors
);
echo json_encode ($opt);
mysqli_close($con);
?>