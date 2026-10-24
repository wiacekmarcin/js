<?php
require_once "db.php";
require_post();

$zid = post_int('id', -1);
$p = [post_str('nazwa'), post_int('przewod_miejsce_id'), post_int('rodzaj'), post_int('ilosc_pin')];

if ($zid == -1) {
    q("INSERT INTO `zakonczenie` (`etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `ilosc_pin`) VALUES (?, ?, ?, ?)", $p);
    $zid = db()->insert_id;
} else {
    q("UPDATE `zakonczenie` SET `etykieta` = ?, `przewod_miejsce_id` = ?, `rodzaj_zakonczenia` = ?, `ilosc_pin` = ? WHERE `id` = ?", [...$p, $zid]);
}

json_out(["status" => "OK", "zid" => $zid]);
