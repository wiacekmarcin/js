<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");


$id = $_POST["id"];
$pin = $_POST["pin"];
$queries = array();


array_push($queries, 
    "INSERT INTO `polaczenie_plytka_polaczenie`(`id`, `polaczenie_plytka_id`, `elementy_plytkowe_piny_id`) VALUES (NULL, $id, $pin)"
);


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

