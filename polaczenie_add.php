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
$count = count($miejscaarray);
$prev = -1;
$zylyarray = array();
$k = '(';
for ($i = 0; $i < $count; $i++) {

    $query = "SELECT `pm`.`kabel_id` as `kid`, `p`.`description` as `descr`, `p`.`ilosc_zyl` as `cnt` ";
    $query .= "FROM `przewod_miejsce` `pm` LEFT JOIN `przewod` `p` on `p`.`id` = `pm`.`kabel_id` WHERE `pm`.`miejsce_id` = ". $miejscaarray[$i]['id'];
    $query .= " ORDER BY `pm`.`kabel_id`";
    
    $result = mysqli_query($con, $query);

	while($row = mysqli_fetch_array($result)) {
        if ($prev != $row['kid']) {
            $prev = $row['kid'];
            array_push($miejscaarray[$i]['kable'], $row['kid']);
            $zylyarray[$row['kid']] = array();
            $k = $k . $row['kid'] . ',';
        }
	}
}
$k .= '-1)';

$query = "SELECT `id`, `przewod_id`, `opis`, `name`, `html` FROM `ZylaWidok` WHERE `przewod_id` in " . $k . "ORDER BY `name` ";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
	array_push($zylyarray[$row['przewod_id']], array( 'id' => $row['id'], 
                                    'opis' => $row['opis'],
                                    'cname' => $row['name'],
                                    'chtml' => $row['html'],
                                    ));
}
$opt = array(
    "miejsca" => $miejscaarray,
    "zbiorcze" => $zbiorczearray,
    "zyly" => $zylyarray,
);
echo json_encode ($opt);
mysqli_close($con);
?>