<?php
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con,"utf8");


$queries = array();

$length = $_POST["length"];
for ($i = 0; $i < $length; $i++)
{
    $key = $_POST["index_" . $i];
    $nazwa = $_POST["nazwa_" . $key];
    $pos = $_POST["pos_" . $key];
    array_push($queries, 
            "UPDATE `elementy_plytkowe_pin` SET `nazwa`='$nazwa', `pos`=$pos WHERE id = $key"
        );
}



$count = count($queries);
print_r($queries);
$err = 0;
for ($i = 0; $i < $count; $i++) {
    if (!mysqli_query($con, $queries[$i])) {
        print ("ERR : " . $queries[$i]);
        $err = 1;
    }
}


if ($err == 0)
    print ("OK");
mysqli_close($con);
?>