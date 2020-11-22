<?php
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `kabel_id`, `miejsce_id`, `name`, `description`, `zbiorcze`, `id_pomieszczenia`, `kod`, `polaczenie`, `pomieszczenie`, `pdescription`, `ilosc_zyl` FROM `PrzewodyView`";
$result = mysqli_query($con, $query);

$kableArray = array();
$przewod_prev = -1;


$namepom1 = '';
$mid1 = -1;
$namepom2 = '';
$mid1 = -1;
$zbiorcze1 = 0;
$zbiorcze2 = 0;
$zylyArray = array();
while($row = mysqli_fetch_array($result)) {
    $pid = $row['kabel_id'];
    $zylyArray[$pid] = array();
    if ($przewod_prev != $pid) {
        $namepom1 = $row['name'];
        $mid1 = $row['miejsce_id'];
        $zbiorcze1 = $row['zbiorcze'];
        $przewod_prev = $pid;
    } else if ($przewod_prev == $pid) {
        $namepom2 = $row['name'];
        $mid2 = $row['miejsce_id'];
        $zbiorcze2= $row['zbiorcze'];

        array_push($kableArray, array(
            'id' => $pid,
            'descr' => $row['pdescription'],
            'miejsce1' => $namepom1, 
            'miejsce2' => $namepom2, 
            'mid1' => $mid1,
            'mid2' => $mid2,
            'zbiorcze1' => $zbiorcze1,
            'zbiorcze2' => $zbiorcze2,
            'ilosc_zyl' => $row['ilosc_zyl']
        )); 
    }
}

$query = "SELECT `id`, `przewod_id`, `opis`, `name`, `html` FROM `ZylaWidok` ORDER by `przewod_id`, `name`";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    array_push($zylyArray[$row['przewod_id']], array(
        "zid" => $row['id'],
        "opis" => $row['opis'],
        "cname" => $row['name'],
        "chtml" => $row['html']
    ));
}

$query = "SELECT `id`, `name`, `pomieszczenie` FROM `MiejsceView` WHERE `zbiorcze` = 1 ORDER BY `name`";
$result = mysqli_query($con, $query);

$zbiorczeArray = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zbiorczeArray , array('id' => $row['id'], 'name' => $row['name'], 'pomieszczenie' => $row['pomieszczenie']));
}

/*
$miejsceArray = array();
$query = "SELECT `id`, `name` FROM `miejsce` ORDER BY `name`";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    array_push($miejsceArray , array('id' => $row['id'], 'name' => $row['name']));
}
*/
$opt = array(
    'zbiorcze' => $zbiorczeArray,
    'przewody' => $kableArray,
    'zyly' => $zylyArray
    /*,'miejsca' => $miejsceArray,*/
);

echo json_encode($opt);
mysqli_close($con);
?>