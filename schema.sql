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
INSERT INTO `student` (`student_id`, `firstname`, `lastname`, `year`, `gender`, `course_id`) VALUES
('2023-0001', 'Janella', 'Balantac', '1st', 'Female', 'BSChemEng'),
('2023-0002', 'John', 'Doe', '1st', 'Male', 'BSEnviEng'),
('2023-0003', 'Maria', 'Garcia', '1st', 'Female', 'BSCE'),
('2023-0004', 'Daniel', 'Johnson', '1st', 'Male', 'BSComEng'),
('2023-0005', 'Sophia', 'Martinez', '1st', 'Female', 'BSEE'),
('2022-0006', 'Ethan', 'Smith', '2nd', 'Male', 'BSECE'),
('2022-0007', 'Olivia', 'Jones', '2nd', 'Female', 'BSIAM'),
('2022-0008', 'Liam', 'Williams', '2nd', 'Male', 'BSCerEng'),
('2022-0009', 'Ava', 'Brown', '2nd', 'Female', 'BSMetEng'),
('2022-0010', 'Noah', 'Miller', '2nd', 'Male', 'BSME'),
('2021-0011', 'Emma', 'Davis', '3rd', 'Female', 'BSMechEng'),
('2021-0012', 'William', 'Rodriguez', '3rd', 'Male', 'BSBio'),
('2021-0013', 'Isabella', 'Gomez', '3rd', 'Female', 'BSChem'),
('2021-0014', 'James', 'Hernandez', '3rd', 'Male', 'BSMath'),
('2021-0015', 'Sophie', 'Smith', '3rd', 'Female', 'BSStat'),
('2020-0016', 'Alexander', 'Taylor', '4th', 'Male', 'BSPhy'),
('2020-0017', 'Mia', 'Anderson', '4th', 'Female', 'BSCS'),
('2020-0018', 'Benjamin', 'Martinez', '4th', 'Male', 'BSIT'),
('2020-0019', 'Aria', 'Brown', '4th', 'Female', 'BSIS'),
('2020-0020', 'Elijah', 'Gonzalez', '4th', 'Male', 'BSCA'),
('2023-0021', 'Evelyn', 'Lopez', '1st', 'Female', 'BEE'),
('2023-0022', 'Logan', 'Perez', '1st', 'Male', 'BSE'),
('2023-0023', 'Abigail', 'Turner', '1st', 'Female', 'BPE'),
('2023-0024', 'Eli', 'Gonzalez', '1st', 'Male', 'BAFil'),
('2023-0025', 'Amelia', 'Fisher', '1st', 'Female', 'BAHis'),
('2022-0026', 'Lucas', 'Wright', '2nd', 'Male', 'BAPan'),
('2022-0027', 'Harper', 'Martin', '2nd', 'Female', 'BAPolSci'),
('2022-0028', 'Jackson', 'Anderson', '2nd', 'Male', 'BAPsych'),
('2022-0029', 'Luna', 'Taylor', '2nd', 'Female', 'BASoc'),
('2022-0030', 'Mateo', 'Garcia', '2nd', 'Male', 'BAPhil'),
('2021-0031', 'Stella', 'Hill', '3rd', 'Female', 'BSPsych'),
('2021-0032', 'Leo', 'Thompson', '3rd', 'Male', 'BSA'),
('2021-0033', 'Violet', 'Lewis', '3rd', 'Female', 'BSBA'),
('2021-0034', 'Zachary', 'Clark', '3rd', 'Male', 'BSEnt'),
('2021-0035', 'Aurora', 'Lopez', '3rd', 'Female', 'BSHM'),
('2020-0036', 'Nolan', 'Young', '4th', 'Male', 'BSN'),
('2020-0037', 'Elena', 'Morales', '4th', 'Female', 'BSChemEng'),
('2020-0038', 'Gabriel', 'King', '4th', 'Male', 'BSEnviEng'),
('2020-0039', 'Hazel', 'Scott', '4th', 'Female', 'BSCE'),
('2020-0040', 'Mason', 'Harris', '4th', 'Male', 'BSComEng'),
('2023-0041', 'Piper', 'Cooper', '1st', 'Female', 'BSEE'),
('2023-0042', 'Henry', 'Rivera', '1st', 'Male', 'BSECE'),
('2023-0043', 'Nova', 'Perez', '1st', 'Female', 'BSIAM'),
('2023-0044', 'Oscar', 'Fisher', '1st', 'Male', 'BSCerEng'),
('2023-0045', 'Sophia', 'Mitchell', '1st', 'Female', 'BSMetEng'),
('2022-0046', 'Max', 'Gomez', '2nd', 'Male', 'BSME'),
('2022-0047', 'Ava', 'Diaz', '2nd', 'Female', 'BSMechEng'),
('2022-0048', 'Liam', 'Rodriguez', '2nd', 'Male', 'BSBio'),
('2022-0049', 'Isabella', 'Smith', '2nd', 'Female', 'BSChem'),
('2022-0050', 'Noah', 'Hernandez', '2nd', 'Male', 'BSMath');

-- Data exporting was unselected.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
