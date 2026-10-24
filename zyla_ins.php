<?php
require_once "db.php";
require_post();

$count = post_int('count', 0);
$przewod_id = $count > 0 ? post_int('przewod') : 0;

$ids = tx(function () use ($count, $przewod_id) {
    $ids = [];
    for ($i = 0; $i < $count; $i++) {
        $id = post_int("id_$i", -1);
        $kolor = post_int("kolor_$i");
        $opis = post_str("opis_$i");
        if ($id == -1) {
            q("INSERT INTO `zyla` (`kolor_id`, `przewod_id`, `opis`) VALUES (?, ?, ?)", [$kolor, $przewod_id, $opis]);
            $id = db()->insert_id;
        } else {
            q("UPDATE `zyla` SET `kolor_id` = ?, `opis` = ? WHERE `id` = ?", [$kolor, $opis, $id]);
        }
        $ids[] = $id;
    }
    return $ids;
});

json_out(["status" => "OK", "ids" => $ids]);
