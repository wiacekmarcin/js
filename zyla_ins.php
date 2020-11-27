<?php
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con,"utf8");

$params = array();
$count = 0;
if (isset($_POST['count']))
	$count = $_POST['count'];

for ($i = 0 ; $i < $count; $i++) {
	array_push($params , array('color_id' => $_POST['color_' . $i],
								'descr' => $_POST['descr_' . $i],
								'id' => $_POST['id_' . $i],
								'przewod_id' => $_POST['przewod'],
	));
}

$query = '';
for ($i = 0 ; $i < $count; $i++) {
	if ($params[$i]['id'] == -1) {
		$query = "INSERT INTO `zyla`(`id`, `color_id`, `przewod_id`, `opis`) VALUES (NULL, " . $params[$i]['color_id'] . ", " . $params[$i]['przewod_id'] . ", \"" . $params[$i]['descr'] . "\");";
	} else {
		$query = "UPDATE `zyla` SET `color_id`=" . $params[$i]['color_id'] . ", `opis`= \"" . $params[$i]['descr'] . "\" WHERE `id` = " . $params[$i]['id']. ";";
    }
    $result = mysqli_query($con, $query);
    echo $i . ($result ? '-OK ' : '-ERR ');
}

mysqli_close($con);

?>
