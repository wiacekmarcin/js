<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = mysqli_connect("127.0.0.1",$username,$password,$database);
mysqli_set_charset($con, "utf8");

$query = "SELECT `id`, `opis`, `ilosc_zyl` FROM `przewod` WHERE 1 ORDER by `id` ";
$przewodyindexarray = array();
$przewodyarray = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    array_push($przewodyindexarray, $row["id"]);
    $przewodyarray[$row['id']] = array(
        "opis" => $row["opis"],
        "il_zyl" => $row["ilosc_zyl"],
        "miejsca" => array(),
        "zyly" => array()
    );
}

$miejscearray = array();
$query = "SELECT `id`, `nazwa`, `opis`, `zbiorcze`, `polaczenie`, `pomieszczenie` FROM `MiejsceView` WHERE 1";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $miejscearray[$row['id']] = array(
        "nazwa" => $row['nazwa'],
        "opis" => $row['opis'],
        "zbior" => $row['zbiorcze'],
        "polac" => $row['polaczenie'],
        "pomie" => $row['pomieszczenie'],
    );
}


$przewodmiejscearray = array();
$query =  "SELECT `zid`, `etykieta`, `przewod_miejsce_id_zlacze`, `rodzaj_zakonczenia`, `przewod_id`, `miejsce_id`, ";
$query .= "`przewod_miejsce_id`, `nazwa`, `kod` FROM `PrzewodMiejsceZakonczenieView` WHERE 1";
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {

    array_push($przewodyarray[$row["przewod_id"]]["miejsca"], array(
        "pmid" => $row["przewod_miejsce_id"],
        "mid" => $row["miejsce_id"],
        "zakid" => $row["zid"],
        "etyk" => $row["etykieta"],
        "r_zak" => $row["rodzaj_zakonczenia"],
        "r_naz" => $row["nazwa"],
        "r_kod" => $row["kod"],
    ));
}

$query = "SELECT `id`, `przewod_id`, `opis`, `kolor`, `html` FROM `ZylaWidok` WHERE 1 ORdER by `przewod_id`";
$result = mysqli_query($con, $query);
$zylyarray = array();
while($row = mysqli_fetch_array($result)) {
    array_push($przewodyarray[$row['przewod_id']]["zyly"], $row["id"]);

    $zylyarray[$row['id']] = array(
        "kolor" => $row['kolor'],
        "opis" => $row['opis'],
        "html" => $row['html'],
        "pid" => $row["przewod_id"]
    );
}

$query = "SELECT `id`, `przewod_id`, `miejsce_id` FROM `przewod_miejsce` ORDER BY `przewod_id` ";
$przewod_miejsce = array();
$prevprzew = -1;
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($row["przewod_id"] != $prevprzew) {
        $przewod_miejsce[$row["przewod_id"]] = array();
        $prevprzew = $row["przewod_id"];
    }

    $przewod_miejsce[$row["przewod_id"]][$row["miejsce_id"]] = $row["id"];
};

$query = "SELECT `zkid`, `zakonczenie_id`, `przewod_miejsce_id`, `zyla_id`, `pos`, `zid`, `przewod_id`, `opis`, `kolor`, `html` ";
$query .= "FROM `ZlaczeKolejnoscView` WHERE 1";
$prevzak = -1;
$zakarr1 = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($row["przewod_miejsce_id"] != $prevzak) {
        $zakarr1[$row["przewod_miejsce_id"]] = array();
        $prevzak = $row["przewod_miejsce_id"];
    }
    array_push($zakarr1[$row["przewod_miejsce_id"]], array(
        "zyla_id" => $row["zyla_id"],
        "kolor" => $row["kolor"],
        "pos" => $row["pos"],
        "opis" => $row["opis"],
        "html" => $row["html"],
    ));
}

$query = "SELECT `id`, `zyla_id_1`, `zyla_id_2`, `zakonczenie_id` FROM `polaczenie_zyla` ORDER BY `zakonczenie_id`, `zyla_id_1` ";
$prevzik = -1;
$zakarr2 = array();
$result = mysqli_query($con, $query);
$prevzyla= -1;
while($row = mysqli_fetch_array($result)) {
    if ($prevzik  != $row["zakonczenie_id"]) {
        $zakarr2[$row["zakonczenie_id"]] = array();
        $prevzik  = $row["zakonczenie_id"];
        $prevzyla= -1;
    }
    if  ($prevzyla != $row["zyla_id_1"]) {
        $zakarr2[$row["zakonczenie_id"]][$row["zyla_id_1"]] = array();
        $prevzyla = $row["zyla_id_1"];
    }

    array_push($zakarr2[$row["zakonczenie_id"]][$row["zyla_id_1"]], $row["zyla_id_2"]);

}

$query = "SELECT `urzadzenie_zakonczenie`.`id`, `urzadzenie_zakonczenie`.`zakonczenie_id`, `urzadzenie_zakonczenie`.`zyla_id`, ";
$query .= "`urzadzenie_zakonczenie`.`opis`, `kolor`.`nazwa`, `kolor`.`html` ";
$query .= "FROM `urzadzenie_zakonczenie` LEFT JOIN `kolor` ON `kolor`.`id` = `urzadzenie_zakonczenie`.`kolor_id` ";
$query .= "ORDER by `urzadzenie_zakonczenie`.`zakonczenie_id` ";
$prevzik = -1;
$zakarr3 = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($prevzik  != $row["zakonczenie_id"]) {
        $zakarr3[$row["zakonczenie_id"]] = array();
        $prevzik  = $row["zakonczenie_id"];
    }
    array_push($zakarr3[$row["zakonczenie_id"]], array(
        "id" => $row["zyla_id"],
        "opis" => $row["opis"],
        "kolor" => $row["nazwa"],
        "html" => $row["html"]
    ));
}

$opt = array(
    'przewody' => $przewodyindexarray,
    'przewod' => $przewodyarray,
    'zyla' => $zylyarray,
    'miejsce' => $miejscearray,
    'przewod_miejsce' => $przewod_miejsce,
    "zakonczenie1" => $zakarr1,
    "zakonczenie2" => $zakarr2,
    "zakonczenie3" => $zakarr3
);

echo json_encode($opt);
mysqli_close($con);

?>