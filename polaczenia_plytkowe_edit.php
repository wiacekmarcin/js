<?php
require_once "db.php";
require_post();

$id = post_int('id', -1);
$nazwa = post_str('nazwa');

if ($id != -1) {
    q("UPDATE `polaczenie_plytka` SET `nazwa` = ? WHERE `id` = ?", [$nazwa, $id]);
} else {
    q("INSERT INTO `polaczenie_plytka` (`nazwa`, `plytka_id`) VALUES (?, ?)", [$nazwa, post_int('plytka_id')]);
    $id = db()->insert_id;
}

json_out(["status" => "OK", "id" => $id]);
