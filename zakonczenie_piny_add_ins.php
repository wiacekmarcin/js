<?php
require_once "database.php";

$con = db_connect();
mysqli_set_charset($con,"utf8");

$length = $_POST["length"];
$zakonczenie_id = $_POST["zkid"];
$queries = array();
for ($i = 0; $i < $length; $i++)
{
    $opis = $_POST["opis_" . $i];
    $zyla_id = $_POST["zyla_id_" . $i];
    $pos = $_POST["pos_" . $i];
    $id = $_POST["id_" . $i];
    print $zyla_id . " " . $id . "\n";
    if ($zyla_id != -1) {
        
        if ($id != -1)
            array_push($queries, 
            "UPDATE `zakonczenie_zyly` SET `zyla_id`=$zyla_id,`pos`=$pos,`opis`='$opis' WHERE `id`=$id"
            );
        else
            array_push($queries, 
            "INSERT INTO `zakonczenie_zyly`(`id`, `zakonczenie_id`, `zyla_id`, `pos`, `opis`) VALUES (NULL,$zakonczenie_id,$zyla_id,$pos,'$opis')"
        );
    } elseif ($id != -1) {
        array_push($queries, 
            "DELETE FROM `zakonczenie_zyly` WHERE `id`=$id"
        );
    }
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