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

$query = "SELECT `wtyczka_id`, `zlacze_id`, `epid`, `epnazwa`, `eppos`, `zyla_id`, `zzpos`, `zzopis`, `zzetykieta`, `zid`, `kolor_id`, ";
$query .= "`przewod_id`, `opis`, `kolor`, `html` FROM `ZlaczeWtyczkaView` WHERE `zlacze_id` = $id";

$zyly = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $zyly[$row["epid"]] = array(
        "zyla_id" => $row["zyla_id"],
        "zzetykieta" => $row["zzetykieta"],
        "przewod_id" => $row["przewod_id"],
        "opis" => $row["opis"],
        "kolor" => $row["kolor"],
        "html" => $row["html"],
    );
}

$opt = array(
    'pins' => $piny,
    'zyly' => $zyly,
);

echo json_encode($opt);
mysqli_close($con);

?>