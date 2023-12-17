<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");
$query = "SELECT `id`, `nazwa`, `zbiorcze`, `kod`, `polaczenie`, `pomieszczenie` FROM `MiejsceView` WHERE `polaczenie` = 1";

$result = mysqli_query($con, $query);
$miejscaarray = array();
$zbiorczearray = array();
while($row = mysqli_fetch_array($result)) {
	array_push($miejscaarray, array( 'id' => $row['id'], 
                                    'name' => $row['nazwa'] . " (" . $row['pomieszczenie'] . ")", 
									'kable' => array()
                                    ));
    $zbiorczearray[$row['id']] = $row['zbiorcze'];
}
$count = count($miejscaarray);
$prev = -1;
$zylyarray = array();
$k = '(';
for ($i = 0; $i < $count; $i++) {

    $query = "SELECT `pm`.`przewod_id` as `kid`, `p`.`opis` as `descr`, `p`.`ilosc_zyl` as `cnt` ";
    $query .= "FROM `przewod_miejsce` `pm` LEFT JOIN `przewod` `p` on `p`.`id` = `pm`.`przewod_id` WHERE `pm`.`miejsce_id` = ". $miejscaarray[$i]['id'];
    $query .= " ORDER BY `pm`.`przewod_id`";
    
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

$query = "SELECT `id`, `przewod_id`, `opis`, `kolor`, `html` FROM `ZylaWidok` WHERE `przewod_id` in " . $k . " ORDER BY `kolor` ";

$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
	array_push($zylyarray[$row['przewod_id']], array( 'id' => $row['id'], 
                                    'opis' => $row['opis'],
                                    'cname' => $row['kolor'],
                                    'chtml' => $row['html'],
                                    ));
}

$prevmid = -1;
$query = "SELECT `zid`, concat(`przewod_id`, ':', `etykieta`) as `nazwa`, `miejsce_id`, `przewod_id` FROM `ZakonczePrzewodMiejsce` WHERE `rodzaj_zakonczenia` = 2 AND `polaczenie` = 1 ORDER BY `miejsce_id`" ; 
$result = mysqli_query($con, $query);
$polmiejsce = array();
while($row = mysqli_fetch_array($result)) {
    if ($prevmid != $row['miejsce_id']) {
        $prevmid = $row['miejsce_id'];
        $polmiejsce[$row['miejsce_id']] = array();
    }
    array_push($polmiejsce[$row['miejsce_id']], array(
        'id' => $row['zid'],
        'name' => $row['nazwa'],
        'przewod_id' => $row['przewod_id']
    ));
}
$opt = array(
    "miejsca" => $miejscaarray,
    "zbiorcze" => $zbiorczearray,
    "zyly" => $zylyarray,
    "polmiejsca" => $polmiejsce
);
echo json_encode ($opt);
mysqli_close($con);
?>