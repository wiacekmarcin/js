<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once "database_new.php";
$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

#$query = "SELECT `kolor_id`, count(`kolor_id`) as `cnt` FROM `zyla` Group by `kolor_id`";
#$result = mysqli_query($con, $query);
#$clrarr = array();
#while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
#  $clrarr[$rs['kolor_id']] = $rs['cnt'];
#}

$query = "SELECT `id`, `nazwa`, `html`  FROM `kolorZyly` ";
$result = mysqli_query($con, $query);

$outp = "";
while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
  if ($outp != "") {$outp .= ",";}
  $outp .= '{"id":"'  . $rs["id"] . '",';
  $outp .= '"nazwa":"'   . $rs["nazwa"]        . '",';
  $outp .= '"html":"'. $rs["html"]     . '",';
  #$outp .= '"cnt":"'. $clrarr[$rs["id"]]" .'"';
  $outp .= '"cnt":"0"';
  $outp .=  '}';
}
$outp ='{"records":['.$outp.']}';
$con->close();

echo($outp);
?>

