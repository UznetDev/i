-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 04, 2024 at 08:31 PM
-- Server version: 8.0.36-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `birthday` varchar(50) NOT NULL,
  `grade` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `birthday`, `grade`) VALUES
(1, 'Umidjon', '2003-02-10', 5),
(2, 'Shahzod', '2002-12-20', 3),
(3, 'Nodir', '2003-07-15', 3),
(4, 'Dilshod', '2002-11-02', 4),
(5, 'Farruh', '2003-02-18', 5),
(6, 'Gulbahor', '2003-02-25', 5),
(7, 'Davron', '2003-09-05', 5),
(8, 'Feruza', '2003-04-12', 3),
(9, 'Zuhra', '2002-10-25', 4),
(10, 'Sobir', '2003-08-08', 4),
(11, 'Sobir', '2003-08-08', 4),
(12, 'Shahzod', '2002-12-20', 3);

-- --------------------------------------------------------

--
-- Table structure for table `talaba`
--

CREATE TABLE `talaba` (
  `id` int NOT NULL,
  `ism` varchar(50) NOT NULL,
  `yosh` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `talaba`
--

INSERT INTO `talaba` (`id`, `ism`, `yosh`) VALUES
(1, 'Vali', 20),
(2, 'Michael', 21),
(3, 'Linda', 19),
(4, 'Tom', 23),
(5, 'Conor', 20),
(6, 'Tom', 23),
(7, 'Conor', 20),
(8, 'Tom', 23),
(9, 'Conor', 20),
(10, 'Tom', 23);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `talaba`
--
ALTER TABLE `talaba`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `talaba`
--
ALTER TABLE `talaba`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;