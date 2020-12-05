

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `PolaczenieView`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `PolaczenieView`;
CREATE TABLE `PolaczenieView` (
`pid` smallint(11)
,`miejsce_id` tinyint(3) unsigned
,`opis` text
,`mid` tinyint(3) unsigned
,`nazwa` text
,`opis` text
,`zbiorcze` tinyint(1)
,`id_pomieszczenie` tinyint(3) unsigned
,`kod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` text
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `PolaczenieZylaWidok`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `PolaczenieZylaWidok`;
CREATE TABLE `PolaczenieZylaWidok` (
`id` smallint(6)
,`polaczenie_id` smallint(6)
,`zyla_id_1` smallint(6) unsigned
,`zyla_id_2` smallint(6) unsigned
,`cid1` tinyint(3) unsigned
,`pid1` tinyint(3) unsigned
,`opis1` text
,`cname1` text
,`html1` text
,`cid2` tinyint(3) unsigned
,`pid2` tinyint(3) unsigned
,`opis2` text
,`cname2` text
,`html2` text
,`miejsce_id` tinyint(3) unsigned
,`pol_opis` text
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `polaczenie_zyla`
--

DROP TABLE IF EXISTS `polaczeniezyl`;
CREATE TABLE `polaczenie_zyla` (
  `id` smallint(6) NOT NULL,
  `polaczenie_id` smallint(6) NOT NULL,
  `zyla_id_1` smallint(6) UNSIGNED NOT NULL,
  `zyla_id_2` smallint(6) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELACJE DLA TABELI `polaczenie_zyla`:
--   `zyla_id_1`
--       `zyla` -> `id`
--   `zyla_id_2`
--       `zyla` -> `id`
--   `polaczenie_id`
--       `polaczenie` -> `id`
--

--
-- Tabela Truncate przed wstawieniem `polaczenie_zyla`
--

TRUNCATE TABLE `polaczenie_zyla`;
--
-- Zrzut danych tabeli `polaczenie_zyla`
--

INSERT INTO `polaczenie_zyla` (`id`, `polaczenie_id`, `zyla_id_1`, `zyla_id_2`) VALUES
(3, 1, 1, 398),
(5, 1, 2, 399),
(7, 1, 3, 401),
(1, 1, 4, 400),
(9, 1, 5, 404),
(11, 1, 6, 402),
(13, 1, 7, 405),
(15, 1, 8, 403),
(4, 1, 398, 1),
(6, 1, 399, 2),
(2, 1, 400, 4),
(8, 1, 401, 3),
(12, 1, 402, 6),
(16, 1, 403, 8),
(10, 1, 404, 5),
(14, 1, 405, 7),
(35, 2, 256, 315),
(17, 2, 257, 278),
(19, 2, 258, 277),
(21, 2, 259, 276),
(23, 2, 260, 275),
(53, 2, 261, 274),
(27, 2, 262, 273),
(31, 2, 263, 272),
(49, 2, 264, 271),
(33, 2, 265, 270),
(34, 2, 270, 265),
(50, 2, 271, 264),
(32, 2, 272, 263),
(28, 2, 273, 262),
(54, 2, 274, 261),
(24, 2, 275, 260),
(22, 2, 276, 259),
(20, 2, 277, 258),
(18, 2, 278, 257),
(36, 2, 315, 256),
(43, 3, 266, 281),
(45, 3, 267, 280),
(47, 3, 268, 279),
(39, 3, 269, 314),
(48, 3, 279, 268),
(46, 3, 280, 267),
(44, 3, 281, 266),
(40, 3, 314, 269),
(55, 4, 282, 290),
(57, 4, 283, 291),
(59, 4, 284, 292),
(61, 4, 285, 293),
(63, 4, 286, 294),
(65, 4, 287, 295),
(67, 4, 288, 296),
(69, 4, 289, 297),
(56, 4, 290, 282),
(58, 4, 291, 283),
(60, 4, 292, 284),
(62, 4, 293, 285),
(64, 4, 294, 286),
(66, 4, 295, 287),
(68, 4, 296, 288),
(70, 4, 297, 289),
(108, 5, 410, 431),
(71, 5, 411, 418),
(76, 5, 411, 419),
(86, 5, 411, 424),
(88, 5, 411, 425),
(102, 5, 411, 428),
(104, 5, 411, 429),
(84, 5, 412, 423),
(78, 5, 413, 420),
(82, 5, 413, 422),
(106, 5, 413, 430),
(80, 5, 414, 421),
(98, 5, 415, 426),
(100, 5, 416, 427),
(120, 5, 416, 433),
(118, 5, 417, 432),
(72, 5, 418, 411),
(75, 5, 419, 411),
(77, 5, 420, 413),
(79, 5, 421, 414),
(81, 5, 422, 413),
(83, 5, 423, 412),
(85, 5, 424, 411),
(87, 5, 425, 411),
(97, 5, 426, 415),
(99, 5, 427, 416),
(101, 5, 428, 411),
(103, 5, 429, 411),
(105, 5, 430, 413),
(107, 5, 431, 410),
(117, 5, 432, 417),
(119, 5, 433, 416);








-- --------------------------------------------------------


--
-- Struktura tabeli dla tabeli `urzadzenie_polaczenie`
--

DROP TABLE IF EXISTS `urzadzenie_polaczenie`;
CREATE TABLE `urzadzenie_polaczenie` (
  `id` smallint(6) NOT NULL,
  `urzadzenie_id` smallint(5) UNSIGNED NOT NULL,
  `miejsce_id` tinyint(5) UNSIGNED NOT NULL,
  `zyla_id` smallint(5) UNSIGNED NOT NULL,
  `pin_id` smallint(5) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELACJE DLA TABELI `urzadzenie_polaczenie`:
--   `miejsce_id`
--       `miejsce` -> `id`
--   `pin_id`
--       `urzadzenie_piny` -> `id`
--   `urzadzenie_id`
--       `urządzenia` -> `id`
--   `zyla_id`
--       `zyla` -> `id`
--

--
-- Tabela Truncate przed wstawieniem `urzadzenie_polaczenie`
--

TRUNCATE TABLE `urzadzenie_polaczenie`;
--
-- Zrzut danych tabeli `urzadzenie_polaczenie`
--

INSERT INTO `urzadzenie_polaczenie` (`id`, `urzadzenie_id`, `miejsce_id`, `zyla_id`, `pin_id`) VALUES
(1, 3, 2, 90, 16),
(2, 3, 2, 88, 14),
(3, 3, 2, 89, 15),
(4, 3, 2, 91, 17);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `urzadzenie_zyla`
--





-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `WewnetrzneKableView`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `WewnetrzneKableView`;
CREATE TABLE `WewnetrzneKableView` (
`kabel_id` tinyint(3) unsigned
,`miejsce_id` tinyint(3) unsigned
,`c` bigint(21)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZewnetrzneKableView`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `ZewnetrzneKableView`;
CREATE TABLE `ZewnetrzneKableView` (
`kabel_id` tinyint(3) unsigned
,`miejsce_id` tinyint(3) unsigned
,`c` bigint(21)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZlaczaView`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `ZlaczaView`;
CREATE TABLE `ZlaczaView` (
);



-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZlaczePrzewodView`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `ZlaczePrzewodView`;
CREATE TABLE `ZlaczePrzewodView` (
`id` smallint(6) unsigned
,`kabel_id` tinyint(3) unsigned
,`miejsce_id` tinyint(3) unsigned
,`etykieta` varchar(10)
,`zlacze_id` smallint(5) unsigned
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZlaczeView`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `ZlaczeView`;
CREATE TABLE `ZlaczeView` (
`zk_id` int(11) unsigned
,`zlacze_id` smallint(5) unsigned
,`zyla_id` smallint(5) unsigned
,`pos` tinyint(4)
,`etykieta` varchar(10)
,`miejsce_id` tinyint(3) unsigned
,`pm_id` smallint(6) unsigned
,`opis` varchar(50)
,`name` varchar(20)
,`html` text
,`przewod_id` tinyint(3) unsigned
);


INSERT INTO `zlacze_kolejnosc` (`id`, `zlacze_id`, `zyla_id`, `pos`) VALUES
(1, 1, 1, 1),
(2, 1, 2, 2),
(3, 1, 3, 3),
(4, 1, 4, 4),
(5, 1, 5, 5),
(6, 1, 6, 6),
(7, 1, 7, 7),
(8, 1, 8, 8),
(9, 2, 9, 1),
(10, 2, 10, 2),
(11, 2, 11, 3),
(12, 2, 12, 4),
(13, 2, 13, 5),
(14, 2, 14, 6),
(15, 2, 15, 7),
(16, 2, 16, 8),
(17, 3, 17, 1),
(18, 3, 18, 2),
(19, 3, 19, 3),
(20, 3, 20, 4),
(21, 3, 21, 5),
(22, 3, 22, 6),
(23, 3, 23, 7),
(24, 3, 24, 8),
(25, 4, 25, 1),
(26, 4, 26, 2),
(27, 4, 27, 3),
(28, 4, 28, 4),
(29, 5, 29, 1),
(30, 5, 30, 2),
(31, 6, 31, 1),
(32, 6, 32, 2),
(33, 6, 33, 3),
(34, 6, 34, 4),
(35, 7, 35, 1),
(36, 7, 36, 2),
(37, 7, 37, 3),
(38, 8, 38, 1),
(39, 8, 39, 2),
(40, 8, 40, 3),
(41, 9, 41, 1),
(42, 9, 42, 2),
(43, 9, 43, 3),
(44, 9, 44, 4),
(45, 9, 45, 5),
(46, 9, 46, 6),
(47, 9, 47, 7),
(48, 9, 48, 8),
(49, 10, 49, 1),
(50, 10, 50, 2),
(51, 10, 51, 3),
(52, 10, 52, 4),
(53, 10, 53, 5),
(54, 10, 54, 6),
(55, 10, 55, 7),
(56, 10, 56, 8),
(57, 11, 57, 1),
(58, 11, 58, 2),
(59, 11, 59, 3),
(60, 11, 60, 4),
(61, 11, 61, 5),
(62, 11, 62, 6),
(63, 11, 63, 7),
(64, 11, 64, 8),
(65, 12, 65, 1),
(66, 12, 69, 2),
(67, 12, 66, 3),
(68, 12, 67, 4),
(69, 12, 68, 5),
(70, 12, 70, 6),
(71, 12, 71, 7),
(72, 12, 72, 8),
(73, 13, 73, 1),
(74, 13, 74, 2),
(75, 13, 75, 3),
(76, 13, 76, 4),
(77, 14, 77, 3),
(78, 15, 80, 1),
(79, 15, 81, 2),
(80, 15, 82, 3),
(81, 15, 83, 4),
(82, 15, 84, 5),
(83, 15, 85, 6),
(84, 15, 86, 7),
(85, 15, 87, 8),
(86, 15, 88, 12),
(87, 15, 89, 11),
(88, 15, 90, 10),
(89, 15, 91, 9),
(90, 16, 10, 1),
(91, 16, 14, 2),
(92, 16, 16, 3),
(93, 16, 15, 4),
(94, 16, 13, 5),
(95, 16, 12, 6),
(96, 16, 11, 7),
(97, 16, 9, 8),
(98, 17, 92, 1),
(99, 17, 93, 2),
(100, 17, 94, 3),
(101, 17, 95, 4),
(102, 17, 96, 5),
(103, 17, 97, 6),
(104, 17, 98, 7),
(105, 17, 99, 8),
(106, 17, 100, 9),
(107, 17, 101, 10),
(108, 17, 102, 11),
(109, 17, 103, 12),
(110, 19, 114, 1),
(111, 19, 113, 2),
(112, 19, 115, 3),
(113, 19, 112, 4),
(114, 18, 121, 1),
(115, 18, 120, 2),
(116, 18, 119, 3),
(117, 18, 118, 4),
(118, 18, 117, 5),
(119, 18, 116, 6),
(120, 14, 79, 1),
(121, 14, 78, 2),
(122, 20, 323, 1),
(123, 20, 322, 2),
(124, 20, 321, 3),
(125, 20, 320, 4),
(126, 20, 319, 5),
(127, 20, 318, 6),
(128, 20, 317, 7),
(129, 20, 316, 8),
(130, 21, 328, 1),
(131, 21, 329, 2),
(132, 21, 330, 3),
(133, 21, 331, 4),
(134, 21, 332, 5),
(135, 21, 333, 6),
(136, 22, 324, 1),
(137, 22, 325, 2),
(138, 22, 326, 3),
(139, 22, 327, 4),
(140, 23, 344, 1),
(141, 23, 345, 2),
(142, 23, 346, 3),
(143, 23, 347, 4),
(144, 23, 348, 5),
(145, 23, 349, 6),
(146, 23, 350, 7),
(147, 23, 351, 8),
(148, 24, 334, 1),
(149, 24, 335, 2),
(150, 24, 336, 3),
(151, 24, 337, 4),
(152, 24, 338, 5),
(153, 24, 339, 6),
(154, 24, 340, 7),
(155, 24, 341, 8),
(156, 24, 342, 9),
(157, 24, 343, 10),
(158, 25, 352, 1),
(159, 25, 353, 2),
(160, 25, 354, 3),
(161, 25, 355, 4),
(162, 26, 356, 1),
(163, 26, 357, 2),
(164, 26, 358, 3),
(165, 26, 359, 4),
(166, 26, 360, 5),
(167, 26, 361, 6),
(168, 26, 362, 7),
(169, 26, 363, 8),
(170, 26, 364, 9),
(171, 26, 365, 10),
(172, 27, 366, 1),
(173, 27, 367, 2),
(174, 27, 368, 3),
(175, 27, 369, 4),
(176, 27, 370, 5),
(177, 27, 371, 6),
(178, 27, 372, 7),
(179, 27, 373, 8),
(180, 27, 374, 9),
(181, 27, 375, 10),
(182, 29, 104, 1),
(183, 29, 105, 2),
(184, 29, 106, 3),
(185, 29, 107, 4),
(186, 28, 108, 1),
(187, 28, 109, 2),
(188, 28, 110, 3),
(189, 28, 111, 4);



-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZylaZlaczeKolejnoscView`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `ZylaZlaczeKolejnoscView`;
CREATE TABLE `ZylaZlaczeKolejnoscView` (
`pm_id` smallint(6) unsigned
,`pm_kabel_id` tinyint(3) unsigned
,`pm_miejsce_id` tinyint(3) unsigned
,`zw_id` smallint(5) unsigned
,`zw_color` tinyint(3) unsigned
,`zw_przewod_id` tinyint(3) unsigned
,`zw_opis` varchar(50)
,`zw_kolor_name` varchar(20)
,`zw_kolor_html` text
,`zlw_zlacze_id` smallint(5) unsigned
,`zlw_zyla_id` smallint(5) unsigned
,`zlw_pos` tinyint(4)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZylaZlaczeView`
-- (Zobacz poniżej rzeczywisty widok)
--
DROP VIEW IF EXISTS `ZylaZlaczeView`;
CREATE TABLE `ZylaZlaczeView` (
`id` smallint(5) unsigned
,`zlacze_id` smallint(5) unsigned
,`zyla_id` smallint(5) unsigned
,`pos` tinyint(4)
,`opis` varchar(50)
,`name` varchar(20)
,`html` text
,`przewod_id` tinyint(3) unsigned
);

-- --------------------------------------------------------




--
-- Struktura widoku `PolaczenieView`
--
DROP TABLE IF EXISTS `PolaczenieView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `PolaczenieView`  AS  select `p`.`id` AS `pid`,`p`.`miejsce_id` AS `miejsce_id`,`p`.`opis` AS `opis`,`m`.`id` AS `mid`,`m`.`name` AS `name`,`m`.`description` AS `description`,`m`.`zbiorcze` AS `zbiorcze`,`m`.`id_pomieszczenie` AS `id_pomieszczenie`,`m`.`kod` AS `kod`,`m`.`polaczenie` AS `polaczenie`,`m`.`pomieszczenie` AS `pomieszczenie` from (`polaczenie` `p` left join `MiejsceView` `m` on((`p`.`miejsce_id` = `m`.`id`))) where 1 ;

-- --------------------------------------------------------

--
-- Struktura widoku `PolaczenieZylaWidok`
--
DROP TABLE IF EXISTS `PolaczenieZylaWidok`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `PolaczenieZylaWidok`  AS  select `pz`.`id` AS `id`,`pz`.`polaczenie_id` AS `polaczenie_id`,`pz`.`zyla_id_1` AS `zyla_id_1`,`pz`.`zyla_id_2` AS `zyla_id_2`,`p1`.`color_id` AS `cid1`,`p1`.`przewod_id` AS `pid1`,`p1`.`opis` AS `opis1`,`p1`.`name` AS `cname1`,`p1`.`html` AS `html1`,`p2`.`color_id` AS `cid2`,`p2`.`przewod_id` AS `pid2`,`p2`.`opis` AS `opis2`,`p2`.`name` AS `cname2`,`p2`.`html` AS `html2`,`poz`.`miejsce_id` AS `miejsce_id`,`poz`.`opis` AS `pol_opis` from (((`polaczenie_zyla` `pz` left join `ZylaWidok` `p1` on((`p1`.`id` = `pz`.`zyla_id_1`))) left join `ZylaWidok` `p2` on((`p2`.`id` = `pz`.`zyla_id_2`))) left join `polaczenie` `poz` on((`pz`.`polaczenie_id` = `poz`.`id`))) where 1 order by `p1`.`przewod_id`,`poz`.`miejsce_id`,`p2`.`przewod_id` ;

-- --------------------------------------------------------




-- --------------------------------------------------------

--
-- Struktura widoku `ZlaczaView`
--
DROP TABLE IF EXISTS `ZlaczaView`;

CREATE ALGORITHM=TEMPTABLE DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZlaczaView`  AS  select `zk`.`id` AS `id`,`zk`.`zlacze_id` AS `zlacze_id`,`zk`.`zyla_id` AS `zyla_id`,`zk`.`pos` AS `pos`,`z`.`etykieta` AS `etykieta`,`z`.`miejsce_id` AS `miejsce_id`,`zw`.`opis` AS `opis`,`zw`.`name` AS `name`,`zw`.`html` AS `html`,`zw`.`przewod_id` AS `przewod_id` from ((`zlacze_kolejnosc` `zk` left join `zlacze` `z` on((`zk`.`zlacze_id` = `z`.`id`))) left join `ZylaWidok` `zw` on((`zk`.`zyla_id` = `zw`.`id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZlaczePrzewodView`
--
DROP TABLE IF EXISTS `ZlaczePrzewodView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZlaczePrzewodView`  AS  select `pm`.`id` AS `id`,`pm`.`kabel_id` AS `kabel_id`,`pm`.`miejsce_id` AS `miejsce_id`,`z`.`etykieta` AS `etykieta`,`z`.`id` AS `zlacze_id` from (`przewod_miejsce` `pm` left join `zlacze` `z` on((`z`.`przewod_miejsce_id` = `pm`.`id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZlaczeView`
--
DROP TABLE IF EXISTS `ZlaczeView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZlaczeView`  AS  select `zk`.`id` AS `zk_id`,`zk`.`zlacze_id` AS `zlacze_id`,`zk`.`zyla_id` AS `zyla_id`,`zk`.`pos` AS `pos`,`z`.`etykieta` AS `etykieta`,`pm`.`miejsce_id` AS `miejsce_id`,`pm`.`id` AS `pm_id`,`zw`.`opis` AS `opis`,`zw`.`name` AS `name`,`zw`.`html` AS `html`,`zw`.`przewod_id` AS `przewod_id` from (((`zlacze_kolejnosc` `zk` left join `zlacze` `z` on((`zk`.`zlacze_id` = `z`.`id`))) left join `ZylaWidok` `zw` on((`zk`.`zyla_id` = `zw`.`id`))) left join `przewod_miejsce` `pm` on((`pm`.`id` = `z`.`przewod_miejsce_id`))) ;

-- --------------------------------------------------------



--
-- Struktura widoku `ZylaZlaczeKolejnoscView`
--
DROP TABLE IF EXISTS `ZylaZlaczeKolejnoscView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZylaZlaczeKolejnoscView`  AS  select `pm`.`id` AS `pm_id`,`pm`.`kabel_id` AS `pm_kabel_id`,`pm`.`miejsce_id` AS `pm_miejsce_id`,`zw`.`id` AS `zw_id`,`zw`.`color_id` AS `zw_color`,`zw`.`przewod_id` AS `zw_przewod_id`,`zw`.`opis` AS `zw_opis`,`zw`.`name` AS `zw_kolor_name`,`zw`.`html` AS `zw_kolor_html`,`zlw`.`zlacze_id` AS `zlw_zlacze_id`,`zlw`.`zyla_id` AS `zlw_zyla_id`,`zlw`.`pos` AS `zlw_pos` from ((`przewod_miejsce` `pm` left join `ZylaWidok` `zw` on((`pm`.`kabel_id` = `zw`.`przewod_id`))) left join `ZlaczeView` `zlw` on((`zlw`.`pm_id` = `pm`.`id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZylaZlaczeView`
--
DROP TABLE IF EXISTS `ZylaZlaczeView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZylaZlaczeView`  AS  select `zw`.`id` AS `id`,`zk`.`zlacze_id` AS `zlacze_id`,`zk`.`zyla_id` AS `zyla_id`,`zk`.`pos` AS `pos`,`zw`.`opis` AS `opis`,`zw`.`name` AS `name`,`zw`.`html` AS `html`,`zw`.`przewod_id` AS `przewod_id` from (`ZylaWidok` `zw` left join `zlacze_kolejnosc` `zk` on((`zk`.`zyla_id` = `zw`.`id`))) ;

--
-- Indeksy dla zrzutów tabel
--




--
-- Indeksy dla tabeli `polaczenie`
--
ALTER TABLE `polaczenie`
  ADD PRIMARY KEY (`id`),
  ADD KEY `miejsce_id` (`miejsce_id`);

--
-- Indeksy dla tabeli `polaczenie_zyla`
--
ALTER TABLE `polaczenie_zyla`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pol_zylas` (`polaczenie_id`,`zyla_id_1`,`zyla_id_2`) USING BTREE,
  ADD KEY `zyla_id_1` (`zyla_id_1`),
  ADD KEY `polaczenie_id` (`polaczenie_id`) USING BTREE,
  ADD KEY `zyla_id_2` (`zyla_id_2`);











--
-- Indeksy dla tabeli `urzadzenie_polaczenie`
--
ALTER TABLE `urzadzenie_polaczenie`
  ADD PRIMARY KEY (`id`),
  ADD KEY `urzadzenie_id` (`urzadzenie_id`),
  ADD KEY `miejsce_id` (`miejsce_id`),
  ADD KEY `zyla_id` (`zyla_id`),
  ADD KEY `pin_id` (`pin_id`);










--
-- AUTO_INCREMENT dla tabel zrzutów
--





--
-- AUTO_INCREMENT dla tabeli `polaczenie`
--
ALTER TABLE `polaczenie`
  MODIFY `id` smallint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `polaczenie_zyla`
--
ALTER TABLE `polaczenie_zyla`
  MODIFY `id` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;











--
-- AUTO_INCREMENT dla tabeli `urzadzenie_polaczenie`
--
ALTER TABLE `urzadzenie_polaczenie`
  MODIFY `id` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;





--
-- AUTO_INCREMENT dla tabeli `zlacze_kolejnosc`
--
ALTER TABLE `zlacze_kolejnosc`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=190;



--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `polaczenie`
--
ALTER TABLE `polaczenie`
  ADD CONSTRAINT `mieidfg` FOREIGN KEY (`miejsce_id`) REFERENCES `miejsce` (`id`);

--
-- Ograniczenia dla tabeli `polaczenie_zyla`
--
ALTER TABLE `polaczenie_zyla`
  ADD CONSTRAINT `polzyla1fg` FOREIGN KEY (`zyla_id_1`) REFERENCES `zyla` (`id`),
  ADD CONSTRAINT `polzyla2fg` FOREIGN KEY (`zyla_id_2`) REFERENCES `zyla` (`id`),
  ADD CONSTRAINT `polzylfg` FOREIGN KEY (`polaczenie_id`) REFERENCES `polaczenie` (`id`);





--
-- Ograniczenia dla tabeli `urzadzenie_polaczenie`
--
ALTER TABLE `urzadzenie_polaczenie`
  ADD CONSTRAINT `upmidfg` FOREIGN KEY (`miejsce_id`) REFERENCES `miejsce` (`id`),
  ADD CONSTRAINT `uppidfg` FOREIGN KEY (`pin_id`) REFERENCES `urzadzenie_piny` (`id`),
  ADD CONSTRAINT `upuidfg` FOREIGN KEY (`urzadzenie_id`) REFERENCES `urządzenia` (`id`),
  ADD CONSTRAINT `upzidfg` FOREIGN KEY (`zyla_id`) REFERENCES `zyla` (`id`);








/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
