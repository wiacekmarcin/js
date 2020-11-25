<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");
$query = "SELECT `id`, `name`, `zbiorcze`, `kod`, `polaczenie`, `pomieszczenie` FROM `MiejsceView` WHERE `polaczenie` = 1";

$result = mysqli_query($con, $query);
$miejscaarray = array();
$zbiorczearray = array();
while($row = mysqli_fetch_array($result)) {
	array_push($miejscaarray, array( 'id' => $row['id'], 
                                    'name' => $row['name'] . " (" . $row['pomieszczenie'] . ")", 
									'kable' => array()
                                    ));
    $zbiorczearray[$row['id']] = $row['zbiorcze'];
}

$opt = array(
    "miejsca" => $miejscaarray,
    "zbiorcze" => $zbiorczearray,
    "zyly" => $zylyarray,
);
echo json_encode ($opt);
mysqli_close($con);