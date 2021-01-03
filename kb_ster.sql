-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Czas generowania: 03 Sty 2021, 23:57
-- Wersja serwera: 8.0.22-0ubuntu0.20.04.3
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
,`element_plytkowy_id` tinyint unsigned
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
,`element_plytkowy_id` tinyint unsigned
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
`id` tinyint unsigned
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
  `id` tinyint UNSIGNED NOT NULL,
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
(10, 'Arduino pro micro 16 MHz 5V', 24, 2, 3);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `elementy_plytkowe_pin`
--

CREATE TABLE `elementy_plytkowe_pin` (
  `id` smallint UNSIGNED NOT NULL,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `pos` tinyint NOT NULL,
  `element_plytkowy_id` tinyint UNSIGNED NOT NULL
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
(90, '10 (A10)', 24, 10);

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
(5, 'Płytka rozdzielcza', 23);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `PolaczenieZylaWidok`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `PolaczenieZylaWidok` (
);

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
(27, '', 2),
(28, 'CPU9', 2);

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
(63, 28, 34);

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
(145, 'Lazienka - kabel w puszcze do włacznikow', 10),
(146, 'Lazienka, pokoje kabel do wlacznikow', 10),
(147, 'WC procesor, zasilanie i i2c układu wejścia/wyjścia 0x01', 4),
(148, 'WC procesor, zasilanie i i2c układu wejścia/wyjścia 0x00', 4),
(149, 'WC sufit zasilanie 4 przekaźników', 6),
(150, 'WC sufit, zasilanie 2 przekaźników', 4),
(151, 'Rozdzielnia pokój, zasilanie i i2c dla expnadera 0x100', 4),
(152, 'Rozdzielnia pokój, zasilanie i i2c dla przekaźników oświetlenia.', 8),
(153, 'Zasilanie i sterowanie przekażnikami ogrzewania', 10),
(154, 'Zasialnie przekaźników dla wiatrakó', 4),
(155, 'Zasialnie przekaźników do gniazd', 10),
(156, 'Zasialnie przekaźników dla oświetlania', 10),
(157, 'Zasilanie expander 0x100 i kabli 77 i 78', 8),
(158, 'Zasilanie konwertetów RS232<->TTL', 4),
(159, 'RS232 (WC)', 4),
(160, 'RS232 x2', 4),
(161, 'RS232x2', 4),
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
(6, 2, 20),
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
(317, 158, 1),
(318, 158, 1),
(319, 159, 1),
(320, 159, 1),
(321, 160, 1),
(322, 160, 1),
(323, 161, 1),
(324, 161, 1);

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
  `rodzaj_zakonczenia` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `zakonczenie`
--

INSERT INTO `zakonczenie` (`id`, `etykieta`, `przewod_miejsce_id`, `rodzaj_zakonczenia`) VALUES
(1, 'O', 41, 1),
(2, 'J', 49, 1),
(3, 'M', 51, 1),
(4, 'B', 53, 1),
(5, 'C', 55, 1),
(6, 'G', 57, 1),
(7, 'I', 65, 1),
(8, 'E', 68, 1),
(9, 'A', 70, 1),
(10, 'P', 72, 1),
(11, 'D', 74, 1),
(12, 'N', 76, 1),
(13, 'H', 79, 1),
(14, 'L', 81, 1),
(15, 'K', 97, 1),
(16, 'A', 50, 1),
(17, 'F', 99, 1),
(18, 'B', 299, 1),
(19, 'C', 301, 1),
(20, 'A', 78, 1),
(21, 'B', 108, 1),
(22, 'C', 303, 1),
(23, 'D', 305, 1),
(24, 'F', 307, 1),
(25, 'G', 309, 1),
(26, 'H', 311, 1),
(27, 'I', 313, 1),
(28, 'Q', 296, 1),
(29, 'R', 298, 1),
(30, '20-21-22', 42, 2),
(31, '20-21-22', 43, 2),
(32, '20-21-22', 45, 2),
(33, '7-8-9-10-11-12-19', 16, 2),
(34, '7-8-9-10-11-12-19', 18, 2),
(35, '7-8-9-10-11-12-19', 19, 2),
(36, '7-8-9-10-11-12-19', 21, 2),
(37, '7-8-9-10-11-12-19', 24, 2),
(38, '7-8-9-10-11-12-19', 25, 2),
(39, '7-8-9-10-11-12-19', 39, 2),
(40, '13-14-15-16', 28, 2),
(41, '13-14-15-16', 29, 2),
(42, '13-14-15-16', 32, 2),
(43, '13-14-15-16', 33, 2),
(44, 'Czujnik temperatury w podłodze w WC', 66, 3),
(45, '42-43-44-45-46-47', 86, 2),
(46, '42-43-44-45-46-47', 88, 2),
(48, '42-43-44-45-46-47', 90, 2),
(49, '42-43-44-45-46-47', 91, 2),
(50, '42-43-44-45-46-47', 93, 2),
(51, '42-43-44-45-46-47', 95, 2),
(52, 'Czujnik temperatury ogrz. wodne ściana w salonie', 20, 3),
(53, 'Czujnik temperatury ogrz. wodnego podłoga w kuchni', 22, 3),
(54, 'Czujnik temperatury ogrz. wodnego podłoga w łazience', 23, 3),
(55, 'Czujnik temperatury przy pompie', 26, 3),
(56, 'Kontaktron od drzwiczek rewizyjnych', 40, 3),
(57, 'Czujnik ruchu WC', 54, 3),
(58, 'Czujnik temperatury w podłodze w Holu', 67, 3);

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
(122, 20, 323, 1, '1'),
(123, 20, 322, 2, '2'),
(124, 20, 321, 3, '3'),
(125, 20, 320, 4, '4'),
(126, 20, 319, 5, '5'),
(127, 20, 318, 6, '6'),
(128, 20, 317, 7, '7'),
(129, 20, 316, 8, '8'),
(130, 21, 328, 1, '1'),
(131, 21, 329, 2, '2'),
(132, 21, 330, 3, '3'),
(133, 21, 331, 4, '4'),
(134, 21, 332, 5, '5'),
(135, 21, 333, 6, '6'),
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
(287, 49, 426, 2, 'Kontakt. pracownia');

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
(147, 5, 93, 'Czujnik ruhu  drzwi'),
(148, 6, 93, 'Czujnike ruchu kuchnia'),
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
(221, 6, 1, 'Lampka 1'),
(222, 1, 1, 'Lampka 2'),
(223, 3, 1, 'Lampka 3'),
(224, 9, 1, 'Lampka 4'),
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
(316, 9, 38, 'kanał 8 - zasilanie pompy'),
(317, 7, 38, 'kanał 7 - sterowanie term. kuchnia/łazienka/salon'),
(318, 1, 38, 'kanał 6 - sterowanie term. kuchnia/łazienka/salon'),
(319, 5, 38, 'kanał 5 - sterowanie term. kuchnia/łazienka/salon'),
(320, 6, 38, 'kanał 4 - sterowanie oświetleniem pod wanną'),
(321, 8, 38, 'kanał 3 - termostat kaloryfer'),
(322, 3, 38, 'kanał 2 - oświetlenie kwiatów prysznic'),
(323, 4, 38, 'kanał 1 - oświetlenie kwiatów wanna'),
(324, 2, 151, '+5V'),
(325, 9, 151, 'SDA'),
(326, 3, 151, 'SCL'),
(327, 6, 151, 'GND'),
(328, 6, 53, 'GND'),
(329, 4, 53, '+5V'),
(330, 3, 53, 'Kanał 1 - wiatrak 1'),
(331, 1, 53, 'Kanał 2 - wiatrak 2'),
(332, 9, 53, '-'),
(333, 8, 53, '-'),
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
(345, 8, 152, '53.żółty'),
(346, 4, 152, '+5V'),
(347, 3, 152, 'SCL'),
(348, 9, 152, 'SDA'),
(349, 7, 152, 'GND'),
(350, 6, 152, 'GND'),
(351, 5, 152, '+5Vp (dla przekaźników)'),
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
(379, 1, 52, 'Sygnał wieczoru'),
(380, 3, 52, 'TX'),
(381, 9, 52, 'RX'),
(382, 5, 52, '-'),
(383, 6, 52, '-'),
(384, 6, 54, '-'),
(385, 4, 54, '-'),
(386, 1, 54, '-'),
(387, 3, 54, '-'),
(388, 8, 54, '-'),
(389, 9, 54, '-'),
(390, 4, 157, '+5V '),
(391, 7, 157, 'GND'),
(392, 3, 157, 'SCL'),
(393, 9, 157, 'SDA'),
(394, 1, 157, '-'),
(395, 8, 157, '-'),
(396, 6, 157, '-'),
(397, 5, 157, '-'),
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
(433, 1, 47, 'GND');

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
-- Struktura widoku `PolaczenieZylaWidok`
--
DROP TABLE IF EXISTS `PolaczenieZylaWidok`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `PolaczenieZylaWidok`  AS  select `polaczenie_zyla`.`id` AS `id`,`polaczenie_zyla`.`zyla_id_1` AS `zyla_id_1`,`polaczenie_zyla`.`zyla_id_2` AS `zyla_id_2`,`polaczenie_zyla`.`zakonczenie_id` AS `zakonczenie_id`,`z1`.`przewod_id` AS `przewod_id1`,`z1`.`opis` AS `opis1`,`z1`.`kolor` AS `kolor1`,`z1`.`html` AS `html1`,`z2`.`przewod_id` AS `przewod_id2`,`z2`.`opis` AS `opis2`,`z2`.`kolor` AS `kolor2`,`z2`.`html` AS `html2` from ((`polaczenie_zyla` left join `ZylaWidok` `z1` on((`z1`.`id` = `polaczenie_zyla`.`zyla_id_1`))) left join `ZylaWidok` `z2` on((`z2`.`id` = `polaczenie_zyla`.`zyla_id_2`))) ;

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

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZakonczenieView`  AS  select `zakonczenie`.`id` AS `id`,`zakonczenie`.`etykieta` AS `etykieta`,`zakonczenie`.`przewod_miejsce_id` AS `przewod_miejsce_id`,`zakonczenie`.`rodzaj_zakonczenia` AS `rodzaj_zakonczenia`,`przewod_miejsce`.`przewod_id` AS `przewod_id`,`przewod_miejsce`.`miejsce_id` AS `miejsce_id`,`rodzaj_zakonczenia`.`nazwa` AS `nazwa`,`rodzaj_zakonczenia`.`kod` AS `kod` from ((`zakonczenie` left join `przewod_miejsce` on((`przewod_miejsce`.`id` = `zakonczenie`.`przewod_miejsce_id`))) left join `rodzaj_zakonczenia` on((`rodzaj_zakonczenia`.`id` = `zakonczenie`.`rodzaj_zakonczenia`))) ;

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

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZakonczePrzewodMiejsce`  AS  select `ZakonczenieView`.`id` AS `zid`,`ZakonczenieView`.`etykieta` AS `etykieta`,`ZakonczenieView`.`przewod_miejsce_id` AS `przewod_miejsce_id`,`ZakonczenieView`.`rodzaj_zakonczenia` AS `rodzaj_zakonczenia`,`ZakonczenieView`.`przewod_id` AS `przewod_id`,`ZakonczenieView`.`miejsce_id` AS `miejsce_id`,`ZakonczenieView`.`nazwa` AS `znazwa`,`ZakonczenieView`.`kod` AS `zkod`,`MiejsceView`.`nazwa` AS `mnazwa`,`MiejsceView`.`opis` AS `mopis`,`MiejsceView`.`zbiorcze` AS `zbiorcze`,`MiejsceView`.`kod` AS `mkod`,`MiejsceView`.`polaczenie` AS `polaczenie`,`MiejsceView`.`pomieszczenie` AS `pomieszczenie`,`przewod`.`opis` AS `popis`,`przewod`.`ilosc_zyl` AS `ilosc_zyl` from ((`ZakonczenieView` left join `MiejsceView` on((`MiejsceView`.`id` = `ZakonczenieView`.`miejsce_id`))) left join `przewod` on((`przewod`.`id` = `ZakonczenieView`.`przewod_id`))) where (0 <> 1) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZewnetrzneKableView`
--
DROP TABLE IF EXISTS `ZewnetrzneKableView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZewnetrzneKableView`  AS  select `przewod_miejsce`.`przewod_id` AS `przewod_id`,`przewod_miejsce`.`miejsce_id` AS `miejsce_id`,count(`przewod_miejsce`.`przewod_id`) AS `c` from `przewod_miejsce` group by `przewod_miejsce`.`miejsce_id`,`przewod_miejsce`.`przewod_id` having (`c` = 1) ;

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
  MODIFY `id` tinyint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT dla tabeli `elementy_plytkowe_pin`
--
ALTER TABLE `elementy_plytkowe_pin`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=91;

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
  MODIFY `id` tinyint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `polaczenie_plytka`
--
ALTER TABLE `polaczenie_plytka`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT dla tabeli `polaczenie_plytka_polaczenie`
--
ALTER TABLE `polaczenie_plytka_polaczenie`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

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
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=325;

--
-- AUTO_INCREMENT dla tabeli `rodzaj_zakonczenia`
--
ALTER TABLE `rodzaj_zakonczenia`
  MODIFY `id` tinyint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `zakonczenie`
--
ALTER TABLE `zakonczenie`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT dla tabeli `zakonczenie_zyly`
--
ALTER TABLE `zakonczenie_zyly`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=288;

--
-- AUTO_INCREMENT dla tabeli `zyla`
--
ALTER TABLE `zyla`
  MODIFY `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=434;

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
-- Ograniczenia dla tabeli `zyla`
--
ALTER TABLE `zyla`
  ADD CONSTRAINT `zyla_kolfk_1` FOREIGN KEY (`kolor_id`) REFERENCES `kolor` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `zyla_przfk_2` FOREIGN KEY (`przewod_id`) REFERENCES `przewod` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;