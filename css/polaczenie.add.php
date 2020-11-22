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
