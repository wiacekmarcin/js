<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$mid = -1;

if (isset($_GET['mid'])) {
    $mid = $_GET['mid'];
}
$query = "SELECT `id`, `name`, `description`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` ";
$query .=" FROM `MiejsceView` WHERE `id` = " . $mid;

$result = mysqli_query($con, $query);
$miejsce = array();
while($row = mysqli_fetch_array($result)) {
    $miejsce = array(
        "id" => $row['id'],
        "name" => $row['name'],
        "descr" => $row['description'],
        "zb" => $row["zbiorcze"],
        "id_p" => $row['id_pomieszczenie'],
        "kod" => $row['kod'],
        "pol" => $row['polaczenie'],
        "pom" => $row['pomieszczenie']
    );
}

$przewodyid = '(';
$query = "SELECT `kabel_id` FROM `ZewnetrzneKableView` WHERE `miejsce_id` = " . $mid;
$result = mysqli_query($con, $query);
$zewnetrzne = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zewnetrzne, $row['kabel_id']);
    $przewodyid .= $row['kabel_id'] . ",";
}


$query = "SELECT `kabel_id` FROM `WewnetrzneKableView` WHERE `miejsce_id` = " . $mid;
$result = mysqli_query($con, $query);
$wewnetrzne = array();
while($row = mysqli_fetch_array($result)) {
    array_push($wewnetrzne, $row['kabel_id']);
    $przewodyid .= $row['kabel_id'] . ",";
}

$przewodyid .= "-1)";

$query = "SELECT `id`, `description`, `ilosc_zyl` FROM `przewod` WHERE `id` in" . $przewodyid;
$result = mysqli_query($con, $query);
$przewody = array();
while($row = mysqli_fetch_array($result)) {
    $przewody[$row['id']] = array("desc" => $row["description"], "il_zyl" => $row["ilosc_zyl"]);
}

$query = "SELECT `id`, `color_id`, `przewod_id`, `opis`, `name`, `html` FROM `ZylaWidok` WHERE `przewod_id` in " . $przewodyid . " ORDER by `przewod_id`, `name`";
$result = mysqli_query($con, $query);
$prevprzew = -1;
$zyly = array();
while($row = mysqli_fetch_array($result)) {
    if ($prevprzew != $row['przewod_id']) {
        $prevprzew = $row['przewod_id'];
        $zyly[$row['przewod_id']] = array();
    }
    array_push($zyly[$row['przewod_id']], array(
        "zid" => $row['id'],
        "cid" => $row['color_id'],
        "pid" => $row['przewod_id'],
        "opis" => $row['opis'],
        "cname" => $row['name'],
        "chtml" => $row['html']
    ));
    
}
$opt = array(
    'miejsce' => $miejsce,
    'zewnetrzne' => $zewnetrzne,
    'wewnetrzne' => $wewnetrzne,
    'przewody' => $przewody,
    'zyly' => $zyly
);

echo json_encode($opt);
mysqli_close($con);


?>