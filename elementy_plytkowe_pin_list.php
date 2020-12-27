<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$id = 0;
if (isset($_GET['id'])) {
    $id = $_GET["id"];
}

$query = "SELECT `id`, `nazwa`, `pos` FROM `elementy_plytkowe_pin` WHERE `element_plytkowy_id` = $id ORDER BY `pos`";
$piny = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    array_push($piny, array(
        "id" => $row["id"],
        "nazwa" => $row["nazwa"],
        "pos" => $row["pos"],
    ));
}


$opt = array(
    'pins' => $piny,
);

echo json_encode($opt);
mysqli_close($con);

?>