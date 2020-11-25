<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");


$pid = -1;

if (isset($_GET['pid'])) {
    $pid = $_GET['pid'];
}

$query = "SELECT `id`, `color_id`, `opis`, `name`, `html` FROM `ZylaWidok` WHERE `przewod_id` = $pid ORDER by `id`";
$result = mysqli_query($con, $query);
$zyly = array();
while($row = mysqli_fetch_array($result)) {
    array_push($zyly, array(
            'id' => $row['id'],
            'cid' => $row['color_id'],
            'opis' => $row['opis'],
            'cname' => $row['name'],
            'html' => $row['html']
    ));
}    

$opt = array(
    "zyly" => $zyly
);
echo json_encode ($opt);
mysqli_close($con);
?>