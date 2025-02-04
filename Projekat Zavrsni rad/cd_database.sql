-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 13, 2024 at 11:45 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cd_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `porudzbine`
--

CREATE TABLE `porudzbine` (
  `broj_stola` int(4) NOT NULL,
  `naziv_proizvoda` varchar(120) NOT NULL,
  `cena_proizvoda` double(32,2) NOT NULL,
  `kolicina` int(4) NOT NULL,
  `ukupna_cena` double(32,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `proizvodi`
--

CREATE TABLE `proizvodi` (
  `sifra_proizvoda` int(4) NOT NULL,
  `naziv_proizvoda` varchar(200) DEFAULT NULL,
  `cena_proizvoda` float(32,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `proizvodi`
--

INSERT INTO `proizvodi` (`sifra_proizvoda`, `naziv_proizvoda`, `cena_proizvoda`) VALUES
(8001, 'Espresso', 200.00),
(8002, 'Machiato', 210.00),
(8003, 'Espresso sa mlekom', 245.00),
(8004, 'Kapucino', 280.00),
(8005, 'Latte', 280.00),
(8006, 'Moka', 320.00),
(8007, 'Krem kafa', 320.00),
(8008, 'Krem kafa sa ukusima', 350.00),
(8009, 'Late machiato', 300.00),
(8010, 'Cedjena pomoradnza', 350.00),
(8011, 'Cedjeni grejp', 380.00),
(8012, 'Cedjeni ananas', 450.00),
(8013, 'Limunada', 230.00),
(8014, 'Cedjeni mix', 400.00),
(8016, 'Cedjena jabuka', 320.00);

-- --------------------------------------------------------

--
-- Table structure for table `sirovine`
--

CREATE TABLE `sirovine` (
  `sifra_artikla` int(4) NOT NULL,
  `ime_artikla` varchar(200) DEFAULT NULL,
  `cena_artikla_po_jedinici_mere` float(32,2) DEFAULT NULL,
  `kolicina_artikala` float(32,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `sirovine`
--

INSERT INTO `sirovine` (`sifra_artikla`, `ime_artikla`, `cena_artikla_po_jedinici_mere`, `kolicina_artikala`) VALUES
(9001, 'Espresso sirovina', 1500.00, 16.00),
(9002, 'Domaca kafa sirovina', 1000.00, 8.50),
(9003, 'Ness sirovina', 1200.00, 4.45),
(9004, 'Mleko sirovina', 135.00, 47.00),
(9005, 'Cokolada sirovina', 540.00, 11.10),
(9006, 'Slatka pavlaka sirovina', 245.00, 18.00),
(9007, 'Sirupi sirovina', 1589.00, 2.70),
(9008, 'Pomorandza sirovina', 123.00, 9.14),
(9009, 'Limun sirovina', 120.00, 8.50),
(9010, 'Grejp sirovina', 145.00, 8.45),
(9011, 'Jabuka sirovina', 102.00, 5.90),
(9012, 'Ananas sirovina', 260.00, 4.50),
(9013, 'Banane sirovina', 150.00, 4.80),
(9014, 'Mango sirovina', 250.00, 4.80),
(9015, 'Sladoled', 450.00, 10.50);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `porudzbine`
--
ALTER TABLE `porudzbine`
  ADD PRIMARY KEY (`naziv_proizvoda`,`broj_stola`) USING BTREE;

--
-- Indexes for table `proizvodi`
--
ALTER TABLE `proizvodi`
  ADD PRIMARY KEY (`sifra_proizvoda`);

--
-- Indexes for table `sirovine`
--
ALTER TABLE `sirovine`
  ADD PRIMARY KEY (`sifra_artikla`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
