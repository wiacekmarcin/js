<?php
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con,"utf8");

$params = array();

$edit = $_POST["edit"];
$id = $_POST["id"];
$nazwa = $_POST["nazwa"];
$miejsce_id = $_POST["miejsce_id"];

$queries = array();

if ($edit == "true") {
    array_push($queries, "UPDATE `plytki` SET `nazwa`='$nazwa',`miejsce_id`=$miejsce_id WHERE `id` = $id");
} else {
    array_push($queries, "INSERT INTO `plytki`(`id`, `nazwa`, `miejsce_id`) VALUES (NULL,'$nazwa', $miejsce_id)");
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
