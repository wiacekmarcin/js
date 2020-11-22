<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$id = $_POST['id'];
$kod = $_POST['kod'];
$name = $_POST['name'];
$id_pomieszczenie = $_POST['id_pomieszczenie'];
$description = $_POST['description'];
$zbiorcze = $_POST['zbiorcze'];
$polaczenie = $_POST['polaczenie'];

if ($id == -1) {
    $query = "INSERT INTO `miejsce`(`id`, `name`, `description`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`) ";
    $query.= "VALUES (NULL, '" . $name . "', '" . $description . "', " . $zbiorcze . ", " . $id_pomieszczenie . ", '" . $kod . "', " . $polaczenie . ");";
} else {
    $query = "UPDATE `miejsce` SET `name`='". $name . "', `description`='" . $description . "'. `zbiorcze`=" . $zbiorcze . ",`id_pomieszczenie`=";
    $query .= $id_pomieszczenie . "`kod`='" . $kod . "',`polaczenie`=" . $polaczenie . " WHERE `id` = " . $id . ";";
}

print($query);
?>