<?php
require_once "db.php";
require_post();

$count = post_int('count', 0);
$pmid = $count > 0 ? post_int('polaczenie_miejsce_id') : 0;

tx(function () use ($count, $pmid) {
    $stmt = db()->prepare("INSERT INTO `polaczenie_zyla` (`polaczenie_id`, `zyla_id_1`, `zyla_id_2`) VALUES (?, ?, ?)");
    for ($i = 0; $i < $count; $i++) {
        $a = post_int("id1_$i");
        $b = post_int("id2_$i");
        // Połączenie zapisujemy symetrycznie (a-b i b-a).
        foreach ([[$a, $b], [$b, $a]] as [$z1, $z2]) {
            $stmt->bind_param("iii", $pmid, $z1, $z2);
            $stmt->execute();
        }
    }
});

json_out(["status" => "OK"]);
