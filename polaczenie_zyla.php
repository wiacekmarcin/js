<?php
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `pid1`, `opis1`, `cname1`, `html1`, ";
$query.="`pid2`, `opis2`, `cname2`, `html2`, `miejsce_id`, `pol_opis` FROM `PolaczenieZylaWidok`";

$result = mysqli_query($con, $query);
$zyly = array();
$przewody = array();
$prevcid = -1;
while($row = mysqli_fetch_array($result)) {
    if ($prevcid != $row['pid1']) {
        array_push($przewody, $row['pid1']);
        $zyly[$row['pid1']] = array();
        $prevcid = $row['pid1'];
    }
    array_push($zyly[$row['pid1']], array(
        'pid2' => $row['pid2'],
        'opis1' => $row['opis1'],
        'opis2' => $row['opis2'],
        'cname1' => $row['cname1'],
        'cname2' => $row['cname2'],
        'html1' => $row['html1'],
        'html2' => $row['html2']
    ));
}
$opt = array(
    "zyly" => $zyly,
    'przewody' => $przewody,
);
echo json_encode ($opt);
mysqli_close($con);    

?>