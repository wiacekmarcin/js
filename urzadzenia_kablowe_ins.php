<?php
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con,"utf8");

$zid=$_POST["id"];
$etykieta = $_POST["nazwa"];
$pmid = $_POST["przewod_miejsce_id"];
$rodzaj = $_POST["rodzaj"];
$ilosc_pinow = $_POST["ilosc_pin"];



if ($zid ==  -1) {
    $query = "INSERT INTO `zakonczenie`(`id`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `ilosc_pin`) VALUES ";
    $query .= "(NULL, '$etykieta',$pmid,$rodzaj,$ilosc_pinow)";
} else {
    $query = "UPDATE `zakonczenie` SET `etykieta`='$etykieta', `przewod_miejsce_id`=$pmid,`rodzaj_zakonczenia`=$rodzaj, ";
    $query .= "`ilosc_pin`=$ilosc_pinow WHERE `id` = $zid";
}
#print $query;
$result = mysqli_query($con, $query);
if ($zid == -1)
    $zid = $con->insert_id;
$opt = array(
    'zid' => $zid,
);
echo json_encode($opt);
mysqli_close($con);

?>