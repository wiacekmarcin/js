<?php
require_once "db.php";
require_post();

$length = post_int('length', 0);

tx(function () use ($length) {
    $stmt = db()->prepare("UPDATE `elementy_plytkowe_pin` SET `nazwa` = ?, `pos` = ? WHERE `id` = ?");
    for ($i = 0; $i < $length; $i++) {
        $key = post_int("index_$i");
        $nazwa = post_str("nazwa_$key");
        $pos = post_int("pos_$key");
        $stmt->bind_param("sii", $nazwa, $pos, $key);
        $stmt->execute();
    }
});

json_out(["status" => "OK"]);
