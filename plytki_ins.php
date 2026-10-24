<?php
require_once "db.php";
require_post();

$edit = post_str('edit') === 'true';
$id = post_int('id', -1);
$nazwa = post_str('nazwa');
$miejsce_id = post_int('miejsce_id');

if ($edit) {
    q("UPDATE `plytki` SET `nazwa` = ?, `miejsce_id` = ? WHERE `id` = ?", [$nazwa, $miejsce_id, $id]);
} else {
    q("INSERT INTO `plytki` (`nazwa`, `miejsce_id`) VALUES (?, ?)", [$nazwa, $miejsce_id]);
    $id = db()->insert_id;
}

json_out(["status" => "OK", "id" => $id]);
