-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Czas generowania: 27 Lis 2020, 06:14
-- Wersja serwera: 5.7.32
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
-- Baza danych: `kb_ster`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `kolor`
--

CREATE TABLE `kolor` (
  `id` tinyint(4) UNSIGNED NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `html` text CHARACTER SET ascii NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `kolor`
--

INSERT INTO `kolor` (`id`, `name`, `html`) VALUES
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
(13, 'Różowy', 'fuchsia');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `KolorView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `KolorView` (
`id` tinyint(4) unsigned
,`name` varchar(20)
,`html` text
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `miejsce`
--

CREATE TABLE `miejsce` (
  `id` tinyint(3) UNSIGNED NOT NULL,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `zbiorcze` tinyint(1) NOT NULL,
  `id_pomieszczenie` tinyint(3) UNSIGNED NOT NULL,
  `kod` varchar(16) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  `polaczenie` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `miejsce`
--

INSERT INTO `miejsce` (`id`, `name`, `description`, `zbiorcze`, `id_pomieszczenie`, `kod`, `polaczenie`) VALUES
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
(27, 'Rozdzielnia przy pompie wody', 'Łazienka, umieszczona za wanną. ', 1, 8, 'LAZ-POMPA', 0),
(28, 'Rozdzielnia sypialnia', 'Umieszczona w sypialni na ścianie z przedpokojem po lewej stronie w rogu ze ścianą od salonu', 1, 3, 'SYP-ROZD', 0),
(29, 'Grzejnik jadalnia', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w jadalni', 0, 9, 'JAD-GRZEJNIK', 0),
(30, 'Gniazda 230V pokój', 'Umieszczone na ścianie z salonem pod oknem i na ścianie na naprzeciwko bliżej okna i bliżej łazienki. ', 0, 4, 'POK-GNIAZDA', 0),
(31, 'Grzejnik pracownia', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w pracowni', 0, 5, 'PRAC-GRZEJNIK', 0),
(32, 'Grzejnik salon', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w salonie', 0, 6, 'SAL-GRZEJNIK', 0),
(33, 'Grzejnik sypialnia', 'Zasilanie termostatu i czujnik temperatury przy grzejniku w sypialni', 0, 3, 'SYP-GRZEJNIK', 0),
(34, 'Sciana w holu z drzwiami od pokojów', 'Sciana w holu z drzwiami od pokojów', 0, 1, 'HOL-SC_POKOJE', 0),
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
(91, 'Łazienka, ściana z drzwiami', 'Łazienka, ściana z drzwiami obok wanny', 0, 8, 'LAZ-SC_DRZWI', 0),
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
`id` tinyint(3) unsigned
,`name` varchar(64)
,`description` varchar(255)
,`zbiorcze` tinyint(1)
,`id_pomieszczenie` tinyint(3) unsigned
,`kod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` varchar(25)
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `polaczenie`
--

CREATE TABLE `polaczenie` (
  `id` smallint(11) NOT NULL,
  `miejsce_id` tinyint(3) NOT NULL,
  `opis` varchar(64) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `polaczenie`
--

INSERT INTO `polaczenie` (`id`, `miejsce_id`, `opis`) VALUES
(1, 105, 'Połączenie przewodu 20 i 21');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `PolaczenieView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `PolaczenieView` (
`pid` smallint(11)
,`miejsce_id` tinyint(3)
,`opis` varchar(64)
,`mid` tinyint(3) unsigned
,`name` varchar(64)
,`description` varchar(255)
,`zbiorcze` tinyint(1)
,`id_pomieszczenie` tinyint(3) unsigned
,`kod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` varchar(25)
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `polaczenie_zyla`
--

CREATE TABLE `polaczenie_zyla` (
  `id` smallint(6) NOT NULL,
  `polaczenie_id` smallint(6) NOT NULL,
  `zyla_id_1` smallint(6) NOT NULL,
  `zyla_id_2` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `polaczenie_zyla`
--

INSERT INTO `polaczenie_zyla` (`id`, `polaczenie_id`, `zyla_id_1`, `zyla_id_2`) VALUES
(1, 1, 4, 400),
(2, 1, 400, 4),
(3, 1, 1, 398),
(4, 1, 398, 1),
(5, 1, 2, 399),
(6, 1, 399, 2),
(7, 1, 3, 401),
(8, 1, 401, 3),
(9, 1, 5, 404),
(10, 1, 404, 5),
(11, 1, 6, 402),
(12, 1, 402, 6),
(13, 1, 7, 405),
(14, 1, 405, 7),
(15, 1, 8, 403),
(16, 1, 403, 8);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pomieszczenie`
--

CREATE TABLE `pomieszczenie` (
  `id` tinyint(3) UNSIGNED NOT NULL,
  `name` varchar(25) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `pomieszczenie`
--

INSERT INTO `pomieszczenie` (`id`, `name`) VALUES
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
  `id` tinyint(3) UNSIGNED NOT NULL,
  `description` varchar(250) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `ilosc_zyl` tinyint(3) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `przewod`
--

INSERT INTO `przewod` (`id`, `description`, `ilosc_zyl`) VALUES
(0, 'Zasilanie +24V, impulsy od licznika energi', 8),
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
(43, 'Hol, czujnik ruchu w Holu umieszczony nad drzwiami do pokoju. Kabel powiązany z 42', 3),
(44, 'Pracowania, czujnik ruchu nad drzwiami. Kabel powiązany z 42', 3),
(45, 'Pracowania, kontaktron w drzwiach. Kabel powiązany z 42', 2),
(46, 'Pokoj, czujnik ruchu umieszczony nad drzwiami. Kabel powiązany z 42', 3),
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
(157, 'Zasilanie expander 0x100 i kabli 77 i 78', 8);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `PrzewodyView`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `PrzewodyView` (
`id` smallint(6) unsigned
,`kabel_id` tinyint(3) unsigned
,`miejsce_id` tinyint(3) unsigned
,`name` varchar(64)
,`description` varchar(255)
,`zbiorcze` tinyint(1)
,`id_pomieszczenia` tinyint(3) unsigned
,`kod` varchar(16)
,`polaczenie` tinyint(1)
,`pomieszczenie` varchar(25)
,`pdescription` varchar(250)
,`ilosc_zyl` tinyint(3) unsigned
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `przewod_miejsce`
--

CREATE TABLE `przewod_miejsce` (
  `id` smallint(6) UNSIGNED NOT NULL,
  `kabel_id` tinyint(3) UNSIGNED NOT NULL,
  `miejsce_id` tinyint(3) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=ascii COLLATE=ascii_bin;

--
-- Zrzut danych tabeli `przewod_miejsce`
--

INSERT INTO `przewod_miejsce` (`id`, `kabel_id`, `miejsce_id`) VALUES
(1, 0, 1),
(2, 0, 25),
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
(90, 44, 36),
(91, 45, 34),
(92, 45, 36),
(93, 46, 34),
(94, 46, 35),
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
(316, 157, 26);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `urzadzenie_zyla`
--

CREATE TABLE `urzadzenie_zyla` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `urzadzenie_id` smallint(5) UNSIGNED NOT NULL,
  `nazwa` varchar(200) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `pos` tinyint(4) NOT NULL,
  `zyla_id` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `urządzenia`
--

CREATE TABLE `urządzenia` (
  `id` smallint(11) NOT NULL,
  `miejsce_id` smallint(11) NOT NULL,
  `opis` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `urządzenia`
--

INSERT INTO `urządzenia` (`id`, `miejsce_id`, `opis`) VALUES
(1, 2, 'GND wspolna masa'),
(2, 2, '5V oswietlenia'),
(3, 2, '5V ogrzewanie'),
(4, 2, 'Przetwornica 24/5 oświetlenie'),
(5, 2, 'Expander portów I/O 0x00'),
(6, 2, 'Expander portów I/O 0x01'),
(7, 2, 'Mikrokontroler'),
(8, 2, 'Przekaźniki ogrzewania 2x'),
(9, 2, 'Czujnik temperatury DS1820'),
(10, 2, 'Złączka przewodów 230V');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `WewnetrzneKableView`
-- (Zobacz poniżej rzeczywisty widok)
--
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
CREATE TABLE `ZlaczaView` (
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zlacze`
--

CREATE TABLE `zlacze` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `etykieta` varchar(10) NOT NULL,
  `przewod_miejsce_id` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `zlacze`
--

INSERT INTO `zlacze` (`id`, `etykieta`, `przewod_miejsce_id`) VALUES
(1, 'O', 41),
(2, 'J', 49),
(3, 'M', 51),
(4, 'B', 53),
(5, 'C', 55),
(6, 'G', 57),
(7, 'I', 65),
(8, 'E', 68),
(9, 'A', 70),
(10, 'P', 72),
(11, 'D', 74),
(12, 'N', 76),
(13, 'H', 79),
(14, 'L', 81),
(15, 'K', 97),
(16, 'A', 50),
(17, 'F', 99),
(18, 'B', 299),
(19, 'C', 301),
(20, 'A', 78),
(21, 'B', 108),
(22, 'C', 303),
(23, 'D', 305),
(24, 'F', 307),
(25, 'G', 309),
(26, 'H', 311),
(27, 'I', 313);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZlaczePrzewodView`
-- (Zobacz poniżej rzeczywisty widok)
--
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

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zlacze_kolejnosc`
--

CREATE TABLE `zlacze_kolejnosc` (
  `id` int(11) UNSIGNED NOT NULL,
  `zlacze_id` smallint(5) UNSIGNED NOT NULL,
  `zyla_id` smallint(5) UNSIGNED NOT NULL,
  `pos` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `zlacze_kolejnosc`
--

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
(181, 27, 375, 10);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zyla`
--

CREATE TABLE `zyla` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `color_id` tinyint(3) UNSIGNED NOT NULL,
  `przewod_id` tinyint(3) UNSIGNED NOT NULL,
  `opis` varchar(50) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `zyla`
--

INSERT INTO `zyla` (`id`, `color_id`, `przewod_id`, `opis`) VALUES
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
(47, 1, 34, 'Sygnał dla wiatraka'),
(48, 8, 34, 'Sygnał zapalonego światła'),
(49, 8, 35, 'user 1'),
(50, 1, 35, 'user 2'),
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
(80, 6, 48, 'User 1'),
(81, 9, 48, 'User 2'),
(82, 2, 48, '-'),
(83, 10, 48, '-'),
(84, 12, 48, 'Sygnał od lokalnego czujnika temperatury'),
(85, 7, 48, 'Pin1 do gabarytu'),
(86, 11, 48, 'Pin2 do gabarytu'),
(87, 4, 48, 'Pin3 do gabarytu'),
(88, 5, 48, 'Przekaźnik 4 (zawór)'),
(89, 3, 48, 'Przekaźnik 3 (lustro)'),
(90, 1, 48, 'Przekaźnik 2 (światło)'),
(91, 8, 48, 'Przekaźnik 1 (regał)'),
(92, 11, 49, 'Sygnał wejściowy czujnika ruchu'),
(93, 12, 49, 'Sygnał wejściowy czujnika zbliżeniowego'),
(94, 10, 49, 'Sygnał wejściowy kontaktron'),
(95, 2, 49, 'Sygnałwejściowy klawisza włącznika światła'),
(96, 4, 49, '+5V'),
(97, 8, 49, 'Sygnał wyjściowy światło'),
(98, 1, 49, 'Sygnał wyjściowy wiatrak'),
(99, 5, 49, 'Sygnał wejściowy wieczoru'),
(100, 6, 49, 'Sygnał wejściowy nocy'),
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
(264, 0, 7, 'Sygnał czujnika temperatury'),
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
(405, 1, 22, '');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZylaWidok`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `ZylaWidok` (
`id` smallint(5) unsigned
,`color_id` tinyint(3) unsigned
,`przewod_id` tinyint(3) unsigned
,`opis` varchar(50)
,`name` varchar(20)
,`html` text
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `ZylaZlaczeKolejnoscView`
-- (Zobacz poniżej rzeczywisty widok)
--
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
-- Struktura widoku `KolorView`
--
DROP TABLE IF EXISTS `KolorView`;

CREATE ALGORITHM=TEMPTABLE DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `KolorView`  AS  select `kolor`.`id` AS `id`,`kolor`.`name` AS `name`,`kolor`.`html` AS `html` from `kolor` order by `kolor`.`name` ;

-- --------------------------------------------------------

--
-- Struktura widoku `MiejsceView`
--
DROP TABLE IF EXISTS `MiejsceView`;

CREATE ALGORITHM=TEMPTABLE DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `MiejsceView`  AS  select `miejsce`.`id` AS `id`,`miejsce`.`name` AS `name`,`miejsce`.`description` AS `description`,`miejsce`.`zbiorcze` AS `zbiorcze`,`miejsce`.`id_pomieszczenie` AS `id_pomieszczenie`,`miejsce`.`kod` AS `kod`,`miejsce`.`polaczenie` AS `polaczenie`,`pomieszczenie`.`name` AS `pomieszczenie` from (`miejsce` left join `pomieszczenie` on((`miejsce`.`id_pomieszczenie` = `pomieszczenie`.`id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `PolaczenieView`
--
DROP TABLE IF EXISTS `PolaczenieView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `PolaczenieView`  AS  select `p`.`id` AS `pid`,`p`.`miejsce_id` AS `miejsce_id`,`p`.`opis` AS `opis`,`m`.`id` AS `mid`,`m`.`name` AS `name`,`m`.`description` AS `description`,`m`.`zbiorcze` AS `zbiorcze`,`m`.`id_pomieszczenie` AS `id_pomieszczenie`,`m`.`kod` AS `kod`,`m`.`polaczenie` AS `polaczenie`,`m`.`pomieszczenie` AS `pomieszczenie` from (`polaczenie` `p` left join `MiejsceView` `m` on((`p`.`miejsce_id` = `m`.`id`))) where 1 ;

-- --------------------------------------------------------

--
-- Struktura widoku `PrzewodyView`
--
DROP TABLE IF EXISTS `PrzewodyView`;

CREATE ALGORITHM=TEMPTABLE DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `PrzewodyView`  AS  select `pm`.`id` AS `id`,`pm`.`kabel_id` AS `kabel_id`,`pm`.`miejsce_id` AS `miejsce_id`,`m`.`name` AS `name`,`m`.`description` AS `description`,`m`.`zbiorcze` AS `zbiorcze`,`m`.`id_pomieszczenie` AS `id_pomieszczenia`,`m`.`kod` AS `kod`,`m`.`polaczenie` AS `polaczenie`,`m`.`pomieszczenie` AS `pomieszczenie`,`p`.`description` AS `pdescription`,`p`.`ilosc_zyl` AS `ilosc_zyl` from ((`przewod_miejsce` `pm` left join `MiejsceView` `m` on((`m`.`id` = `pm`.`miejsce_id`))) left join `przewod` `p` on((`p`.`id` = `pm`.`kabel_id`))) order by `pm`.`kabel_id` ;

-- --------------------------------------------------------

--
-- Struktura widoku `WewnetrzneKableView`
--
DROP TABLE IF EXISTS `WewnetrzneKableView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `WewnetrzneKableView`  AS  select `przewod_miejsce`.`kabel_id` AS `kabel_id`,`przewod_miejsce`.`miejsce_id` AS `miejsce_id`,count(`przewod_miejsce`.`kabel_id`) AS `c` from `przewod_miejsce` group by `przewod_miejsce`.`miejsce_id`,`przewod_miejsce`.`kabel_id` having (`c` = 2) ;

-- --------------------------------------------------------

--
-- Struktura widoku `ZewnetrzneKableView`
--
DROP TABLE IF EXISTS `ZewnetrzneKableView`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZewnetrzneKableView`  AS  select `przewod_miejsce`.`kabel_id` AS `kabel_id`,`przewod_miejsce`.`miejsce_id` AS `miejsce_id`,count(`przewod_miejsce`.`kabel_id`) AS `c` from `przewod_miejsce` group by `przewod_miejsce`.`miejsce_id`,`przewod_miejsce`.`kabel_id` having (`c` = 1) ;

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
-- Struktura widoku `ZylaWidok`
--
DROP TABLE IF EXISTS `ZylaWidok`;

CREATE ALGORITHM=UNDEFINED DEFINER=`phpmyadmin`@`localhost` SQL SECURITY DEFINER VIEW `ZylaWidok`  AS  select `z`.`id` AS `id`,`z`.`color_id` AS `color_id`,`z`.`przewod_id` AS `przewod_id`,`z`.`opis` AS `opis`,`k`.`name` AS `name`,`k`.`html` AS `html` from (`zyla` `z` left join `kolor` `k` on((`k`.`id` = `z`.`color_id`))) where 1 order by `k`.`name` ;

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
  ADD KEY `pMiejscePol` (`polaczenie`);

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
  ADD KEY `zyla_id_1` (`zyla_id_1`),
  ADD KEY `polaczenie_id` (`polaczenie_id`) USING BTREE,
  ADD KEY `zyla_id_2` (`zyla_id_2`);

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
  ADD KEY `kbididx` (`kabel_id`),
  ADD KEY `miididx` (`miejsce_id`);

--
-- Indeksy dla tabeli `urzadzenie_zyla`
--
ALTER TABLE `urzadzenie_zyla`
  ADD PRIMARY KEY (`id`),
  ADD KEY `zyla_id` (`zyla_id`);

--
-- Indeksy dla tabeli `urządzenia`
--
ALTER TABLE `urządzenia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `miejsce_id` (`miejsce_id`);

--
-- Indeksy dla tabeli `zlacze`
--
ALTER TABLE `zlacze`
  ADD PRIMARY KEY (`id`),
  ADD KEY `przewod_miejsce_id` (`przewod_miejsce_id`);

--
-- Indeksy dla tabeli `zlacze_kolejnosc`
--
ALTER TABLE `zlacze_kolejnosc`
  ADD PRIMARY KEY (`id`),
  ADD KEY `zlacze_id` (`zlacze_id`),
  ADD KEY `zyla_id` (`zyla_id`);

--
-- Indeksy dla tabeli `zyla`
--
ALTER TABLE `zyla`
  ADD PRIMARY KEY (`id`),
  ADD KEY `color_id` (`color_id`),
  ADD KEY `przewod_id` (`przewod_id`);

--
-- AUTO_INCREMENT dla tabel zrzutów
--

--
-- AUTO_INCREMENT dla tabeli `kolor`
--
ALTER TABLE `kolor`
  MODIFY `id` tinyint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT dla tabeli `miejsce`
--
ALTER TABLE `miejsce`
  MODIFY `id` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT dla tabeli `polaczenie`
--
ALTER TABLE `polaczenie`
  MODIFY `id` smallint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `polaczenie_zyla`
--
ALTER TABLE `polaczenie_zyla`
  MODIFY `id` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT dla tabeli `pomieszczenie`
--
ALTER TABLE `pomieszczenie`
  MODIFY `id` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT dla tabeli `przewod`
--
ALTER TABLE `przewod`
  MODIFY `id` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=158;

--
-- AUTO_INCREMENT dla tabeli `przewod_miejsce`
--
ALTER TABLE `przewod_miejsce`
  MODIFY `id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=317;

--
-- AUTO_INCREMENT dla tabeli `urzadzenie_zyla`
--
ALTER TABLE `urzadzenie_zyla`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `urządzenia`
--
ALTER TABLE `urządzenia`
  MODIFY `id` smallint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT dla tabeli `zlacze`
--
ALTER TABLE `zlacze`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT dla tabeli `zlacze_kolejnosc`
--
ALTER TABLE `zlacze_kolejnosc`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=182;

--
-- AUTO_INCREMENT dla tabeli `zyla`
--
ALTER TABLE `zyla`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=406;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `miejsce`
--
ALTER TABLE `miejsce`
  ADD CONSTRAINT `pomieszczenie_fgkey` FOREIGN KEY (`id_pomieszczenie`) REFERENCES `pomieszczenie` (`id`);

--
-- Ograniczenia dla tabeli `polaczenie_zyla`
--
ALTER TABLE `polaczenie_zyla`
  ADD CONSTRAINT `polzylfg` FOREIGN KEY (`polaczenie_id`) REFERENCES `polaczenie` (`id`);

--
-- Ograniczenia dla tabeli `przewod_miejsce`
--
ALTER TABLE `przewod_miejsce`
  ADD CONSTRAINT `kidfg` FOREIGN KEY (`kabel_id`) REFERENCES `przewod` (`id`),
  ADD CONSTRAINT `midfg` FOREIGN KEY (`miejsce_id`) REFERENCES `miejsce` (`id`);

--
-- Ograniczenia dla tabeli `zlacze_kolejnosc`
--
ALTER TABLE `zlacze_kolejnosc`
  ADD CONSTRAINT `fkkol_fg1` FOREIGN KEY (`zlacze_id`) REFERENCES `zlacze` (`id`),
  ADD CONSTRAINT `fkkol_fg2` FOREIGN KEY (`zyla_id`) REFERENCES `zyla` (`id`);

--
-- Ograniczenia dla tabeli `zyla`
--
ALTER TABLE `zyla`
  ADD CONSTRAINT `zyla_ibfk_1` FOREIGN KEY (`color_id`) REFERENCES `kolor` (`id`),
  ADD CONSTRAINT `zyla_ibfk_2` FOREIGN KEY (`przewod_id`) REFERENCES `przewod` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
