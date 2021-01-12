<?php
require_once "database.php";

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con,"utf8");

$params = array();

$edit = $_POST["edit"];
$id = $_POST["id"];
$nazwa = $_POST["nazwa"];
$ilosc_pinow = $_POST["ilosc_pinow"];
$remove_pin = $_POST["remove_pin"];
$plyta_id = $_POST["plyta_id"];
$rodzaj_id = $_POST["rodzaj_id"];


$queries = array();

if ($edit == "true") {
    array_push($queries, "UPDATE `elementy_plytkowe` SET `nazwa`='$nazwa', `plytka_id`=$plyta_id, `rodzaj_urzadzenia`=$rodzaj_id, `ilosc_pin` = $ilosc_pinow WHERE `id` = $id");
    if ($remove_pin) {
        array_push($queries,"DELETE FROM `elementy_plytkowe_pin` WHERE `element_plytkowy_id` = $id");
    }
} else {
    array_push($queries, "INSERT INTO `elementy_plytkowe`(`id`, `nazwa`, `ilosc_pin`, `plytka_id`, `rodzaj_urzadzenia`) VALUES (NULL,'$nazwa', $ilosc_pinow, $plyta_id, $rodzaj_id)");

}

$count = count($queries);
print_r($queries);
$err = 0;
for ($i = 0; $i < $count; $i++) {
    if (!mysqli_query($con, $queries[$i])) {
        print ("ERR : " . $queries[$i]);
        $err = 1;
    }
    if ($edit != "true") {
        $id = $con->insert_id;
    }
}

$queries = [];
for ($i = 0 ; $i < $ilosc_pinow; $i++) {
    array_push($queries, "INSERT INTO `elementy_plytkowe_pin`(`id`, `nazwa`, `pos`, `element_plytkowy_id`) VALUES (NULL,'-',". ($i+1) . ",$id)");
}
print_r($queries);
$count = count($queries);
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