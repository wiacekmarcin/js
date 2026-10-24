<?php
require_once "db.php";
require_post();

$edit = post_str('edit') === 'true';
$id = post_int('id');
$opis = post_str('opis');
$ilosc_zyl = post_int('ilosc_zyl');
$miejsce_id_1 = post_int('miejsce_id_1');
$miejsce_id_2 = post_int('miejsce_id_2');

tx(function () use ($edit, $id, $opis, $ilosc_zyl, $miejsce_id_1, $miejsce_id_2) {
    if ($edit) {
        q("UPDATE `przewod` SET `opis` = ?, `ilosc_zyl` = ? WHERE `id` = ?", [$opis, $ilosc_zyl, $id]);
        $sql = "UPDATE `przewod_miejsce` SET `miejsce_id` = ? WHERE `id` = ? AND `przewod_id` = ?";
        q($sql, [$miejsce_id_1, post_int('pmid_1'), $id]);
        q($sql, [$miejsce_id_2, post_int('pmid_2'), $id]);
    } else {
        q("INSERT INTO `przewod` (`id`, `opis`, `ilosc_zyl`) VALUES (?, ?, ?)", [$id, $opis, $ilosc_zyl]);
        $sql = "INSERT INTO `przewod_miejsce` (`przewod_id`, `miejsce_id`) VALUES (?, ?)";
        q($sql, [$id, $miejsce_id_1]);
        q($sql, [$id, $miejsce_id_2]);
    }
});

json_out(["status" => "OK", "id" => $id]);
