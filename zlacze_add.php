<?php
require_once "db.php";

$przewody = q_all("SELECT `id`, `opis` AS `descr`, `ilosc_zyl` FROM `przewod` ORDER BY `id`");

json_out(["przewody" => $przewody]);
