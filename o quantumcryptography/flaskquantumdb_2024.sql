-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2024 at 01:05 PM
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
-- Database: `flaskquantumdb_2024`
--

-- --------------------------------------------------------

--
-- Table structure for table `flaskquantumdb_2024_area`
--

CREATE TABLE `flaskquantumdb_2024_area` (
  `id` int(10) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `areaone` varchar(255) NOT NULL,
  `areatwo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `flaskquantumdb_2024_area`
--

INSERT INTO `flaskquantumdb_2024_area` (`id`, `uid`, `name`, `email`, `password`, `phone`, `areaone`, `areatwo`) VALUES
(5, 'uid_BNpcyGnNqs', 'area', 'area@area.com', 'area', '9876543210', 'Area 1', 'Area 2');

-- --------------------------------------------------------

--
-- Table structure for table `flaskquantumdb_2024_central`
--

CREATE TABLE `flaskquantumdb_2024_central` (
  `id` int(10) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `flaskquantumdb_2024_central`
--

INSERT INTO `flaskquantumdb_2024_central` (`id`, `uid`, `name`, `email`, `password`, `phone`) VALUES
(3, 'uid_yFoI01Fz1I', 'central', 'central@central.com', 'central', '9876543210');

-- --------------------------------------------------------

--
-- Table structure for table `flaskquantumdb_2024_detail`
--

CREATE TABLE `flaskquantumdb_2024_detail` (
  `id` int(10) NOT NULL,
  `area` varchar(255) DEFAULT NULL,
  `house` varchar(255) DEFAULT NULL,
  `hospital` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `industry` varchar(255) DEFAULT NULL,
  `dated` varchar(255) DEFAULT NULL,
  `central` varchar(255) NOT NULL,
  `centralname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `flaskquantumdb_2024_area`
--
ALTER TABLE `flaskquantumdb_2024_area`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `flaskquantumdb_2024_central`
--
ALTER TABLE `flaskquantumdb_2024_central`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `flaskquantumdb_2024_detail`
--
ALTER TABLE `flaskquantumdb_2024_detail`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `flaskquantumdb_2024_area`
--
ALTER TABLE `flaskquantumdb_2024_area`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `flaskquantumdb_2024_central`
--
ALTER TABLE `flaskquantumdb_2024_central`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `flaskquantumdb_2024_detail`
--
ALTER TABLE `flaskquantumdb_2024_detail`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
