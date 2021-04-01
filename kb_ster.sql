-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Czas generowania: 01 Kwi 2021, 23:43
-- Wersja serwera: 8.0.23-0ubuntu0.20.04.1
-- Wersja PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `kb_ster_test`
--

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ElementyPlytkowePinView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ElementyPlytkowePinView` (
`id` smallint unsigned
,`pinnazwa` text
,`pos` tinyint
,`element_plytkowy_id` smallint unsigned
,`elementnazwa` text
,`ilosc_pin` tinyint
,`plytka_id` tinyint unsigned
,`rodzaj_urzadzenia` tinyint unsigned
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ElementyPlytkowePolaczeniaPinView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ElementyPlytkowePolaczeniaPinView` (
`id` smallint unsigned
,`polaczenie_plytka_id` smallint unsigned
,`elementy_plytkowe_piny_id` smallint unsigned
,`pinnazwa` text
,`pos` tinyint
,`element_plytkowy_id` smallint unsigned
,`elemnazwa` text
,`ilosc_pin` tinyint
,`plytka_id` tinyint unsigned
,`rodzaj_urzadzenia` tinyint unsigned
,`rodznazwa` text
,`kod` varchar(1)
,`przewod` tinyint(1)
,`plytka` tinyint(1)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ElementyPlytkoweView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ElementyPlytkoweView` (
`id` smallint unsigned
,`nazwa` text
,`ilosc_pin` tinyint
,`plytka_id` tinyint unsigned
,`miejsce_id` tinyint unsigned
,`pnazwa` text
,`urzadzenie_rodzaj_id` tinyint
,`urzadzenie_nazwa` text
,`urzadzenie_rodzaj_kod` varchar(1)
,`urzadzenie_plytka` tinyint(1)
,`urzadzenie_przewod` tinyint(1)
,`mnazwa` text
,`opis` text
,`zbiorcze` tinyint(1)
,`id_pomieszczenie` tinyint unsigned
,`kod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` text
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `elementy_plytkowe`
--

CREATE TABLE `elementy_plytkowe` (
  `id` smallint UNSIGNED NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `ilosc_pin` tinyint NOT NULL,
  `plytka_id` tinyint UNSIGNED NOT NULL,
  `rodzaj_urzadzenia` tinyint UNSIGNED NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `elementy_plytkowe`
--

INSERT INTO `elementy_plytkowe` (`id`, `nazwa`, `ilosc_pin`, `plytka_id`, `rodzaj_urzadzenia`) VALUES
(1, 'Ekspander portów I/O 0x00 - porty', 9, 2, 3),
(2, 'Ekspander portów I/O 0x01 - porty', 9, 2, 3),
(3, 'Ekspander portów I/O 0x00 - zasilanie	', 4, 2, 5),
(4, 'Ekspander portów I/O 0x01 - zasilanie	', 4, 2, 5),
(5, 'Przewód 48', 12, 2, 4),
(6, 'Przewód 49', 12, 2, 4),
(7, 'Przewód 148', 4, 2, 4),
(8, 'Przewód 147', 4, 2, 4),
(9, 'Konwerter RS <-> TTL', 8, 2, 3),
(10, 'Arduino pro micro 16 MHz 5V', 24, 2, 3),
(11, 'Konwerter 0.5A 24/5V', 4, 1, 3),
(12, 'A', 8, 1, 5),
(13, 'B', 4, 1, 5),
(14, 'C', 2, 1, 5),
(15, 'D', 8, 1, 5),
(16, 'E', 3, 1, 5),
(17, 'F', 12, 1, 5),
(18, 'G', 4, 1, 5),
(19, 'H', 4, 1, 5),
(20, 'I', 3, 1, 5),
(21, 'J', 8, 1, 5),
(22, 'K', 12, 1, 5),
(23, 'L', 3, 1, 5),
(24, 'M', 8, 1, 5),
(25, 'N', 8, 1, 5),
(26, 'O', 8, 1, 5),
(27, 'P', 8, 1, 5),
(28, 'czujnik temperatury DS1820', 3, 1, 3),
(29, 'Ekspander portów 0x00', 20, 6, 3),
(30, 'Ekspander portów 0x00 - zasilanie', 5, 6, 3),
(31, 'Ekspander portów 0x01', 20, 6, 3),
(32, 'Ekspander portów 0x01 - zasilanie', 5, 6, 3),
(33, 'A', 10, 6, 5),
(34, 'B', 6, 6, 5),
(35, 'C', 6, 6, 5),
(36, 'D', 12, 6, 5),
(37, 'E', 12, 6, 5),
(38, 'F', 4, 6, 5),
(39, 'H', 8, 6, 5),
(40, 'K Ekspander 0x00', 20, 6, 5),
(41, 'L Ekspander 0x01', 20, 6, 5),
(42, 'M Ekspander 0x00', 5, 6, 4),
(43, 'N Ekspander 0x01', 5, 6, 4),
(44, 'Przetwornica step-dwon 32/5V 2.5A', 5, 8, 3),
(45, 'A', 2, 8, 5),
(46, 'B', 4, 8, 5),
(47, 'C', 4, 8, 5),
(48, 'D', 8, 8, 5),
(49, 'KonwerterTTL-RS', 6, 8, 3);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `elementy_plytkowe_pin`
--

CREATE TABLE `elementy_plytkowe_pin` (
  `id` smallint UNSIGNED NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `pos` tinyint NOT NULL,
  `element_plytkowy_id` smallint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `elementy_plytkowe_pin`
--

INSERT INTO `elementy_plytkowe_pin` (`id`, `nazwa`, `pos`, `element_plytkowy_id`) VALUES
(1, 'P0', 1, 1),
(2, 'P1', 2, 1),
(3, 'P2', 3, 1),
(4, 'P3', 4, 1),
(5, 'P4', 5, 1),
(6, 'P5', 6, 1),
(7, 'P6', 7, 1),
(8, 'P7', 8, 1),
(9, 'INT', 9, 1),
(10, 'VCC', 1, 3),
(11, 'GND', 2, 3),
(12, 'SDA', 3, 3),
(13, 'SCL', 4, 3),
(14, 'P0', 1, 2),
(15, 'P1', 2, 2),
(16, 'P2', 3, 2),
(17, 'P3', 4, 2),
(18, 'P4', 5, 2),
(19, 'P5', 6, 2),
(20, 'P6', 7, 2),
(21, 'P7', 8, 2),
(22, 'INT', 9, 2),
(23, 'VCC', 1, 4),
(24, 'GND', 2, 4),
(25, 'SDA', 3, 4),
(26, 'SCL', 4, 4),
(27, 'żółty 0x01.3', 1, 5),
(28, 'biały 0x01.2', 2, 5),
(29, 'niebieski 0x01.1', 3, 5),
(30, 'fioletowy 0x01.0', 4, 5),
(31, 'czerwony -', 5, 5),
(32, 'zielony jasny -', 6, 5),
(33, 'czarny -', 7, 5),
(34, 'brązowy jasny cpu 9', 8, 5),
(35, 'szary -', 9, 5),
(36, 'pomaranczowy -', 10, 5),
(37, 'zielony 0x01.5', 11, 5),
(38, 'brązowy 0x01.4', 12, 5),
(39, 'brązowy 0x00.5', 1, 6),
(40, 'fioletowy 0x00.4', 2, 6),
(41, 'biały 0x00.7', 3, 6),
(42, 'żółty 0x00.6', 4, 6),
(43, 'pomarańczowy 0x00.3', 5, 6),
(44, 'szary 0x00.2', 6, 6),
(45, 'jasno brązowy 0x00.1', 7, 6),
(46, 'jasno zielony 0x00.0', 8, 6),
(47, 'zielony RS RX', 9, 6),
(48, 'niebieski RS TX', 10, 6),
(49, 'czarny GND', 11, 6),
(50, 'czerwony 5V', 12, 6),
(51, 'pomarańczowy 5V', 1, 7),
(52, 'bialy GND', 2, 7),
(53, 'żółty SDA', 3, 7),
(54, 'szary SCL', 4, 7),
(55, 'pomarańczowy 5V', 1, 8),
(56, 'biały GND', 2, 8),
(57, 'żółty SDA', 3, 8),
(58, 'szary SCL', 4, 8),
(59, '5V', 1, 9),
(60, 'GND', 2, 9),
(61, 'RX TTL', 3, 9),
(62, 'TX TTL', 4, 9),
(63, '12V', 5, 9),
(64, 'GND', 6, 9),
(65, 'RX RS', 7, 9),
(66, 'TX RS', 8, 9),
(67, '1 (TX)', 1, 10),
(68, '0 (RX)', 2, 10),
(69, 'GND', 3, 10),
(70, 'GND', 4, 10),
(71, '2 (SDA)', 5, 10),
(72, '3 (SCL)', 6, 10),
(73, '4 (A6)', 7, 10),
(74, '5', 8, 10),
(75, '6 (A7)', 9, 10),
(76, '7', 10, 10),
(77, '8 (A8)', 11, 10),
(78, '9 (A9)', 12, 10),
(79, 'RAW', 13, 10),
(80, 'GND', 14, 10),
(81, 'RST', 15, 10),
(82, 'VCC', 16, 10),
(83, '21 (A3)', 17, 10),
(84, '20 (A2)', 18, 10),
(85, '19 (A1)', 19, 10),
(86, '18 (A0)', 20, 10),
(87, '15 (SCLK)', 21, 10),
(88, '14 (MISO)', 22, 10),
(89, '16 (MOSI)', 23, 10),
(90, '10 (A10)', 24, 10),
(91, 'SHON', 1, 11),
(92, 'Vin (24V)', 2, 11),
(93, 'GND', 3, 11),
(94, 'Vout (5V)', 4, 11),
(95, '24V', 1, 12),
(96, 'A.2-F.12', 2, 12),
(97, 'A.3-F.11', 3, 12),
(98, 'A.4-F.10', 4, 12),
(99, 'A.5-F.9', 5, 12),
(100, 'A.6-F.8', 6, 12),
(101, 'A.7-F.7', 7, 12),
(102, 'A.8-F.6', 8, 12),
(103, 'Sygnał czujnik ruchu', 1, 13),
(104, '5V', 2, 13),
(105, 'GND', 3, 13),
(106, 'GND', 4, 13),
(107, 'Styk kontakt.', 1, 14),
(108, 'GND', 2, 14),
(109, '5V ogrz', 1, 15),
(110, 'D.2-H.3', 2, 15),
(111, 'D.3-H.2', 3, 15),
(112, 'GND', 4, 15),
(113, 'D.5-0.2', 5, 15),
(114, 'D.6-N.3', 6, 15),
(115, 'D.7-I.2', 7, 15),
(116, 'D.8-E.2', 8, 15),
(117, '5V ogrz', 1, 16),
(118, 'E.2-D.8', 2, 16),
(119, 'GND', 3, 16),
(120, 'F.1-B.1', 1, 17),
(121, 'F.2-G.1', 2, 17),
(122, 'F.3-C.1', 3, 17),
(123, 'F.4-L.3', 4, 17),
(124, '5V', 5, 17),
(125, 'F.6-A.8', 6, 17),
(126, 'F.7-A.7', 7, 17),
(127, 'F.8-A.6', 8, 17),
(128, 'F.9-A.5', 9, 17),
(129, 'F.10-A.4', 10, 17),
(130, 'F.11-A.3', 11, 17),
(131, 'F.12-A.2', 12, 17),
(132, 'Sygnał czujnika zbliżeniowego', 1, 18),
(133, '5V', 2, 18),
(134, 'GND', 3, 18),
(135, 'GND', 4, 18),
(136, 'GND', 1, 19),
(137, 'H.2-D.3', 2, 19),
(138, 'H.3-D.2', 3, 19),
(139, '5V ogrz', 4, 19),
(140, 'GND', 1, 20),
(141, 'I.2-D.7', 2, 20),
(142, '5V ogrz', 3, 20),
(143, 'GND', 1, 21),
(144, '5V ogrz', 2, 21),
(145, 'J.3-P.4', 3, 21),
(146, 'J.4-P.3', 4, 21),
(147, 'J.5-K.12', 5, 21),
(148, 'J.6-K.11', 6, 21),
(149, 'J.7-K.10', 7, 21),
(150, 'J.8-K.9', 8, 21),
(151, 'K.1-P.1', 1, 22),
(152, 'K.2-P.2', 2, 22),
(153, 'K.3', 3, 22),
(154, 'K.4', 4, 22),
(155, 'K.5', 5, 22),
(156, 'K.6-O.8', 6, 22),
(157, 'K.7-O.7', 7, 22),
(158, 'K.8-O.6', 8, 22),
(159, 'K.9-J.8', 9, 22),
(160, 'K.10-J.7', 10, 22),
(161, 'K.11-J.6', 11, 22),
(162, 'K.12-J.5', 12, 22),
(163, 'Podświetlenie wł.', 1, 23),
(164, 'GND', 2, 23),
(165, 'Klawisz wł', 3, 23),
(166, 'M.1', 1, 24),
(167, 'M.2', 2, 24),
(168, 'M.3', 3, 24),
(169, 'M.4', 4, 24),
(170, 'M.5', 5, 24),
(171, 'M.6', 6, 24),
(172, 'M.7', 7, 24),
(173, 'M.8', 8, 24),
(174, '5V ogrz', 1, 25),
(175, '5V', 2, 25),
(176, 'N.3-O.6', 3, 25),
(177, 'GND', 4, 25),
(178, 'N.5-P.8', 5, 25),
(179, 'N.6-P.7', 6, 25),
(180, 'N.7-P.6', 7, 25),
(181, 'Podświetlenie', 8, 25),
(182, '-', 1, 26),
(183, '-', 2, 26),
(184, '-', 3, 26),
(185, 'GND', 4, 26),
(186, 'GND', 5, 26),
(187, 'O.6-K.8', 6, 26),
(188, 'O.7-K.7', 7, 26),
(189, 'O.8-K.6', 8, 26),
(190, 'P.1-K.1', 1, 27),
(191, 'P.2-K.2', 2, 27),
(192, 'P.3-J.4', 3, 27),
(193, 'P.4-J.3', 4, 27),
(194, 'Podświetlenie', 5, 27),
(195, 'P.6-N.7', 6, 27),
(196, 'P.7-N.6', 7, 27),
(197, 'P.8-N.5', 8, 27),
(198, 'GND', 1, 28),
(199, 'Sygnał', 2, 28),
(200, '5V', 3, 28),
(256, 'GND', 1, 29),
(257, 'GND', 2, 29),
(258, 'B0', 3, 29),
(259, 'A0', 4, 29),
(260, 'B1', 5, 29),
(261, 'A1', 6, 29),
(262, 'B2', 7, 29),
(263, 'A2', 8, 29),
(264, 'B3', 9, 29),
(265, 'A3', 10, 29),
(266, 'B4', 11, 29),
(267, 'A4', 12, 29),
(268, 'B5', 13, 29),
(269, 'A5', 14, 29),
(270, 'B6', 15, 29),
(271, 'A6', 16, 29),
(272, 'B7', 17, 29),
(273, 'A7', 18, 29),
(274, '+5V', 19, 29),
(275, '+5V', 20, 29),
(276, 'INT 0X00', 1, 30),
(277, 'SCL', 2, 30),
(278, 'SDA', 3, 30),
(279, 'GND', 4, 30),
(280, '+5V', 5, 30),
(281, 'GND', 1, 31),
(282, 'GND', 2, 31),
(283, 'B0', 3, 31),
(284, 'A0', 4, 31),
(285, 'B1', 5, 31),
(286, 'A1', 6, 31),
(287, 'B2', 7, 31),
(288, 'A2', 8, 31),
(289, 'B3', 9, 31),
(290, 'A3', 10, 31),
(291, 'B4', 11, 31),
(292, 'A4', 12, 31),
(293, 'B5', 13, 31),
(294, 'A5', 14, 31),
(295, 'B6', 15, 31),
(296, 'A6', 16, 31),
(297, 'B7', 17, 31),
(298, 'A7', 18, 31),
(299, '+5V', 19, 31),
(300, '+5V', 20, 31),
(301, 'INT 0X01', 1, 32),
(302, 'SCL', 2, 32),
(303, 'SDA', 3, 32),
(304, 'GND', 4, 32),
(305, '+5V', 5, 32),
(306, 'GND', 1, 33),
(307, 'przekaźnik 1', 2, 33),
(308, 'przekaźnik 2', 3, 33),
(309, 'przekaźnik 3', 4, 33),
(310, 'przekaźnik 4', 5, 33),
(311, 'przekaźnik 5', 6, 33),
(312, 'przekaźnik 6', 7, 33),
(313, 'przekaźnik 7', 8, 33),
(314, 'przekaźnik 8', 9, 33),
(315, '+5V', 10, 33),
(316, 'GND', 1, 34),
(317, 'Przekaźnik 1', 2, 34),
(318, 'Przekaźnik 2', 3, 34),
(319, 'Przekaźnik 3', 4, 34),
(320, 'Przekaźnik 4', 5, 34),
(321, '+5V', 6, 34),
(322, 'GND', 1, 35),
(323, 'PWM kanał 1', 2, 35),
(324, 'PWM kanał 2', 3, 35),
(325, 'Przekaźnik 1', 4, 35),
(326, 'Przekaźnik 2', 5, 35),
(327, '+5V', 6, 35),
(328, 'GND', 1, 36),
(329, 'GND', 2, 36),
(330, '-', 3, 36),
(331, '-', 4, 36),
(332, '-', 5, 36),
(333, '-', 6, 36),
(334, '-', 7, 36),
(335, '-', 8, 36),
(336, '-', 9, 36),
(337, '-', 10, 36),
(338, 'GND', 11, 36),
(339, 'GND', 12, 36),
(340, 'GND', 1, 37),
(341, 'GND', 2, 37),
(342, '-', 3, 37),
(343, '-', 4, 37),
(344, '-', 5, 37),
(345, '-', 6, 37),
(346, '-', 7, 37),
(347, '-', 8, 37),
(348, '-', 9, 37),
(349, '-', 10, 37),
(350, 'GND', 11, 37),
(351, 'GND', 12, 37),
(356, 'GND', 1, 38),
(357, '3.2', 2, 38),
(358, '3.3', 3, 38),
(359, '+5V', 4, 38),
(360, '+5V', 1, 39),
(361, 'GND', 2, 39),
(362, '3.3', 3, 39),
(363, '3.2', 4, 39),
(364, 'SDA', 5, 39),
(365, 'SCL', 6, 39),
(366, 'INT 0x01', 7, 39),
(367, 'INT 0x00', 8, 39),
(368, 'GND', 1, 40),
(369, 'GND', 2, 40),
(370, 'B0', 3, 40),
(371, 'A0', 4, 40),
(372, 'B1', 5, 40),
(373, 'A1', 6, 40),
(374, 'B2', 7, 40),
(375, 'A2', 8, 40),
(376, 'B3', 9, 40),
(377, 'A3', 10, 40),
(378, 'B4', 11, 40),
(379, 'A4', 12, 40),
(380, 'B5', 13, 40),
(381, 'A5', 14, 40),
(382, 'B6', 15, 40),
(383, 'A6', 16, 40),
(384, 'B7', 17, 40),
(385, 'A7', 18, 40),
(386, '+5V', 19, 40),
(387, '+5V', 20, 40),
(388, 'GND', 1, 41),
(389, 'GND', 2, 41),
(390, 'B0', 3, 41),
(391, 'A0', 4, 41),
(392, 'B1', 5, 41),
(393, 'A1', 6, 41),
(394, 'B2', 7, 41),
(395, 'A2', 8, 41),
(396, 'B3', 9, 41),
(397, 'A3', 10, 41),
(398, 'B4', 11, 41),
(399, 'A4', 12, 41),
(400, 'B5', 13, 41),
(401, 'A5', 14, 41),
(402, 'B6', 15, 41),
(403, 'A6', 16, 41),
(404, 'B7', 17, 41),
(405, 'A7', 18, 41),
(406, '+5V', 19, 41),
(407, '+5V', 20, 41),
(408, 'INT 0x00', 1, 42),
(409, 'SCL', 2, 42),
(410, 'SDA', 3, 42),
(411, 'GND', 4, 42),
(412, '+5V', 5, 42),
(413, 'INT 0x01', 1, 43),
(414, 'SCL', 2, 43),
(415, 'SDA', 3, 43),
(416, 'GND', 4, 43),
(417, '+5V', 5, 43),
(508, 'PG', 1, 44),
(509, 'EN', 2, 44),
(510, 'IN', 3, 44),
(511, 'GND', 4, 44),
(512, 'OUT', 5, 44),
(513, '+5V', 1, 45),
(514, 'GND', 2, 45),
(515, 'TTL<-', 1, 46),
(516, 'TTL->', 2, 46),
(517, 'GND', 3, 46),
(518, '+5V', 4, 46),
(519, 'Wieczór', 1, 47),
(520, 'Noc', 2, 47),
(521, '2 taryfa', 3, 47),
(522, 'Zas. awarujne', 4, 47),
(523, '24V', 1, 48),
(524, 'GND', 2, 48),
(525, 'RS ->', 3, 48),
(526, 'RS <-', 4, 48),
(527, 'Zas. awaryjne', 5, 48),
(528, '2 taryfa', 6, 48),
(529, 'Noc', 7, 48),
(530, 'Wieczór', 8, 48),
(531, '-', 1, 49),
(532, '+', 2, 49),
(533, 'TTL ->', 3, 49),
(534, 'TTL <-', 4, 49),
(535, 'RS ->', 5, 49),
(536, 'RS <-', 6, 49);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `kolor`
--

CREATE TABLE `kolor` (
  `id` tinyint UNSIGNED NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `html` text CHARACTER SET ascii COLLATE ascii_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `kolor`
--

INSERT INTO `kolor` (`id`, `nazwa`, `html`) VALUES
(0, 'Nieokreślony', 'gray'),
(1, 'Biały', 'white'),
(2, 'Pomarańczowy', '#FF6600'),
(3, 'Niebieski', 'blue'),
(4, 'Czerwony', 'red'),
(5, 'Fioletowy', 'purple'),
(6, 'Brązowy', 'maroon'),
(7, 'Czarny', 'black'),
(8, 'Żółty', 'yellow'),
(9, 'Zielony', 'green'),
(10, 'Szary', 'silver'),
(11, 'Jasnozielony', 'lime'),
(12, 'Jasnobrązowy', '#CD853F'),
(13, 'Różowy', 'fuchsia'),
(14, 'Błękitny', 'aqua');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `KolorView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `KolorView` (
`id` tinyint unsigned
,`nazwa` text
,`html` text
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `miejsce`
--

CREATE TABLE `miejsce` (
  `id` tinyint UNSIGNED NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `opis` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `zbiorcze` tinyint(1) NOT NULL,
  `id_pomieszczenie` tinyint UNSIGNED NOT NULL,
  `kod` varchar(16) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  `polaczenie` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `miejsce`
--

INSERT INTO `miejsce` (`id`, `nazwa`, `opis`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`) VALUES
(1, 'Główna centrala', 'Główna centralka w przedpokoju na ścianie od łazienki', 1, 1, 'HOL-GR', 0),
(2, 'Rozdzielnia WC', 'Rozdzielnia w WC umieszczona w wnęce na wprost wejścia na ścianie od Holu.', 1, 2, 'WC-ROZD', 0),
(3, 'Sufit WC', 'Przekaźniki umieszczone w suficie w WC koło lampy', 1, 2, 'WC-SUFIT', 0),
(4, 'Kontaktron WC', 'Czujnik otwarcia dzwi WC', 0, 2, 'WC-DRZWI', 0),
(5, 'Lustro WC', 'Puszka umieszczona pod lustrem WC na ścianie od Holu', 0, 2, 'WC-POD_LUS', 0),
(6, 'Czujnik lustro WC', 'Czujnik zbliżeniowy umieszczony pod lustrem w WC na ścianie z Holem', 0, 2, 'WC-LUSTRO', 0),
(7, 'Włącznik WC', 'Włącznik światła WC umieszczony w Holu na ścianie WC obok drzwi', 0, 2, 'WC-WLACZ', 0),
(8, 'Włącznik hol WC', 'Podwójny włącznik światła w holu na ścianie WC', 0, 1, 'HOL-WLACZ_SC_WC', 0),
(9, 'Umywalka WC', 'Czujniki przepływu wody w WC pod umywalką', 0, 2, 'WC-UMYWALKA', 0),
(10, 'Pralka WC', 'Czujniki przepływu wody w WC koło pralki', 0, 2, 'WC-PRALKA', 0),
(11, 'Czujnik zalania WC', 'Czujnik zalania koło drzwi w WC', 0, 2, 'WC-SC_LUSTRO', 0),
(12, 'Gabaryt WC', 'Umieszczony w środku gabarytu (stelaż sedesu) w WC', 0, 2, 'WC-GABARYT', 0),
(13, 'Temperatura WC', 'Czujnik temperatury w WC na stelażu kibla', 0, 2, 'WC-TEMP', 0),
(14, 'Czujnik ruchu WC', 'Umieszczony w WC na ścianie z drzwiami nad nimi', 0, 2, 'WC-RUCH', 0),
(15, 'Temperatura podłoga WC', 'Czujnik temperatury w podłodze WC', 0, 2, 'WC-PODL_TEMP', 0),
(16, 'Temperatura podłoga hol', 'Czujnik temperatury w podłodze przedpokoju', 0, 1, 'HOL-TEMP_PODL', 0),
(17, 'Włącznik pokój', 'Podwójny włącznik pokój na ścianie przy drzwiach', 0, 4, 'POK-WLACZ', 0),
(18, 'Temperatura pokój', 'Czujnik temperatury umieszczony w pokoju przy drzwiach na ścianie od pracowni', 0, 4, 'POK-TEMPERATURA', 0),
(19, 'Grzejnik pokój', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w pokoju', 0, 4, 'POK-GRZEJNIK', 0),
(20, 'Sufit łazienka', 'Umieszczone pod sufitem w łazience przy lampie', 1, 8, 'LAZ-SUFIT', 0),
(21, 'Łazienka, puszka pod umywalką', 'Rozdzielnia pod liczniki wody a także dla czujników temperatur', 1, 8, 'LAZ_UMYW', 0),
(22, 'Rozdzielnia w kuchni', 'Główna rozdzielnia w kuchni umieszczona nad otworem wejściowym na bocznej ścianie. ', 1, 7, 'KUCH-ROZD', 0),
(23, 'Rozdzielnia światła (listw) LED w kuchni', 'Rodzielnia umieszczona nad drzwiami szklanymi zasłonięta przez szafkę nad lodówką', 1, 7, 'KUCH-ROZD_LOD', 0),
(24, 'Puszka w kuchni obok gazu', 'W kuchni na ścianie w kanałem odpowietrzającym obok rury gazowej', 1, 7, 'KUCH-SZAF_GAZ', 0),
(25, 'Rozdzielnia licznik', 'W holu umieszczona nad drzwiami wejściowymi', 1, 1, 'HOL-LICZNIK', 0),
(26, 'Rozdzielnia pokój', 'Umieszczona na dłuższej ścianie dłuższej łazienki. ', 1, 4, 'POK-ROZD', 0),
(27, 'Rozdzielnia przy pompie wody', 'Łazienka, umieszczona za wanną. ', 0, 8, 'LAZ-POMPA', 1),
(28, 'Rozdzielnia sypialnia', 'Umieszczona w sypialni na ścianie z przedpokojem po lewej stronie w rogu ze ścianą od salonu', 1, 3, 'SYP-ROZD', 0),
(29, 'Grzejnik jadalnia', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w jadalni', 0, 9, 'JAD-GRZEJNIK', 0),
(30, 'Gniazda 230V pokój', 'Umieszczone na ścianie z salonem pod oknem i na ścianie na naprzeciwko bliżej okna i bliżej łazienki. ', 0, 4, 'POK-GNIAZDA', 0),
(31, 'Grzejnik pracownia', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w pracowni', 0, 5, 'PRAC-GRZEJNIK', 0),
(32, 'Grzejnik salon', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w salonie', 0, 6, 'SAL-GRZEJNIK', 0),
(33, 'Grzejnik sypialnia', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w sypialni', 0, 3, 'SYP-GRZEJNIK', 0),
(34, 'Sciana w holu z drzwiami od pokojów', 'Sciana w holu z drzwiami od pokojów', 0, 1, 'HOL-SC_POKOJE', 1),
(35, 'Kontaktron pokój', 'Kontaktron umieszczony w drzwiach od pokoju', 0, 4, 'POK-KONTAKTRON', 0),
(36, 'Kontaktron pracownia', 'Kontaktron umieszczony w drzwiach od pracowni ', 0, 5, 'PRAC-KONTAKTRON', 0),
(37, 'Czujniki ruchu w holu od pokoi', 'Czujnik ruchu umieszczony na ścianie z drzwiami od pokoju na górze przy rurze gazowej', 0, 1, 'HOL-RUCH_POK', 0),
(38, 'Czujniki ruchu w holu od łazienki', 'Czujniki ruchu umieszczone w holu na ścianie od łazienki z drzwiami na rogu bliżej salonu', 0, 1, 'HOL-RUCH_LAZ', 0),
(39, 'Czujniki ruchu w holu od sypialni', 'Czujnik ruchu umieszczony na ścianie od sypialni na rogu bliżej salonu', 0, 1, 'HOL-RUCH-SYP', 0),
(40, 'Gniazda 230V w WC', 'Umieszcozne koło pralki', 0, 2, 'WC-GNIAZDA', 0),
(41, 'Temperatura hol', 'Czujnik temperatury umieszczony koło włącznika do WC', 0, 1, 'HOL-TEMP', 0),
(42, 'Włączniki hol na ścianie sypialni', 'Dwa włączniki podwójne w holu na ścianie od sypialni', 0, 1, 'HOL-WLACZ_SYP', 0),
(43, 'Włącznik hol drzwi wejściowe', 'Pojedyńczy włącznik w holu umieszczony przy samych drzwiach', 0, 1, 'HOL-WLACZ_DRZWI', 0),
(44, 'Temperatura sypialnia', 'Czujnik temperatury w sypialni umieszczony na ścianie od salonu', 0, 3, 'SYP-TEMPERATURA', 0),
(45, 'Gniazda 230V w sypialni', 'Umieszczone na ścianie z salonem wysoko, na ścianie naprzeciw obok łózka nisko , na ścianie od holu nisko za szafą', 0, 3, 'SYP-GNIAZDA', 0),
(46, 'Włącznik sypialnia', 'Podwójny włącznik sypialnia umieszczony obok drzwi do sypialni', 0, 3, 'SYP-WLACZ', 0),
(47, 'Ukryta puszka sypialnia', 'Ukryta puszka w sypialni obok drzwi do sypialni po drugiej stronie co włącznik, ma służyć jak włącznik rolet/zasłon', 0, 3, 'SYP-UKR_PUSZKA', 0),
(48, 'Ukryta puszka salon', 'Ukryta puszka w salonie obok drzwi do sypialni po drugiej stronie co włącznik, ma służyć jak włącznik rolet/zasłon', 0, 6, 'SAL-UKR_PUSZKA', 0),
(49, 'Ukryta puszka pokój', 'Umieszczona obok okna po prawej stronie służy do włącznika rolety/zasłony', 0, 4, 'POK-UKR_PUSZKA', 0),
(50, 'Czujnik ruchu w pokoju', 'Umieszczona nad drzwiami w pokoju', 0, 4, 'POK_RUCH', 0),
(51, 'Czujnik ruchu w pracowni', 'Umieszczony nad drzwiami w pracowni', 0, 5, 'PRAC-RUCH', 0),
(52, 'Temperatura pracownia', 'Czujnik temperatury w pracowni umieszczony na ścianie od pokoi blisko drzwi', 0, 5, 'PRAC-TEMPERATURA', 0),
(53, 'Włącznik pracownia', 'Podwójny włącznik umieszczony na ścianie od wc przy drzwiach', 0, 5, 'PRAC-WLACZ', 0),
(54, 'Ukryta puszka w pracowni', 'Umieszczona przy oknie po lewej stronie jako włącznik rolet/zasłon', 0, 5, 'PRAC-UKR_PUSZKA', 0),
(55, 'Gniazdko z kablem sterowniczym', 'Gniazdko z kablem sterowniczym umieszczone po prawej stronie okna razem z gniazdem ethernetowym', 0, 5, 'PRAC-GN_STER', 0),
(56, 'Gniazda 230V w pracowni', 'Umieszczone przy oknie po obu stronach na ścianach od pokoju i z drugiej strony', 0, 5, 'PRAC-GNIAZDA', 0),
(57, 'Gniazdo z gwarantowanym 230V', 'Gniazdko z niewyłączalnym zasilaniem umieszczone na dłuższej ścianie WC', 0, 5, 'PRAC-GW_GNIAZD', 0),
(58, 'Temperatura salon', 'Czujnik temperatury w salonie umieszczony na ścianie od sypialni', 0, 6, 'SAL-TEMPERATURA', 0),
(59, 'Czujnik ruchu w salonie', 'Umieszczony w salonie na ścianie od kuchni nad drzwiami szklanymi', 0, 6, 'SAL-RUCH', 0),
(60, 'Włącznik w salonie przy holu', 'Podwójny włącznik w salonie przy holu', 0, 6, 'SAL-WLACZ_HOL', 0),
(61, 'Włącznik przy drzwiach sypialni', 'Dwa podwójne włączniki przy drzwiach sypialni', 0, 6, 'SAL-WLACZ_SYP', 0),
(62, 'Włącznik salon na ścianie łazienki', 'Podwójny włącznik w salonie na ścianie łazienki', 0, 6, 'SAL-WLACZ_LAZ', 0),
(63, 'Włącznik w salonie od kuchni', 'Dwa podwójne włączniki w salonie umieszczone na ścianie od kuchni od strony jadalni', 0, 6, 'SAL-WLACZ_KUCH', 0),
(64, 'Gniazda 230V w salonie', 'Umieszczone sa na ścianie od sypialni po obu stronach, na ścianie od łazienki, na ścianie od kuchni. ', 0, 6, 'SAL-GNIAZDA', 0),
(65, 'Temperatura salon/jadalnia', 'Czujnik temperatury w salonie na ścianie od kuchni od strony jadalni przy włącznikach', 0, 6, 'SAL-TEMP_JAD', 0),
(66, 'Temperatura kuchnia/jadalnia', 'Czujnik temperatury w kuchni na ścianie od salonu od strony jadalni przy włącznikach', 0, 7, 'KUCH-TEMP_JAD', 0),
(67, 'Temperatura kuchnia', 'Czujnik temperatury umieszczony na meblach ', 0, 7, 'KUCH-TEMPERATURA', 0),
(68, 'Temperatura Jadalnia', 'Czujnik temperatury umieszczony w jadalnie przy oknie.', 0, 9, 'JAD_TEMPERATURA', 0),
(69, 'Temperatura salon/łazienka', 'Czujnik temperatury umieszczony w ścianie od łazienki', 0, 6, 'SAL-TEMP_SC_LAZ', 0),
(70, 'Temperatura salon podłoga', 'Czujnik temperatury umieszczony w podłodze przy ścianie łazienki od ogrzewania elektrycznego', 0, 6, 'SAL-TEMP_PODL', 0),
(71, 'Temperatura hol podłoga środek', 'Czujnik temperatury w holu w podłodze umieszczony na środku kwadratu od ogrzewania elektrycznego', 0, 1, 'HOL-TEMP_PODL_SR', 0),
(72, 'Puszka za szafką łazienka', 'Umieszczona w łazience za szafką umywalkową. ', 1, 8, 'LAZ-SZAFKA', 0),
(73, 'Rozdzielnia wody za umywalką', 'Rozdzielnia wody w łazience za szafką umywalkową ', 1, 8, 'LAZ-ROZD_WODY', 0),
(74, 'Ukryta puszka w jadalni', 'Umieszczona na ścianie z oknem po lewej stronie przy czujniku temperatury', 0, 9, 'JAD-UKRYTPUSZKA', 0),
(75, 'Czujnik ruchu w kuchni drzwi', 'Czujnik ruchu w kuchni umieszczony nad drzwiami szklanymi', 0, 7, 'KUCH-RUCH_DRZWI', 0),
(76, 'Drzwi rewizyjne od pompy', 'Drzwiczki rewizyjne umieszczone w kuchni koło lodówki na pompę od ogrzewania podłogowego', 0, 7, 'KUCH-DRZWI_REW', 0),
(77, 'Drzwi w kuchni', 'Drzwi szklanie w kuchni', 0, 7, 'KUCH-DRZWI', 0),
(78, 'Filar w kuchni', 'Kuchnia, ściana z wywietrznikiem', 0, 7, 'KUCH-FILAR', 0),
(79, 'Temperatura kuchnia podłoga ', 'Czujnik temperatury w podłodze w kuchni (ogrzewanie wodne)', 0, 7, 'KUCH-PODL_TEMP', 0),
(80, 'Zawory wody w kuchni pod zlewem', 'Zawory wody w kuchni pod zlewem', 0, 7, 'KUCH-ZLEW', 0),
(81, 'Radio w kuchni', 'Gniazda umieszczone w szafka na końcu kuchni przy jadalni gdzie jest radio', 0, 7, 'KUCH-RADIO', 0),
(82, 'Włącznik w kuchni/jadalnia', 'Dwa podwójne włączniki w kuchni umieszczone na ścianie od salonu od strony jadalni', 0, 7, 'KUCH-WLACZ-JAD', 0),
(83, 'Pod szafkami w kuchni', 'Pod szafkami w kuchni', 0, 7, 'KUCH-POD_SZAF', 0),
(84, 'Wyciąg w kuchni', 'Puszka umieszczona w górnej szafce nad wyciągiem', 1, 7, 'KUCH-WYCIAG', 0),
(85, 'Zawór gazu w kuchni', 'Zawór gazu w kuchni umieszczony pod płytą gazową', 0, 7, 'KUCH-ZAWOR', 0),
(86, 'Kontaktron łazienka', 'Kontaktron umieszczony w drzwiach od łazienki', 0, 8, 'LAZ-KONTAKTRON', 0),
(87, 'Gniazdo 230V w łazience prawe', 'Gniazdo 230V w łazience umieszczone po prawej stronie drzwi (koło sedesu)', 0, 8, 'LAZ-GNIAZD_PRAWE', 0),
(88, 'Gniazdo 230V w łazience lewe', 'Gniazdo 230V w łazience lewe umieszczone po lewej stronie drzwi bliżej wanny', 0, 8, 'LAZ-GNIAZD_LEWE', 0),
(89, 'Monitor pod lustrem', 'Monitor pod lustrem w łazience. ', 0, 8, 'LAZ-MONITOR', 0),
(90, 'Temperatura łazienka podłoga', 'Czujnik temperatury w podłodze w łazience (ogrzewanie wodne)', 0, 7, 'LAZ-PODL_TEMP', 0),
(91, 'Łazienka, ściana z drzwiami', 'Łazienka, ściana z drzwiami obok wanny', 0, 8, 'LAZ-SC_DRZWI', 1),
(92, 'Gabaryt w łazience', 'Gabaryt w łazience', 0, 8, 'LAZ-GABARYT', 0),
(93, 'Gniazdo 230V w pod lustrem lewe', 'Gniazdo 230V w pod lustrem lewe w łazience bliżej wanny', 0, 8, 'LAZ-GND-LUS-LEWE', 0),
(94, 'Gniazda 230V pod lustrem prawe', 'Gniazda 230V pod lustrem prawe bliżej prysznica w łazience', 0, 8, 'LAZ-GND-LUS-PRAW', 0),
(95, 'Okno jadalnia', 'Kontaktrony w oknie w jadalni', 0, 9, 'OKNO-JADALNIA', 0),
(96, 'Okno salon', 'Kontaktrony w oknie w salonie', 0, 6, 'OKNO-SALON', 0),
(97, 'Okno sypialnia', 'Kontaktrony w oknie w sypialni', 0, 3, 'OKNO-SYPIALNIA', 0),
(98, 'Okno pokój', 'Kontaktrony w oknie w pokoju', 0, 4, 'OKNO-POKOJ', 0),
(99, 'Okno pracownia', 'Kontaktrony w oknie w pracowni', 0, 5, 'OKNO-PRACOWNIA', 0),
(100, 'Pompa od ogrzewania podłogowego', 'Pompa od ogrzewania podłogowego umieszczona za wanną', 0, 8, 'POMPA-OGRZ', 0),
(101, 'Gniazdka koło TV', 'Gniazdka koło TV w salone umieszczone na ścianie od kuchni', 0, 6, 'SAL-TV', 0),
(102, 'Włącznik kuchnia/hol', 'Cztery (w tym jeden schowany) podwójne włączniki w kuchni od strony holu, bliżej łazienki. Dwa dotycząca salonu, jeden widoczny i jeden schowany dotyczą kuchni', 0, 7, 'KUCH-WLACZ-HOL', 0),
(103, 'Czujnik ruchu w łazience po lewej stronie drzwi', 'Czujnik ruchu w łazience po lewej stronie bliżej wanny', 0, 8, 'LAZ-RUCH_LEWY', 0),
(104, 'Czujnik ruchu w łazience po prawej stronie drzwi', 'Czujnik ruchu w łazience po prawej stronie drzwi bliżej kibla', 0, 8, 'LAZ-RUCH_PRAWY', 0),
(105, 'Połączenie kabli 20, 21, 22 WC gabaryt', 'Połączenie kabli 20 8 żył na dwa 4 żyłowe 21, 22 WC gabaryt', 0, 2, 'P-20.21.22', 1),
(106, 'Kuchnia, ukryta puszka ', 'Kuchnia, ukryta puszka koło włączników umieszczona na przeciwko lodówki obok włącznika światła w ', 0, 7, 'KUCH-UKR_PUSZ', 0);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `MiejscePrzewodView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `MiejscePrzewodView` (
`id` smallint unsigned
,`pid` tinyint unsigned
,`mid` tinyint unsigned
,`nazwa` text
,`opis` text
,`zbiorcze` tinyint(1)
,`id_pomieszczenie` tinyint unsigned
,`kod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` text
,`ppid` tinyint unsigned
,`popis` text
,`ilosc_zyl` tinyint unsigned
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `MiejsceView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `MiejsceView` (
`id` tinyint unsigned
,`nazwa` text
,`opis` text
,`zbiorcze` tinyint(1)
,`id_pomieszczenie` tinyint unsigned
,`kod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` text
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `PlytkaMiejsceView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `PlytkaMiejsceView` (
`id` tinyint unsigned
,`nazwa` text
,`miejsce_id` tinyint unsigned
,`mnazwa` text
,`opis` text
,`zbiorcze` tinyint(1)
,`id_pomieszczenie` tinyint unsigned
,`kod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` text
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `plytki`
--

CREATE TABLE `plytki` (
  `id` tinyint UNSIGNED NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `miejsce_id` tinyint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `plytki`
--

INSERT INTO `plytki` (`id`, `nazwa`, `miejsce_id`) VALUES
(1, 'Płytka rozdzielcza', 2),
(2, 'Płytka z procesorem', 2),
(3, 'Płytka rozdzielcza', 22),
(4, 'Płytka z procesorem', 22),
(5, 'Płytka rozdzielcza', 23),
(6, 'Płytka A I/O', 26),
(7, 'Płytka B I/O', 26),
(8, 'Płytka C Zasilanie', 26);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `polaczenie_plytka`
--

CREATE TABLE `polaczenie_plytka` (
  `id` smallint UNSIGNED NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `plytka_id` tinyint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `polaczenie_plytka`
--

INSERT INTO `polaczenie_plytka` (`id`, `nazwa`, `plytka_id`) VALUES
(1, 'SDA', 2),
(2, 'SCL', 2),
(3, '0x00.P0', 2),
(4, '0x00.P1', 2),
(5, '0x00.P2', 2),
(6, '0x00.P3', 2),
(7, '0x00.P4', 2),
(8, '0x00.P5', 2),
(9, '0x00.P6', 2),
(10, '0x00.P7', 2),
(11, '0x00.INT', 2),
(12, 'GND', 2),
(13, '5V', 2),
(14, 'TTL RX', 2),
(15, 'TTL TX', 2),
(16, 'RS RX', 2),
(17, 'RS TX', 2),
(18, '0x01.INT', 2),
(19, '0x01.P0', 2),
(20, '0x01.P1', 2),
(21, '0x01.P2', 2),
(22, '0x01.P3', 2),
(23, '0x01.P4', 2),
(24, '0x01.P5', 2),
(25, '0x01.P6', 2),
(26, '0x01.P7', 2),
(27, '5V ogrz.', 1),
(28, 'CPU9', 2),
(29, 'GND', 1),
(30, '5V', 1),
(31, '24V', 1),
(32, 'A2-F12', 1),
(33, 'A3-F11', 1),
(34, 'A4-F10', 1),
(35, 'A5-F9', 1),
(36, 'A6-F8', 1),
(37, 'A7-F7', 1),
(38, 'A8-F6', 1),
(39, 'Włącznik', 1),
(40, 'Kontaktron', 1),
(41, 'Podświetlenie', 1),
(42, 'D2-H3', 1),
(43, 'Cz. ruchu', 1),
(44, 'Cz. zbliż.', 1),
(45, 'D3-H2', 1),
(46, 'D8-E2', 1),
(47, 'D7-I2', 1),
(48, 'N7-P6', 1),
(49, 'N6-P7', 1),
(50, 'N5-P8', 1),
(51, 'K1-P1', 1),
(52, 'K2-P2', 1),
(53, 'K6-O8', 1),
(54, 'K7-O7', 1),
(55, 'K8-O6', 1),
(56, 'J8-K9', 1),
(57, 'J7-K10', 1),
(58, 'J6-K11', 1),
(59, 'J5-K12', 1),
(60, 'J4-P3', 1),
(61, 'J3-P4', 1),
(62, 'GND', 6),
(63, '+5V', 6),
(64, 'SDA', 6),
(65, 'SCL', 6),
(66, 'INT 0X00', 6),
(67, 'INT 0x01', 6),
(68, '3.2-158.4', 6),
(69, '3.3-158.3', 6),
(70, '145.3-1b7', 6),
(71, '145.4-1b6', 6),
(72, '145.5-1b5', 6),
(73, '145.6-1b4', 6),
(74, '145.7-1b3', 6),
(75, '145.8-1b2', 6),
(76, '145.9-1b1', 6),
(77, '145.10-1b0', 6),
(78, '146.3-1a7', 6),
(79, '146.4-1a6', 6),
(80, '146.5-1a5', 6),
(81, '146.6-1a4', 6),
(82, '146.7-1a3', 6),
(83, '146.8-1a2', 6),
(84, '146.9-1a1', 6),
(85, '146.10-1a0', 6),
(86, '2.2-0b0', 6),
(87, '2.3-0b1', 6),
(88, '2.4-0b2', 6),
(89, '2.5-0b3', 6),
(90, '2.6-0b4', 6),
(91, '2.7-0b5', 6),
(92, '2.8-0b6', 6),
(93, '2.9-0b7', 6),
(94, '1.2-0a3', 6),
(95, '1.3-0a2', 6),
(96, '1.4-0a1', 6),
(97, '1.5-0a0', 6),
(98, '3.4-0a6', 6),
(99, '3.5-0a5', 6),
(100, 'GND', 8),
(101, '24V', 8),
(102, '+5V', 8),
(103, 'WIE', 8),
(104, 'NOC', 8),
(105, '2TAR', 8),
(106, 'Z.AW', 8),
(107, 'RS.RX', 8),
(108, 'RS.TX', 8),
(109, 'TTL.RX', 8),
(110, 'TTL.TX', 8);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `polaczenie_plytka_polaczenie`
--

CREATE TABLE `polaczenie_plytka_polaczenie` (
  `id` smallint UNSIGNED NOT NULL,
  `polaczenie_plytka_id` smallint UNSIGNED NOT NULL,
  `elementy_plytkowe_piny_id` smallint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `polaczenie_plytka_polaczenie`
--

INSERT INTO `polaczenie_plytka_polaczenie` (`id`, `polaczenie_plytka_id`, `elementy_plytkowe_piny_id`) VALUES
(1, 1, 71),
(2, 1, 25),
(3, 1, 12),
(4, 2, 72),
(5, 2, 26),
(6, 2, 13),
(7, 11, 9),
(8, 11, 76),
(9, 12, 52),
(10, 12, 56),
(11, 12, 49),
(12, 12, 70),
(13, 12, 11),
(14, 12, 80),
(15, 12, 60),
(16, 12, 24),
(17, 12, 64),
(18, 12, 69),
(19, 13, 50),
(20, 13, 51),
(21, 13, 55),
(22, 13, 23),
(23, 13, 82),
(24, 13, 10),
(25, 16, 65),
(26, 17, 66),
(27, 15, 67),
(28, 15, 61),
(29, 14, 68),
(30, 14, 62),
(31, 3, 46),
(32, 3, 1),
(33, 4, 2),
(34, 4, 45),
(35, 5, 16),
(36, 5, 44),
(37, 6, 4),
(38, 6, 43),
(39, 7, 5),
(40, 7, 40),
(41, 8, 6),
(42, 8, 39),
(43, 9, 7),
(44, 10, 8),
(45, 9, 42),
(46, 10, 41),
(47, 18, 22),
(48, 19, 14),
(49, 19, 30),
(50, 20, 15),
(51, 20, 29),
(52, 21, 16),
(53, 21, 28),
(54, 22, 17),
(55, 22, 27),
(56, 23, 18),
(57, 23, 38),
(58, 24, 19),
(59, 24, 37),
(60, 25, 20),
(61, 26, 21),
(62, 28, 78),
(63, 28, 34),
(64, 29, 105),
(65, 29, 106),
(66, 29, 134),
(67, 29, 135),
(68, 29, 108),
(69, 29, 112),
(70, 29, 136),
(71, 29, 119),
(72, 29, 140),
(73, 29, 164),
(74, 29, 185),
(75, 29, 186),
(76, 29, 143),
(77, 29, 177),
(78, 29, 198),
(79, 29, 93),
(80, 30, 124),
(81, 30, 104),
(82, 30, 200),
(83, 27, 109),
(84, 27, 117),
(85, 27, 139),
(86, 27, 142),
(87, 27, 144),
(88, 27, 174),
(89, 30, 133),
(90, 30, 94),
(91, 30, 175),
(92, 31, 95),
(93, 31, 92),
(94, 32, 96),
(95, 32, 131),
(96, 33, 97),
(97, 33, 130),
(98, 34, 98),
(99, 34, 129),
(100, 35, 99),
(101, 35, 128),
(102, 36, 100),
(103, 36, 127),
(104, 37, 101),
(105, 37, 126),
(106, 38, 102),
(107, 38, 125),
(108, 39, 123),
(109, 40, 122),
(110, 40, 107),
(111, 39, 165),
(112, 41, 181),
(113, 41, 194),
(114, 41, 163),
(115, 43, 103),
(116, 43, 120),
(117, 42, 138),
(118, 42, 110),
(119, 44, 121),
(120, 44, 132),
(121, 45, 137),
(122, 45, 110),
(123, 46, 116),
(124, 46, 118),
(125, 47, 115),
(126, 47, 141),
(127, 61, 145),
(128, 61, 193),
(129, 60, 146),
(130, 60, 192),
(131, 59, 147),
(132, 59, 162),
(133, 58, 148),
(134, 58, 161),
(135, 57, 149),
(136, 57, 160),
(137, 56, 150),
(138, 56, 159),
(139, 51, 151),
(140, 51, 190),
(141, 52, 152),
(142, 52, 191),
(143, 53, 156),
(144, 53, 187),
(145, 54, 157),
(146, 54, 188),
(147, 55, 158),
(148, 55, 187),
(149, 50, 178),
(150, 50, 197),
(151, 49, 179),
(152, 49, 196),
(153, 48, 180),
(154, 48, 195),
(155, 62, 306),
(156, 62, 316),
(157, 62, 322),
(158, 62, 328),
(159, 62, 329),
(160, 62, 338),
(161, 62, 339),
(162, 62, 340),
(163, 62, 341),
(164, 62, 350),
(165, 62, 351),
(166, 62, 356),
(167, 62, 361),
(168, 62, 368),
(169, 62, 369),
(170, 62, 388),
(171, 62, 389),
(172, 62, 411),
(173, 62, 416),
(174, 63, 315),
(175, 63, 321),
(176, 63, 327),
(177, 63, 359),
(178, 63, 360),
(179, 63, 386),
(180, 63, 387),
(181, 63, 406),
(182, 63, 407),
(183, 63, 412),
(184, 63, 417),
(185, 64, 410),
(186, 64, 415),
(187, 64, 364),
(188, 65, 365),
(189, 65, 409),
(190, 65, 414),
(191, 66, 367),
(192, 66, 408),
(193, 67, 366),
(194, 67, 413),
(195, 68, 323),
(196, 68, 357),
(197, 68, 363),
(198, 69, 324),
(199, 69, 358),
(200, 69, 362),
(201, 70, 330),
(202, 70, 404),
(203, 71, 331),
(204, 71, 402),
(205, 72, 332),
(206, 72, 400),
(207, 73, 333),
(208, 73, 398),
(209, 74, 334),
(210, 74, 396),
(211, 75, 335),
(212, 75, 394),
(213, 76, 336),
(214, 76, 392),
(215, 77, 337),
(216, 77, 390),
(217, 78, 342),
(218, 78, 405),
(219, 79, 343),
(220, 79, 403),
(221, 80, 344),
(222, 80, 401),
(223, 81, 345),
(224, 81, 399),
(225, 82, 346),
(226, 82, 397),
(227, 83, 347),
(228, 83, 395),
(229, 84, 348),
(230, 84, 393),
(231, 85, 349),
(232, 85, 391),
(233, 86, 307),
(234, 86, 258),
(235, 87, 308),
(236, 87, 372),
(237, 88, 309),
(238, 88, 374),
(239, 89, 310),
(240, 89, 376),
(241, 90, 311),
(242, 90, 378),
(243, 91, 312),
(244, 91, 380),
(245, 92, 313),
(246, 92, 382),
(247, 93, 314),
(248, 93, 384),
(249, 94, 317),
(250, 94, 377),
(251, 98, 325),
(252, 98, 383),
(253, 99, 326),
(254, 99, 381),
(255, 95, 318),
(256, 95, 375),
(257, 96, 319),
(258, 96, 373),
(259, 97, 320),
(260, 97, 371),
(261, 100, 514),
(262, 100, 517),
(263, 100, 524),
(264, 100, 531),
(265, 100, 511),
(266, 101, 523),
(267, 101, 510),
(268, 102, 513),
(269, 102, 518),
(270, 102, 532),
(271, 102, 512),
(272, 103, 519),
(273, 103, 530),
(274, 104, 520),
(275, 104, 529),
(276, 105, 521),
(277, 105, 528),
(278, 106, 522),
(279, 106, 527),
(280, 107, 526),
(281, 107, 536),
(282, 108, 525),
(283, 108, 535),
(284, 109, 515),
(285, 109, 534),
(286, 110, 516),
(287, 110, 533);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `polaczenie_zyla`
--

CREATE TABLE `polaczenie_zyla` (
  `id` smallint UNSIGNED NOT NULL,
  `zakonczenie_zyly_id` smallint UNSIGNED NOT NULL,
  `zyla_id` smallint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `polaczenie_zyla`
--

INSERT INTO `polaczenie_zyla` (`id`, `zakonczenie_zyly_id`, `zyla_id`) VALUES
(1, 204, 4),
(2, 204, 400),
(3, 205, 1),
(4, 205, 398),
(5, 206, 8),
(6, 206, 403),
(7, 207, 2),
(8, 207, 399),
(9, 208, 7),
(10, 208, 405),
(11, 209, 3),
(12, 209, 401),
(13, 210, 6),
(14, 210, 402),
(15, 211, 5),
(16, 211, 404),
(17, 212, 400),
(18, 212, 4),
(19, 213, 401),
(20, 213, 3),
(21, 214, 399),
(22, 214, 2),
(23, 215, 398),
(24, 215, 1),
(25, 216, 402),
(26, 216, 6),
(27, 217, 405),
(28, 217, 7),
(29, 218, 403),
(30, 218, 8),
(31, 219, 404),
(32, 219, 5),
(33, 220, 260),
(34, 220, 275),
(35, 221, 256),
(36, 221, 315),
(37, 222, 265),
(38, 222, 270),
(39, 223, 263),
(40, 223, 272),
(41, 224, 264),
(42, 224, 271),
(43, 225, 262),
(44, 225, 273),
(45, 226, 261),
(46, 226, 274),
(47, 227, 259),
(48, 227, 276),
(49, 228, 258),
(50, 228, 277),
(51, 229, 257),
(52, 229, 278),
(53, 230, 268),
(54, 230, 279),
(55, 231, 269),
(56, 231, 314),
(57, 232, 267),
(58, 232, 280),
(59, 233, 266),
(60, 233, 281),
(61, 234, 271),
(62, 234, 264),
(63, 235, 272),
(64, 235, 263),
(65, 236, 270),
(66, 236, 265),
(67, 237, 274),
(68, 237, 261),
(69, 238, 273),
(70, 238, 262),
(71, 239, 275),
(72, 239, 260),
(73, 240, 276),
(74, 240, 259),
(75, 241, 277),
(76, 241, 258),
(77, 242, 278),
(78, 242, 257),
(79, 243, 281),
(80, 243, 266),
(81, 244, 280),
(82, 244, 267),
(83, 245, 279),
(84, 245, 268),
(85, 246, 314),
(86, 246, 269),
(87, 247, 315),
(88, 247, 256),
(89, 248, 283),
(90, 248, 291),
(91, 249, 289),
(92, 249, 297),
(93, 250, 288),
(94, 250, 296),
(95, 251, 287),
(96, 251, 295),
(97, 252, 286),
(98, 252, 294),
(99, 253, 285),
(100, 253, 293),
(101, 254, 284),
(102, 254, 292),
(103, 255, 282),
(104, 255, 290),
(105, 256, 291),
(106, 256, 283),
(107, 257, 290),
(108, 257, 282),
(109, 258, 293),
(110, 258, 285),
(111, 259, 292),
(112, 259, 284),
(113, 260, 294),
(114, 260, 286),
(115, 261, 295),
(116, 261, 287),
(117, 262, 296),
(118, 262, 288),
(119, 263, 297),
(120, 263, 289),
(121, 288, 427),
(122, 288, 416),
(123, 289, 426),
(124, 289, 415),
(125, 290, 429),
(126, 290, 411),
(127, 291, 430),
(128, 291, 413),
(129, 292, 428),
(130, 292, 411),
(131, 293, 431),
(132, 293, 410),
(133, 294, 432),
(134, 294, 417),
(135, 295, 433),
(136, 295, 416),
(137, 264, 411),
(138, 264, 418),
(139, 264, 419),
(140, 264, 424),
(141, 264, 425),
(142, 264, 428),
(143, 264, 429),
(144, 265, 420),
(145, 265, 422),
(146, 265, 430),
(147, 265, 413),
(148, 266, 416),
(149, 266, 427),
(150, 266, 433),
(151, 267, 412),
(152, 267, 423),
(153, 268, 414),
(154, 268, 421),
(155, 269, 410),
(156, 269, 431),
(157, 270, 415),
(158, 270, 426),
(159, 271, 417),
(160, 271, 432),
(161, 272, 418),
(162, 272, 411),
(163, 273, 419),
(164, 273, 411),
(165, 274, 420),
(166, 274, 413),
(167, 275, 421),
(168, 275, 414),
(169, 276, 424),
(170, 276, 411),
(171, 277, 425),
(172, 277, 411),
(173, 278, 422),
(174, 278, 413),
(175, 279, 423),
(176, 279, 412),
(177, 280, 428),
(178, 280, 411),
(179, 281, 429),
(180, 281, 411),
(181, 282, 430),
(182, 282, 413),
(183, 283, 431),
(184, 283, 410),
(185, 284, 433),
(186, 284, 416),
(187, 285, 432),
(188, 285, 417),
(189, 286, 427),
(190, 286, 416),
(191, 287, 426),
(192, 287, 415);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pomieszczenie`
--

CREATE TABLE `pomieszczenie` (
  `id` tinyint UNSIGNED NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `pomieszczenie`
--

INSERT INTO `pomieszczenie` (`id`, `nazwa`) VALUES
(1, 'Przedpokój'),
(2, 'WC'),
(3, 'Sypialnia'),
(4, 'Pokój'),
(5, 'Pracownia'),
(6, 'Salon'),
(7, 'Kuchnia'),
(8, 'Łazienka'),
(9, 'Jadalnia');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `przewod`
--

CREATE TABLE `przewod` (
  `id` tinyint UNSIGNED NOT NULL,
  `opis` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `ilosc_zyl` tinyint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `przewod`
--

INSERT INTO `przewod` (`id`, `opis`, `ilosc_zyl`) VALUES
(1, 'Łazienka, sterowanie oświetlenie prysznica', 6),
(2, 'Łazienka, sterowanie światłem nad wanną i nad lustrem, ogrzewaniem szyby, radiem, magicmirror', 10),
(3, 'Łazienka, sterowanie światłem głównym', 6),
(4, 'Łazienka,sterowanie raspberry, monitorem, radiem, oświetleniem nad lustrem', 8),
(5, 'Łazienka, czujnik temperatury monitora', 3),
(6, 'Łazienka, czujnik temperatury i wilgotności  przy kabinie prysznicowej', 4),
(7, 'Czujniki ogrzewania podłogowego w kuchni, łazience, w salonie. Kabel A', 10),
(8, 'Czujniki ogrzewania podłogowego w kuchni, łazience, w salonie. Kabel B', 4),
(9, 'Salon, czujnik temperatury od ogrzewania ściennego', 3),
(10, 'Kuchnia, czujnik temperatury od ogrzewania podłogowego', 3),
(11, 'Łazienka, czujnik temperatury od ogrzewania podłogowego', 3),
(12, 'Łazienka, czujnik temperatury od ogrzewania podłogowego w łazience', 3),
(13, 'Łazienka, czujniki ruchu i kontaktron', 8),
(14, 'Łazienka, kontaktron', 2),
(15, 'Łazienka, czujnik ruchu po prawej stronie (wanna)', 3),
(16, 'Łazienka, czujniki ruchu po lewej stronie (prysznic)', 3),
(17, 'Łazienka, kabel na przyszłość w gniazdku w łazience', 10),
(18, 'Łazienka, do czujnika wody i przycisku od wiatraka w łazience', 6),
(19, 'Kuchnia, kontaktron drzwiczek rewizyjnych do pompy', 2),
(20, 'WC, czujniki poziomu wody w gabarycie i przycisku wiatraka, temperatury w WC', 8),
(21, 'WC. czujnik temperatury na gabarycie z boku, powiązane z kablem 20', 4),
(22, 'WC, czujnik poziomu wody w sedesie, powiązane z kablem 20', 4),
(23, 'WC, przycisk od wiatraka i przepływomierz', 4),
(24, 'WC, sterowanie oświetleniem', 8),
(25, 'WC, dodatkowa funkcjonalność pod lustrem', 8),
(26, 'WC, czujnik ruchu nad drzwiami', 4),
(27, 'WC, kontaktron drzwi wejściowych', 2),
(28, 'WC, czujnik ruchu pod lustrem', 4),
(29, 'WC, czujnik przepływu wody w umywalce', 6),
(30, 'WC, czujnik zalania wody w WC', 6),
(31, 'WC. czujnik przepływu wody w pralce', 6),
(32, 'WC. czujnik temperatury w podłodze', 3),
(33, 'Hol, czujnik temperatury w podłodze', 3),
(34, 'Łącznik centrali WC i głównej centrali kabel A (zasilanie)', 8),
(35, 'Łącznik centrali WC i głównej centrali. Kabel B (Inne).', 8),
(36, 'Łącznik centrali WC i głównej centrali kabel C (ogrzewanie)', 8),
(37, 'Hol, czujnik temperatury, włącznik dwukanałowy. Przerwany niebieski i czarny.', 8),
(38, 'Łącznik cenrali pokój z centralą główną (steroanie ogrzewanie i ośw. kwiatów)', 8),
(39, 'Przekaźniki ogrzewania w WC', 4),
(40, 'Włącznik światła WC', 3),
(41, 'Hol, dodatkowy kabel w zabudowie rury gazowej', 8),
(42, 'Hol, kabel od czujników ruchu i kontaktronów. Powiązany z kablami 43, 44, 45, 46, 47', 8),
(43, 'Hol, czujnik ruchu w Holu umieszczony nad drzwiami do pokoju. Kabel powiązany z 42', 4),
(44, 'Pracowania, czujnik ruchu nad drzwiami. Kabel powiązany z 42', 4),
(45, 'Pracowania, kontaktron w drzwiach. Kabel powiązany z 42', 2),
(46, 'Pokoj, czujnik ruchu umieszczony nad drzwiami. Kabel powiązany z 42', 4),
(47, 'Pokoj, kontaktron w drzwiach. Kabel powiązany z 42', 2),
(48, 'WC, do mikroprocesora kabel A (prawa strona)', 12),
(49, 'WC, do mikroprocesora, kabel B (lewa strona)', 12),
(50, 'Łazienka, do przepływomierzy, kabel A', 10),
(51, 'Łazienka, do przepływomierzy, kabel B', 4),
(52, 'Pokoj. łącznik puszka pokoj z główną rozdzielnią. Zasilanie', 8),
(53, 'Pokoj, łącznik rozdzielni pokój z rodzielnią główną. (Zasilanie przekaźników, wiatraki)', 6),
(54, 'Pokoj, łącznik z puszki w pokoju z główną rozdzialnią. Inne', 6),
(55, 'Hol, czujnik ruchu w holu na ścianie Sypialni', 8),
(56, 'Hol, dodatkowo funkcjonalność na ścianie od sypialni', 10),
(57, 'Sypialnia, łącznik centrali w sypialni z rodzielnią główną. Kabel A', 8),
(58, 'Sypialnia, łącznik centrali w sypialni z rodzielnią główną. Kabel B', 8),
(59, 'Sypialnia, łącznik centrali w sypialni z rodzielnią główną. Kabel C', 8),
(60, 'Kuchnia, kontaktron drzwi szklanych', 4),
(61, 'Kuchnia sterowanie ogrzewanie w kuchni (nie podlaczone); Sygnal czujnikow ruchu.', 6),
(62, 'Kuchnia, kabel do czujników ruchu w kuchni nad drzwiami', 8),
(63, 'Kuchnia, czujnik ruchu w salonie nad drzwiami kuchni', 4),
(64, 'Kuchnia, sterowanie ledami sufit, drzwi', 8),
(65, 'Kuchnia, czujnik ruchu nad drzwiami w kuchni', 4),
(66, 'Kuchnia, puszka nad lodówką. Sterowanie przekażnikami ogrzewania z kabla 61', 4),
(67, 'Kuchnia. Puszka nad lodówką sterowanie przekaźnikami od ledów z kabla 64', 6),
(68, 'Kuchnia, Puszka nad lodówką sterowanie zasilaczem dla Ledow z kabla 64', 3),
(69, 'Licznik wody w kuchni', 8),
(70, 'Jadalnia, czujnik temperatury przy oknie', 8),
(71, 'Czujnik zewnetrzny temperatury', 8),
(72, 'Balkon', 10),
(73, 'Łazienka, czujnik temperatury przy drzwiach, powiazane z kablem 75', 4),
(74, 'Łazienka, czujnik zalania w łazienice, powiązane z kablem 75', 4),
(75, 'Łazienka czujnik zalania i czujnk temperatury przy drzwiach', 8),
(76, 'Łazienka, dodatkowa funkcjonalność dla raspberry', 10),
(77, 'Łazienka, dodatkowa funkcjonalność w szafce pod lustrem, kabel A', 8),
(78, 'Łazienka, dodatkowa funkcjonalność w szafce pod umywalką, kabel B', 8),
(79, 'Łazienka, kabel sterowniczy od panelu monitora', 6),
(80, 'Pokoj, czujnik temperatury niedaleko drzwi', 8),
(81, 'Pracownia, czujnik temperatury niedaleko drzwi', 8),
(82, 'Sypialnia, dodatkowa funkcjonalność w właczniku sypialni', 8),
(83, 'Salon, czujnik ruchu umieszczony na ścianie łązienki', 8),
(84, 'Sypialnia, czujnik temperatury na ścianie z salonem', 8),
(85, 'Salon, czujnik temperatury na ścianie z sypialnią', 8),
(86, 'Kuchnia, kabel w szafkach', 8),
(87, 'Kuchnia, kabel pod zlewem', 8),
(88, 'Kuchnia, do włącznika w Jadalni', 8),
(89, 'Kuchnia, kabel do szafek nad okapem i czujnika ruchu w kuchni. Kabel powiązany z 90 i 99 ', 8),
(90, 'Kuchnia do puszki nad okapem, kabel powiązany z kablami 89, 99', 8),
(91, 'Kuchnia , kabel od okapu do szafek', 4),
(92, 'Kuchnia, kabel od okapu do radia', 4),
(93, 'Kuchnia, łącznik z rozdzielnią główna. Kabel A.', 8),
(94, 'Kuchnia, łącznik z rodzielnią główną. Kabel B. Brak fioletowego.', 8),
(95, 'Kuchnia, do ukrytej puszki na ścianie z rozdzielnią.', 8),
(96, 'Hol, dodatkowa funkcjonalność obok rury gazowej', 8),
(97, 'Kuchnia, czujnik zalania w kuchni. Kabel powiązany z 87', 3),
(98, 'Kuchnia, czujnik temperatury w kuchni, kabel powiązany z 87', 4),
(99, 'Kuchnia, czujnik ruchu w kuchni obok czujnika gazu. Kabel powiązany z 89, 90, 99', 8),
(100, 'Kuchnia, kabel od umywalki do zaworu gazu. ', 4),
(101, 'Kuchnia, czujnik przepływu wody (żółty)', 3),
(102, 'Kuchnia, czujnik przepływu wody ciepła woda (niebieski)', 3),
(103, 'Kuchnia, czujnik przepływu wody, woda zimna (zielony)', 3),
(104, 'WC, czujnik przepływu wody ciepła woda (żółty)', 3),
(105, 'WC, czujnik przepływu wody zimna woda, (biały)', 3),
(106, 'WC, czujnik przepływu wody pralka zimna woda', 3),
(107, 'WC, czujnik przepływu wody, ciepła woda', 3),
(108, 'Łazienka, czunik przepływu wody', 3),
(109, 'Łazienka, czujnik przepływu wody', 3),
(110, 'Łazienka, czujnik przepływu wody', 3),
(111, 'Łazienka, czujnik przepływu wody', 3),
(112, 'Łazienka, czujnik przepływu wody', 3),
(113, 'Łazienka, czujnik przepływu wody', 3),
(114, 'Łazienka, czujnik przepływu wody', 3),
(115, 'Łazienka, uszkodzony kabel do Raspberry', 8),
(116, 'Kuchnia czujnik wilgotności i temperatury na zabudowie wysokiej kabel powiązany z 98', 3),
(117, 'Kuchnia, przycisk na zabudowie wysokiej kabel powiązany z 98', 2),
(118, 'Rodzielnia kuchnia - zasilanie i sterowanie przekaźnikami (4 kanał)', 6),
(119, 'Rozdzielnia kuchnia - łącznik do procesora', 8),
(120, 'Rozdzielnia kuchnia - zasilanie i sterowanie przekaźnikami (8 kanałów)', 10),
(121, 'Rozdzielnia kuchnia - zasilanie i sterowania przekaźniki (1 sztuka)', 3),
(122, 'Rozdzielnia kuchnia, łacznik z włącznikami', 10),
(123, 'Rozdzielnia kuchnia, łącznik z włącznikami', 10),
(124, 'Rozdzielnia kuchnia - rs dla procesora', 2),
(125, 'Jadalnia, kabel sterowniczy do grzejnika', 4),
(126, 'Salon, kabel sterowniczy do grzejnika', 4),
(127, 'Sypialnia, kabel sterowniczy do grzejnika', 4),
(128, 'Pokoj, kabel sterowniczy do grzejnika w pokoju', 4),
(129, 'Pracownia, kabel sterowniczy do grzejnika', 4),
(130, 'Jadalnia, kabel sterowniczy do okna', 4),
(131, 'Salon, kabel sterowniczy do okna', 4),
(132, 'Sypialnia, kabel sterowniczy do okna', 4),
(133, 'Pokój, kabel sterowniczy do okna', 4),
(134, 'Pracownia, kabel sterowniczy do okna', 4),
(135, 'Rozdzielnia, kabel łącznikowy powiązany z 125-134', 10),
(136, 'Rozdzielnia główna kabel łącznikowy powiązany z kablami 125-134', 10),
(137, 'Rozdzielnia główna, kabel łącznikowy powiązanych z 125-134', 10),
(138, 'Rozdzielnia główna, kabel łącznikowy powiązany z kablami 125-134', 10),
(139, 'Pracownia, ukryta puszka do rolet', 8),
(140, 'Pokoj, ukryta puszka do rolet', 8),
(141, 'Sypialnia, do ukrytej puszki do rolet', 8),
(142, 'Salon, do ukrytej puszki w salonie dla rolet', 8),
(143, 'Jadalnia, kabel oznakowany jako jadalnia w rozdzielni głównej', 8),
(144, 'Salon, kabel oznakowany jako salon, być może dochodzi do TV', 8),
(145, 'Lazienka - kabel w puszcze do włacznikow', 12),
(146, 'Lazienka, pokoje kabel do wlacznikow', 12),
(147, 'WC procesor, zasilanie i i2c układu wejścia/wyjścia 0x01', 4),
(148, 'WC procesor, zasilanie i i2c układu wejścia/wyjścia 0x00', 4),
(149, 'WC sufit zasilanie 4 przekaźników', 6),
(150, 'WC sufit, zasilanie 2 przekaźników', 4),
(151, 'Zasilanie przekaźników mechanicznych 2x LED/Zawór', 4),
(152, 'Rozdzielnia pokój, zasilanie i i2c dla przekaźników oświetlenia.', 12),
(153, 'Zasilanie i sterowanie przekażnikami ogrzewania', 10),
(154, 'Zasialnie przekaźników dla wiatrakó', 4),
(155, 'Zasialnie przekaźników do gniazd', 10),
(156, 'Zasialnie przekaźników dla oświetlania', 10),
(157, 'Zasilanie expander 0x000', 4),
(158, 'Łącznik płytki A z procesorem', 8),
(159, 'Zasilanie dolnej części płytki A', 4),
(160, 'Zasilanie ekspandera 0x001', 5),
(161, 'Masa dolnej i górnej płytki A', 2),
(162, 'Zasialanie płytek 5V', 2),
(163, 'Zasialnie procka i RX/TX', 4),
(164, 'Noc, wieczór. 2taryfa, zasilanie awaryjne', 4),
(165, 'Właczniki pokój C', 4),
(166, 'Lacznik do ekspandera', 3),
(167, 'Zasilanie przekaźnika awaryjnego', 4),
(168, 'łacznik płytek', 6),
(169, 'łacznik płytek', 2),
(174, '+5V', 2),
(175, 'Łacznik z mikroprocesorem', 12),
(176, 'Łacznik z mikroprocesorem', 12),
(177, 'Łącznik z centralą', 12),
(178, 'Łącznik z mikroprocesorem', 12),
(179, 'Łącznik z płytką mikroprocesową', 12),
(180, 'Czujnik temperatury podłogi w holu', 3),
(181, 'Ogrzewanie elektryczne przekaźniki', 4),
(182, 'Czujnik temperatury', 3),
(183, 'Łącznik z mikrokontrolerem', 12),
(184, '24V', 2),
(185, 'Łacznik centrali RS232', 12),
(186, 'Sygnały Wieczór, noc, 2 taryfa, zasilanie awaryjne', 4),
(187, '5V', 2),
(188, 'Łacznik z płytką mikroprocesora', 12),
(189, '24V i 5V', 4),
(190, 'łącznik z mikroprocesorem', 10),
(191, 'Wejście sygnały 5V (noc, wieczór, 2 taryfa, zas. awaryjne)', 4),
(192, 'Łacznik z prockiem', 12),
(193, '+5V stałe', 2),
(194, 'Łącznik z plytką do rozdzielni prądowej', 8),
(195, '24V sterowane', 2),
(196, 'Masa układu 3.3V', 2),
(197, 'Sygnał 3.3V nocy, zasilania awaryjnego, nocy, wieczoru, 2 taryfy', 4),
(198, 'Zasilanie 5V płytki z tranzystoramia', 2),
(199, 'Wyjście sygnałów 5V (noc, wieczór, 2 taryfa, zasilanie awaryjne)', 4),
(200, 'Zasilanie +24V, impulsy od licznika energi', 8);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `PrzewodMiejsceZakonczenieView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `PrzewodMiejsceZakonczenieView` (
`zid` smallint unsigned
,`etykieta` text
,`przewod_miejsce_id_zlacze` smallint unsigned
,`rodzaj_zakonczenia` tinyint(1)
,`przewod_id` tinyint unsigned
,`miejsce_id` tinyint unsigned
,`przewod_miejsce_id` smallint unsigned
,`nazwa` text
,`kod` varchar(1)
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `przewod_miejsce`
--

CREATE TABLE `przewod_miejsce` (
  `id` smallint UNSIGNED NOT NULL,
  `przewod_id` tinyint UNSIGNED NOT NULL,
  `miejsce_id` tinyint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=ascii COLLATE=ascii_bin;

--
-- Zrzut danych tabeli `przewod_miejsce`
--

INSERT INTO `przewod_miejsce` (`id`, `przewod_id`, `miejsce_id`) VALUES
(1, 200, 1),
(2, 200, 25),
(3, 1, 26),
(4, 1, 20),
(5, 2, 26),
(6, 2, 26),
(7, 3, 26),
(8, 3, 20),
(9, 4, 26),
(10, 4, 20),
(11, 5, 89),
(12, 5, 20),
(13, 6, 89),
(14, 6, 20),
(15, 7, 1),
(16, 7, 27),
(17, 8, 1),
(18, 8, 27),
(19, 9, 27),
(20, 9, 69),
(21, 10, 27),
(22, 10, 79),
(23, 11, 90),
(24, 11, 27),
(25, 12, 27),
(26, 12, 100),
(27, 13, 26),
(28, 13, 91),
(29, 14, 91),
(30, 14, 86),
(31, 15, 104),
(32, 15, 91),
(33, 16, 91),
(34, 16, 103),
(35, 17, 26),
(36, 17, 87),
(37, 18, 26),
(38, 18, 92),
(39, 19, 27),
(40, 19, 76),
(41, 20, 2),
(42, 20, 105),
(43, 21, 105),
(44, 21, 13),
(45, 22, 105),
(46, 22, 12),
(47, 23, 1),
(48, 23, 12),
(49, 24, 2),
(50, 24, 3),
(51, 25, 2),
(52, 25, 5),
(53, 26, 2),
(54, 26, 14),
(55, 27, 2),
(56, 27, 4),
(57, 28, 2),
(58, 28, 6),
(59, 29, 9),
(60, 29, 1),
(61, 30, 1),
(62, 30, 11),
(63, 31, 1),
(64, 31, 10),
(65, 32, 2),
(66, 32, 15),
(67, 33, 16),
(68, 33, 2),
(69, 34, 1),
(70, 34, 2),
(71, 35, 1),
(72, 35, 2),
(73, 36, 1),
(74, 36, 2),
(75, 37, 8),
(76, 37, 2),
(77, 38, 1),
(78, 38, 26),
(79, 39, 2),
(80, 39, 2),
(81, 40, 2),
(82, 40, 2),
(83, 41, 1),
(84, 41, 34),
(85, 42, 1),
(86, 42, 34),
(87, 43, 34),
(88, 43, 34),
(89, 44, 8),
(90, 44, 34),
(91, 45, 34),
(92, 45, 36),
(93, 46, 34),
(94, 46, 50),
(95, 47, 34),
(96, 47, 35),
(97, 48, 2),
(98, 48, 2),
(99, 49, 2),
(100, 49, 2),
(101, 50, 73),
(102, 50, 1),
(103, 51, 73),
(104, 51, 1),
(105, 52, 1),
(106, 52, 26),
(107, 53, 1),
(108, 53, 26),
(109, 54, 1),
(110, 54, 26),
(111, 55, 28),
(112, 55, 39),
(113, 56, 28),
(114, 56, 39),
(115, 57, 1),
(116, 57, 28),
(117, 58, 1),
(118, 58, 28),
(119, 59, 1),
(120, 59, 28),
(121, 60, 77),
(122, 60, 23),
(123, 61, 1),
(124, 61, 23),
(125, 62, 77),
(126, 62, 23),
(127, 63, 75),
(128, 63, 77),
(129, 64, 22),
(130, 64, 23),
(131, 65, 75),
(132, 65, 77),
(133, 66, 23),
(134, 66, 23),
(135, 67, 23),
(136, 67, 23),
(137, 68, 23),
(138, 68, 23),
(139, 69, 80),
(140, 69, 1),
(141, 70, 1),
(142, 70, 68),
(143, 71, 1),
(144, 71, 68),
(145, 72, 1),
(146, 72, 68),
(147, 73, 91),
(148, 73, 86),
(149, 74, 91),
(150, 74, 86),
(151, 75, 1),
(152, 75, 86),
(153, 76, 72),
(154, 76, 20),
(155, 77, 72),
(156, 77, 26),
(157, 78, 72),
(158, 78, 26),
(159, 79, 72),
(160, 79, 89),
(161, 80, 1),
(162, 80, 18),
(163, 81, 1),
(164, 81, 52),
(165, 82, 1),
(166, 82, 44),
(167, 83, 1),
(168, 83, 38),
(169, 84, 1),
(170, 84, 44),
(171, 85, 1),
(172, 85, 58),
(173, 86, 81),
(174, 86, 1),
(175, 87, 80),
(176, 87, 1),
(177, 88, 82),
(178, 88, 22),
(179, 89, 78),
(180, 89, 22),
(181, 90, 84),
(182, 90, 78),
(183, 91, 84),
(184, 91, 84),
(185, 92, 81),
(186, 92, 84),
(187, 93, 1),
(188, 93, 22),
(189, 94, 1),
(190, 94, 22),
(191, 95, 22),
(192, 95, 106),
(193, 96, 1),
(194, 96, 34),
(195, 97, 78),
(196, 97, 78),
(197, 98, 78),
(198, 98, 78),
(199, 99, 78),
(200, 99, 78),
(201, 100, 80),
(202, 100, 85),
(203, 101, 80),
(204, 101, 80),
(205, 102, 80),
(206, 102, 80),
(207, 103, 80),
(208, 103, 80),
(209, 104, 9),
(210, 104, 9),
(211, 105, 9),
(212, 105, 9),
(213, 106, 10),
(214, 106, 10),
(215, 107, 10),
(216, 107, 10),
(217, 108, 73),
(218, 108, 73),
(219, 109, 73),
(220, 109, 73),
(221, 110, 73),
(222, 110, 73),
(223, 111, 73),
(224, 111, 73),
(225, 112, 73),
(226, 112, 73),
(227, 113, 73),
(228, 113, 73),
(229, 114, 73),
(230, 114, 73),
(231, 115, 89),
(232, 115, 20),
(233, 116, 78),
(234, 116, 78),
(235, 117, 78),
(236, 117, 78),
(237, 118, 22),
(238, 118, 22),
(239, 119, 22),
(240, 119, 22),
(241, 120, 22),
(242, 120, 22),
(243, 121, 22),
(244, 121, 22),
(245, 122, 22),
(246, 122, 22),
(247, 123, 22),
(248, 123, 22),
(249, 124, 22),
(250, 124, 22),
(251, 125, 1),
(252, 125, 29),
(253, 126, 32),
(254, 126, 1),
(255, 127, 33),
(256, 127, 1),
(257, 128, 1),
(258, 128, 19),
(259, 129, 1),
(260, 129, 31),
(261, 130, 1),
(262, 130, 95),
(263, 131, 96),
(264, 131, 1),
(265, 132, 97),
(266, 132, 1),
(267, 133, 1),
(268, 133, 98),
(269, 134, 1),
(270, 134, 99),
(271, 135, 1),
(272, 135, 1),
(273, 136, 1),
(274, 136, 1),
(275, 137, 1),
(276, 137, 1),
(277, 138, 1),
(278, 138, 1),
(279, 139, 1),
(280, 139, 54),
(281, 140, 1),
(282, 140, 54),
(283, 141, 1),
(284, 141, 47),
(285, 142, 48),
(286, 142, 1),
(287, 143, 1),
(288, 143, 74),
(289, 144, 1),
(290, 144, 101),
(291, 145, 26),
(292, 145, 26),
(293, 146, 26),
(294, 146, 26),
(295, 147, 2),
(296, 147, 2),
(297, 148, 2),
(298, 148, 2),
(299, 149, 3),
(300, 149, 3),
(301, 150, 3),
(302, 150, 3),
(303, 151, 26),
(304, 151, 26),
(305, 152, 26),
(306, 152, 26),
(307, 153, 26),
(308, 153, 26),
(309, 154, 26),
(310, 154, 26),
(311, 155, 26),
(312, 155, 26),
(313, 156, 26),
(314, 156, 26),
(315, 157, 26),
(316, 157, 26),
(317, 158, 26),
(318, 158, 26),
(319, 159, 26),
(320, 159, 26),
(321, 160, 26),
(322, 160, 26),
(323, 161, 26),
(324, 161, 26),
(325, 162, 26),
(326, 162, 26),
(327, 163, 26),
(328, 163, 26),
(329, 164, 26),
(330, 164, 26),
(331, 165, 26),
(332, 165, 26),
(333, 166, 26),
(334, 166, 26),
(335, 167, 26),
(336, 167, 26),
(337, 168, 26),
(338, 168, 26),
(339, 169, 26),
(340, 169, 26),
(341, 199, 1),
(342, 199, 1),
(343, 198, 1),
(344, 198, 1),
(345, 197, 1),
(346, 197, 25),
(347, 196, 1),
(348, 196, 1),
(349, 195, 1),
(350, 195, 1),
(351, 194, 1),
(352, 194, 1),
(353, 193, 1),
(354, 193, 1),
(355, 192, 1),
(356, 192, 1),
(357, 191, 1),
(358, 191, 1),
(359, 190, 1),
(360, 190, 1),
(361, 189, 1),
(362, 189, 1),
(363, 188, 1),
(364, 188, 1),
(365, 187, 1),
(366, 187, 1),
(367, 186, 1),
(368, 186, 1),
(369, 184, 1),
(370, 184, 1),
(371, 185, 1),
(372, 185, 1),
(373, 184, 1),
(374, 184, 1),
(375, 183, 1),
(376, 183, 1),
(377, 182, 1),
(378, 182, 71),
(379, 180, 1),
(380, 180, 16),
(381, 181, 1),
(382, 181, 1),
(383, 178, 1),
(384, 178, 1),
(385, 177, 1),
(386, 177, 1),
(387, 176, 1),
(388, 176, 1),
(389, 175, 1),
(390, 175, 1),
(391, 174, 1),
(392, 174, 1),
(393, 179, 1),
(394, 179, 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `rodzaj_zakonczenia`
--

CREATE TABLE `rodzaj_zakonczenia` (
  `id` tinyint NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `kod` varchar(1) NOT NULL,
  `przewod` tinyint(1) NOT NULL,
  `plytka` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `rodzaj_zakonczenia`
--

INSERT INTO `rodzaj_zakonczenia` (`id`, `nazwa`, `kod`, `przewod`, `plytka`) VALUES
(1, 'Wtyczka', 'W', 1, 0),
(2, 'Połączenie kabli', 'K', 1, 0),
(3, 'Urządzenie', 'U', 1, 1),
(4, 'Połączenie płytki', 'P', 1, 1),
(5, 'Złącze', 'Z', 0, 1);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `WewnetrzneKableView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `WewnetrzneKableView` (
`przewod_id` tinyint unsigned
,`miejsce_id` tinyint unsigned
,`c` bigint
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zakonczenie`
--

CREATE TABLE `zakonczenie` (
  `id` smallint UNSIGNED NOT NULL,
  `etykieta` text NOT NULL,
  `przewod_miejsce_id` smallint UNSIGNED NOT NULL,
  `rodzaj_zakonczenia` tinyint(1) NOT NULL,
  `ilosc_pin` tinyint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `zakonczenie`
--

INSERT INTO `zakonczenie` (`id`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`, `ilosc_pin`) VALUES
(1, 'O', 41, 1, 0),
(2, 'J', 49, 1, 0),
(3, 'M', 51, 1, 0),
(4, 'B', 53, 1, 0),
(5, 'C', 55, 1, 0),
(6, 'G', 57, 1, 0),
(7, 'I', 65, 1, 0),
(8, 'E', 68, 1, 0),
(9, 'A', 70, 1, 0),
(10, 'P', 72, 1, 0),
(11, 'D', 74, 1, 0),
(12, 'N', 76, 1, 0),
(13, 'H', 79, 1, 0),
(14, 'L', 81, 1, 0),
(15, 'K', 97, 1, 0),
(16, 'A', 50, 1, 0),
(17, 'F', 99, 1, 0),
(18, 'B', 299, 1, 0),
(19, 'C', 301, 1, 0),
(20, 'A', 78, 1, 0),
(21, 'C', 108, 1, 6),
(22, 'brak', 303, 1, 0),
(23, 'D', 305, 1, 0),
(24, 'F', 307, 1, 0),
(25, 'G', 309, 1, 0),
(26, 'H', 311, 1, 0),
(27, 'I', 313, 1, 0),
(28, 'Q', 296, 1, 0),
(29, 'R', 298, 1, 0),
(30, '20-21-22', 42, 2, 0),
(31, '20-21-22', 43, 2, 0),
(32, '20-21-22', 45, 2, 0),
(33, '7-8-9-10-11-12-19', 16, 2, 0),
(34, '7-8-9-10-11-12-19', 18, 2, 0),
(35, '7-8-9-10-11-12-19', 19, 2, 0),
(36, '7-8-9-10-11-12-19', 21, 2, 0),
(37, '7-8-9-10-11-12-19', 24, 2, 0),
(38, '7-8-9-10-11-12-19', 25, 2, 0),
(39, '7-8-9-10-11-12-19', 39, 2, 0),
(40, '13-14-15-16', 28, 2, 0),
(41, '13-14-15-16', 29, 2, 0),
(42, '13-14-15-16', 32, 2, 0),
(43, '13-16', 33, 2, 3),
(44, 'Czujnik temperatury w podłodze w WC', 66, 3, 0),
(45, '42-43-44-45-46-47', 86, 2, 0),
(46, '42-43-44-45-46-47', 88, 2, 0),
(48, '42-43-44-45-46-47', 90, 2, 0),
(49, '42-43-44-45-46-47', 91, 2, 0),
(50, '42-43-44-45-46-47', 93, 2, 0),
(51, '42-43-44-45-46-47', 95, 2, 0),
(52, 'Czujnik temperatury ogrz. wodne ściana w salonie', 20, 3, 0),
(53, 'Czujnik temperatury ogrz. wodnego podłoga w kuchni', 22, 3, 0),
(54, 'Czujnik temperatury ogrz. wodnego podłoga w łazience', 23, 3, 0),
(55, 'Czujnik temperatury przy pompie', 26, 3, 0),
(56, 'Kontaktron od drzwiczek rewizyjnych', 40, 3, 0),
(57, 'Czujnik ruchu WC', 54, 3, 0),
(58, 'Czujnik temperatury w podłodze w Holu', 67, 3, 0),
(59, 'A', 5, 1, 10),
(60, 'Przewody pokój A', 291, 3, 12),
(61, 'B', 3, 1, 6),
(62, 'Przekaźnik oświetlnia A 8x', 6, 3, 10),
(63, 'Przekaźnik oświetlenia B 4x', 4, 3, 6),
(64, 'Lampa sufitowa łazienka', 8, 3, 6),
(65, 'C', 7, 1, 6),
(66, 'D', 292, 1, 12),
(67, 'E', 293, 1, 12),
(68, 'Przewód do właczników pokój B', 294, 3, 12),
(69, 'Ekspander 0', 315, 3, 5),
(70, 'B', 316, 1, 4),
(71, 'Plytka', 320, 4, 4),
(72, 'B', 319, 1, 4),
(73, 'A', 322, 1, 6),
(74, 'A', 325, 1, 2),
(75, 'C', 329, 1, 4),
(76, 'B', 328, 1, 4),
(77, 'D', 106, 1, 8),
(78, 'Procek', 304, 2, 6),
(79, 'Ekspander 1', 321, 3, 6),
(80, 'Masa', 323, 4, 2),
(81, 'A', 341, 1, 4),
(82, 'B', 344, 1, 2),
(83, 'D', 346, 1, 4),
(84, 'C', 348, 1, 4),
(85, 'A', 349, 1, 2),
(86, 'B', 351, 1, 8),
(87, 'C', 353, 1, 2),
(88, 'D', 355, 1, 12),
(89, 'E', 358, 1, 4),
(90, 'E', 85, 1, 8),
(91, 'G', 109, 1, 6),
(92, 'H', 187, 1, 8),
(93, 'I', 360, 1, 10),
(94, 'J', 362, 1, 4),
(95, 'K', 174, 1, 8),
(96, 'L', 71, 1, 8),
(97, 'M', 119, 1, 8),
(98, 'N', 115, 1, 8),
(99, 'P', 117, 1, 8),
(100, 'Q', 363, 1, 12),
(101, 'O', 69, 1, 8),
(102, 'S', 189, 1, 8),
(103, 'T', 167, 1, 8),
(104, 'Podwójny czujnik ruchu na ścianie łazienki', 168, 3, 4),
(105, 'T', 105, 1, 8),
(106, 'W', 365, 1, 4),
(107, 'V', 367, 1, 4),
(108, 'X', 371, 1, 12),
(109, 'Y', 369, 1, 2),
(110, 'Z', 107, 1, 6),
(111, 'A', 375, 1, 12),
(112, 'B', 377, 1, 3),
(113, 'C', 17, 1, 4),
(114, 'Czujnik temperatury', 378, 3, 3),
(115, 'Czujnik temperatury', 380, 3, 3),
(116, 'Przekaźnik 2xSSR ogrzewanie elektryczne', 382, 3, 4),
(117, 'E', 381, 1, 4),
(118, 'D', 379, 1, 3),
(119, 'Y', 370, 1, 2),
(120, 'f', 383, 1, 12),
(121, 'g', 385, 1, 12),
(122, 'H', 77, 1, 8),
(123, 'i', 123, 1, 6),
(124, 'j', 73, 1, 8),
(125, 'K', 15, 1, 10),
(126, 'L', 141, 1, 8),
(127, 'M', 161, 1, 8),
(128, 'n', 387, 1, 12),
(129, 'N', 389, 1, 12),
(130, 'P', 163, 1, 8),
(131, 'Q', 169, 1, 8),
(132, 'r85', 171, 1, 8),
(133, 's', 145, 1, 10),
(134, 'T', 143, 1, 8),
(135, 'V', 391, 1, 2),
(136, 'U', 366, 1, 2),
(137, 'W', 393, 1, 12);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZakonczenieView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ZakonczenieView` (
`id` smallint unsigned
,`etykieta` text
,`przewod_miejsce_id` smallint unsigned
,`rodzaj_zakonczenia` tinyint(1)
,`ilosc_pin` tinyint unsigned
,`przewod_id` tinyint unsigned
,`miejsce_id` tinyint unsigned
,`nazwa` text
,`kod` varchar(1)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZakonczenieZylyView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ZakonczenieZylyView` (
`zzid` smallint unsigned
,`zakonczenie_id` smallint unsigned
,`zyla_id` smallint unsigned
,`pos` tinyint
,`opis` text
,`zid` smallint unsigned
,`etykieta` text
,`przewod_miejsce_id` smallint unsigned
,`rodzaj_zakonczenia` tinyint(1)
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zakonczenie_zyly`
--

CREATE TABLE `zakonczenie_zyly` (
  `id` smallint UNSIGNED NOT NULL,
  `zakonczenie_id` smallint UNSIGNED NOT NULL,
  `zyla_id` smallint UNSIGNED NOT NULL,
  `pos` tinyint NOT NULL,
  `opis` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `zakonczenie_zyly`
--

INSERT INTO `zakonczenie_zyly` (`id`, `zakonczenie_id`, `zyla_id`, `pos`, `opis`) VALUES
(1, 1, 1, 1, '1'),
(2, 1, 2, 2, '2'),
(3, 1, 3, 3, '3'),
(4, 1, 4, 4, '4'),
(5, 1, 5, 5, '5'),
(6, 1, 6, 6, '6'),
(7, 1, 7, 7, '7'),
(8, 1, 8, 8, '8'),
(9, 2, 9, 1, '1'),
(10, 2, 10, 2, '2'),
(11, 2, 11, 3, '3'),
(12, 2, 12, 4, '4'),
(13, 2, 13, 5, '5'),
(14, 2, 14, 6, '6'),
(15, 2, 15, 7, '7'),
(16, 2, 16, 8, '8'),
(17, 3, 17, 1, '1'),
(18, 3, 18, 2, '2'),
(19, 3, 19, 3, '3'),
(20, 3, 20, 4, '4'),
(21, 3, 21, 5, '5'),
(22, 3, 22, 6, '6'),
(23, 3, 23, 7, '7'),
(24, 3, 24, 8, '8'),
(25, 4, 25, 1, '1'),
(26, 4, 26, 2, '2'),
(27, 4, 27, 3, '3'),
(28, 4, 28, 4, '4'),
(29, 5, 29, 1, '1'),
(30, 5, 30, 2, '2'),
(31, 6, 31, 1, '1'),
(32, 6, 32, 2, '2'),
(33, 6, 33, 3, '3'),
(34, 6, 34, 4, '4'),
(35, 7, 35, 1, '1'),
(36, 7, 36, 2, '2'),
(37, 7, 37, 3, '3'),
(38, 8, 38, 1, '1'),
(39, 8, 39, 2, '2'),
(40, 8, 40, 3, '3'),
(41, 9, 41, 1, '1'),
(42, 9, 42, 2, '2'),
(43, 9, 43, 3, '3'),
(44, 9, 44, 4, '4'),
(45, 9, 45, 5, '5'),
(46, 9, 46, 6, '6'),
(47, 9, 47, 7, '7'),
(48, 9, 48, 8, '8'),
(49, 10, 49, 1, '1'),
(50, 10, 50, 2, '2'),
(51, 10, 51, 3, '3'),
(52, 10, 52, 4, '4'),
(53, 10, 53, 5, '5'),
(54, 10, 54, 6, '6'),
(55, 10, 55, 7, '7'),
(56, 10, 56, 8, '8'),
(57, 11, 57, 1, '1'),
(58, 11, 58, 2, '2'),
(59, 11, 59, 3, '3'),
(60, 11, 60, 4, '4'),
(61, 11, 61, 5, '5'),
(62, 11, 62, 6, '6'),
(63, 11, 63, 7, '7'),
(64, 11, 64, 8, '8'),
(65, 12, 65, 1, '1'),
(66, 12, 69, 2, '2'),
(67, 12, 66, 3, '3'),
(68, 12, 67, 4, '4'),
(69, 12, 68, 5, '5'),
(70, 12, 70, 6, '6'),
(71, 12, 71, 7, '7'),
(72, 12, 72, 8, '8'),
(73, 13, 73, 1, '1'),
(74, 13, 74, 2, '2'),
(75, 13, 75, 3, '3'),
(76, 13, 76, 4, '4'),
(77, 14, 77, 3, '3'),
(78, 15, 80, 1, '1'),
(79, 15, 81, 2, '2'),
(80, 15, 82, 3, '3'),
(81, 15, 83, 4, '4'),
(82, 15, 84, 5, '5'),
(83, 15, 85, 6, '6'),
(84, 15, 86, 7, '7'),
(85, 15, 87, 8, '8'),
(86, 15, 88, 12, '12'),
(87, 15, 89, 11, '11'),
(88, 15, 90, 10, '10'),
(89, 15, 91, 9, '9'),
(90, 16, 10, 1, '1'),
(91, 16, 14, 2, '2'),
(92, 16, 16, 3, '3'),
(93, 16, 15, 4, '4'),
(94, 16, 13, 5, '5'),
(95, 16, 12, 6, '6'),
(96, 16, 11, 7, '7'),
(97, 16, 9, 8, '8'),
(98, 17, 92, 1, '1'),
(99, 17, 93, 2, '2'),
(100, 17, 94, 3, '3'),
(101, 17, 95, 4, '4'),
(102, 17, 96, 5, '5'),
(103, 17, 97, 6, '6'),
(104, 17, 98, 7, '7'),
(105, 17, 99, 8, '8'),
(106, 17, 100, 9, '9'),
(107, 17, 101, 10, '10'),
(108, 17, 102, 11, '11'),
(109, 17, 103, 12, '12'),
(110, 19, 114, 1, '1'),
(111, 19, 113, 2, '2'),
(112, 19, 115, 3, '3'),
(113, 19, 112, 4, '4'),
(114, 18, 121, 1, '1'),
(115, 18, 120, 2, '2'),
(116, 18, 119, 3, '3'),
(117, 18, 118, 4, '4'),
(118, 18, 117, 5, '5'),
(119, 18, 116, 6, '6'),
(120, 14, 79, 1, '1'),
(121, 14, 78, 2, '2'),
(122, 20, 322, 1, '1'),
(123, 20, 323, 2, '2'),
(124, 20, 321, 3, '3'),
(125, 20, 320, 4, '4'),
(126, 20, 319, 5, '5'),
(127, 20, 318, 6, '6'),
(128, 20, 317, 7, '7'),
(129, 20, 316, 8, '8'),
(130, 21, 330, 1, '1'),
(131, 21, 332, 2, '2'),
(132, 21, 329, 3, '3'),
(133, 21, 328, 4, '4'),
(134, 21, 333, 5, '5'),
(135, 21, 331, 6, '6'),
(136, 22, 324, 1, '1'),
(137, 22, 325, 2, '2'),
(138, 22, 326, 3, '3'),
(139, 22, 327, 4, '4'),
(140, 23, 344, 1, '1'),
(141, 23, 345, 2, '2'),
(142, 23, 346, 3, '3'),
(143, 23, 347, 4, '4'),
(144, 23, 348, 5, '5'),
(145, 23, 349, 6, '6'),
(146, 23, 350, 7, '7'),
(147, 23, 351, 8, '8'),
(148, 24, 334, 1, '1'),
(149, 24, 335, 2, '2'),
(150, 24, 336, 3, '3'),
(151, 24, 337, 4, '4'),
(152, 24, 338, 5, '5'),
(153, 24, 339, 6, '6'),
(154, 24, 340, 7, '7'),
(155, 24, 341, 8, '8'),
(156, 24, 342, 9, '9'),
(157, 24, 343, 10, '10'),
(158, 25, 352, 1, '1'),
(159, 25, 353, 2, '2'),
(160, 25, 354, 3, '3'),
(161, 25, 355, 4, '4'),
(162, 26, 356, 1, '1'),
(163, 26, 357, 2, '2'),
(164, 26, 358, 3, '3'),
(165, 26, 359, 4, '4'),
(166, 26, 360, 5, '5'),
(167, 26, 361, 6, '6'),
(168, 26, 362, 7, '7'),
(169, 26, 363, 8, '8'),
(170, 26, 364, 9, '9'),
(171, 26, 365, 10, '10'),
(172, 27, 366, 1, '1'),
(173, 27, 367, 2, '2'),
(174, 27, 368, 3, '3'),
(175, 27, 369, 4, '4'),
(176, 27, 370, 5, '5'),
(177, 27, 371, 6, '6'),
(178, 27, 372, 7, '7'),
(179, 27, 373, 8, '8'),
(180, 27, 374, 9, '9'),
(181, 27, 375, 10, '10'),
(182, 29, 104, 1, '1'),
(183, 29, 105, 2, '2'),
(184, 29, 106, 3, '3'),
(185, 29, 107, 4, '4'),
(186, 28, 108, 1, '1'),
(187, 28, 109, 2, '2'),
(188, 28, 110, 3, '3'),
(189, 28, 111, 4, '4'),
(190, 52, 270, 1, 'Zasilanie +5V'),
(191, 52, 271, 2, 'Sygnał czujnika'),
(192, 52, 272, 3, 'Masa'),
(193, 53, 273, 1, 'Zasilanie +5V'),
(194, 53, 274, 2, 'Sygnał czujnika'),
(195, 53, 275, 3, 'Masa'),
(196, 54, 276, 1, 'Zasilanie +5V'),
(197, 54, 277, 2, 'Sygnał czujnika'),
(198, 54, 278, 3, 'Masa '),
(199, 55, 279, 1, 'Zasilanie +5V'),
(200, 55, 280, 2, 'Sygnał czujnika'),
(201, 55, 281, 3, 'Masa '),
(202, 56, 314, 2, 'Masa'),
(203, 56, 315, 1, 'Styk'),
(204, 30, 4, 1, '21.1'),
(205, 30, 1, 2, '21.4'),
(206, 30, 8, 3, '22.3'),
(207, 30, 2, 4, '21.3'),
(208, 30, 7, 5, '22.2'),
(209, 30, 3, 6, '21.2'),
(210, 30, 6, 7, '22.1'),
(211, 30, 5, 8, '22.4'),
(212, 31, 400, 1, '20.1'),
(213, 31, 401, 2, '20.6'),
(214, 31, 399, 3, '20.4'),
(215, 31, 398, 4, '20.3'),
(216, 32, 402, 1, '20.7'),
(217, 32, 405, 2, '20.5'),
(218, 32, 403, 3, '20.3'),
(219, 32, 404, 4, '20.8'),
(220, 33, 260, 1, 'GND'),
(221, 33, 256, 2, 'Kontaktron'),
(222, 33, 265, 3, '+5V'),
(223, 33, 263, 4, 'GND'),
(224, 33, 264, 5, 'Sygnał'),
(225, 33, 262, 6, '+5V'),
(226, 33, 261, 7, 'Sygnał'),
(227, 33, 259, 8, '+5V'),
(228, 33, 258, 9, 'Sygnał'),
(229, 33, 257, 10, 'GND'),
(230, 34, 268, 1, '+5V'),
(231, 34, 269, 2, 'GND kontaktronu'),
(232, 34, 267, 3, 'Sygnał'),
(233, 34, 266, 4, 'GND'),
(234, 35, 271, 1, 'Sygnał'),
(235, 35, 272, 2, 'GND'),
(236, 35, 270, 3, '+5V'),
(237, 36, 274, 1, 'Sygnał'),
(238, 36, 273, 2, '+5V'),
(239, 36, 275, 3, 'GND'),
(240, 37, 276, 1, '+5V'),
(241, 37, 277, 2, 'Sygnał'),
(242, 37, 278, 3, 'GND'),
(243, 38, 281, 1, 'GND'),
(244, 38, 280, 2, 'Sygnał'),
(245, 38, 279, 3, '+5V'),
(246, 39, 314, 1, 'GND'),
(247, 39, 315, 2, 'Styk'),
(248, 40, 283, 1, 'Sygnał'),
(249, 40, 289, 2, 'GND'),
(250, 40, 288, 3, 'Sygnał'),
(251, 40, 287, 4, '+5V'),
(252, 40, 286, 5, 'GND'),
(253, 40, 285, 6, 'Sygnał'),
(254, 40, 284, 7, '+5V'),
(255, 40, 282, 8, 'GND'),
(256, 41, 291, 1, 'Sygnał'),
(257, 41, 290, 2, 'GND'),
(258, 42, 293, 1, 'Sygnał'),
(259, 42, 292, 2, '+5V'),
(260, 42, 294, 3, 'GND'),
(261, 43, 295, 1, '+5V'),
(262, 43, 296, 2, 'Sygnał'),
(263, 43, 297, 3, 'GND'),
(264, 45, 411, 1, 'GND czuj.'),
(265, 45, 413, 2, '+5V czuj'),
(266, 45, 416, 3, 'GND kont.'),
(267, 45, 412, 4, 'Sygnał cz.r pracownia'),
(268, 45, 414, 5, 'Sygnał cz. r. hol'),
(269, 45, 410, 6, 'Sygnał cz. r. pokój'),
(270, 45, 415, 7, 'Kontakt. pracownia'),
(271, 45, 417, 8, 'Kontakt. pokój'),
(272, 46, 418, 1, 'GND czuj.'),
(273, 46, 419, 2, 'GND czuj.'),
(274, 46, 420, 3, '+5V czuj'),
(275, 46, 421, 4, 'Sygnał cz. r. hol'),
(276, 48, 424, 1, 'GND czuj.'),
(277, 48, 425, 2, 'GND czuj.'),
(278, 48, 422, 3, '+5V czuj'),
(279, 48, 423, 4, 'Sygnał cz.r pracownia'),
(280, 50, 428, 1, 'GND czuj.'),
(281, 50, 429, 2, 'GND czuj.'),
(282, 50, 430, 3, '+5V czuj'),
(283, 50, 431, 4, 'Sygnał cz. r. pokój'),
(284, 51, 433, 1, 'GND kont.'),
(285, 51, 432, 2, 'Kontakt. pokój'),
(286, 49, 427, 1, 'GND kont.'),
(287, 49, 426, 2, 'Kontakt. pracownia'),
(288, 59, 226, 1, '1'),
(289, 59, 227, 2, '2'),
(290, 59, 228, 3, '3'),
(291, 59, 229, 4, '4'),
(292, 59, 230, 5, '5'),
(293, 59, 231, 6, '6'),
(294, 59, 232, 7, '7'),
(295, 59, 233, 8, '8'),
(296, 59, 234, 9, '9'),
(297, 59, 225, 10, '10'),
(298, 64, 235, 1, 'Zasilanie'),
(299, 64, 236, 2, 'Masa'),
(300, 64, 237, 3, 'Przekażnik lewej lampy'),
(301, 64, 238, 4, 'Przekaźnik prawej lampy'),
(302, 64, 239, 5, '-'),
(303, 64, 240, 6, '-'),
(304, 65, 236, 1, '1'),
(305, 65, 239, 2, '2'),
(306, 65, 240, 3, '3'),
(307, 65, 237, 4, '4'),
(308, 65, 238, 5, '5'),
(309, 65, 235, 6, '6'),
(310, 63, 219, 1, 'Zasilanie'),
(311, 63, 220, 2, 'Masa'),
(312, 63, 221, 3, 'CH 1'),
(313, 63, 222, 4, 'CH 2'),
(314, 63, 223, 5, 'CH 3'),
(315, 63, 224, 6, 'CH 4'),
(316, 61, 220, 1, '1'),
(317, 61, 221, 2, '2'),
(318, 61, 222, 3, '3'),
(319, 61, 223, 4, '4'),
(320, 61, 224, 5, '5'),
(321, 61, 219, 6, '6'),
(322, 62, 225, 1, 'Zasilanie'),
(323, 62, 226, 2, 'Masa'),
(324, 62, 227, 3, 'CH 1'),
(325, 62, 228, 4, 'CH 2'),
(326, 62, 229, 5, 'CH 3'),
(327, 62, 230, 6, 'CH 4'),
(328, 62, 231, 7, 'CH 5'),
(329, 62, 232, 8, 'CH 6'),
(330, 62, 233, 9, 'CH 7'),
(331, 62, 234, 10, 'CH 8'),
(332, 66, 465, 1, '1'),
(333, 66, 466, 2, '2'),
(334, 66, 467, 3, '3'),
(335, 66, 468, 4, '4'),
(336, 66, 469, 5, '5'),
(337, 66, 470, 6, '6'),
(338, 66, 471, 7, '7'),
(339, 66, 472, 8, '8'),
(340, 66, 473, 9, '9'),
(341, 66, 474, 10, '10'),
(342, 66, 475, 11, '11'),
(343, 66, 476, 12, '12'),
(344, 60, 465, 1, '69'),
(345, 60, 471, 2, '70'),
(346, 60, 472, 3, '71'),
(347, 60, 466, 4, '73'),
(348, 60, 473, 5, '74'),
(349, 60, 474, 6, '75'),
(350, 60, 475, 7, '82'),
(351, 60, 476, 8, '83'),
(352, 60, 469, 9, '88'),
(353, 60, 470, 10, '89'),
(354, 60, 467, 11, '90'),
(355, 60, 468, 12, '91'),
(356, 67, 477, 1, '1'),
(357, 67, 478, 2, '2'),
(358, 67, 479, 3, '3'),
(359, 67, 480, 4, '4'),
(360, 67, 481, 5, '5'),
(361, 67, 482, 6, '6'),
(362, 67, 483, 7, '7'),
(363, 67, 484, 8, '8'),
(364, 67, 485, 9, '9'),
(365, 67, 486, 10, '10'),
(366, 67, 487, 11, '11'),
(367, 67, 488, 12, '12'),
(368, 68, 477, 1, '81'),
(369, 68, 488, 2, '84'),
(370, 68, 478, 3, '85'),
(371, 68, 485, 4, '86'),
(372, 68, 487, 5, '86'),
(373, 68, 486, 6, '87'),
(374, 68, 479, 7, '95'),
(375, 68, 480, 8, '96'),
(376, 68, 481, 9, '97'),
(377, 68, 482, 10, '98'),
(378, 68, 483, 11, '99'),
(379, 68, 484, 12, '100'),
(380, 69, 390, 1, '+5V'),
(381, 69, 391, 2, 'GND'),
(382, 69, 393, 3, 'SDA'),
(383, 69, 392, 4, 'SCL'),
(384, 69, 0, 5, 'INT'),
(385, 70, 390, 1, '1'),
(386, 70, 392, 2, '2'),
(387, 70, 393, 3, '3'),
(388, 70, 391, 4, '4'),
(389, 71, 489, 1, '1'),
(390, 71, 490, 2, '2'),
(391, 71, 491, 3, '3'),
(392, 71, 492, 4, '4'),
(393, 72, 492, 1, '1'),
(394, 72, 491, 2, '2'),
(395, 72, 490, 3, '3'),
(396, 72, 489, 4, '4'),
(397, 73, 493, 1, '1'),
(398, 73, 496, 2, '2'),
(399, 73, 495, 3, '3'),
(400, 73, 494, 4, '4'),
(401, 73, 497, 5, '5'),
(402, 76, 501, 1, '1'),
(403, 76, 502, 2, '2'),
(404, 76, 500, 3, '3'),
(405, 76, 499, 4, '4'),
(406, 78, 324, 1, 'VCC'),
(407, 78, 327, 2, 'GND'),
(408, 78, 325, 3, 'SDA'),
(409, 78, 326, 4, 'SCL'),
(410, 79, 493, 1, 'VCC'),
(411, 79, 494, 2, 'GND'),
(412, 79, 495, 3, 'SDA'),
(413, 79, 496, 4, 'SCL'),
(414, 79, 497, 5, 'INT'),
(415, 80, 503, 1, '1'),
(416, 80, 504, 2, '2'),
(417, 83, 515, 1, '1'),
(418, 83, 516, 2, '2'),
(419, 83, 517, 3, '3'),
(420, 83, 518, 4, '4'),
(421, 84, 519, 1, '1'),
(422, 84, 519, 2, '2'),
(423, 85, 521, 1, '1'),
(424, 85, 521, 2, '2'),
(425, 86, 523, 1, '1'),
(426, 86, 524, 2, '2'),
(427, 86, 525, 3, '3'),
(428, 86, 526, 4, '4'),
(429, 86, 527, 5, '5'),
(430, 86, 528, 6, '6'),
(431, 86, 529, 7, '7'),
(432, 86, 530, 8, '8'),
(433, 87, 531, 1, '1'),
(434, 87, 532, 2, '2'),
(435, 88, 533, 1, '1'),
(436, 88, 534, 2, '2'),
(437, 88, 535, 3, '3'),
(438, 88, 536, 4, '4'),
(439, 88, 537, 5, '5'),
(440, 88, 538, 6, '6'),
(441, 88, 539, 7, '7'),
(442, 88, 540, 8, '8'),
(443, 88, 541, 9, '9'),
(444, 88, 542, 10, '10'),
(445, 88, 543, 11, '11'),
(446, 88, 544, 12, '12'),
(447, 89, 545, 1, '1'),
(448, 89, 546, 2, '2'),
(449, 89, 547, 3, '3'),
(450, 89, 548, 4, '4'),
(451, 90, 410, 1, '1'),
(452, 90, 412, 2, '2'),
(453, 90, 414, 3, '3'),
(454, 90, 417, 4, '4'),
(455, 90, 415, 5, '5'),
(456, 90, 416, 6, '6'),
(457, 90, 411, 7, '7'),
(458, 90, 413, 8, '8'),
(459, 91, 384, 1, '1'),
(460, 91, 385, 2, '2'),
(461, 91, 386, 3, '3'),
(462, 91, 387, 4, '4'),
(463, 91, 388, 5, '5'),
(464, 91, 389, 6, '6'),
(465, 92, 152, 1, '1'),
(466, 92, 151, 2, '2'),
(467, 92, 145, 3, '3'),
(468, 92, 146, 4, '4'),
(469, 92, 149, 5, '5'),
(470, 92, 150, 6, '6'),
(471, 92, 148, 7, '7'),
(472, 92, 147, 8, '8'),
(473, 93, 549, 1, '1'),
(474, 93, 550, 2, '2'),
(475, 93, 551, 3, '3'),
(476, 93, 552, 4, '4'),
(477, 93, 553, 5, '5'),
(478, 93, 554, 6, '6'),
(479, 93, 555, 7, '7'),
(480, 93, 556, 8, '8'),
(481, 93, 557, 9, '9'),
(482, 93, 558, 10, '10'),
(483, 94, 559, 1, '1'),
(484, 94, 560, 2, '2'),
(485, 94, 561, 3, '3'),
(486, 94, 562, 4, '4'),
(487, 95, 563, 1, '1'),
(488, 95, 564, 2, '2'),
(489, 95, 565, 3, '3'),
(490, 95, 566, 4, '4'),
(491, 95, 567, 5, '5'),
(492, 95, 568, 6, '6'),
(493, 95, 569, 7, '7'),
(494, 95, 570, 8, '8'),
(495, 96, 52, 1, '1'),
(496, 96, 51, 2, '2'),
(497, 96, 50, 3, '3'),
(498, 96, 49, 4, '4'),
(499, 96, 53, 5, '5'),
(500, 96, 54, 6, '6'),
(501, 96, 55, 7, '7'),
(502, 96, 56, 8, '8'),
(503, 97, 571, 1, '1'),
(504, 97, 572, 2, '2'),
(505, 97, 573, 3, '3'),
(506, 97, 574, 4, '4'),
(507, 97, 575, 5, '5'),
(508, 97, 576, 6, '6'),
(509, 97, 577, 7, '7'),
(510, 97, 578, 8, '8'),
(511, 98, 579, 1, '1'),
(512, 98, 580, 2, '2'),
(513, 98, 581, 3, '3'),
(514, 98, 582, 4, '4'),
(515, 98, 583, 5, '5'),
(516, 98, 584, 6, '6'),
(517, 98, 585, 7, '7'),
(518, 98, 586, 8, '8'),
(519, 99, 587, 1, '1'),
(520, 99, 588, 2, '2'),
(521, 99, 589, 3, '3'),
(522, 99, 590, 4, '4'),
(523, 99, 591, 5, '5'),
(524, 99, 592, 6, '6'),
(525, 99, 593, 7, '7'),
(526, 99, 594, 8, '8'),
(527, 100, 595, 1, '1'),
(528, 100, 596, 2, '2'),
(529, 100, 597, 3, '3'),
(530, 100, 598, 4, '4'),
(531, 100, 599, 5, '5'),
(532, 100, 600, 6, '6'),
(533, 100, 601, 7, '7'),
(534, 100, 602, 8, '8'),
(535, 100, 603, 9, '9'),
(536, 100, 604, 10, '10'),
(537, 100, 605, 11, '11'),
(538, 100, 606, 12, '12'),
(539, 101, 43, 1, '1'),
(540, 101, 44, 2, '2'),
(541, 101, 48, 3, '3'),
(542, 101, 47, 4, '4'),
(543, 101, 45, 5, '5'),
(544, 101, 46, 6, '6'),
(545, 101, 41, 7, '7'),
(546, 101, 42, 8, '8'),
(547, 102, 154, 1, '1'),
(548, 102, 155, 2, '2'),
(549, 102, 156, 3, '3'),
(550, 102, 157, 4, '4'),
(551, 102, 158, 5, '5'),
(552, 102, 159, 6, '6'),
(553, 102, 160, 7, '7'),
(554, 102, 153, 8, '8'),
(555, 103, 607, 1, '1'),
(556, 103, 608, 2, '2'),
(557, 103, 609, 3, '3'),
(558, 103, 610, 4, '4'),
(559, 103, 611, 5, '5'),
(560, 103, 612, 6, '6'),
(561, 103, 613, 7, '7'),
(562, 103, 614, 8, '8'),
(563, 104, 611, 1, 'Sygnał od salon'),
(564, 104, 612, 2, 'Sygnał od holu'),
(565, 104, 613, 3, 'Zasilanie'),
(566, 104, 614, 4, 'Masa'),
(567, 105, 381, 1, '1'),
(568, 105, 380, 2, '2'),
(569, 105, 377, 3, '3'),
(570, 105, 376, 4, '4'),
(571, 105, 378, 5, '5'),
(572, 105, 379, 6, '6'),
(573, 105, 382, 7, '7'),
(574, 105, 383, 8, '8'),
(575, 106, 615, 1, '1'),
(576, 106, 616, 2, '2'),
(577, 107, 617, 1, '1'),
(578, 107, 618, 2, '2'),
(579, 107, 619, 3, '3'),
(580, 107, 620, 4, '4'),
(581, 108, 621, 1, '1'),
(582, 108, 622, 2, '2'),
(583, 108, 623, 3, '3'),
(584, 108, 624, 4, '4'),
(585, 108, 625, 5, '5'),
(586, 108, 626, 6, '6'),
(587, 108, 627, 7, '7'),
(588, 108, 628, 8, '8'),
(589, 108, 629, 9, '9'),
(590, 108, 630, 10, '10'),
(591, 108, 631, 11, '11'),
(592, 108, 632, 12, '12'),
(593, 109, 633, 1, '1'),
(594, 109, 634, 2, '2'),
(595, 110, 329, 1, '1'),
(596, 110, 332, 2, '2'),
(597, 110, 330, 3, '3'),
(598, 110, 331, 4, '4'),
(599, 110, 333, 5, '5'),
(600, 110, 328, 6, '6'),
(601, 111, 635, 1, '1'),
(602, 111, 636, 2, '2'),
(603, 111, 637, 3, '3'),
(604, 111, 638, 4, '4'),
(605, 111, 639, 5, '5'),
(606, 111, 640, 6, '6'),
(607, 111, 641, 7, '7'),
(608, 111, 642, 8, '8'),
(609, 111, 643, 9, '9'),
(610, 111, 644, 10, '10'),
(611, 111, 645, 11, '11'),
(612, 111, 646, 12, '12'),
(613, 112, 647, 1, '1'),
(614, 112, 648, 2, '2'),
(615, 112, 649, 3, '3'),
(616, 113, 268, 1, '1'),
(617, 113, 267, 2, '2'),
(618, 113, 266, 3, '3'),
(619, 113, 269, 4, '4'),
(620, 114, 647, 1, 'Masa'),
(621, 114, 648, 2, 'Sygnał'),
(622, 114, 649, 3, 'Zasilanie'),
(623, 115, 650, 1, 'Masa'),
(624, 115, 651, 2, 'Sygnał'),
(625, 115, 652, 3, 'Zasilanie'),
(626, 116, 653, 1, 'Zasilanie'),
(627, 116, 655, 2, 'Kanał 1'),
(628, 116, 656, 3, 'Kanał 2'),
(629, 116, 654, 4, 'GND'),
(630, 117, 653, 1, '1'),
(631, 117, 654, 2, '2'),
(632, 117, 655, 3, '3'),
(633, 117, 656, 4, '4'),
(634, 118, 650, 1, '1'),
(635, 118, 651, 2, '2'),
(636, 118, 652, 3, '3'),
(637, 119, 633, 1, '1'),
(638, 119, 634, 2, '2'),
(639, 120, 657, 1, '1'),
(640, 120, 658, 2, '2'),
(641, 120, 659, 3, '3'),
(642, 120, 660, 4, '4'),
(643, 120, 661, 5, '5'),
(644, 120, 662, 6, '6'),
(645, 120, 663, 7, '7'),
(646, 120, 664, 8, '8'),
(647, 120, 665, 9, '9'),
(648, 120, 666, 10, '10'),
(649, 120, 667, 11, '11'),
(650, 120, 668, 12, '12'),
(651, 121, 669, 1, '1'),
(652, 121, 670, 2, '2'),
(653, 121, 671, 3, '3'),
(654, 121, 672, 4, '4'),
(655, 121, 673, 5, '5'),
(656, 121, 674, 6, '6'),
(657, 121, 675, 7, '7'),
(658, 121, 676, 8, '8'),
(659, 121, 677, 9, '9'),
(660, 121, 678, 10, '10'),
(661, 121, 679, 11, '11'),
(662, 121, 680, 12, '12'),
(663, 122, 316, 1, '1'),
(664, 122, 317, 2, '2'),
(665, 122, 318, 3, '3'),
(666, 122, 319, 4, '4'),
(667, 122, 320, 5, '5'),
(668, 122, 321, 6, '6'),
(669, 122, 322, 7, '7'),
(670, 122, 323, 8, '8'),
(671, 123, 438, 1, '1'),
(672, 123, 443, 2, '2'),
(673, 123, 439, 3, '3 F.9'),
(674, 123, 441, 4, '4 F.12'),
(675, 123, 442, 5, '5 F.11'),
(676, 123, 440, 6, '6 F.10'),
(677, 124, 58, 1, '1 - G.6'),
(678, 124, 59, 2, '2 - G.5'),
(679, 124, 61, 3, '3 - G.4'),
(680, 124, 62, 4, '4 - G.3'),
(681, 124, 63, 5, '5 - G.2'),
(682, 124, 64, 6, '6 - G.1'),
(683, 124, 60, 7, '7'),
(684, 124, 57, 8, '8'),
(685, 125, 257, 1, '1'),
(686, 125, 260, 2, '2'),
(687, 125, 263, 3, '3'),
(688, 125, 259, 4, '4'),
(689, 125, 262, 5, '5'),
(690, 125, 265, 6, '6'),
(691, 125, 256, 7, '7 - G.12'),
(692, 125, 258, 8, '8 - G.11'),
(693, 125, 261, 9, '9 - G.10'),
(694, 125, 264, 10, '10 - G.9'),
(695, 126, 682, 1, '1'),
(696, 126, 681, 2, '2'),
(697, 126, 683, 3, '3 - A.6'),
(698, 126, 684, 4, '4 - O.12'),
(699, 126, 685, 5, '5 - O.11'),
(700, 126, 686, 6, '6 - O.10'),
(701, 126, 687, 7, '7 - O.9'),
(702, 126, 688, 8, '8 - O.8'),
(703, 127, 691, 1, '1 - O.5'),
(704, 127, 692, 2, '2 - O.4'),
(705, 127, 692, 3, '3 - O.3'),
(706, 127, 693, 4, '4 - O.2'),
(707, 127, 695, 5, '5 - O.1'),
(708, 127, 696, 6, '6 - A.4'),
(709, 127, 689, 7, '7'),
(710, 127, 690, 8, '8'),
(711, 128, 697, 1, '1'),
(712, 128, 698, 2, '2'),
(713, 128, 699, 3, '3'),
(714, 128, 700, 4, '4'),
(715, 128, 701, 5, '5'),
(716, 128, 702, 6, '6'),
(717, 128, 703, 7, '7'),
(718, 128, 704, 8, '8'),
(719, 128, 705, 9, '9'),
(720, 128, 706, 10, '10'),
(721, 128, 707, 11, '11'),
(722, 128, 708, 12, '12'),
(723, 129, 709, 1, '1'),
(724, 129, 710, 2, '2'),
(725, 129, 711, 3, '3'),
(726, 129, 712, 4, '4'),
(727, 129, 713, 5, '5'),
(728, 129, 714, 6, '6'),
(729, 129, 715, 7, '7'),
(730, 129, 716, 8, '8'),
(731, 129, 716, 9, '9'),
(732, 129, 718, 10, '10'),
(733, 129, 719, 11, '11'),
(734, 129, 720, 12, '12'),
(735, 130, 721, 1, '1'),
(736, 130, 722, 2, '2'),
(737, 130, 723, 3, '3'),
(738, 130, 724, 4, '4'),
(739, 130, 725, 5, '5'),
(740, 130, 726, 6, '6'),
(741, 130, 727, 7, '7'),
(742, 130, 728, 8, '8'),
(743, 131, 729, 1, '1'),
(744, 131, 730, 2, '2'),
(745, 131, 731, 3, '3'),
(746, 131, 732, 4, '4'),
(747, 131, 733, 5, '5'),
(748, 131, 734, 6, '6'),
(749, 131, 735, 7, '7'),
(750, 131, 736, 8, '8'),
(751, 132, 737, 1, '1'),
(752, 132, 738, 2, '2'),
(753, 132, 739, 3, '3'),
(754, 132, 740, 4, '4'),
(755, 132, 741, 5, '5'),
(756, 132, 742, 6, '6'),
(757, 132, 743, 7, '7'),
(758, 132, 744, 8, '8'),
(759, 133, 745, 1, '1'),
(760, 133, 746, 2, '2'),
(761, 133, 747, 3, '3'),
(762, 133, 748, 4, '4'),
(763, 133, 749, 5, '5'),
(764, 133, 750, 6, '6'),
(765, 133, 751, 7, '7'),
(766, 133, 752, 8, '8'),
(767, 133, 753, 9, '9'),
(768, 133, 754, 10, '10'),
(769, 134, 755, 1, '1'),
(770, 134, 756, 2, '2'),
(771, 134, 757, 3, '3'),
(772, 134, 758, 4, '4'),
(773, 134, 759, 5, '5'),
(774, 134, 760, 6, '6'),
(775, 134, 761, 7, '7'),
(776, 134, 762, 8, '8'),
(777, 135, 763, 1, '1'),
(778, 135, 764, 2, '2'),
(779, 136, 616, 1, '1'),
(780, 136, 615, 2, '2'),
(781, 137, 765, 1, '1'),
(782, 137, 766, 2, '2'),
(783, 137, 767, 3, '3'),
(784, 137, 768, 4, '4'),
(785, 137, 769, 5, '5'),
(786, 137, 770, 6, '6'),
(787, 137, 771, 7, '7'),
(788, 137, 771, 8, '8'),
(789, 137, 773, 9, '9'),
(790, 137, 774, 10, '10'),
(791, 137, 775, 11, '11'),
(792, 137, 776, 12, '12');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZakonczePrzewodMiejsce`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ZakonczePrzewodMiejsce` (
`zid` smallint unsigned
,`etykieta` text
,`przewod_miejsce_id` smallint unsigned
,`rodzaj_zakonczenia` tinyint(1)
,`przewod_id` tinyint unsigned
,`miejsce_id` tinyint unsigned
,`znazwa` text
,`zkod` varchar(1)
,`ilosc_pin` tinyint unsigned
,`mnazwa` text
,`mopis` text
,`zbiorcze` tinyint(1)
,`mkod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` text
,`popis` text
,`ilosc_zyl` tinyint unsigned
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZewnetrzneKableView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ZewnetrzneKableView` (
`przewod_id` tinyint unsigned
,`miejsce_id` tinyint unsigned
,`c` bigint
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZlaczeWtyczkaView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ZlaczeWtyczkaView` (
`wtyczka_id` smallint unsigned
,`zlacze_id` smallint unsigned
,`epid` smallint unsigned
,`epnazwa` text
,`eppos` tinyint
,`zyla_id` smallint unsigned
,`zzpos` tinyint
,`zzopis` text
,`zzetykieta` text
,`zid` smallint unsigned
,`kolor_id` tinyint unsigned
,`przewod_id` tinyint unsigned
,`opis` text
,`kolor` text
,`html` text
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zlacze_wtyczka`
--

CREATE TABLE `zlacze_wtyczka` (
  `id` smallint UNSIGNED NOT NULL,
  `wtyczka_id` smallint UNSIGNED NOT NULL,
  `zlacze_id` smallint UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `zlacze_wtyczka`
--

INSERT INTO `zlacze_wtyczka` (`id`, `wtyczka_id`, `zlacze_id`) VALUES
(1, 1, 26),
(2, 2, 21),
(3, 3, 24),
(4, 4, 13),
(5, 5, 14),
(6, 6, 18),
(7, 7, 20),
(8, 8, 16),
(9, 9, 12),
(10, 10, 27),
(11, 11, 15),
(12, 12, 25),
(13, 13, 19),
(14, 14, 23),
(15, 15, 22),
(16, 17, 17);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zyla`
--

CREATE TABLE `zyla` (
  `id` smallint UNSIGNED NOT NULL,
  `kolor_id` tinyint UNSIGNED NOT NULL,
  `przewod_id` tinyint UNSIGNED NOT NULL,
  `opis` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `zyla`
--

INSERT INTO `zyla` (`id`, `kolor_id`, `przewod_id`, `opis`) VALUES
(1, 2, 20, '+5V zasialanie dla czujnika temperatury'),
(2, 3, 20, 'Sygnał czujnika temperatury'),
(3, 8, 20, '-'),
(4, 1, 20, 'GND dla czujnika temperatury'),
(5, 7, 20, 'GND dla gabarytu'),
(6, 6, 20, 'Pin1 do gabarytu'),
(7, 9, 20, 'Pin2 do gabarytu'),
(8, 4, 20, 'Pin3 do gabarytu'),
(9, 7, 24, 'GND'),
(10, 4, 24, '5V Zasilanie przekaźników'),
(11, 6, 24, 'Przekażnik 6 '),
(12, 9, 24, 'Przekażnik 5'),
(13, 5, 24, 'Przekażnik 4 (zawór)'),
(14, 3, 24, 'Przekaźnik 3 (lustro)'),
(15, 1, 24, 'Przekaźnik 2 (światło)'),
(16, 8, 24, 'Przekaźnik 1 (regał)'),
(17, 6, 25, '-'),
(18, 7, 25, '-'),
(19, 9, 25, '-'),
(20, 4, 25, '-'),
(21, 5, 25, '-'),
(22, 3, 25, '-'),
(23, 1, 25, '-'),
(24, 8, 25, '-'),
(25, 3, 26, 'Sygnał od czujnka ruchu'),
(26, 2, 26, 'Zasilanie 5V czujnika ruchu'),
(27, 1, 26, 'GND dla czujnika ruchu'),
(28, 1, 26, 'GND dla czujnika ruchu'),
(29, 3, 27, 'Sygnał od kontaktronu'),
(30, 1, 27, 'GND'),
(31, 3, 28, 'Sygnał od czujnka zbliżeniowego'),
(32, 2, 28, 'Zasilanie 5V czujnika zbliżeniowego'),
(33, 1, 28, 'GND dla czujnika zbliżeniowego'),
(34, 1, 28, 'GND dla czujnika zbliżeniowego'),
(35, 7, 32, 'GND'),
(36, 8, 32, 'Sygnał temperatury WC w podłodze'),
(37, 4, 32, 'Zasilanie +5V'),
(38, 4, 33, '+5V'),
(39, 8, 33, 'Sygnał czujnika temperatury w podłodze hol'),
(40, 7, 33, 'GND'),
(41, 4, 34, '+24V '),
(42, 7, 34, 'GND'),
(43, 9, 34, 'RX'),
(44, 3, 34, 'TX'),
(45, 6, 34, 'Sygnał Nocy'),
(46, 5, 34, 'Sygnał wieczora (pomarańczowy)'),
(47, 1, 34, 'Sygnał OFF'),
(48, 8, 34, 'Sygnał ON'),
(49, 8, 35, 'Wyjście światło'),
(50, 1, 35, 'Wyjście wiatrak'),
(51, 6, 35, 'Sygnał dla przekaźnika 5'),
(52, 5, 35, 'Sygnał dla przekaźnika 6'),
(53, 4, 35, 'Podświetlenie włączników'),
(54, 9, 35, 'Sygnał klawisza 1 włącznika '),
(55, 3, 35, 'Sygnał klawisza 2 włącznika '),
(56, 7, 35, 'GND'),
(57, 4, 36, '+5V dla przekaźników/czujników temperatur'),
(58, 9, 36, 'Przekaźnik ogrzewanie Hol'),
(59, 8, 36, 'Przekaźnik ogrzewanie WC'),
(60, 7, 36, 'GND'),
(61, 6, 36, 'Sygnał czujnika temperatury WC'),
(62, 5, 36, 'Sygnał czujnika temperatury Hol'),
(63, 3, 36, 'Sygnał czujnika temperatury podłoga WC'),
(64, 1, 36, 'Sygnał czujnika temperatury podłoga Hol'),
(65, 4, 37, '5V dla czujnika temperatury'),
(66, 9, 37, 'Sygnał czujnika temperatury'),
(67, 7, 37, 'GND czujnika temperatury'),
(68, 3, 37, 'GND'),
(69, 6, 37, '5V'),
(70, 1, 37, 'Klawisz włącznika 1'),
(71, 8, 37, 'Klawisz włącznika 2'),
(72, 5, 37, 'Podświetlenie włączników (pomarańczowy)'),
(73, 7, 39, 'GND'),
(74, 8, 39, 'Przekażnik WC'),
(75, 9, 39, 'Przekażnik Hol'),
(76, 4, 39, '+5V'),
(77, 1, 40, 'Klawisz '),
(78, 3, 40, 'GND'),
(79, 2, 40, 'Podświetlenie włącznika'),
(80, 6, 48, 'Wyjście światło 0x01.5'),
(81, 9, 48, 'Wyjście wiatrak 0x01.6'),
(82, 2, 48, '-'),
(83, 10, 48, '-'),
(84, 12, 48, 'Sygnał od lokalnego czujnika temperatury'),
(85, 7, 48, 'Pin1 do gabarytu'),
(86, 11, 48, 'Pin2 do gabarytu'),
(87, 4, 48, 'Pin3 do gabarytu'),
(88, 5, 48, 'Przekaźnik 4 (zawór) 0x01,1'),
(89, 3, 48, 'Przekaźnik 3 (lustro) 0x01.2'),
(90, 1, 48, 'Przekaźnik 2 (światło) 0x01.3'),
(91, 8, 48, 'Przekaźnik 1 (regał) 0x01.4'),
(92, 11, 49, 'Sygnał wejściowy czujnika ruchu 0x00.1'),
(93, 12, 49, 'Sygnał wejściowy czujnika zbliżeniowego 0x00.2'),
(94, 10, 49, 'Sygnał wejściowy kontaktron 0x00.3'),
(95, 2, 49, 'Sygnałwejściowy klawisza włącznika światła 0x00.4'),
(96, 4, 49, '+5V'),
(97, 8, 49, 'Sygnał wejściowy ON 0x00.7'),
(98, 1, 49, 'Sygnał wejściowy OFF 0x00.8'),
(99, 5, 49, 'Sygnał wejściowy wieczoru 0x00.5'),
(100, 6, 49, 'Sygnał wejściowy nocy 0x00.6'),
(101, 3, 49, 'TX'),
(102, 9, 49, 'RX'),
(103, 7, 49, 'GND'),
(104, 2, 147, 'Zasilanie 5V'),
(105, 1, 147, 'GND'),
(106, 8, 147, 'Sygnał i2c SDA'),
(107, 10, 147, 'Sygnał i2c SCL'),
(108, 2, 148, 'Zasilanie +5V'),
(109, 1, 148, 'GND'),
(110, 8, 148, 'Sygnał i2c SDA'),
(111, 10, 148, 'Sygnał i2c SCL'),
(112, 4, 150, 'Zasilanie +5V'),
(113, 9, 150, 'CH 1 - kanał 5 wiatrak '),
(114, 6, 150, 'CH 2 - kanal 6 nie podłaczone'),
(115, 7, 150, 'GND'),
(116, 4, 149, 'Zasilanie +5V'),
(117, 7, 149, 'GND'),
(118, 8, 149, 'CH 1 (Kanał 1) Regał'),
(119, 1, 149, 'CH 2 (Kanał 2)  Światło'),
(120, 3, 149, 'CH 3 (Kanał 3) Lustro'),
(121, 5, 149, 'CH 4 (Kanał 4) Zawór'),
(122, 6, 64, 'Kontaktron od szklanych drzwi'),
(123, 3, 64, 'Oświetlenie drzwi LED 2 '),
(124, 9, 64, 'Oświetlenie drzwi LED 1'),
(125, 8, 64, 'Oświetlenie listwa LED przy lodówce'),
(126, 1, 64, 'Oświetlenie listwa LED przy jadalni'),
(127, 7, 64, 'GND'),
(128, 4, 64, '+5V'),
(129, 1, 88, 'Sygnał 1'),
(130, 8, 88, 'Sygnał 2'),
(131, 4, 88, '+5V'),
(132, 7, 88, 'GND'),
(133, 9, 88, '-'),
(134, 3, 88, '-'),
(135, 6, 88, '-'),
(136, 5, 88, '-'),
(137, 7, 89, 'GND'),
(138, 4, 89, '+5V'),
(139, 8, 89, 'Sygnał 1'),
(140, 1, 89, 'Sygnał 2'),
(141, 0, 89, '-'),
(142, 0, 89, '-'),
(143, 0, 89, '-'),
(144, 0, 89, '-'),
(145, 7, 93, 'GND'),
(146, 4, 93, '+24V'),
(147, 5, 93, 'Zasilanie awaryjne'),
(148, 6, 93, '2 taryfa'),
(149, 8, 93, 'Sygnał wieczoru'),
(150, 1, 93, 'Sygnał nocy'),
(151, 3, 93, 'TX'),
(152, 9, 93, 'RX'),
(153, 5, 94, 'X'),
(154, 4, 94, 'Podświetlenie klawiszy'),
(155, 7, 94, 'Włącznik kuchnia prawy prawy'),
(156, 6, 94, 'Włącznik kuchnia prawy lewy'),
(157, 8, 94, 'Włącznik salon prawy prawy'),
(158, 1, 94, 'Włącznik salon prawy lewy'),
(159, 3, 94, 'Włącznik salon lewy prawy'),
(160, 9, 94, 'Włącznik salon lewy lewy'),
(161, 9, 95, '-'),
(162, 3, 95, '-'),
(163, 1, 95, '-'),
(164, 8, 95, '-'),
(165, 6, 95, '-'),
(166, 7, 95, '-'),
(167, 4, 95, '-'),
(168, 5, 95, '-'),
(169, 4, 118, '+5V'),
(170, 3, 118, 'GND'),
(171, 1, 118, 'kanał 12'),
(172, 8, 118, 'kanał 11'),
(173, 9, 118, 'kanał 10'),
(174, 6, 118, 'kanał 9'),
(175, 4, 119, '+5V'),
(176, 7, 119, 'GND'),
(177, 9, 119, 'SDC'),
(178, 8, 119, 'SDA'),
(179, 1, 119, 'Przerwanie od 000'),
(180, 5, 119, 'Przerwanie od 101'),
(181, 3, 119, 'Przerwanie od 110'),
(182, 6, 119, 'Przerwanie od 111'),
(183, 10, 120, 'Kanał 1'),
(184, 5, 120, 'Kanał 2'),
(185, 9, 120, 'Kanał 3'),
(186, 6, 120, 'Kanał 4'),
(187, 3, 120, 'Kanał 5'),
(188, 2, 120, 'Kanał 6'),
(189, 8, 120, 'Kanał 7'),
(190, 1, 120, 'Kanał 8'),
(191, 7, 120, 'GND'),
(192, 4, 120, '+5V'),
(193, 9, 121, 'kanał 13'),
(194, 7, 121, 'Masa'),
(195, 4, 121, '+5V'),
(196, 7, 122, 'Przewód 12 B.PE Klawisz B.1'),
(197, 6, 122, 'Przewód 10 B.L Klawisz B.1'),
(198, 8, 122, 'Przewód 18 G.L1 Klawisz G.1.1'),
(199, 9, 122, 'Przewód 17 G.L2 Klawisz G.1.2'),
(200, 3, 122, 'Przewód 18 G.L3 Klawisz G.2.1'),
(201, 1, 122, 'Przewód 19 G.N Klawisz G.2.2'),
(202, 4, 122, 'Przewód 20 .PE Oświetlenie włącznika'),
(203, 5, 122, 'Przewód 13 D.L -'),
(204, 10, 122, 'Przewód 14 D.N -'),
(205, 2, 122, 'Przewód 15 D.PE -'),
(206, 1, 123, 'Przewód 7 B.PE Klawisz B.1'),
(207, 8, 123, 'Przewód 9 B.L Klawisz B.2'),
(208, 2, 123, 'Przewód 6 E.PE Klawisz E.1'),
(209, 3, 123, 'Przewód 4 E.L Klawisz E.2'),
(210, 9, 123, 'Przewód 5 F.PE Klawisz F.1'),
(211, 10, 123, 'Przewód 11 F.L Klawisz F.2'),
(212, 4, 123, 'Przewód 1 B.N Oświetlenie'),
(213, 5, 123, 'Przewód 11 F.N Oświetlenie'),
(214, 6, 123, 'Przewód 2 E.N Masa'),
(215, 7, 123, 'Przewód 8 C.N Masa'),
(216, 3, 124, 'RX'),
(217, 1, 124, 'TX'),
(218, 5, 64, 'Zasilacz LED'),
(219, 4, 1, '+5V'),
(220, 7, 1, 'GND'),
(221, 6, 1, 'Lampka 1 tył lewy'),
(222, 1, 1, 'Lampka 2 tył prawy'),
(223, 3, 1, 'Lampka 3 przód lewy'),
(224, 9, 1, 'Lampka 4 przód prawy'),
(225, 4, 2, '+5V'),
(226, 7, 2, 'GND'),
(227, 3, 2, 'Światło nad lustrem prawe'),
(228, 13, 2, 'Światło nad lustrem lewe'),
(229, 6, 2, 'Zasilanie raspberry'),
(230, 9, 2, 'Zasilanie radia'),
(231, 8, 2, 'Zasilanie monitora'),
(232, 10, 2, 'Swiatło główne'),
(233, 1, 2, 'Lampka nad wanną 1'),
(234, 5, 2, 'Lampka nad wanną 2'),
(235, 4, 3, '+5V'),
(236, 7, 3, 'GND'),
(237, 8, 3, 'Lewa lampa'),
(238, 9, 3, 'Prawa lampa'),
(239, 3, 3, '-'),
(240, 1, 3, '-'),
(241, 6, 4, '-'),
(242, 7, 4, '-'),
(243, 9, 4, '-'),
(244, 4, 4, '-'),
(245, 2, 4, '-'),
(246, 3, 4, '-'),
(247, 1, 4, '-'),
(248, 8, 4, '-'),
(249, 7, 5, 'GND'),
(250, 8, 5, 'Sygnał czujnika '),
(251, 4, 5, '+5V'),
(252, 4, 6, '-'),
(253, 3, 6, '-'),
(254, 1, 6, '-'),
(255, 9, 6, '-'),
(256, 1, 7, 'Styk kontraktronu'),
(257, 8, 7, 'GND'),
(258, 2, 7, 'Sygnał czujnika temperatury'),
(259, 4, 7, '+5V'),
(260, 9, 7, 'GND'),
(261, 3, 7, 'Sygnał czujnika temperatury'),
(262, 5, 7, '+5V'),
(263, 6, 7, 'GND'),
(264, 14, 7, 'Sygnał czujnika temperatury'),
(265, 7, 7, '+5V'),
(266, 9, 8, 'GND'),
(267, 6, 8, 'Sygnał czujnika temperatury'),
(268, 8, 8, '+5V'),
(269, 4, 8, 'GND kontaktronu'),
(270, 4, 9, '+5V'),
(271, 8, 9, 'Sygnał czujnika'),
(272, 7, 9, 'GND'),
(273, 4, 10, '+5V'),
(274, 8, 10, 'Sygnał czujnika temperatury'),
(275, 7, 10, 'GND'),
(276, 4, 11, '+5V'),
(277, 8, 11, 'Sygnał czujnika'),
(278, 7, 11, 'GND'),
(279, 4, 12, '+5V'),
(280, 8, 12, 'Sygnał czujnika temperatury'),
(281, 7, 12, 'GND'),
(282, 1, 13, 'GND'),
(283, 3, 13, 'Sygnał'),
(284, 5, 13, '+5V'),
(285, 9, 13, 'Sygnałowy'),
(286, 6, 13, 'GND'),
(287, 4, 13, '+5V'),
(288, 8, 13, 'Sygnałowy'),
(289, 7, 13, 'GND'),
(290, 1, 14, 'GND'),
(291, 3, 14, 'Sygnał kontaktronu'),
(292, 4, 15, '+5V'),
(293, 8, 15, 'Sygnał czujnika ruchu'),
(294, 7, 15, 'GND'),
(295, 4, 16, '+5V'),
(296, 8, 16, 'Sygnał czujnika ruchu'),
(297, 7, 16, 'GND'),
(298, 1, 17, '-'),
(299, 1, 17, '-'),
(300, 1, 17, '-'),
(301, 1, 17, '--'),
(302, 1, 17, '-'),
(303, 2, 17, '-'),
(304, 3, 17, '-'),
(305, 9, 17, '-'),
(306, 10, 17, '-'),
(307, 6, 17, '-'),
(308, 1, 18, '-'),
(309, 7, 18, '-'),
(310, 4, 18, '-'),
(311, 3, 18, '-'),
(312, 0, 18, ''),
(313, 0, 18, ''),
(314, 1, 19, 'GND'),
(315, 3, 19, 'Styk kontaktoru'),
(316, 9, 38, 'kanał 8 - Swiatłło pod wanną'),
(317, 7, 38, 'kanał 7 - sterowanie term. salon'),
(318, 1, 38, 'kanał 6 - sterowanie term. kuchnia'),
(319, 5, 38, 'kanał 5 - sterowanie term. łazienka'),
(320, 6, 38, 'kanał 4 - Sterowanie pompą'),
(321, 8, 38, 'kanał 3 - termostat kaloryfer'),
(322, 3, 38, 'kanał 1 - oświetlenie kwiatów prysznic'),
(323, 4, 38, 'kanał 2 - oświetlenie kwiatów wanna'),
(324, 0, 151, '+5Vp'),
(325, 0, 151, 'Kanał 1'),
(326, 0, 151, 'Kanał 2'),
(327, 0, 151, 'GND'),
(328, 6, 53, 'GND'),
(329, 4, 53, '+5V'),
(330, 3, 53, 'Kanał 1 - wiatrak 1 (kuchnia)'),
(331, 1, 53, 'Kanał 2 - wiatrak 2 (łazienka)'),
(332, 9, 53, 'Swiatło przedpokój'),
(333, 8, 53, 'Podświetlenie klawiszy'),
(334, 4, 153, '+5V'),
(335, 7, 153, 'GND'),
(336, 9, 153, 'Kanał 8 - pompa'),
(337, 10, 153, 'Kanał 7 - termostat'),
(338, 1, 153, 'Kanał 6 - termostat'),
(339, 5, 153, 'kanał 5 - termostat'),
(340, 6, 153, 'kanał 4 - oświetlenie pod wanną'),
(341, 8, 153, 'kanał 3 - kaloryfer'),
(342, 3, 153, 'Kanał 2 - oświetlenie prysznic'),
(343, 2, 153, 'Kanał 1 - oświetlenie wanna'),
(344, 1, 152, '53.zielony'),
(345, 3, 152, '53.żółty'),
(346, 6, 152, '+5V'),
(347, 11, 152, 'SCL'),
(348, 10, 152, 'SDA'),
(349, 7, 152, 'GND'),
(350, 4, 152, 'GND'),
(351, 0, 152, '+5Vp (dla przekaźników)'),
(352, 7, 154, 'GND'),
(353, 4, 154, '+5V'),
(354, 9, 154, 'Kanał 1 - wiatrak 1'),
(355, 8, 154, 'Kanał 2 - wiatrak 2'),
(356, 4, 155, '+5V'),
(357, 7, 155, 'GND'),
(358, 9, 155, '0x010.A0 - Kanał 1 wskażnik gn. lewy'),
(359, 10, 155, '0x010.A1 - Kanał 2 wskażnik gn. prawy'),
(360, 1, 155, '0x010.A2 - Kanał 3 gniazdo lewe'),
(361, 8, 155, '0x010.A3 - Kanał 4 gniazdo prawe'),
(362, 2, 155, '0x010.A4 - Kanał 5 ogrz. lustra'),
(363, 3, 155, '0x010.A5 - Kanał 6 kaloryfer el.'),
(364, 6, 155, '0x010.A6 - Kanał 7 suszarka'),
(365, 5, 155, '0x010.A7 - Kanał 8 gniazdo k/kaloryfera'),
(366, 6, 156, '0x010.B7 Kanał 8 Zasilacz 12V 15W'),
(367, 2, 156, '0x010.B6 Kanał 7 Zasilacz 12V 150W'),
(368, 3, 156, '0x010.B5 Kanał 6 ośw. przedpokój'),
(369, 5, 156, '0x010.B4 Kanał 5 małe lusterko'),
(370, 1, 156, '0x010.B3 Kanał 4 oświetlenie pokój 2.B'),
(371, 8, 156, '0x010.B2 Kanał 3 oświetlenie pokój 2.A'),
(372, 9, 156, '0x010.B1 Kanał 2 oświetlenie pokój 1.B'),
(373, 10, 156, '0x010.B0 Kanał 1 oświetlenie pokój 1.A'),
(374, 7, 156, 'GND'),
(375, 4, 156, '+5V'),
(376, 4, 52, '+24V'),
(377, 7, 52, 'GND'),
(378, 8, 52, 'Sygnał wieczoru'),
(379, 1, 52, 'Sygnał nocy'),
(380, 3, 52, 'TX'),
(381, 9, 52, 'RX'),
(382, 5, 52, '2 taryfa'),
(383, 6, 52, 'zasilanie awaryjne'),
(384, 6, 54, '-'),
(385, 4, 54, '-'),
(386, 1, 54, '-'),
(387, 3, 54, '-'),
(388, 8, 54, '-'),
(389, 9, 54, '-'),
(390, 4, 157, '+5V '),
(391, 7, 157, 'GND'),
(392, 8, 157, 'SCL'),
(393, 3, 157, 'SDA'),
(398, 2, 21, '+5V'),
(399, 3, 21, 'Sygnał czujnika temp. i wilg'),
(400, 1, 21, 'GND'),
(401, 1, 21, 'GND'),
(402, 2, 22, '-'),
(403, 3, 22, '-'),
(404, 1, 22, '-'),
(405, 1, 22, ''),
(406, 2, 23, '+5V dla przepływomierza'),
(407, 3, 23, 'GND'),
(408, 1, 23, 'Sygnał od przepływomierza'),
(409, 1, 23, 'Sygnał od przycisku'),
(410, 6, 42, 'Sygnał czujnika ruchu dla pokoju'),
(411, 7, 42, 'GND dla czujników ruchu'),
(412, 9, 42, 'Sygnał czujnika ruchu dla pracowni'),
(413, 4, 42, '+5V dla czujników ruchu'),
(414, 2, 42, 'Sygnał czujnika ruchu dla holu'),
(415, 3, 42, 'Sygnał kontaktronu pracowania'),
(416, 1, 42, 'GND dla kontaktronów'),
(417, 8, 42, 'Sygnał kontaktronu dla pokoju'),
(418, 6, 43, 'GND'),
(419, 9, 43, 'GND'),
(420, 13, 43, '+5V'),
(421, 8, 43, 'Sygnał'),
(422, 4, 44, '+5V'),
(423, 9, 44, 'Sygnał'),
(424, 3, 44, 'GND'),
(425, 1, 44, 'GND'),
(426, 3, 45, 'Sygnał'),
(427, 1, 45, 'GND'),
(428, 6, 46, 'GND'),
(429, 7, 46, 'GND'),
(430, 5, 46, '+5V'),
(431, 8, 46, 'Sygnał'),
(432, 3, 47, 'Sygnał'),
(433, 1, 47, 'GND'),
(434, 1, 60, '-'),
(435, 1, 60, '-'),
(436, 2, 60, 'Sygnał od kontaktronu'),
(437, 3, 60, 'GND'),
(438, 4, 61, '+5V'),
(439, 1, 61, 'Sygnał od temperatury kuchnia'),
(440, 8, 61, 'Sygnał od temperatury salon'),
(441, 6, 61, 'Ogrzewanie kuchni'),
(442, 9, 61, 'Ogrzewanie salon'),
(443, 3, 61, 'GND'),
(444, 1, 62, '-'),
(445, 8, 62, '-'),
(446, 9, 62, 'Temperatura kuchnia'),
(447, 4, 62, '+5V'),
(448, 3, 62, 'Sygnał kuchnia'),
(449, 5, 62, '+5V'),
(450, 6, 62, 'GND'),
(451, 7, 62, 'GND'),
(452, 4, 66, '+5V zasilanie'),
(453, 6, 66, 'Ogrzewanie salon'),
(454, 9, 66, 'Ogrzewanie kuchnia'),
(455, 7, 66, 'GND'),
(456, 4, 67, '+5V'),
(457, 1, 67, 'Listwa LED sufit przy jadalni'),
(458, 8, 67, 'Listwa LED sufit przy lodówce'),
(459, 9, 67, 'Listwa LED 1 przy drzwiach'),
(460, 3, 67, 'Listwa LED  drzwi 2'),
(461, 7, 67, 'GND'),
(462, 4, 68, '+5V'),
(463, 5, 68, 'Zasilanie zasilacza 12V'),
(464, 7, 68, 'GND'),
(465, 7, 145, 'GND - 71'),
(466, 6, 145, 'GND - 73'),
(467, 9, 145, '1.B7 - 90'),
(468, 13, 145, '1.B6 -  91'),
(469, 8, 145, '1.B5 - 88'),
(470, 5, 145, '1.B4 - 89'),
(471, 10, 145, '1.B3 - 70'),
(472, 11, 145, '1.B2 - 69'),
(473, 3, 145, '1.B1 - 74'),
(474, 1, 145, '1.B0 - 75'),
(475, 2, 145, 'GND - 82'),
(476, 4, 145, 'GND - 83'),
(477, 7, 146, 'GND - 81'),
(478, 6, 146, 'GND - 85'),
(479, 9, 146, '1.A7 - 95'),
(480, 13, 146, '1.A6 - 96'),
(481, 8, 146, '1.A5 - 97'),
(482, 5, 146, '1.A4 - 98'),
(483, 10, 146, '1.A3 - 99'),
(484, 11, 146, '1.A2 - 100'),
(485, 3, 146, '1.A1 - 86'),
(486, 1, 146, '1.A0 - 87'),
(487, 2, 146, 'GND - 86'),
(488, 4, 146, 'GND - 84'),
(489, 4, 159, '+5V przekaźników'),
(490, 8, 159, '-'),
(491, 5, 159, '-'),
(492, 7, 159, 'GND'),
(493, 4, 160, '+5V'),
(494, 7, 160, 'GND'),
(495, 3, 160, 'SDA'),
(496, 8, 160, 'SCL'),
(497, 2, 160, 'INT'),
(499, 4, 163, '+5V'),
(500, 1, 163, 'GND'),
(501, 3, 163, 'RX'),
(502, 9, 163, 'TX'),
(503, 1, 161, 'GND'),
(504, 3, 161, 'GND'),
(505, 5, 152, ''),
(506, 9, 152, ''),
(507, 8, 152, ''),
(508, 2, 152, ''),
(509, 0, 198, '+5V'),
(510, 0, 198, 'GND'),
(511, 0, 199, 'Sygnał wieczoru'),
(512, 0, 199, 'Sygnal nocy'),
(513, 0, 199, 'Sygnał 2 taryfa'),
(514, 0, 199, 'Sygnał zasilanie awaryjne'),
(515, 0, 197, 'Sygnał wieczoru'),
(516, 0, 197, 'Sygnał nocy'),
(517, 0, 197, 'Sygnał 2 taryfy'),
(518, 0, 197, 'Sygnał zasilania awaryjnego'),
(519, 0, 196, 'GND'),
(520, 0, 196, 'GND'),
(521, 0, 195, '+24V'),
(522, 0, 195, 'GND'),
(523, 0, 194, 'Zasilanie awarune'),
(524, 0, 194, '2 taryfa'),
(525, 0, 194, 'noc'),
(526, 0, 194, 'wieczór'),
(527, 0, 194, '+24 V sterowane'),
(528, 0, 194, 'GND'),
(529, 0, 194, 'GND'),
(530, 0, 194, '+24 V'),
(531, 0, 193, '+5V'),
(532, 0, 193, 'GND'),
(533, 0, 192, '42.4 kontantron pracownia4'),
(534, 0, 192, '42.5 kontaktron pokój'),
(535, 0, 192, '42.6 czujnik ruchu nad drzwiami do pokojów'),
(536, 0, 192, '42.7 czujnik ruchu pracownia'),
(537, 0, 192, '42.8 czujnik ruchu pokój'),
(538, 0, 192, '53.2'),
(539, 0, 192, '54.6'),
(540, 0, 192, '54.5'),
(541, 0, 192, '54.4'),
(542, 0, 192, '54.3'),
(543, 0, 192, '54.2'),
(544, 0, 192, '54.1'),
(545, 0, 191, 'Zasilanie awaryjne'),
(546, 0, 191, '2 taryfa'),
(547, 0, 191, 'noc'),
(548, 0, 191, 'wieczór'),
(549, 0, 190, '`35.5 Światło w WC (in)'),
(550, 0, 190, '35.6 Żadanie uruchomienie wiatraka w WC (in)'),
(551, 0, 190, '35.7 Przekażnik 5 WC (out)'),
(552, 0, 190, '35.8 Przekaźnik 6 WC (out)'),
(553, 0, 190, '53.4 Przekaźnik wiatrak 1 przedpokoj'),
(554, 0, 190, '53.5 Przekaźnik wiatrak 2'),
(555, 0, 190, '59.8 -'),
(556, 0, 190, '59.7'),
(557, 0, 190, '59.6'),
(558, 0, 190, '59.5'),
(559, 0, 189, '+5V'),
(560, 0, 189, 'GND'),
(561, 0, 189, 'GND'),
(562, 0, 189, '+24V'),
(563, 0, 86, 'RX'),
(564, 0, 86, 'TX'),
(565, 0, 86, 'Zasilanie awaryjne'),
(566, 0, 86, '2 taryfa'),
(567, 0, 86, 'noc'),
(568, 0, 86, 'wieczór'),
(569, 0, 86, '+24V sterowalne'),
(570, 0, 86, 'GND'),
(571, 0, 59, 'Podświetlenie klawiszy'),
(572, 0, 59, 'Podświetlenie klawiszy'),
(573, 0, 59, 'Klawisz lewy Hol'),
(574, 0, 59, 'Klawisz prawy Hol'),
(575, 0, 59, '-'),
(576, 0, 59, '-'),
(577, 0, 59, '-'),
(578, 0, 59, '-'),
(579, 0, 57, 'RX'),
(580, 0, 57, 'TX'),
(581, 0, 57, 'GND'),
(582, 0, 57, '+24V'),
(583, 0, 57, 'wieczór'),
(584, 0, 57, 'noc'),
(585, 0, 57, '2 taryfa'),
(586, 0, 57, 'zasilanie awaryjne'),
(587, 5, 58, 'GND'),
(588, 9, 58, 'włacznik salon lewy klawisz lewy'),
(589, 3, 58, 'włącznik salon lewy klawisz prawy'),
(590, 1, 58, 'włącznik salon prawy klawisz lewy'),
(591, 8, 58, 'włącznik salon prawy klawisz prawy'),
(592, 6, 58, 'włącznik kuchnia klawisz lewy'),
(593, 7, 58, 'włącznik kuchnia klawisz prawy'),
(594, 4, 58, 'podświetlenie klawiszy'),
(595, 0, 188, '83.6 czujnik ruchu 1'),
(596, 0, 188, '83.5 czujnik ruchu 2'),
(597, 0, 188, '83.4'),
(598, 0, 188, '83.3'),
(599, 0, 188, '83.2'),
(600, 0, 188, '83.1'),
(601, 0, 188, '84.3 Czujnik ruchu 1'),
(602, 0, 188, '84.8'),
(603, 0, 188, '84.7'),
(604, 0, 188, '84.6'),
(605, 0, 188, '64.5'),
(606, 0, 188, '84.3 Czujnik ruchu 2'),
(607, 5, 83, '-'),
(608, 6, 83, '-'),
(609, 3, 83, '-'),
(610, 9, 83, '-'),
(611, 8, 83, 'Sygnał czujnika 2 (w stronę salonu)'),
(612, 1, 83, 'Sygnał czujnika 1 (w stronę holu)'),
(613, 4, 83, '+5V'),
(614, 7, 83, 'GND'),
(615, 0, 187, 'GND'),
(616, 0, 187, '+5V'),
(617, 0, 186, 'Wieczór'),
(618, 0, 186, 'Noc'),
(619, 0, 186, '2 taryfa'),
(620, 0, 186, 'Zasilanie awaryjne'),
(621, 0, 185, '93.1'),
(622, 0, 185, '93.2'),
(623, 0, 185, '86,1'),
(624, 0, 185, '86.2'),
(625, 0, 185, '57.1'),
(626, 0, 185, '57.2'),
(627, 0, 185, '34.1'),
(628, 0, 185, '34.2'),
(629, 0, 185, '52.1'),
(630, 0, 185, '52.2'),
(631, 0, 185, 'GND'),
(632, 0, 185, '+5V'),
(633, 0, 184, 'GND'),
(634, 0, 184, '+24V'),
(635, 0, 183, 'D183.2'),
(636, 0, 183, 'D181.2'),
(637, 0, 183, 'B182.2'),
(638, 0, 183, 'M80.6'),
(639, 0, 183, 'Q84,3'),
(640, 0, 183, 'L70.3'),
(641, 0, 183, 'P81.6'),
(642, 0, 183, 'R85.6'),
(643, 0, 183, 'T71.6'),
(644, 0, 183, 'T71.5'),
(645, 0, 183, 'T71.4'),
(646, 0, 183, 'T71.3'),
(647, 7, 182, 'GND'),
(648, 8, 182, 'Sygnał'),
(649, 4, 182, '+5V'),
(650, 7, 180, 'GND'),
(651, 8, 180, 'Sygnał'),
(652, 4, 180, '+5V'),
(653, 0, 181, 'Zasilanie +5V'),
(654, 0, 181, 'GND'),
(655, 0, 181, 'G.7'),
(656, 0, 181, 'G.8'),
(657, 0, 178, 'H38.8'),
(658, 0, 178, 'H38.7'),
(659, 0, 178, 'H38.6'),
(660, 0, 178, 'H38.5'),
(661, 0, 178, 'H38.4'),
(662, 0, 178, 'H38.3'),
(663, 0, 178, 'H38.2'),
(664, 0, 178, 'H38.1'),
(665, 0, 178, 'I61,3'),
(666, 0, 178, 'I61,6'),
(667, 0, 178, 'I61.5'),
(668, 0, 178, 'I61.4'),
(669, 0, 177, 'J36.6'),
(670, 0, 177, 'J36.5'),
(671, 0, 177, 'J36.4'),
(672, 0, 177, 'J36.3'),
(673, 0, 177, 'J36.2'),
(674, 0, 177, 'J36.1'),
(675, 0, 177, 'E181.3'),
(676, 0, 177, 'E181.4'),
(677, 0, 177, 'K7.10'),
(678, 0, 177, 'K7.9'),
(679, 0, 177, 'K7.8'),
(680, 0, 177, 'K7.7'),
(681, 0, 70, '+5V'),
(682, 0, 70, 'GND'),
(683, 0, 70, '-'),
(684, 0, 70, '-'),
(685, 0, 70, '-'),
(686, 0, 70, '-'),
(687, 0, 70, '-'),
(688, 0, 70, ''),
(689, 0, 80, '+5V'),
(690, 0, 80, 'GND'),
(691, 0, 80, '-'),
(692, 0, 80, '-'),
(693, 0, 80, '-'),
(694, 0, 80, '-'),
(695, 0, 80, '-'),
(696, 0, 80, '-'),
(697, 0, 176, 'P81.5'),
(698, 0, 176, 'P81,4'),
(699, 0, 176, 'P81.3'),
(700, 0, 176, 'P81.2'),
(701, 0, 176, 'P81.1'),
(702, 0, 176, 'R85.2'),
(703, 0, 176, 'R85.3'),
(704, 0, 176, 'Q84.8'),
(705, 0, 176, 'Q84.7'),
(706, 0, 176, 'Q84.6'),
(707, 0, 176, 'Q84.5'),
(708, 0, 176, 'Q84.4'),
(709, 0, 175, 'M80.5'),
(710, 0, 175, 'M80.4'),
(711, 0, 175, 'M80.3'),
(712, 0, 175, 'M80.2'),
(713, 0, 175, 'M80.1'),
(714, 0, 175, 'R85.2'),
(715, 0, 175, 'R85.3'),
(716, 0, 175, 'Q84.8'),
(717, 0, 175, 'Q84.7'),
(718, 0, 175, 'Q84.6'),
(719, 0, 175, 'Q84.5'),
(720, 0, 175, 'Q84.4'),
(721, 0, 81, 'N.5'),
(722, 0, 81, 'N.4'),
(723, 0, 81, 'N.3'),
(724, 0, 81, 'N.2'),
(725, 0, 81, 'N.1'),
(726, 0, 81, 'A.7'),
(727, 0, 81, '+5V'),
(728, 0, 81, 'GND'),
(729, 0, 84, 'GND'),
(730, 0, 84, '+5V'),
(731, 0, 84, 'A.5'),
(732, 0, 84, 'N12'),
(733, 0, 84, 'N.11'),
(734, 0, 84, 'N.10'),
(735, 0, 84, 'N.9'),
(736, 0, 84, 'N.8'),
(737, 0, 85, 'W.4'),
(738, 0, 85, 'N.6'),
(739, 0, 85, 'N.7'),
(740, 0, 85, 'O.6'),
(741, 0, 85, '0.7'),
(742, 0, 85, 'A.8'),
(743, 0, 85, '+5V'),
(744, 0, 85, 'GND'),
(745, 0, 72, 'GND'),
(746, 0, 72, '+5V'),
(747, 0, 72, 'W.12'),
(748, 0, 72, 'W.11'),
(749, 0, 72, 'W.10'),
(750, 0, 72, 'W.9'),
(751, 0, 72, 'W.8'),
(752, 0, 72, 'W.7'),
(753, 0, 72, 'W.6'),
(754, 0, 72, 'W.5'),
(755, 0, 71, 'W2'),
(756, 0, 71, 'W3'),
(757, 0, 71, 'A12'),
(758, 0, 71, 'A11'),
(759, 0, 71, 'A10'),
(760, 0, 71, 'A9'),
(761, 0, 71, '+5V'),
(762, 0, 71, 'GND'),
(763, 0, 174, '+5V'),
(764, 0, 174, 'GND'),
(765, 0, 179, 'GND'),
(766, 0, 179, 'T71.1'),
(767, 0, 179, 'T71.2'),
(768, 0, 179, 'R85.4'),
(769, 0, 179, 'S72.10'),
(770, 0, 179, 'S72.9'),
(771, 0, 179, 'S72.8'),
(772, 0, 179, 'S72.7'),
(773, 0, 179, 'S72.6'),
(774, 0, 179, 'S72.5'),
(775, 0, 179, 'S72.4'),
(776, 0, 179, 'S72.3');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZylaWidok`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ZylaWidok` (
`id` smallint unsigned
,`kolor_id` tinyint unsigned
,`przewod_id` tinyint unsigned
,`opis` text
,`kolor` text
,`html` text
);

-- --------------------------------------------------------

--
-- Struktura widoku `ElementyPlytkowePinView`
--
DROP TABLE IF EXISTS `ElementyPlytkowePinView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ElementyPlytkowePinView`  AS  select `elementy_plytkowe_pin`.`id` AS `id`,`elementy_plytkowe_pin`.`nazwa` AS `pinnazwa`,`elementy_plytkowe_pin`.`pos` AS `pos`,`elementy_plytkowe_pin`.`element_plytkowy_id` AS `element_plytkowy_id`,`elementy_plytkowe`.`nazwa` AS `elementnazwa`,`elementy_plytkowe`.`ilosc_pin` AS `ilosc_pin`,`elementy_plytkowe`.`plytka_id` AS `plytka_id`,`elementy_plytkowe`.`rodzaj_urzadzenia` AS `rodzaj_urzadzenia` from (`elementy_plytkowe_pin` left join `elementy_plytkowe` on((`elementy_plytkowe_pin`.`element_plytkowy_id` = `elementy_plytkowe`.`id`))) where (0 <> 1) order by `elementy_plytkowe`.`plytka_id`,`elementy_plytkowe`.`nazwa`,`elementy_plytkowe_pin`.`pos` ;

-- --------------------------------------------------------

--
-- Struktura widoku `ElementyPlytkowePolaczeniaPinView`
--
DROP TABLE IF EXISTS `ElementyPlytkowePolaczeniaPinView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ElementyPlytkowePolaczeniaPinView`  AS  select `polaczenie_plytka_polaczenie`.`id` AS `id`,`polaczenie_plytka_polaczenie`.`polaczenie_plytka_id` AS `polaczenie_plytka_id`,`polaczenie_plytka_polaczenie`.`elementy_plytkowe_piny_id` AS `elementy_plytkowe_piny_id`,`elementy_plytkowe_pin`.`nazwa` AS `pinnazwa`,`elementy_plytkowe_pin`.`pos` AS `pos`,`elementy_plytkowe_pin`.`element_plytkowy_id` AS `element_plytkowy_id`,`elementy_plytkowe`.`nazwa` AS `elemnazwa`,`elementy_plytkowe`.`ilosc_pin` AS `ilosc_pin`,`elementy_plytkowe`.`plytka_id` AS `plytka_id`,`elementy_plytkowe`.`rodzaj_urzadzenia` AS `rodzaj_urzadzenia`,`rodzaj_zakonczenia`.`nazwa` AS `rodznazwa`,`rodzaj_zakonczenia`.`kod` AS `kod`,`rodzaj_zakonczenia`.`przewod` AS `przewod`,`rodzaj_zakonczenia`.`plytka` AS `plytka` from (((`polaczenie_plytka_polaczenie` left join `elementy_plytkowe_pin` on((`polaczenie_plytka_polaczenie`.`elementy_plytkowe_piny_id` = `elementy_plytkowe_pin`.`id`))) left join `elementy_plytkowe` on((`elementy_plytkowe_pin`.`element_plytkowy_id` = `elementy_plytkowe`.`id`))) left join `rodzaj_zakonczenia` on((`elementy_plytkowe`.`rodzaj_urzadzenia` = `rodzaj_zakonczenia`.`id`))) where (0 <> 1) order by `polaczenie_plytka_polaczenie`.`polaczenie_plytka_id`,`elementy_plytkowe_pin`.`pos` ;

-- --------------------------------------------------------

--
-- Struktura widoku `ElementyPlytkoweView`
--
DROP TABLE IF EXISTS `ElementyPlytkoweView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ElementyPlytkoweView`  AS  select `elementy_plytkowe`.`id` AS `id`,`elementy_plytkowe`.`nazwa` AS `nazwa`,`elementy_plytkowe`.`ilosc_pin` AS `ilosc_pin`,`elementy_plytkowe`.`plytka_id` AS `plytka_id`,`plytki`.`miejsce_id` AS `miejsce_id`,`plytki`.`nazwa` AS `pnazwa`,`rodzaj_zakonczenia`.`id` AS `urzadzenie_rodzaj_id`,`rodzaj_zakonczenia`.`nazwa` AS `urzadzenie_nazwa`,`rodzaj_zakonczenia`.`kod` AS `urzadzenie_rodzaj_kod`,`rodzaj_zakonczenia`.`plytka` AS `urzadzenie_plytka`,`rodzaj_zakonczenia`.`przewod` AS `urzadzenie_przewod`,`MiejsceView`.`nazwa` AS `mnazwa`,`MiejsceView`.`opis` AS `opis`,`MiejsceView`.`zbiorcze` AS `zbiorcze`,`MiejsceView`.`id_pomieszczenie` AS `id_pomieszczenie`,`MiejsceView`.`kod` AS `kod`,`MiejsceView`.`polaczenie` AS `polaczenie`,`MiejsceView`.`pomieszczenie` AS `pomieszczenie` from (((`elementy_plytkowe` left join `plytki` on((`plytki`.`id` = `elementy_plytkowe`.`plytka_id`))) left join `MiejsceView` on((`plytki`.`miejsce_id` = `MiejsceView`.`id`))) left join `rodzaj_zakonczenia` on((`elementy_plytkowe`.`rodzaj_urzadzenia` = `rodzaj_zakonczenia`.`id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `KolorView`
--
DROP TABLE IF EXISTS `KolorView`;

CREATE ALGORITHM=TEMPTABLE DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `KolorView`  AS  select `kolor`.`id` AS `id`,`kolor`.`nazwa` AS `nazwa`,`kolor`.`html` AS `html` from `kolor` order by `kolor`.`nazwa` ;

-- --------------------------------------------------------

--
-- Struktura widoku `MiejscePrzewodView`
--
DROP TABLE IF EXISTS `MiejscePrzewodView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `MiejscePrzewodView`  AS  select `przewod_miejsce`.`id` AS `id`,`przewod_miejsce`.`przewod_id` AS `pid`,`przewod_miejsce`.`miejsce_id` AS `mid`,`MiejsceView`.`nazwa` AS `nazwa`,`MiejsceView`.`opis` AS `opis`,`MiejsceView`.`zbiorcze` AS `zbiorcze`,`MiejsceView`.`id_pomieszczenie` AS `id_pomieszczenie`,`MiejsceView`.`kod` AS `kod`,`MiejsceView`.`polaczenie` AS `polaczenie`,`MiejsceView`.`pomieszczenie` AS `pomieszczenie`,`przewod`.`id` AS `ppid`,`przewod`.`opis` AS `popis`,`przewod`.`ilosc_zyl` AS `ilosc_zyl` from ((`przewod_miejsce` left join `MiejsceView` on((`MiejsceView`.`id` = `przewod_miejsce`.`miejsce_id`))) left join `przewod` on((`przewod`.`id` = `przewod_miejsce`.`przewod_id`))) where (0 <> 1) ;

-- --------------------------------------------------------

--
-- Struktura widoku `MiejsceView`
--
DROP TABLE IF EXISTS `MiejsceView`;

CREATE ALGORITHM=TEMPTABLE DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `MiejsceView`  AS  select `miejsce`.`id` AS `id`,`miejsce`.`nazwa` AS `nazwa`,`miejsce`.`opis` AS `opis`,`miejsce`.`zbiorcze` AS `zbiorcze`,`miejsce`.`id_pomieszczenie` AS `id_pomieszczenie`,`miejsce`.`kod` AS `kod`,`miejsce`.`polaczenie` AS `polaczenie`,`pomieszczenie`.`nazwa` AS `pomieszczenie` from (`miejsce` left join `pomieszczenie` on((`miejsce`.`id_pomieszczenie` = `pomieszczenie`.`id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `PlytkaMiejsceView`
--
DROP TABLE IF EXISTS `PlytkaMiejsceView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `PlytkaMiejsceView`  AS  select `plytki`.`id` AS `id`,`plytki`.`nazwa` AS `nazwa`,`MiejsceView`.`id` AS `miejsce_id`,`MiejsceView`.`nazwa` AS `mnazwa`,`MiejsceView`.`opis` AS `opis`,`MiejsceView`.`zbiorcze` AS `zbiorcze`,`MiejsceView`.`id_pomieszczenie` AS `id_pomieszczenie`,`MiejsceView`.`kod` AS `kod`,`MiejsceView`.`polaczenie` AS `polaczenie`,`MiejsceView`.`pomieszczenie` AS `pomieszczenie` from (`plytki` left join `MiejsceView` on((`plytki`.`miejsce_id` = `MiejsceView`.`id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `PrzewodMiejsceZakonczenieView`
--
DROP TABLE IF EXISTS `PrzewodMiejsceZakonczenieView`;

CREATE ALGORITHM=TEMPTABLE DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `PrzewodMiejsceZakonczenieView`  AS  select `z`.`id` AS `zid`,`z`.`etykieta` AS `etykieta`,`z`.`przewod_miejsce_id` AS `przewod_miejsce_id_zlacze`,`z`.`rodzaj_zakonczenia` AS `rodzaj_zakonczenia`,`pm`.`przewod_id` AS `przewod_id`,`pm`.`miejsce_id` AS `miejsce_id`,`pm`.`id` AS `przewod_miejsce_id`,`rz`.`nazwa` AS `nazwa`,`rz`.`kod` AS `kod` from ((`przewod_miejsce` `pm` left join `zakonczenie` `z` on((`pm`.`id` = `z`.`przewod_miejsce_id`))) left join `rodzaj_zakonczenia` `rz` on((`rz`.`id` = `z`.`rodzaj_zakonczenia`))) where (0 <> 1) order by `pm`.`miejsce_id`,`pm`.`przewod_id`,`z`.`rodzaj_zakonczenia`,`z`.`etykieta` ;

-- --------------------------------------------------------

--
-- Struktura widoku `WewnetrzneKableView`
--
DROP TABLE IF EXISTS `WewnetrzneKableView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `WewnetrzneKableView`  AS  select `przewod_miejsce`.`przewod_id` AS `przewod_id`,`przewod_miejsce`.`miejsce_id` AS `miejsce_id`,count(`przewod_miejsce`.`przewod_id`) AS `c` from `przewod_miejsce` group by `przewod_miejsce`.`miejsce_id`,`przewod_miejsce`.`przewod_id` having (`c` = 2) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZakonczenieView`
--
DROP TABLE IF EXISTS `ZakonczenieView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZakonczenieView`  AS  select `zakonczenie`.`id` AS `id`,`zakonczenie`.`etykieta` AS `etykieta`,`zakonczenie`.`przewod_miejsce_id` AS `przewod_miejsce_id`,`zakonczenie`.`rodzaj_zakonczenia` AS `rodzaj_zakonczenia`,`zakonczenie`.`ilosc_pin` AS `ilosc_pin`,`przewod_miejsce`.`przewod_id` AS `przewod_id`,`przewod_miejsce`.`miejsce_id` AS `miejsce_id`,`rodzaj_zakonczenia`.`nazwa` AS `nazwa`,`rodzaj_zakonczenia`.`kod` AS `kod` from ((`zakonczenie` left join `przewod_miejsce` on((`przewod_miejsce`.`id` = `zakonczenie`.`przewod_miejsce_id`))) left join `rodzaj_zakonczenia` on((`rodzaj_zakonczenia`.`id` = `zakonczenie`.`rodzaj_zakonczenia`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZakonczenieZylyView`
--
DROP TABLE IF EXISTS `ZakonczenieZylyView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `ZakonczenieZylyView`  AS  select `zakonczenie_zyly`.`id` AS `zzid`,`zakonczenie_zyly`.`zakonczenie_id` AS `zakonczenie_id`,`zakonczenie_zyly`.`zyla_id` AS `zyla_id`,`zakonczenie_zyly`.`pos` AS `pos`,`zakonczenie_zyly`.`opis` AS `opis`,`zakonczenie`.`id` AS `zid`,`zakonczenie`.`etykieta` AS `etykieta`,`zakonczenie`.`przewod_miejsce_id` AS `przewod_miejsce_id`,`zakonczenie`.`rodzaj_zakonczenia` AS `rodzaj_zakonczenia` from (`zakonczenie_zyly` left join `zakonczenie` on((`zakonczenie_zyly`.`zakonczenie_id` = `zakonczenie`.`id`))) where (0 <> 1) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZakonczePrzewodMiejsce`
--
DROP TABLE IF EXISTS `ZakonczePrzewodMiejsce`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZakonczePrzewodMiejsce`  AS  select `ZakonczenieView`.`id` AS `zid`,`ZakonczenieView`.`etykieta` AS `etykieta`,`ZakonczenieView`.`przewod_miejsce_id` AS `przewod_miejsce_id`,`ZakonczenieView`.`rodzaj_zakonczenia` AS `rodzaj_zakonczenia`,`ZakonczenieView`.`przewod_id` AS `przewod_id`,`ZakonczenieView`.`miejsce_id` AS `miejsce_id`,`ZakonczenieView`.`nazwa` AS `znazwa`,`ZakonczenieView`.`kod` AS `zkod`,`ZakonczenieView`.`ilosc_pin` AS `ilosc_pin`,`MiejsceView`.`nazwa` AS `mnazwa`,`MiejsceView`.`opis` AS `mopis`,`MiejsceView`.`zbiorcze` AS `zbiorcze`,`MiejsceView`.`kod` AS `mkod`,`MiejsceView`.`polaczenie` AS `polaczenie`,`MiejsceView`.`pomieszczenie` AS `pomieszczenie`,`przewod`.`opis` AS `popis`,`przewod`.`ilosc_zyl` AS `ilosc_zyl` from ((`ZakonczenieView` left join `MiejsceView` on((`MiejsceView`.`id` = `ZakonczenieView`.`miejsce_id`))) left join `przewod` on((`przewod`.`id` = `ZakonczenieView`.`przewod_id`))) where (0 <> 1) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZewnetrzneKableView`
--
DROP TABLE IF EXISTS `ZewnetrzneKableView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZewnetrzneKableView`  AS  select `przewod_miejsce`.`przewod_id` AS `przewod_id`,`przewod_miejsce`.`miejsce_id` AS `miejsce_id`,count(`przewod_miejsce`.`przewod_id`) AS `c` from `przewod_miejsce` group by `przewod_miejsce`.`miejsce_id`,`przewod_miejsce`.`przewod_id` having (`c` = 1) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZlaczeWtyczkaView`
--
DROP TABLE IF EXISTS `ZlaczeWtyczkaView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZlaczeWtyczkaView`  AS  select `zw`.`wtyczka_id` AS `wtyczka_id`,`zw`.`zlacze_id` AS `zlacze_id`,`ep`.`id` AS `epid`,`ep`.`nazwa` AS `epnazwa`,`ep`.`pos` AS `eppos`,`zz`.`zyla_id` AS `zyla_id`,`zz`.`pos` AS `zzpos`,`zz`.`opis` AS `zzopis`,`zz`.`etykieta` AS `zzetykieta`,`z`.`id` AS `zid`,`z`.`kolor_id` AS `kolor_id`,`z`.`przewod_id` AS `przewod_id`,`z`.`opis` AS `opis`,`z`.`kolor` AS `kolor`,`z`.`html` AS `html` from (((`zlacze_wtyczka` `zw` left join `elementy_plytkowe_pin` `ep` on((`ep`.`element_plytkowy_id` = `zw`.`zlacze_id`))) left join `ZakonczenieZylyView` `zz` on(((`zz`.`zakonczenie_id` = `zw`.`wtyczka_id`) and (`ep`.`pos` = `zz`.`pos`)))) left join `ZylaWidok` `z` on((`z`.`id` = `zz`.`zyla_id`))) where (0 <> 1) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZylaWidok`
--
DROP TABLE IF EXISTS `ZylaWidok`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZylaWidok`  AS  select `z`.`id` AS `id`,`z`.`kolor_id` AS `kolor_id`,`z`.`przewod_id` AS `przewod_id`,`z`.`opis` AS `opis`,`k`.`nazwa` AS `kolor`,`k`.`html` AS `html` from (`zyla` `z` left join `kolor` `k` on((`k`.`id` = `z`.`kolor_id`))) where (0 <> 1) order by `k`.`nazwa`,`z`.`przewod_id` ;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `elementy_plytkowe`
--
ALTER TABLE `elementy_plytkowe`
  ADD PRIMARY KEY (`id`),
  ADD KEY `plytka_id` (`plytka_id`);

--
-- Indeksy dla tabeli `elementy_plytkowe_pin`
--
ALTER TABLE `elementy_plytkowe_pin`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pos` (`pos`),
  ADD KEY `urzadzenie_plytkowe_id` (`element_plytkowy_id`);

--
-- Indeksy dla tabeli `kolor`
--
ALTER TABLE `kolor`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `miejsce`
--
ALTER TABLE `miejsce`
  ADD PRIMARY KEY (`id`),
  ADD KEY `zbiorcze` (`zbiorcze`),
  ADD KEY `id_pomieszczenie` (`id_pomieszczenie`),
  ADD KEY `polaczenie` (`polaczenie`);

--
-- Indeksy dla tabeli `plytki`
--
ALTER TABLE `plytki`
  ADD PRIMARY KEY (`id`),
  ADD KEY `miejsce_id` (`miejsce_id`);

--
-- Indeksy dla tabeli `polaczenie_plytka`
--
ALTER TABLE `polaczenie_plytka`
  ADD PRIMARY KEY (`id`),
  ADD KEY `plytka_id` (`plytka_id`);

--
-- Indeksy dla tabeli `polaczenie_plytka_polaczenie`
--
ALTER TABLE `polaczenie_plytka_polaczenie`
  ADD PRIMARY KEY (`id`),
  ADD KEY `polaczenie_plytka_id` (`polaczenie_plytka_id`),
  ADD KEY `elementy_plytkowe_piny_id` (`elementy_plytkowe_piny_id`);

--
-- Indeksy dla tabeli `polaczenie_zyla`
--
ALTER TABLE `polaczenie_zyla`
  ADD PRIMARY KEY (`id`),
  ADD KEY `zakonczenie_zyly_id` (`zakonczenie_zyly_id`),
  ADD KEY `zyla_id` (`zyla_id`);

--
-- Indeksy dla tabeli `pomieszczenie`
--
ALTER TABLE `pomieszczenie`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `przewod`
--
ALTER TABLE `przewod`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `przewod_miejsce`
--
ALTER TABLE `przewod_miejsce`
  ADD PRIMARY KEY (`id`),
  ADD KEY `przemieprzeidx` (`przewod_id`),
  ADD KEY `przemiemieidx` (`miejsce_id`);

--
-- Indeksy dla tabeli `rodzaj_zakonczenia`
--
ALTER TABLE `rodzaj_zakonczenia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `przewod` (`przewod`),
  ADD KEY `plytka` (`plytka`);

--
-- Indeksy dla tabeli `zakonczenie`
--
ALTER TABLE `zakonczenie`
  ADD PRIMARY KEY (`id`),
  ADD KEY `przewod_miejsce_id` (`przewod_miejsce_id`),
  ADD KEY `rodzaj_zakonczenia` (`rodzaj_zakonczenia`);

--
-- Indeksy dla tabeli `zakonczenie_zyly`
--
ALTER TABLE `zakonczenie_zyly`
  ADD PRIMARY KEY (`id`),
  ADD KEY `zakonczenie_id` (`zakonczenie_id`),
  ADD KEY `zyla_id` (`zyla_id`);

--
-- Indeksy dla tabeli `zlacze_wtyczka`
--
ALTER TABLE `zlacze_wtyczka`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `zlacze_id` (`wtyczka_id`,`zlacze_id`),
  ADD KEY `zlawtyzlafg` (`zlacze_id`);

--
-- Indeksy dla tabeli `zyla`
--
ALTER TABLE `zyla`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kolor_id` (`kolor_id`),
  ADD KEY `przewod_id` (`przewod_id`);

--
-- AUTO_INCREMENT dla tabel zrzutów
--

--
-- AUTO_INCREMENT dla tabeli `elementy_plytkowe`
--
ALTER TABLE `elementy_plytkowe`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT dla tabeli `elementy_plytkowe_pin`
--
ALTER TABLE `elementy_plytkowe_pin`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=537;

--
-- AUTO_INCREMENT dla tabeli `kolor`
--
ALTER TABLE `kolor`
  MODIFY `id` tinyint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT dla tabeli `miejsce`
--
ALTER TABLE `miejsce`
  MODIFY `id` tinyint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT dla tabeli `plytki`
--
ALTER TABLE `plytki`
  MODIFY `id` tinyint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT dla tabeli `polaczenie_plytka`
--
ALTER TABLE `polaczenie_plytka`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- AUTO_INCREMENT dla tabeli `polaczenie_plytka_polaczenie`
--
ALTER TABLE `polaczenie_plytka_polaczenie`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=288;

--
-- AUTO_INCREMENT dla tabeli `polaczenie_zyla`
--
ALTER TABLE `polaczenie_zyla`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=193;

--
-- AUTO_INCREMENT dla tabeli `pomieszczenie`
--
ALTER TABLE `pomieszczenie`
  MODIFY `id` tinyint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT dla tabeli `przewod_miejsce`
--
ALTER TABLE `przewod_miejsce`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=395;

--
-- AUTO_INCREMENT dla tabeli `rodzaj_zakonczenia`
--
ALTER TABLE `rodzaj_zakonczenia`
  MODIFY `id` tinyint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `zakonczenie`
--
ALTER TABLE `zakonczenie`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=138;

--
-- AUTO_INCREMENT dla tabeli `zakonczenie_zyly`
--
ALTER TABLE `zakonczenie_zyly`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=793;

--
-- AUTO_INCREMENT dla tabeli `zlacze_wtyczka`
--
ALTER TABLE `zlacze_wtyczka`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT dla tabeli `zyla`
--
ALTER TABLE `zyla`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=777;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `elementy_plytkowe`
--
ALTER TABLE `elementy_plytkowe`
  ADD CONSTRAINT `urzaplytkofg1` FOREIGN KEY (`plytka_id`) REFERENCES `plytki` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `elementy_plytkowe_pin`
--
ALTER TABLE `elementy_plytkowe_pin`
  ADD CONSTRAINT `elementy_plytkowe_pin_ibfk_1` FOREIGN KEY (`element_plytkowy_id`) REFERENCES `elementy_plytkowe` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ograniczenia dla tabeli `miejsce`
--
ALTER TABLE `miejsce`
  ADD CONSTRAINT `miejsce_pom_fgkey` FOREIGN KEY (`id_pomieszczenie`) REFERENCES `pomieszczenie` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `plytki`
--
ALTER TABLE `plytki`
  ADD CONSTRAINT `plytkimiejfg1` FOREIGN KEY (`miejsce_id`) REFERENCES `miejsce` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `polaczenie_plytka`
--
ALTER TABLE `polaczenie_plytka`
  ADD CONSTRAINT `polaczenie_plytka_ibfk_1` FOREIGN KEY (`plytka_id`) REFERENCES `plytki` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `polaczenie_plytka_polaczenie`
--
ALTER TABLE `polaczenie_plytka_polaczenie`
  ADD CONSTRAINT `polnazwaplytkafg` FOREIGN KEY (`polaczenie_plytka_id`) REFERENCES `polaczenie_plytka` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `polpolplytkapinfg` FOREIGN KEY (`elementy_plytkowe_piny_id`) REFERENCES `elementy_plytkowe_pin` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `polaczenie_zyla`
--
ALTER TABLE `polaczenie_zyla`
  ADD CONSTRAINT `polzylazylafg` FOREIGN KEY (`zyla_id`) REFERENCES `zyla` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `przewod_miejsce`
--
ALTER TABLE `przewod_miejsce`
  ADD CONSTRAINT `pmmiefg` FOREIGN KEY (`miejsce_id`) REFERENCES `miejsce` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `pmprzefg` FOREIGN KEY (`przewod_id`) REFERENCES `przewod` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `zakonczenie`
--
ALTER TABLE `zakonczenie`
  ADD CONSTRAINT `zaprmifg` FOREIGN KEY (`przewod_miejsce_id`) REFERENCES `przewod_miejsce` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `zarozlfg` FOREIGN KEY (`rodzaj_zakonczenia`) REFERENCES `rodzaj_zakonczenia` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `zlacze_wtyczka`
--
ALTER TABLE `zlacze_wtyczka`
  ADD CONSTRAINT `zlawtyczzlafg` FOREIGN KEY (`wtyczka_id`) REFERENCES `zakonczenie` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `zlawtyzlafg` FOREIGN KEY (`zlacze_id`) REFERENCES `elementy_plytkowe` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ograniczenia dla tabeli `zyla`
--
ALTER TABLE `zyla`
  ADD CONSTRAINT `zyla_kolfk_1` FOREIGN KEY (`kolor_id`) REFERENCES `kolor` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `zyla_przfk_2` FOREIGN KEY (`przewod_id`) REFERENCES `przewod` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;