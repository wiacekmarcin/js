<?php
require_once "db.php";
require_post();

$length = post_int('length', 0);
$zakonczenie_id = post_int('zkid');

tx(function () use ($length, $zakonczenie_id) {
    for ($i = 0; $i < $length; $i++) {
        $zyla_id = post_int("zyla_id_$i", -1);
        $id = post_int("id_$i", -1);
        $pos = post_int("pos_$i", 0);
        $opis = post_str("opis_$i");
        if ($zyla_id != -1) {
            if ($id != -1) {
                q("UPDATE `zakonczenie_zyly` SET `zyla_id` = ?, `pos` = ?, `opis` = ? WHERE `id` = ? AND `zakonczenie_id` = ?",
                    [$zyla_id, $pos, $opis, $id, $zakonczenie_id]);
            } else {
                q("INSERT INTO `zakonczenie_zyly` (`zakonczenie_id`, `zyla_id`, `pos`, `opis`) VALUES (?, ?, ?, ?)",
                    [$zakonczenie_id, $zyla_id, $pos, $opis]);
            }
        } elseif ($id != -1) {
            q("DELETE FROM `zakonczenie_zyly` WHERE `id` = ? AND `zakonczenie_id` = ?", [$id, $zakonczenie_id]);
        }
    }
});

json_out(["status" => "OK"]);
