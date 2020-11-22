<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

require_once "database.php";
$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `color_id`, count(`color_id`) as `cnt` FROM `zyla` Group by `color_id`";
$result = mysqli_query($con, $query);
$clrarr = array();
while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
  $clrarr[$rs['color_id']] = $rs['cnt'];
}

$query = "SELECT `id`, `name`, `html`  FROM `KolorView` ";
$result = mysqli_query($con, $query);

$outp = "";
while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
  if ($outp != "") {$outp .= ",";}
  $outp .= '{"id":"'  . $rs["id"] . '",';
  $outp .= '"name":"'   . $rs["name"]        . '",';
  $outp .= '"html":"'. $rs["html"]     . '",';
  $outp .= '"cnt":"'. $clrarr[$rs["id"]]     . '"}';
}
$outp ='{"records":['.$outp.']}';
$con->close();

echo($outp);
?>

