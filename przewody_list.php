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

/*
$query = "SELECT `PolaczenieZylaWidok`.`id`, `PolaczenieZylaWidok`.`zyla_id_1`, `PolaczenieZylaWidok`.`zyla_id_2`, `PolaczenieZylaWidok`.`przewod_id1`, ";
$query.= "`PolaczenieZylaWidok`.`kolor1`, `PolaczenieZylaWidok`.`html1`, `PolaczenieZylaWidok`.`przewod_id2`, `PolaczenieZylaWidok`.`opis2`, ";
$query.= "`PolaczenieZylaWidok`.`kolor2`, `PolaczenieZylaWidok`.`html2`, `zakonczenie`.`przewod_miejsce_id` as `przewod_miejsce_id` ";
$query.= "FROM `PolaczenieZylaWidok` LEFT JOIN `zakonczenie` ON `zakonczenie`.`id` = `PolaczenieZylaWidok`.`zakonczenie_id` WHERE 1 ";
$query.= "ORDER BY `zakonczenie`.`przewod_miejsce_id`, `PolaczenieZylaWidok`.`zyla_id_1`, `PolaczenieZylaWidok`.`przewod_id2`";

$prevpolzyl = -1;
$zakarr2 = array();
$result = mysqli_query($con, $query);
$prevzyla = -1;
while($row = mysqli_fetch_array($result)) {
    if ($row["przewod_miejsce_id"] != $prevpolzyl) {
        $zakarr2[$row["przewod_miejsce_id"]] = array();
        $prevpolzyl = $row["przewod_miejsce_id"];
        $prevzyla = -1;
    }
    if ($prevzyla != $row["zyla_id_1"]) {
        $prevzyla != $row["zyla_id_1"];
        $zakarr2[$row["przewod_miejsce_id"]][$row["zyla_id_1"]] = array();
    }

    array_push($zakarr2[$row["przewod_miejsce_id"]][$row["zyla_id_1"]], array(
        "zyla_id_1" => $row["zyla_id_1"],
        "zyla_id_2" => $row["zyla_id_2"],
        "kolor1" => $row["kolor1"],
        "kolor2" => $row["kolor2"],
        "html1" => $row["html1"],
        "html2" => $row["html2"],
        "opis2" => $row["opis2"],
        "przewod_id2" => $row["przewod_id2"]
    ));
}




$query = "SELECT `zid`, `etykieta`, `przewod_miejsce_id_zlacze`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `przewod_id`, `miejsce_id`, `nazwa`, `kod` ";
$query.= "FROM `PrzewodMiejsceZakonczenieView` ORDER by `przewod_id`";
$prevpprzew = -1;
$przemiejscarr = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($row["przewod_id"] != $prevpprzew) {
        $przemiejscarr[$row["przewod_id"]] = array();
        $prevpprzew = $row["przewod_id"];
    }
    array_push($przemiejscarr[$row["przewod_id"]], array(
        "zakonczenie_id" => $row["zid"],
        "przewod_miejsce_id" => $row["przewod_miejsce_id"],
        "przewod_miejsce_id_zlacze" => $row["przewod_miejsce_id_zlacze"],
        "miejsce_id" => $row["miejsce_id"],
        "etykieta" => $row["etykieta"],
        "nazwa" => $row["nazwa"],
        "kod" => $row["kod"],

    ));
}

$query = "SELECT `id`, `nazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` FROM `MiejsceView` WHERE 1";
$miejscearr = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    $miejscearr[$row['id']] = array(
        "id" => $row["id"],
        "nazwa" => $row["nazwa"],
        "opis" => $row["opis"],
        "zbiorcze" => $row["zbiorcze"],
        "kod" => $row["kod"],
        "polaczenie" => $row["polaczenie"],
        "pomieszczenie" => $row["pomieszczenie"],
        "kod" => $row["kod"]
    );
}

$query = "SELECT `id`, `opis`, `ilosc_zyl` FROM `przewod` WHERE 1";
$przewodyarr = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    array_push($przewodyarr, array(
        "id" => $row["id"],
        "opis" => $row["opis"],
        "ilosc_zyl" => "" . $row["ilosc_zyl"],
    ));
}

$query = "SELECT `id`, `kolor_id`, `przewod_id`, `opis`, `kolor`, `html` FROM `ZylaWidok` WHERE 1 order by `przewod_id`";
$prevpprzew = -1;
$zylyarr = array();
$result = mysqli_query($con, $query);
while($row = mysqli_fetch_array($result)) {
    if ($row["przewod_id"] != $prevpprzew) {
        $zylyarr[$row["przewod_id"]] = array();
        $prevpprzew = $row["przewod_id"];
    }
    array_push($zylyarr[$row["przewod_id"]], array(
        "zyla_id" => $row["id"],
        "opis" => $row["opis"],
        "kolor" => $row["kolor"],
        "html" => $row["html"]
    ));
}





$opt = array(
    'miejsca_przewody' => $przemiejscarr,
    'przewody' => $przewodyarr,
    'zyly' => $zylyarr,
    'miejsca' => $miejscearr,
    "zakonczenie1" => $zakarr1,
    "zakonczenie2" => $zakarr2
);

echo json_encode($opt);
mysqli_close($con);

*/

$opt = array(
    'przewody' => $przewodyindexarray,
    'przewod' => $przewodyarray,
    'zyla' => $zylyarray,
    'miejsce' => $miejscearray,
    'przewod_miejsce' => $przewod_miejsce,
    "zakonczenie1" => $zakarr1,
    "zakonczenie2" => $zakarr2
);

echo json_encode($opt);
mysqli_close($con);

?>