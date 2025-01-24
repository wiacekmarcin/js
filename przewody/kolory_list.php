<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

require_once "database.php";
$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `kolor_id`, count(`kolor_id`) as `cnt` FROM `zyla` Group by `kolor_id`";
$result = mysqli_query($con, $query);
$clrarr = array();
while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
  $clrarr[$rs['kolor_id']] = $rs['cnt'];
}

$query = "SELECT `id`, `nazwa`, `html`  FROM `KolorView` ";
$result = mysqli_query($con, $query);

$outp = "";
while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
  if ($outp != "") {$outp .= ",";}
  $outp .= '{"id":"'  . $rs["id"] . '",';
  $outp .= '"nazwa":"'   . $rs["nazwa"]        . '",';
  $outp .= '"html":"'. $rs["html"]     . '",';
  $outp .= '"cnt":"'. $clrarr[$rs["id"]]     . '"}';
}
$outp ='{"records":['.$outp.']}';
$con->close();

echo($outp);
?>

