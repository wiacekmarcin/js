<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con, "utf8");

$id = $_POST['id'];
$kod = $_POST['kod'];
$nazwa = $_POST['nazwa'];
$id_pomieszczenie = $_POST['id_pomieszczenie'];
$opis = $_POST['opis'];
$zbiorcze = $_POST['zbiorcze'];
$polaczenie = $_POST['polaczenie'];

if ($id == -1) {
    $query = "INSERT INTO `miejsce`(`id`, `name`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`) ";
    $query.= "VALUES (NULL, '" . $nazwa . "', '" . $opis . "', " . $zbiorcze . ", " . $id_pomieszczenie . ", '" . $kod . "', " . $polaczenie . ");";
} else {
    $query = "UPDATE `miejsce` SET `nazwa`='". $nazwa . "', `opis`='" . $opis . "', `zbiorcze`=" . $zbiorcze . ", `id_pomieszczenie`=";
    $query .= $id_pomieszczenie . ", `kod`='" . $kod . "', `polaczenie`=" . $polaczenie . " WHERE `id` = " . $id . ";";
}

$result = mysqli_query($con, $query);
echo  ($result ? '-OK ' : '-ERR ' . $query);
mysqli_close($con);
?>