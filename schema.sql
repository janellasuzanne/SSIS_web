-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for ccc151_cs
-- Drop the database if it exists
DROP DATABASE IF EXISTS `ssisweb_db`;

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS `ssisweb_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- Use the database
USE `ssisweb_db`;

-- Drop the table if it exists
DROP TABLE IF EXISTS `student`;

-- Create the student table
CREATE TABLE IF NOT EXISTS `student` (
  `student_id` INT PRIMARY KEY,
  `firstname` VARCHAR(255) NOT NULL,
  `lastname` VARCHAR(255) NOT NULL,
  `year` ENUM('1st', '2nd', '3rd', '4th'),
  `gender` ENUM('Male', 'Female'),
  `course_id` VARCHAR(255) NOT NULL,
  FOREIGN KEY (`course_id`) REFERENCES `course` (`course_code`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Drop the table if it exists
DROP TABLE IF EXISTS `course`;

-- Create the course table
CREATE TABLE IF NOT EXISTS `course` (
  `course_code` VARCHAR(255) PRIMARY KEY,
  `course_name` VARCHAR(255) NOT NULL,
  `college_id` VARCHAR(255) NOT NULL,
  FOREIGN KEY (`college_id`) REFERENCES `college` (`college_code`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Drop the table if it exists
DROP TABLE IF EXISTS `college`;

-- Create the college table
CREATE TABLE IF NOT EXISTS `college` (
  `college_code` VARCHAR(255) PRIMARY KEY,
  `college_name` VARCHAR(255) NOT NULL
);

-- Data exporting was unselected.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
