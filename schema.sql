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
  `student_id` VARCHAR(10) PRIMARY KEY,
  `firstname` VARCHAR(255) NOT NULL,
  `lastname` VARCHAR(255) NOT NULL,
  `course_id` VARCHAR(255) NOT NULL,
  `year` ENUM('1st', '2nd', '3rd', '4th'),
  `gender` ENUM('Male', 'Female'),
  `profile_pic` VARCHAR(255),
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

INSERT INTO `college` (`college_code`, `college_name`) VALUES
('COET', 'College of Engineering and Technology'),
('CSM', 'College of Science and Mathematics'),
('CCS', 'College of Computer Studies'),
('CED', 'College of Education'),
('CAS', 'College of Arts and Science'),
('CEBA', 'College of Economics, Business and Accountancy'),
('CON', 'College of Nursing');

INSERT INTO `course` (`course_code`, `course_name`, `college_id`) VALUES
('BSChemEng', 'Bachelor of Science in Chemical Engineering', 'COET'),
('BSEnviEng', 'Bachelor of Science in Environmental Engineering', 'COET'),
('BSCE', 'Bachelor of Science in Civil Engineering', 'COET'),
('BSComEng', 'Bachelor of Science in Computer Engineering', 'COET'),
('BSEE', 'Bachelor of Science in Electrical Engineering', 'COET'),
('BSECE', 'Bachelor of Science in Electronics and Communication Engineering', 'COET'),
('BSIAM', 'Bachelor of Science in Industrial Automation and Mechatronics', 'COET'),
('BSCerEng', 'Bachelor of Science in Ceramics Engineering', 'COET'),
('BSMetEng', 'Bachelor of Science in Metallurgical Engineering', 'COET'),
('BSME', 'Bachelor of Science in Mining Engineering', 'COET'),
('BSMechEng', 'Bachelor of Science in Mechanical Engineering', 'COET'),
('BSBio', 'Bachelor of Science in Biology', 'CSM'),
('BSChem', 'Bachelor of Science in Chemistry', 'CSM'),
('BSMath', 'Bachelor of Science in Mathematics', 'CSM'),
('BSStat', 'Bachelor of Science in Statistics', 'CSM'),
('BSPhy', 'Bachelor of Science in Physics', 'CSM'),
('BSCS', 'Bachelor of Science in Computer Science', 'CCS'),
('BSIT', 'Bachelor of Science in Information Technology', 'CCS'),
('BSIS', 'Bachelor of Science in Information System', 'CCS'),
('BSCA', 'Bachelor of Science in Computer Application', 'CCS'),
('BEE', 'Bachelor of Elementary Education', 'CED'),
('BSE', 'Bachelor of Secondary Education', 'CED'),
('BPE', 'Bachelor of Physical Education', 'CED'),
('BAFil', 'Bachelor of Arts in Filipino', 'CAS'),
('BAHis', 'Bachelor of Arts in History', 'CAS'),
('BAPan', 'Bachelor of Arts in Panitikan', 'CAS'),
('BAPolSci', 'Bachelor of Arts in Political Science', 'CAS'),
('BAPsych', 'Bachelor of Arts in Psychology', 'CAS'),
('BASoc', 'Bachelor of Arts in Sociology', 'CAS'),
('BAPhil', 'Bachelor of Arts in Philosophy', 'CAS'),
('BSPsych', 'Bachelor of Science in Psychology', 'CAS'),
('BSA', 'Bachelor of Science in Accountancy', 'CEBA'),
('BSBA', 'Bachelor of Science in Business Administration', 'CEBA'),
('BSEnt', 'Bachelor of Science in Entrepreneurship', 'CEBA'),
('BSHM', 'Bachelor of Science in Hospitality Management', 'CEBA'),
('BSN', 'Bachelor of Science in Nursing', 'CON');

-- Insert 50 students
INSERT INTO `student` (`student_id`, `firstname`, `lastname`, `course_id`, `year`, `gender`) VALUES
('2023-0001', 'Janella', 'Balantac', 'BSChemEng', '1st', 'Female'),
('2023-0002', 'John', 'Doe', 'BSEnviEng', '1st', 'Male'),
('2023-0003', 'Maria', 'Garcia', 'BSCE', '1st', 'Female'),
('2023-0004', 'Daniel', 'Johnson', 'BSComEng', '1st', 'Male'),
('2023-0005', 'Sophia', 'Martinez', 'BSEE', '1st', 'Female'),
('2022-0006', 'Ethan', 'Smith', 'BSECE', '2nd', 'Male'),
('2022-0007', 'Olivia', 'Jones', 'BSIAM', '2nd', 'Female'),
('2022-0008', 'Liam', 'Williams', 'BSCerEng', '2nd', 'Male'),
('2022-0009', 'Ava', 'Brown', 'BSMetEng', '2nd', 'Female'),
('2022-0010', 'Noah', 'Miller', 'BSME', '2nd', 'Male'),
('2021-0011', 'Emma', 'Davis', 'BSMechEng', '3rd', 'Female'),
('2021-0012', 'William', 'Rodriguez', 'BSBio', '3rd', 'Male'),
('2021-0013', 'Isabella', 'Gomez', 'BSChem', '3rd', 'Female'),
('2021-0014', 'James', 'Hernandez', 'BSMath', '3rd', 'Male'),
('2021-0015', 'Sophie', 'Smith', 'BSStat', '3rd', 'Female'),
('2020-0016', 'Alexander', 'Taylor', 'BSPhy', '4th', 'Male'),
('2020-0017', 'Mia', 'Anderson', 'BSCS', '4th', 'Female'),
('2020-0018', 'Benjamin', 'Martinez', 'BSIT', '4th', 'Male'),
('2020-0019', 'Aria', 'Brown', 'BSIS', '4th', 'Female'),
('2020-0020', 'Elijah', 'Gonzalez', 'BSCA', '4th', 'Male'),
('2023-0021', 'Evelyn', 'Lopez', 'BEE', '1st', 'Female'),
('2023-0022', 'Logan', 'Perez', 'BSE', '1st', 'Male'),
('2023-0023', 'Abigail', 'Turner', 'BPE', '1st', 'Female'),
('2023-0024', 'Eli', 'Gonzalez', 'BAFil', '1st', 'Male'),
('2023-0025', 'Amelia', 'Fisher', 'BAHis', '1st', 'Female'),
('2022-0026', 'Lucas', 'Wright', 'BAPan', '2nd', 'Male'),
('2022-0027', 'Harper', 'Martin', 'BAPolSci', '2nd', 'Female'),
('2022-0028', 'Jackson', 'Anderson', 'BAPsych', '2nd', 'Male'),
('2022-0029', 'Luna', 'Taylor', 'BASoc', '2nd', 'Female'),
('2022-0030', 'Mateo', 'Garcia', 'BAPhil', '2nd', 'Male'),
('2021-0031', 'Stella', 'Hill', 'BSPsych', '3rd', 'Female'),
('2021-0032', 'Leo', 'Thompson', 'BSA', '3rd', 'Male'),
('2021-0033', 'Violet', 'Lewis', 'BSBA', '3rd', 'Female'),
('2021-0034', 'Zachary', 'Clark', 'BSEnt', '3rd', 'Male'),
('2021-0035', 'Aurora', 'Lopez', 'BSHM', '3rd', 'Female'),
('2020-0036', 'Nolan', 'Young', 'BSN', '4th', 'Male'),
('2020-0037', 'Elena', 'Morales', 'BSChemEng', '4th', 'Female'),
('2020-0038', 'Gabriel', 'King', 'BSEnviEng', '4th', 'Male'),
('2020-0039', 'Hazel', 'Scott', 'BSCE', '4th', 'Female'),
('2020-0040', 'Mason', 'Harris', 'BSComEng', '4th', 'Male'),
('2023-0041', 'Piper', 'Cooper', 'BSEE', '1st', 'Female'),
('2023-0042', 'Henry', 'Rivera', 'BSECE', '1st', 'Male'),
('2023-0043', 'Nova', 'Perez', 'BSIAM', '1st', 'Female'),
('2023-0044', 'Oscar', 'Fisher', 'BSCerEng', '1st', 'Male'),
('2023-0045', 'Sophia', 'Mitchell', 'BSMetEng', '1st', 'Female'),
('2022-0046', 'Max', 'Gomez', 'BSME', '2nd', 'Male'),
('2022-0047', 'Ava', 'Diaz', 'BSMechEng', '2nd', 'Female'),
('2022-0048', 'Liam', 'Rodriguez', 'BSBio', '2nd', 'Male'),
('2022-0049', 'Isabella', 'Smith', 'BSChem', '2nd', 'Female'),
('2022-0050', 'Noah', 'Hernandez', 'BSMath', '2nd', 'Male');

-- Data exporting was unselected.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
