<?php
require_once "db.php";
require_post();

$edit = post_str('edit') === 'true';
$id = post_int('id', -1);
$nazwa = post_str('nazwa');
$ilosc_pinow = post_int('ilosc_pinow');
$plyta_id = post_int('plyta_id');
$rodzaj_id = post_int('rodzaj_id');

if ($ilosc_pinow < 0 || $ilosc_pinow > 1000) {
    fail("Niepoprawna ilość pinów");
}

$id = tx(function () use ($edit, $id, $nazwa, $ilosc_pinow, $plyta_id, $rodzaj_id) {
    $recreate = true;
    if ($edit) {
        $old = q_one("SELECT `ilosc_pin` FROM `elementy_plytkowe` WHERE `id` = ? FOR UPDATE", [$id]);
        if (!$old) {
            fail("Nie znaleziono elementu", 404);
        }
        // Piny (z nazwami) odtwarzamy tylko, gdy zmieniła się ich liczba.
        $recreate = (int)$old['ilosc_pin'] !== $ilosc_pinow;
        q("UPDATE `elementy_plytkowe` SET `nazwa` = ?, `plytka_id` = ?, `rodzaj_urzadzenia` = ?, `ilosc_pin` = ? WHERE `id` = ?",
            [$nazwa, $plyta_id, $rodzaj_id, $ilosc_pinow, $id]);
        if ($recreate) {
            q("DELETE FROM `elementy_plytkowe_pin` WHERE `element_plytkowy_id` = ?", [$id]);
        }
    } else {
        q("INSERT INTO `elementy_plytkowe` (`nazwa`, `ilosc_pin`, `plytka_id`, `rodzaj_urzadzenia`) VALUES (?, ?, ?, ?)",
            [$nazwa, $ilosc_pinow, $plyta_id, $rodzaj_id]);
        $id = db()->insert_id;
    }

    if ($recreate) {
        $stmt = db()->prepare("INSERT INTO `elementy_plytkowe_pin` (`nazwa`, `pos`, `element_plytkowy_id`) VALUES ('-', ?, ?)");
        $pos = 0;
        $stmt->bind_param("ii", $pos, $id);
        for ($pos = 1; $pos <= $ilosc_pinow; $pos++) {
            $stmt->execute();
        }
    }
    return $id;
});

json_out(["status" => "OK", "id" => $id]);
