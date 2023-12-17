<?php
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con,"utf8");

$params = array();
$count = 0;
if (isset($_POST['count']))
	$count = $_POST['count'];

for ($i = 0 ; $i < $count; $i++) {
	array_push($params , array('id1' => $_POST['id1_' . $i],
								'id2' => $_POST['id2_' . $i],
								'pmid' => $_POST['polaczenie_miejsce_id'],
    ));
    array_push($params , array('id1' => $_POST['id2_' . $i],
								'id2' => $_POST['id1_' . $i],
								'pmid' => $_POST['polaczenie_miejsce_id'],
	));
}

$query = '';
for ($i = 0 ; $i < 2*$count; $i++) {
    //$query = "INSERT INTO `polaczenie_zyla`(`id`, `polaczenie_id`, `zyla_id_1`, `zyla_id_2`) VALUES (NULL,";
    //$query .= $params[$i]['pmid'] . ',' . $params[$i]['id1'] . ',' . $params[$i]['id2'] .  ')';
	$query = "INSERT INTO `polaczenie_zyla`(`id`, `zakonczenie_zyly_id`, `zyla_id`) VALUES (NULL,";
    $query .= $params[$i]['pmid'] . ',' . $params[$i]['id1'] . ')';
    $result = mysqli_query($con, $query);
	echo $query . ";";
    //echo $i . ($result ? '-OK ' : '-ERR '. $query . ' | ');
	$query = "INSERT INTO `polaczenie_zyla`(`id`, `zakonczenie_zyly_id`, `zyla_id`) VALUES (NULL,";
    $query .= $params[$i]['pmid'] . ',' . $params[$i]['id2'] . ')';
    $result = mysqli_query($con, $query);
	echo $query . ";";
    //echo $i . ($result ? '-OK ' : '-ERR '. $query . ' | ');
}

mysqli_close($con);

?>
