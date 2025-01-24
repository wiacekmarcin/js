<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con, "utf8");

$index = 0;
$przewody = array();
while(true) {
    $tmp = array();
    $query = "SELECT `id`, `description`, `ilosc_zyl` FROM `przewod` LIMIT " . 50*$index . ",  50";
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

$opt = array(
    "przewody" => $przewody
);
echo json_encode ($opt);
mysqli_close($con);