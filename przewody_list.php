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
        "ilosc_zyl" => $row["ilosc_zyl"],
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

$query = "SELECT `id`, `przewod_id`, `opis`, `kolor`, `html`, `kolor_id` FROM `ZylaWidok` WHERE 1 ORdER by `przewod_id`";
$result = mysqli_query($con, $query);
$zylyarray = array();

while($row = mysqli_fetch_array($result)) {
    array_push($przewodyarray[$row['przewod_id']]["zyly"], $row["id"]);
    $zylyarray[$row['id']] = array(
        "kolor" => $row['kolor'],
        "opis" => $row['opis'],
        "html" => $row['html'],
        "pid" => $row["przewod_id"],
        "kolor_id" => $row["kolor_id"]
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


$query = "SELECT `zzid`, `zakonczenie_id`, `zyla_id`, `pos`, `opis`, `zid`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia` ";
$query .= "FROM `ZakonczenieZylyView` WHERE 1 ORDER BY `przewod_miejsce_id`, `pos`";
$prevpmid = -1;
$zakarr = array();
$result = mysqli_query($con, $query);

while($row = mysqli_fetch_array($result)) {
    if ($row["przewod_miejsce_id"] != $prevpmid) {
        $zakarr[$row["przewod_miejsce_id"]] = array();
        $prevpmid = $row["przewod_miejsce_id"];
    }
    array_push($zakarr[$row["przewod_miejsce_id"]], array(
        "zyla_id" => $row["zyla_id"],
        "pos" => $row["pos"],
        "opis" => $row["opis"],
        "id" => $row["zzid"],
        "zakonczenie_id" => $row["zakonczenie_id"]
    ));
}


$query = "SELECT `id`, `zakonczenie_zyly_id`, `zyla_id` FROM `polaczenie_zyla` WHERE 1 ORDER by `zakonczenie_zyly_id`";
$prevzik = -1;
$arraypolaczenie = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($prevzik  != $row["zakonczenie_zyly_id"]) {
        $arraypolaczenie[$row["zakonczenie_zyly_id"]] = array();
        $prevzik  = $row["zakonczenie_zyly_id"];
    }
    
    array_push($arraypolaczenie[$row["zakonczenie_zyly_id"]], $row["zyla_id"]);

}


$query = "SELECT `zid_1`, `et_1`, `rz_1`, `ip_z1`, `zid_2`, `et_2`, `plytka_id`, `rz_2`, `ip_z2`, `ply_nazwa`, `miejsce_1`, `przewod`, `miejsce_2` FROM `ZlaczeWtyczka` WHERE 1";
$result = mysqli_query($con, $query);
$zlaczewtyczka = array();
while($row = mysqli_fetch_array($result)) {
    $zlaczewtyczka[$row["zid_1"]] = array(
        "wtyczka" => $row["et_1"],
        "wtyczka_id" => $row["zid_1"],
        "zlacze" => $row["et_2"],
        "zlacze_id" => $row["zid_2"],
        "plytka_id" => $row["plytka_id"],
        "plytka" => $row["ply_nazwa"]
    );
}

$query = "SELECT `id`, `nazwa`, `html`  FROM `KolorView` ";
$result = mysqli_query($con, $query);
$kolory = array();
while($row = mysqli_fetch_array($result)) {
    array_push($kolory, array(
        "id" => $row["id"],
        "kolor" => $row["nazwa"],
        "html" => $row["html"]
    ));
}

$arrayurzadzenia = array();

$opt = array(
    'przewody' => $przewodyindexarray,
    'przewod' => $przewodyarray,
    'zyla' => $zylyarray,
    'miejsce' => $miejscearray,
    'przewod_miejsce' => $przewod_miejsce,
    "zakonczenie" => $zakarr,
    "polaczenia" => $arraypolaczenie,
    "urzadzenia" => $arrayurzadzenia,
    "kolory" => $kolory,
    "zlaczewtyczka" => $zlaczewtyczka
);

echo json_encode($opt);
mysqli_close($con);

?>