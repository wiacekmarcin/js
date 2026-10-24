<?php
require_once "db.php";
require_post();

q("INSERT INTO `polaczenie_plytka_polaczenie` (`polaczenie_plytka_id`, `elementy_plytkowe_piny_id`) VALUES (?, ?)",
    [post_int('id'), post_int('pin')]);

json_out(["status" => "OK", "id" => db()->insert_id]);
