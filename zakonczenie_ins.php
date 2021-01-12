<?php
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con,"utf8");

$params = array();

$pmid = $_POST["pmid"];
$zid = $_POST["zid"];
$etykieta = $_POST["etykieta"];
$rodzaj = $_POST["rodzaj_zakonczenia"];

if ($zid ==  -1) {
    $query = "INSERT INTO `zakonczenie`(`id`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`) VALUES ";
    $query .= "(NULL,'$etykieta',$pmid,$rodzaj)";
} else {
    $query = "UPDATE `zakonczenie` SET `etykieta`='$etykieta', `przewod_miejsce_id`=$pmid,`rodzaj_zakonczenia`=$rodzaj WHERE `id` = $zid";
}
$result = mysqli_query($con, $query);
if ($zid == -1)
    $zid = $con->insert_id;
$opt = array(
    'zid' => $zid,
);
echo json_encode($opt);
mysqli_close($con);

?>