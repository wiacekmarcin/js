<?php
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con,"utf8");

$params = array();
$count = 0;
$edit = $_POST["edit"];
$id = $_POST["id"];
$opis = $_POST["opis"];
$ilosc_zyl = $_POST["ilosc_zyl"];
$miejsce_id_1 = $_POST["miejsce_id_1"];
$miejsce_id_2 = $_POST["miejsce_id_2"];

print_r($_POST);
mysqli_close($con);

?>
