<?php
require_once "db.php";

$con = db();
mysqli_set_charset($con, "utf8");

$index = 0;
$przewody = array();
$isrow = true;
while($isrow) {
    $tmp = array();
    $query = "SELECT `id`, `opis`, `ilosc_zyl` FROM `przewod` LIMIT " . 50*$index . ",  50";
    $result = mysqli_query($con, $query);
    $isrow = false;
    while($row = mysqli_fetch_array($result)) {
        $isrow = true;
        array_push($tmp, array(
            'id' => $row['id'],
            'descr' => $row['opis'],
            'ilosc_zyl' => $row['ilosc_zyl']
        ));
    }    
    $index += 1;
    array_push($przewody, $tmp);
}

$query = "SELECT `id`, `nazwa`, `html` FROM `KolorView` WHERE 1";
$result = mysqli_query($con, $query);
$colors = array();
while($row = mysqli_fetch_array($result)) {
    array_push($colors, array(
            'id' => $row['id'],
            'cname' => $row['nazwa'],
            'html' => $row['html']
    ));
}    

$opt = array(
    "przewody" => $przewody,
    "colors" => $colors
);
echo json_encode($opt, JSON_UNESCAPED_UNICODE);
mysqli_close($con);
?>