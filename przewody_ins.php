<?php
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con,"utf8");

$params = array();

$edit = $_POST["edit"];
$id = $_POST["id"];
$opis = $_POST["opis"];
$ilosc_zyl = $_POST["ilosc_zyl"];
$miejsce_id_1 = $_POST["miejsce_id_1"];
$miejsce_id_2 = $_POST["miejsce_id_2"];
$pmid_1 = $_POST["pmid_1"];
$pmid_2 = $_POST["pmid_2"];

$queries = array();

if ($edit == "true") {
    array_push($queries, "UPDATE `przewod` SET `opis`='$opis', `ilosc_zyl`=$ilosc_zyl WHERE `id` = $id");
    array_push($queries, "UPDATE `przewod_miejsce` SET `miejsce_id`= $miejsce_id_1 WHERE  `id` = $pmid_1");
    array_push($queries, "UPDATE `przewod_miejsce` SET `miejsce_id`= $miejsce_id_2 WHERE  `id` = $pmid_2");

} else {
    array_push($queries, "INSERT INTO `przewod`(`id`, `opis`, `ilosc_zyl`) VALUES ($id, '$opis', $ilosc_zyl)");
    array_push($queries, "INSERT INTO `przewod_miejsce`(`id`, `przewod_id`, `miejsce_id`) VALUES (NULL, $id, $miejsce_id_1)");
    array_push($queries, "INSERT INTO `przewod_miejsce`(`id`, `przewod_id`, `miejsce_id`) VALUES (NULL, $id, $miejsce_id_2)");
}

$count = count($queries);

$err = 0;
for ($i = 0; $i < $count; $i++) {
    if (!mysqli_query($con, $queries[$i])) {
        print ("ERR : " . $queries[$i]);
        $err = 1;
    }
}

if ($err == 0)
    print ("OK");
mysqli_close($con);

?>
