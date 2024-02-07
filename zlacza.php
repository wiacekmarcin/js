<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once "database.php";
error_reporting( E_ALL );
ini_set('display_errors', 1);

$con = db_connect();
mysqli_set_charset($con, "utf8");

$query="SELECT `zid`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `przewod_id`, `miejsce_id`, ";
$query.="`znazwa`, `zkod`, `ilosc_pin`, `mnazwa`, `mopis`, `zbiorcze`, `mkod`, `polaczenie`, `pomieszczenie`, ";
$query.="`popis`, `ilosc_zyl` FROM `ZakonczePrzewodMiejsce` WHERE 1 ORDER BY `przewod_id`, `miejsce_id`";
$result = mysqli_query($con, $query);

$k_urzadzenia = array();
$k_zlacza = array();
$k_wtyczki = array();
$k_polaczenia_kablowe = array();
$k_polaczenia_plytkowe = array();
$k_inne = array();

while($row = mysqli_fetch_array($result)) {
    $data = array(
        'zid' => $row['zid'], 
        'etykieta' => $row['etykieta'],
        'przewod_id' => $row['przewod_id'],
        'urzadzenie' => $row['znazwa'],
        'zkod' => $row['zkod'],
        'miejsce' => $row['mnazwa'],
        'pomieszczenie' => $row['pomieszczenie'],
        "przewod_miejsce_id" => $row["przewod_miejsce_id"],
        'opis' => $row['popis'],
        "ilosc_zyl" => $row['ilosc_zyl'],
        "ilosc_pin" => $row['ilosc_pin'],
        "rodzaj_zakonczenia" => $row["rodzaj_zakonczenia"]
    );
    
    if ($row['zkod'] == 'Z') {
        array_push($k_zlacza , $data);
    } 
    elseif ($row['zkod'] == 'U') {
        array_push($k_urzadzenia , $data);
    } 
    elseif ($row['zkod'] == 'P') {
        array_push($k_polaczenia_plytkowe , $data);
    } 
    elseif ($row['zkod'] == 'K') {
        array_push($k_polaczenia_kablowe , $data);
    } 
    elseif ($row['zkod'] == 'W') { 
        array_push($k_wtyczki , $data);
    }
    else {
        array_push($k_inne , $data);
    }
}

$query2 = "SELECT `id`, `nazwa`, `ilosc_pin`, `plytka_id`, `miejsce_id`, `pnazwa`, `urzadzenie_rodzaj_id`, ";
$query2 .= "`urzadzenie_nazwa`, `urzadzenie_rodzaj_kod`, `urzadzenie_plytka`, `urzadzenie_przewod`, ";
$query2 .= "`mnazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`, `pomieszczenie` ";
$query2 .= "FROM `ElementyPlytkoweView` WHERE 1 oRDER BY `miejsce_id`, `plytka_id`, `nazwa` ";
$result2 = mysqli_query($con, $query2);

$p_urzadzenia = array();
$p_zlacza = array();
$p_wtyczki = array();
$p_polaczenia_kablowe = array();
$p_polaczenia_plytkowe = array();
$p_inne = array();

while($row = mysqli_fetch_array($result2)) {
    $data = array(
        'pid' => $row['id'], 
        'etykieta' => $row['nazwa'],
        'plytka_id' => $row['plytka_id'],
        'urzadzenie' => $row['urzadzenie_nazwa'],
        'zkod' => $row['urzadzenie_rodzaj_kod'],
        'miejsce' => $row['mnazwa'],
        'pomieszczenie' => $row['pomieszczenie'],
        'pnazwa' => $row['pnazwa'],
        "ilosc_pin" => $row['ilosc_pin'],
        "rodzaj_zakonczenia" => $row["urzadzenie_rodzaj_id"]
    );
    
    if ($row['urzadzenie_rodzaj_kod'] == 'Z') {
        array_push($p_zlacza , $data);
    } 
    elseif ($row['urzadzenie_rodzaj_kod'] == 'U') {
        array_push($p_urzadzenia , $data);
    } 
    elseif ($row['urzadzenie_rodzaj_kod'] == 'P') {
        array_push($p_polaczenia_plytkowe , $data);
    } 
    elseif ($row['urzadzenie_rodzaj_kod'] == 'K') {
        array_push($p_polaczenia_kablowe , $data);
    } 
    elseif ($row['urzadzenie_rodzaj_kod'] == 'W') { 
        array_push($p_wtyczki , $data);
    }
    else {
        array_push($p_inne , $data);
    }
}

$sql = "SELECT `zw`.`id` as `zwid`, `zw`.`wtyczka_id` as `wtyczka_id`, `zw`.`zlacze_id` as `zlacze_id`, ";
$sql .="`z`.`zid`, `z`.`etykieta`, `z`.`przewod_miejsce_id`, `z`.`rodzaj_zakonczenia`, `z`.`przewod_id`, ";
$sql .="`z`.`miejsce_id`, `z`.`znazwa`, `z`.`zkod`, `z`.`ilosc_pin`, `z`.`mnazwa`, `z`.`mopis`, ";
$sql .="`z`.`zbiorcze`, `z`.`mkod`, `z`.`polaczenie`, `z`.`pomieszczenie`, `z`.`popis`, `z`.`ilosc_zyl` ";
$sql .="FROM `zlacze_wtyczka` `zw` LEFT JOIN `ZakonczePrzewodMiejsce` `z` ON `zw`.`wtyczka_id` = `z`.`zid` ";
$sql .="WHERE 1 ";
$zlacze_wtyczka = array();
$result3 = mysqli_query($con, $sql);
while($row = mysqli_fetch_array($result3)) {
    $zlacze_wtyczka[$row['zlacze_id']] = array(
        "wtyczka_id" => $row["wtyczka_id"],
        "etykieta" => $row["etykieta"],
        "przewod_id" => $row["przewod_id"],
        "znazwa" => $row["znazwa"],
        "zkod" => $row["zkod"],
        "ilosc_pin" => $row["ilosc_pin"],
        "mnazwa" => $row["mnazwa"],
        "pomieszczenie" => $row["pomieszczenie"],
        "opis" => $row["popis"],
        "ilosc_zyl" => $row["ilosc_zyl"]
    );
};

$sql = "SELECT `zw`.`id`, `zw`.`wtyczka_id`, `zw`.`zlacze_id`,`ep`.`id` as `epid`, `ep`.`nazwa`, ";
$sql.= "`ep`.`ilosc_pin`, `ep`.`plytka_id`, `ep`.`miejsce_id`, `ep`.`pnazwa`, `ep`.`urzadzenie_rodzaj_id`, ";
$sql.= "`ep`.`urzadzenie_nazwa`, `ep`.`urzadzenie_rodzaj_kod`, `ep`.`urzadzenie_plytka`, ";
$sql.= "`ep`.`urzadzenie_przewod`, `ep`.`mnazwa`, `ep`.`opis`, `ep`.`zbiorcze`, `ep`.`id_pomieszczenie`, ";
$sql.= "`ep`.`kod`, `ep`.`polaczenie`, `ep`.`pomieszczenie` FROM `zlacze_wtyczka` `zw` LEFT JOIN ";
$sql.= "`ElementyPlytkoweView` `ep` ON `ep`.`id` = `zw`.`zlacze_id` WHERE 1";
$wtyczka_zlacze = array();

$result3 = mysqli_query($con, $sql);
while($row = mysqli_fetch_array($result3)) {
    $wtyczka_zlacze[$row['wtyczka_id']] = array(
        "zlacze_id" => $row["zlacze_id"],
        "etykieta" => $row["nazwa"],
        "plytka_id" => $row["plytka_id"],
        "znazwa" => $row["urzadzenie_nazwa"],
        "zkod" => $row["urzadzenie_rodzaj_kod"],
        "ilosc_pin" => $row["ilosc_pin"],
        "mnazwa" => $row["mnazwa"],
        "pomieszczenie" => $row["pomieszczenie"],
        "plytka_opis" => $row["pnazwa"]
    );
};


$sql = "SELECT `id`, `etykieta`, `przewod_id` FROM `ZakonczenieView` WHERE rodzaj_zakonczenia = 1 ORDER BY `etykieta`, `przewod_id`";

$wtyczki = array();
$result3 = mysqli_query($con, $sql);
while($row = mysqli_fetch_array($result3)) {
    array_push($wtyczki, array(
        "id" => $row["id"],
        "etykieta" => $row["etykieta"],
        "przewod_id" => $row["przewod_id"],
    ));
}
$sql = "SELECT `id`, `kolor_id`, `przewod_id`, `opis`, `kolor`, `html` FROM `ZylaWidok` WHERE 1";
$zyly = array();
$result3 = mysqli_query($con, $sql);
while($row = mysqli_fetch_array($result3)) {
    $zyly[$row["id"]] = array(
        "id" => $row["id"],
        "kolor_id" => $row["kolor_id"],
        "przewod_id" => $row["przewod_id"],
        "opis" => $row["opis"],
        "kolor" => $row["kolor"],
        "html" => $row["html"]
    );
}

$sql = "SELECT `id`, `pinnazwa`, `pos`, `element_plytkowy_id`, `elementnazwa`, `ilosc_pin`, `plytka_id`, ";
$sql.= "`rodzaj_urzadzenia` FROM `ElementyPlytkowePinView` WHERE 1 ORDER BY `pos`";
$piny = array();
$result3 = mysqli_query($con, $sql);
while($row = mysqli_fetch_array($result3)) {
    $piny[$row["id"]] = array(
        "id" => $row["id"],
        "pos" => $row["pos"],
        "pinnazwa" => $row["pinnazwa"],
        "epid" => $row["element_plytkowy_id"],
        "enazwa" => $row["elementnazwa"],
        "ilosc_pin" => $row["ilosc_pin"],
        "plytka_id" => $row["plytka_id"],
    );
}

$sql = "SELECT `zzid`, `zakonczenie_id`, `zyla_id`, `pos`, `opis`, `zid`, `etykieta`, `przewod_miejsce_id`, ";
$sql.= "`rodzaj_zakonczenia` FROM `ZakonczenieZylyView` WHERE 1 ORDER BY `pos`";
$zakon = array();
$result3 = mysqli_query($con, $sql);
while($row = mysqli_fetch_array($result3)) {
    $zakon[$row["zzid"]] = array(
        "zakonczenie_id" => $row["zakonczenie_id"],
        "zyla_id" => $row["zyla_id"],
        "opis" => $row["opis"],
        "zid" => $row["zid"],
        "etykieta" => $row["etykieta"],
    );
}

$sql = "SELECT `zakonczenie_id`, `zyla_id`, `pos` FROM `ZakonczenieZylyView` WHERE 1 ORDER BY `zakonczenie_id`, `pos` ";
$zakonId = array();
$result3 = mysqli_query($con, $sql);
$zid = -1;
while($row = mysqli_fetch_array($result3)) {
    if ($zid != $row["zakonczenie_id"]) {
        $zakonId[$row["zakonczenie_id"]] = array();
        $zid = $row["zakonczenie_id"];
    }
    array_push($zakonId[$row["zakonczenie_id"]], array(
        "id"=>$row["zyla_id"],
        "pos"=>$row["pos"],
    ));
}

$sql = "SELECT `id`, `pos`, `element_plytkowy_id` FROM `ElementyPlytkowePinView` WHERE 1 ORDER BY `element_plytkowy_id`, `pos`";
$plytkaId = array();
$result3 = mysqli_query($con, $sql);
$zid = -1;
while($row = mysqli_fetch_array($result3)) {
    if ($zid != $row["element_plytkowy_id"]) {
        $plytkaId[$row["element_plytkowy_id"]] = array();
        $zid = $row["element_plytkowy_id"];
    }
    array_push($plytkaId[$row["element_plytkowy_id"]], array(
        "id"=>$row["id"],
        "pos"=>$row["pos"],
    ));
}

$sql = "SELECT `ppp`.`id` as `pppid`, `ppp`.`polaczenie_plytka_id`, `ppp`.`elementy_plytkowe_piny_id`, ";
$sql.= "`pp`.`id` as `ppid`, `pp`.`nazwa`, `pp`.`plytka_id` FROM `polaczenie_plytka_polaczenie` `ppp` ";
$sql.= "LEFT JOIN `polaczenie_plytka` `pp` ON `ppp`.`polaczenie_plytka_id` = `pp`.`id` WHERE 1 ";
$sql.= "ORDER BY `ppid`";

$pnazwa = array();
$result3 = mysqli_query($con, $sql);
$zid = -1;
$polaczenia_plytkowe = array();
while($row = mysqli_fetch_array($result3)) {
    if ($zid != $row["ppid"]) {
        $polaczenia_plytkowe[$row["ppid"]] = array();
        $zid = $row["ppid"];
    }
    array_push($polaczenia_plytkowe[$row["ppid"]], $row["elementy_plytkowe_piny_id"]);

    $pnazwa[$row["elementy_plytkowe_piny_id"]] = array( 
        "id"=>$row["ppid"],
        "nazwa"=>$row["nazwa"],
    );
}
$opt = array(
    'k_urzadzenia' => $k_urzadzenia,
    'k_zlacza' => $k_zlacza,
    'k_wtyczki' => $k_wtyczki,
    'k_polaczenia_kablowe' => $k_polaczenia_kablowe,
    'k_polaczenia_plytkowe' => $k_polaczenia_plytkowe,
    'k_inne' => $k_inne,
    'p_urzadzenia' => $p_urzadzenia,
    'p_zlacza' => $p_zlacza,
    'p_wtyczki' => $p_wtyczki,
    'p_polaczenia_kablowe' => $p_polaczenia_kablowe,
    'p_polaczenia_plytkowe' => $p_polaczenia_plytkowe,
    'p_inne' => $p_inne,
    'zlacze_wtyczka' => $zlacze_wtyczka,
    'wtyczka_zlacze' => $wtyczka_zlacze,
    'wtyczki' => $wtyczki,
    'zyly' => $zyly,
    'piny' => $piny,
    'zakon' => $zakon,
    'zakonId' => $zakonId,
    'plytkaId' => $plytkaId,
    'pnazwa' => $pnazwa,
    'polaczenia_plytkowe' => $polaczenia_plytkowe
);

echo json_encode($opt);
mysqli_close($con);

?>