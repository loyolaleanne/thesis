-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2023 at 12:46 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `regteach`
--

CREATE TABLE `regteach` (
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `cnum` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `ssq` varchar(50) NOT NULL,
  `sa` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `regteach`
--

INSERT INTO `regteach` (`fname`, `lname`, `cnum`, `email`, `ssq`, `sa`, `pwd`) VALUES
('Elexis', 'Falceso', '09505934815', 'elexis.falceso@cvsu.edu.ph', 'Your Date of Birth', '1/21/1998', 'Elexisfalceso211998'),
('jenesis', 'falceso', '09514781767', 'jenisis@gmail.com', 'Your Nick Name', 'jen', '1231231010'),
('sad', 'asdsa', 'asdas', 'asdsa', 'Your Date of Birth', 'dsazdas', 'asdsa'),
('asdas', 'asdas', 'asdsa', 'sadas', 'Your Date of Birth', 'sadas', 'asdsa'),
('elexis', 'falceso', '09505934815', 'elexis30@gmail.com', 'Your Nick Name', 'iket', '1231231010'),
('asdas', 'asdas', '262362462486464', 'asdasdasd', 'Your Date of Birth', '212121', 'asdsadas'),
('asdasd', 'asdas', '297682684648', 'sadasdsa', 'Your Date of Birth', 'sadsad', 'asdasdsadas'),
('dasdas', 'asdas', 'asdasdas', 'dasdas', 'Your Date of Birth', 'asdsad', '1231231010'),
('asdas', 'asdas', 'asdas', 'asdasd', 'Your Date of Birth', 'asdsadasd', '1231231010');

-- --------------------------------------------------------

--
-- Table structure for table `stdattendance`
--

CREATE TABLE `stdattendance` (
  `std_id` varchar(255) NOT NULL,
  `std_name` varchar(255) NOT NULL,
  `std_time` time NOT NULL DEFAULT current_timestamp(),
  `std_date` varchar(255) NOT NULL DEFAULT current_timestamp(),
  `std_attendance` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Student_ID` varchar(255) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `mname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `Division` varchar(50) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `DOB` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Roll_No` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Teacher_Name` varchar(50) NOT NULL,
  `PhotoSample` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
