<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");


$id = $_POST["id"];
$nazwa = $_POST["nazwa"];
$plytka_id = $_POST["plytka_id"];
$queries = array();

if ($id != -1) {
    array_push($queries, 
        "UPDATE `polaczenie_plytka` SET `nazwa`='$nazwa' WHERE `id` = $plytka_id"
    );
} else {
    array_push($queries, 
        "INSERT INTO `polaczenie_plytka`(`id`, `nazwa`, `plytka_id`) VALUES (NULL, '$nazwa', $plytka_id)"
    );
}

$count = count($queries);
#print_r($queries);
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