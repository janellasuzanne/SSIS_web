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
  `student_course` VARCHAR(255) NOT NULL,
  `year` ENUM('1st', '2nd', '3rd', '4th'),
  `gender` ENUM('Male', 'Female'),
  `profile_pic` VARCHAR(255) DEFAULT NULL,
  FOREIGN KEY (`student_course`) REFERENCES `course` (`course_name`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Drop the table if it exists
DROP TABLE IF EXISTS `course`;

-- Create the course table
CREATE TABLE IF NOT EXISTS `course` (
  `course_code` VARCHAR(255) PRIMARY KEY,
  `course_name` VARCHAR(255) NOT NULL UNIQUE,
  `college_id` VARCHAR(255) NOT NULL,
  FOREIGN KEY (`college_id`) REFERENCES `college` (`college_code`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Drop the table if it exists
DROP TABLE IF EXISTS `college`;

-- Create the college table
CREATE TABLE IF NOT EXISTS `college` (
  `college_code` VARCHAR(255) PRIMARY KEY,
  `college_name` VARCHAR(255) NOT NULL UNIQUE
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
INSERT INTO `student` (`student_id`, `firstname`, `lastname`, `student_course`, `year`, `gender`) VALUES
('2023-0001', 'Janella', 'Balantac', 'Bachelor of Science in Chemical Engineering', '1st', 'Female'),
('2023-0002', 'John', 'Doe', 'Bachelor of Science in Environmental Engineering', '1st', 'Male'),
('2023-0003', 'Maria', 'Garcia', 'Bachelor of Science in Ceramics Engineering', '1st', 'Female'),
('2023-0004', 'Daniel', 'Johnson', 'Bachelor of Science in Computer Engineering', '1st', 'Male'),
('2023-0005', 'Sophia', 'Martinez', 'Bachelor of Science in Electrical Engineering', '1st', 'Female'),
('2022-0006', 'Ethan', 'Smith', 'Bachelor of Science in Electronics and Communication Engineering', '2nd', 'Male'),
('2022-0007', 'Olivia', 'Jones', 'Bachelor of Science in Industrial Automation and Mechatronics', '2nd', 'Female'),
('2022-0008', 'Liam', 'Williams', 'Bachelor of Science in Ceramics Engineering', '2nd', 'Male'),
('2022-0009', 'Ava', 'Brown', 'Bachelor of Science in Metallurgical Engineering', '2nd', 'Female'),
('2022-0010', 'Noah', 'Miller', 'Bachelor of Science in Mining Engineering', '2nd', 'Male'),
('2021-0011', 'Emma', 'Davis', 'Bachelor of Science in Mechanical Engineering', '3rd', 'Female'),
('2021-0012', 'William', 'Rodriguez', 'Bachelor of Science in Biology', '3rd', 'Male'),
('2021-0013', 'Isabella', 'Gomez', 'Bachelor of Science in Chemistry', '3rd', 'Female'),
('2021-0014', 'James', 'Hernandez', 'Bachelor of Science in Mathematics', '3rd', 'Male'),
('2021-0015', 'Sophie', 'Smith', 'Bachelor of Science in Statistics', '3rd', 'Female'),
('2020-0016', 'Alexander', 'Taylor', 'Bachelor of Science in Physics', '4th', 'Male'),
('2020-0017', 'Mia', 'Anderson', 'Bachelor of Science in Computer Science', '4th', 'Female'),
('2020-0018', 'Benjamin', 'Martinez', 'Bachelor of Science in Information Technology', '4th', 'Male'),
('2020-0019', 'Aria', 'Brown', 'Bachelor of Science in Information System', '4th', 'Female'),
('2020-0020', 'Elijah', 'Gonzalez', 'Bachelor of Science in Computer Application', '4th', 'Male'),
('2023-0021', 'Evelyn', 'Lopez', 'Bachelor of Elementary Education', '1st', 'Female'),
('2023-0022', 'Logan', 'Perez', 'Bachelor of Secondary Education', '1st', 'Male'),
('2023-0023', 'Abigail', 'Turner', 'Bachelor of Physical Education', '1st', 'Female'),
('2023-0024', 'Eli', 'Gonzalez', 'Bachelor of Arts in Filipino', '1st', 'Male'),
('2023-0025', 'Amelia', 'Fisher', 'Bachelor of Arts in History', '1st', 'Female'),
('2022-0026', 'Lucas', 'Wright', 'Bachelor of Arts in Panitikan', '2nd', 'Male'),
('2022-0027', 'Harper', 'Martin', 'Bachelor of Arts in Political Science', '2nd', 'Female'),
('2022-0028', 'Jackson', 'Anderson', 'Bachelor of Arts in Psychology', '2nd', 'Male'),
('2022-0029', 'Luna', 'Taylor', 'Bachelor of Arts in Sociology', '2nd', 'Female'),
('2022-0030', 'Mateo', 'Garcia', 'Bachelor of Arts in Philosophy', '2nd', 'Male'),
('2021-0031', 'Stella', 'Hill', 'Bachelor of Science in Psychology', '3rd', 'Female'),
('2021-0032', 'Leo', 'Thompson', 'Bachelor of Science in Accountancy', '3rd', 'Male'),
('2021-0033', 'Violet', 'Lewis', 'Bachelor of Science in Business Administration', '3rd', 'Female'),
('2021-0034', 'Zachary', 'Clark', 'Bachelor of Science in Entrepreneurship', '3rd', 'Male'),
('2021-0035', 'Aurora', 'Lopez', 'Bachelor of Science in Hospitality Management', '3rd', 'Female'),
('2020-0036', 'Nolan', 'Young', 'Bachelor of Science in Nursing', '4th', 'Male'),
('2020-0037', 'Elena', 'Morales', 'Bachelor of Science in Chemical Engineering', '4th', 'Female'),
('2020-0038', 'Gabriel', 'King', 'Bachelor of Science in Environmental Engineering', '4th', 'Male'),
('2020-0039', 'Hazel', 'Scott', 'Bachelor of Science in Civil Engineering', '4th', 'Female'),
('2020-0040', 'Mason', 'Harris', 'Bachelor of Science in Computer Engineering', '4th', 'Male'),
('2023-0041', 'Piper', 'Cooper', 'Bachelor of Science in Electrical Engineering', '1st', 'Female'),
('2023-0042', 'Henry', 'Rivera', 'Bachelor of Science in Electronics and Communication Engineering', '1st', 'Male'),
('2023-0043', 'Nova', 'Perez', 'Bachelor of Science in Industrial Automation and Mechatronics', '1st', 'Female'),
('2023-0044', 'Oscar', 'Fisher', 'Bachelor of Science in Ceramics Engineering', '1st', 'Male'),
('2023-0045', 'Sophia', 'Mitchell', 'Bachelor of Science in Metallurgical Engineering', '1st', 'Female'),
('2022-0046', 'Max', 'Gomez', 'Bachelor of Science in Mining Engineering', '2nd', 'Male'),
('2022-0047', 'Ava', 'Diaz', 'Bachelor of Science in Mechanical Engineering', '2nd', 'Female'),
('2022-0048', 'Liam', 'Rodriguez', 'Bachelor of Science in Biology', '2nd', 'Male'),
('2022-0049', 'Isabella', 'Smith', 'Bachelor of Science in Chemistry', '2nd', 'Female'),
('2022-0050', 'Noah', 'Hernandez', 'Bachelor of Science in Mathematics', '2nd', 'Male');

-- Data exporting was unselected.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
