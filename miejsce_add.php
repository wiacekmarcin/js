<?php
require_once "db.php";
require_post();

$id = post_int('id', -1);
$p = [
    post_str('nazwa'),
    post_str('opis'),
    post_bool('zbiorcze'),
    post_int('id_pomieszczenie'),
    post_str('kod'),
    post_bool('polaczenie'),
];

if ($id == -1) {
    q("INSERT INTO `miejsce` (`nazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`) VALUES (?, ?, ?, ?, ?, ?)", $p);
    $id = db()->insert_id;
} else {
    q("UPDATE `miejsce` SET `nazwa` = ?, `opis` = ?, `zbiorcze` = ?, `id_pomieszczenie` = ?, `kod` = ?, `polaczenie` = ? WHERE `id` = ?", [...$p, $id]);
}

json_out(["status" => "OK", "id" => $id]);
