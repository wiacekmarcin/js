<?php
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con,"utf8");

$params = array();
$count = 0;
if (isset($_POST['count']))
	$count = $_POST['count'];

for ($i = 0 ; $i < $count; $i++) {
	array_push($params , array('kolor_id' => $_POST['kolor_' . $i],
								'opis' => $_POST['opis_' . $i],
								'id' => $_POST['id_' . $i],
								'przewod_id' => $_POST['przewod'],
	));
}

$query = '';
for ($i = 0 ; $i < $count; $i++) {
	if ($params[$i]['id'] == -1) {
		$query = "INSERT INTO `zyla`(`id`, `kolor_id`, `przewod_id`, `opis`) VALUES (NULL, " . $params[$i]['kolor_id'] . ", " . $params[$i]['przewod_id'] . ", \"" . $params[$i]['opis'] . "\");";
	} else {
		$query = "UPDATE `zyla` SET `kolor_id`=" . $params[$i]['kolor_id'] . ", `opis`= \"" . $params[$i]['opis'] . "\" WHERE `id` = " . $params[$i]['id']. ";";
    }
    $result = mysqli_query($con, $query);
    echo $i . ($result ? '-OK ' : '-ERR ');
}

mysqli_close($con);

?>
