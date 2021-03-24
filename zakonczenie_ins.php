<?php
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con,"utf8");

$zid=$_POST["zid"];
$etykieta = $_POST["etykieta"];
$pmid = $_POST["pmid"];
$rodzaj = $_POST["rodzaj_zakonczenia"];
$ilosc_pinow = $_POST["ilosc_pin"];

if ($zid == -1) {
    $query = "INSERT INTO `zakonczenie`(`id`, `etykieta`, `przewod_miejsce_id`, ";
    $query .= "`rodzaj_zakonczenia`, `ilosc_pin`) VALUES (NULL, '$etykieta',";
    $query .= "$pmid, $rodzaj, $ilosc_pinow);";
} else {

}

$result = mysqli_query($con, $query);
if ($zid == -1)
    $zid = $con->insert_id;
$opt = array(
    'zid' => $zid
);
echo json_encode($opt);
mysqli_close($con);

?>