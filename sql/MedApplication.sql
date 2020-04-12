-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 14, 2020 at 10:40 PM
-- Server version: 8.0.17
-- PHP Version: 7.2.24-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `MedApplication`
--

-- --------------------------------------------------------

--
-- Table structure for table `Appointment`
--

CREATE TABLE `Appointment` (
  `DoctorId` int(11) NOT NULL,
  `HospitalId` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Doctor`
--

CREATE TABLE `Doctor` (
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `specialisation` varchar(50) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `title` varchar(50) NOT NULL,
  `experience` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Hospital`
--

CREATE TABLE `Hospital` (
  `speciality` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Patient`
--

CREATE TABLE `Patient` (
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(1) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `mobileNumber` varchar(10) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `WorksFor`
--

CREATE TABLE `WorksFor` (
  `DoctorId` int(11) NOT NULL,
  `HospitalId` int(11) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Appointment`
--
ALTER TABLE `Appointment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `doctor_id_2` (`DoctorId`),
  ADD KEY `hospital_id_2` (`HospitalId`),
  ADD KEY `user_id` (`UserId`);

--
-- Indexes for table `Doctor`
--
ALTER TABLE `Doctor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Hospital`
--
ALTER TABLE `Hospital`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Patient`
--
ALTER TABLE `Patient`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `WorksFor`
--
ALTER TABLE `WorksFor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `doctor_id` (`DoctorId`),
  ADD KEY `hospital_id` (`HospitalId`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Appointment`
--
ALTER TABLE `Appointment`
  ADD CONSTRAINT `doctor_id_2` FOREIGN KEY (`DoctorId`) REFERENCES `Doctor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `hospital_id_2` FOREIGN KEY (`HospitalId`) REFERENCES `Hospital` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `user_id` FOREIGN KEY (`UserId`) REFERENCES `Patient` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `WorksFor`
--
ALTER TABLE `WorksFor`
  ADD CONSTRAINT `doctor_id` FOREIGN KEY (`DoctorId`) REFERENCES `Doctor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `hospital_id` FOREIGN KEY (`HospitalId`) REFERENCES `Hospital` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
