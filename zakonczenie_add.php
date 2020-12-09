<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `nazwa`, `kod` FROM `rodzaj_zakonczenia` WHERE 1";
$result = mysqli_query($con, $query);
$rodzajzakonczeniaarray = array();
while($row = mysqli_fetch_array($result)) {
    array_push($rodzajzakonczeniaarray, array(
            'id' => $row['id'],
            'nazwa' => $row['nazwa'],
            'kod' => $row['kod'],
    ));
}    


$opt = array(
    'rodzaj_zakonczenia' => $rodzajzakonczeniaarray,
);

echo json_encode($opt);
mysqli_close($con);

?>