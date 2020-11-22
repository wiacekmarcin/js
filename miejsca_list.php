<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$pid = -1;

if (isset($_GET['pid'])) {
    $mid = intval($_GET['pid']);
    if ($mid == 0) {
            $query = "SELECT `id`, `name`, `description`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` FROM ";
            $query.= "`MiejsceView` WHERE `zbiorcze`=1 ORDER BY `pomieszczenie`, `name`";
    } else if ($mid > 0) {
            $query = "SELECT `id`, `name`, `description`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` ";
            $query.= "FROM `MiejsceView` WHERE `id_pomieszczenie`=$mid ORDER BY `name`";
    } else {
        $query = "SELECT `id`, `name`, `description`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` FROM `MiejsceView`";
    }
} else {
    $query = "SELECT `id`, `name`, `description`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` FROM `MiejsceView`";
}


$result = mysqli_query($con, $query);
$miejscaarray = array();
while($row = mysqli_fetch_array($result)) {
	array_push($miejscaarray, array( 'id' => $row['id'], 
                                    'name' => $row['name'], 
                                    'pomieszczenie' => $row['pomieszczenie'], 
                                    'id_pomieszczenie' => $row['id_pomieszczenie'], 
                                    'description' => $row['description'], 
                                    'zbiorcze' => $row['zbiorcze'], 
                                    'kod' => $row['kod'], 
                                    'polaczenie' => $row['polaczenie'],
									'kable' => array()
									));
}
$count = count($miejscaarray);
$prev = -1;

for ($i = 0; $i < $count; $i++) {

    $query = "SELECT `pm`.`kabel_id` as `kid`, `p`.`description` as `descr`, `p`.`ilosc_zyl` as `cnt` ";
    $query .= "FROM `przewod_miejsce` `pm` LEFT JOIN `przewod` `p` on `p`.`id` = `pm`.`kabel_id` WHERE `pm`.`miejsce_id` = ". $miejscaarray[$i]['id'];
    $query .= " ORDER BY `pm`.`kabel_id`";
    
    $result = mysqli_query($con, $query);
	$k = '';
    $j = 0;
    
	while($row = mysqli_fetch_array($result)) {
        if ($prev != $row['kid']) {
            $prev = $row['kid'];
            array_push($miejscaarray[$i]['kable'], $row['kid']);
            $k = $k . '<a href="edit_kabel.php?id=' . $row['kid'] . '">' . $row['kid'] . '</a>, ';
        }
		$j += 1;
	}
	$k = $j . " : " . $k;
	//$miejscaarray[$i]['kable'] = $k;
    
}

$query = "SELECT `id`, `name` FROM `pomieszczenie` WHERE 1 ";
$result = mysqli_query($con, $query);

$pomieszczeniaarray = array();
while($row = mysqli_fetch_array($result)) {
    array_push($pomieszczeniaarray,
            array( "id" => $row['id'],
                "name" => $row['name']));
}

$opt = array(
    "miejsca" => $miejscaarray,
    "pomieszczenia" => $pomieszczeniaarray
);
echo json_encode ($opt);
mysqli_close($con);
?> 
