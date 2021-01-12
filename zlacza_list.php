<?php
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `name`, `pomieszczenie` FROM `MiejsceView` WHERE `zbiorcze` = 1 ORDER BY `name`";
$result = mysqli_query($con, $query);

$zbiorczeArray = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zbiorczeArray , array('id' => $row['id'], 'name' => $row['name'], 'pomieszczenie' => $row['pomieszczenie']));
}


$query = "SELECT `id`, `description`, `ilosc_zyl` FROM `przewod` WHERE 1";
$result = mysqli_query($con, $query);
$kableArray = array();
while($row = mysqli_fetch_array($result)) {
    $kableArray[$row["id"]] = array('desc' => $row['description'], 'il' => $row['ilosc_zyl']);
}


$query = "SELECT `id`, `kabel_id`, `miejsce_id`, `etykieta`, `zlacze_id` FROM `ZlaczePrzewodView` WHERE 1 ORDER BY `miejsce_id`, `etykieta`, `kabel_id` ";
$result = mysqli_query($con, $query);

$zlaczaArray = array();
$zylyArray = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zlaczaArray, array(
            'przewod_id' => $row['kabel_id'],
            'miejsce_id' => $row['miejsce_id'],
            'etykieta' => $row['etykieta'], 
            'zlacze_id' => $row['zlacze_id'] 
    )); 
    $zylyArray[$row['zlacze_id']] = array();
}

$query = "SELECT `id`, `zlacze_id`, `zyla_id`, `pos`, `opis`, `name`, `html`, `przewod_id` FROM `ZylaZlaczeView` WHERE 1 ORDER by `pos`";
$result = mysqli_query($con, $query);

while($row = mysqli_fetch_array($result)) {
    array_push($zylyArray[$row['zlacze_id']], array(
        "id" => $row['id'],
        "zid" => $row['zyla_id'],
        "pos" => $row['pos'],
        "opis" => $row['opis'],
        "cname" => $row['name'],
        "chtml" => $row['html']
    ));
}


$miejsceArray = array();
$query = "SELECT `id`, `name`, `kod`, `pomieszczenie` FROM `MiejsceView`";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $miejsceArray[$row['id']] = array('kod' =>$row['kod'], 
                    'name' => $row['name'], 
                    'pom' => $row['pomieszczenie']);
}

$query = "SELECT `id`, `color_id`, `przewod_id`, `opis`, `name`, `html` FROM `ZylaWidok` WHERE 1 ORDER BY `przewod_id`";
$allzylyArray = array();
$ppid = -1;
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($ppid != $row['przewod_id']) {
        $allzylyArray[$row['przewod_id']] = array();
        $ppid = $row['przewod_id'];
    }
    array_push($allzylyArray[$row['przewod_id']],
                    array("zid" => $row["id"],
                    "cname" => $row["name"],
                    "html" => $row["html"],
                    "opis" => $row["opis"]
                ));
}

$opt = array(
    'zbiorcze' => $zbiorczeArray,
    'zlacza' => $zlaczaArray,
    'przewody' => $kableArray,
    'zyly' => $zylyArray,
    'allzyly' => $allzylyArray,
    'miejsca' => $miejsceArray
);

echo json_encode($opt);
mysqli_close($con);
?>