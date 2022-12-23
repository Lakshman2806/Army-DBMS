-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: Project
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AGE`
--

DROP TABLE IF EXISTS `AGE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AGE` (
  `Age` int NOT NULL,
  `DOB` date NOT NULL,
  PRIMARY KEY (`DOB`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AGE`
--

LOCK TABLES `AGE` WRITE;
/*!40000 ALTER TABLE `AGE` DISABLE KEYS */;
INSERT INTO `AGE` VALUES (38,'1984-01-01'),(31,'1991-06-18'),(26,'1995-12-28'),(26,'1996-07-08'),(24,'1998-02-14'),(24,'1998-08-25'),(23,'1999-12-19'),(22,'2000-08-19'),(22,'2000-10-15'),(22,'2000-11-17'),(21,'2001-05-20'),(21,'2001-09-09'),(20,'2002-11-18');
/*!40000 ALTER TABLE `AGE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Barracks`
--

DROP TABLE IF EXISTS `Barracks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Barracks` (
  `Capacity` varchar(15) NOT NULL,
  `Room_ID` varchar(15) NOT NULL,
  PRIMARY KEY (`Room_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Barracks`
--

LOCK TABLES `Barracks` WRITE;
/*!40000 ALTER TABLE `Barracks` DISABLE KEYS */;
INSERT INTO `Barracks` VALUES ('123','05C'),('987','10P'),('632','11A'),('1290','11B'),('897','12D'),('587','13B'),('500','30A'),('1000','30B'),('500','30C'),('758','31C'),('678','32D'),('587','90A');
/*!40000 ALTER TABLE `Barracks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Commander`
--

DROP TABLE IF EXISTS `Commander`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Commander` (
  `Cmdr_Serviceno` varchar(10) NOT NULL,
  `Cmdr_Rank` varchar(15) NOT NULL,
  PRIMARY KEY (`Cmdr_Serviceno`),
  CONSTRAINT `Commander_ibfk_1` FOREIGN KEY (`Cmdr_Serviceno`) REFERENCES `SOLDIER` (`Service_Number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Commander`
--

LOCK TABLES `Commander` WRITE;
/*!40000 ALTER TABLE `Commander` DISABLE KEYS */;
INSERT INTO `Commander` VALUES ('C50','General'),('C53','Major General'),('C56','Captain'),('C57','Lieutenant Gen'),('C58','Captain');
/*!40000 ALTER TABLE `Commander` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dependent`
--

DROP TABLE IF EXISTS `Dependent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dependent` (
  `First_Name` varchar(100) NOT NULL,
  `Last_name` varchar(100) NOT NULL,
  `RelationwithSoldier` varchar(15) NOT NULL,
  `RelatedSoldier_ServiceNo` varchar(10) NOT NULL,
  PRIMARY KEY (`RelatedSoldier_ServiceNo`,`RelationwithSoldier`),
  CONSTRAINT `Dependent_ibfk_1` FOREIGN KEY (`RelatedSoldier_ServiceNo`) REFERENCES `SOLDIER` (`Service_Number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dependent`
--

LOCK TABLES `Dependent` WRITE;
/*!40000 ALTER TABLE `Dependent` DISABLE KEYS */;
INSERT INTO `Dependent` VALUES ('Santosh','Walia','Father','C50'),('Rekha','Pandey','Wife','C51'),('Reena','Sharma','Mother','C52'),('Sunita','Kalia','Wife','C53'),('Dimple','Batra','Wife','C54'),('Deepti','Singh','Wife','C55'),('Lakshmi','Singh','Mother','C56'),('Ram Lal','Yadav','Father','C57'),('Tez','Rao','Father','C58'),('Radheshyam','Ram','Father','C59'),('Sita','Ram','Mother','C59');
/*!40000 ALTER TABLE `Dependent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Health_Stats`
--

DROP TABLE IF EXISTS `Health_Stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Health_Stats` (
  `Height` int NOT NULL,
  `Weight` int NOT NULL,
  `BMI` double NOT NULL,
  PRIMARY KEY (`Height`,`Weight`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Health_Stats`
--

LOCK TABLES `Health_Stats` WRITE;
/*!40000 ALTER TABLE `Health_Stats` DISABLE KEYS */;
INSERT INTO `Health_Stats` VALUES (175,65,21.224489795),(176,66,21.306818181),(177,65,20.747550193),(178,65,20.515086478),(179,62,19.350207546),(180,65,20.061728395),(180,68,20.98765432),(181,64,19.535423216),(184,87,25.697069943),(188,86,24.332277048);
/*!40000 ALTER TABLE `Health_Stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Inventory`
--

DROP TABLE IF EXISTS `Inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Inventory` (
  `Inventory_Name` varchar(15) NOT NULL,
  `Inventory_Capacity` varchar(15) NOT NULL,
  PRIMARY KEY (`Inventory_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Inventory`
--

LOCK TABLES `Inventory` WRITE;
/*!40000 ALTER TABLE `Inventory` DISABLE KEYS */;
INSERT INTO `Inventory` VALUES ('DRDO','7185'),('Garden Reach','7030'),('HAL','4030'),('ideaForge','9612'),('ISRO','6130'),('Mazagon Dock','3287'),('Punj Lloyd','3030'),('SSS','3230'),('UADNL','5130');
/*!40000 ALTER TABLE `Inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Quarters`
--

DROP TABLE IF EXISTS `Quarters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Quarters` (
  `Quarter_Name` char(9) NOT NULL,
  `Region` char(9) NOT NULL,
  `Capacity` int NOT NULL,
  PRIMARY KEY (`Quarter_Name`,`Region`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Quarters`
--

LOCK TABLES `Quarters` WRITE;
/*!40000 ALTER TABLE `Quarters` DISABLE KEYS */;
INSERT INTO `Quarters` VALUES ('Bhopal','MP',3100),('Lucknow','UP',3500),('Shimla','HP',2500),('Udhampur','JK',3000);
/*!40000 ALTER TABLE `Quarters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SOLDIER`
--

DROP TABLE IF EXISTS `SOLDIER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SOLDIER` (
  `Service_Number` varchar(10) NOT NULL,
  `First_Name` varchar(100) NOT NULL,
  `Last_name` varchar(100) NOT NULL,
  `Height` int NOT NULL,
  `Soldier_Rank` varchar(15) NOT NULL,
  `Weight` int NOT NULL,
  `DOB` date NOT NULL,
  `Zonal_Code` varchar(15) NOT NULL,
  `Quarter_Name` char(9) NOT NULL,
  `Quarter_Region` char(9) NOT NULL,
  `Room_Id` varchar(15) NOT NULL,
  PRIMARY KEY (`Service_Number`),
  KEY `Height` (`Height`,`Weight`),
  KEY `DOB` (`DOB`),
  KEY `Zonal_Code` (`Zonal_Code`),
  KEY `Quarter_Name` (`Quarter_Name`,`Quarter_Region`),
  KEY `Room_Id` (`Room_Id`),
  CONSTRAINT `SOLDIER_ibfk_1` FOREIGN KEY (`Height`, `Weight`) REFERENCES `Health_Stats` (`Height`, `Weight`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SOLDIER_ibfk_2` FOREIGN KEY (`DOB`) REFERENCES `AGE` (`DOB`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SOLDIER_ibfk_3` FOREIGN KEY (`Zonal_Code`) REFERENCES `Zone` (`PIN_Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SOLDIER_ibfk_4` FOREIGN KEY (`Quarter_Name`, `Quarter_Region`) REFERENCES `Quarters` (`Quarter_Name`, `Region`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SOLDIER_ibfk_5` FOREIGN KEY (`Room_Id`) REFERENCES `Barracks` (`Room_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SOLDIER`
--

LOCK TABLES `SOLDIER` WRITE;
/*!40000 ALTER TABLE `SOLDIER` DISABLE KEYS */;
INSERT INTO `SOLDIER` VALUES ('C50','Sudhir','Walia',177,'General',65,'2000-10-15','182101','Udhampur','JK','30A'),('C51','Manoj','Pandey',176,'Field Marshal',66,'1998-08-25','171001','Shimla','HP','30B'),('C52','Som Nath','Sharma',180,'Brigadier',65,'2000-08-19','182101','Udhampur','JK','31C'),('C53','Shaurabh','Kalia',178,'Major General',65,'2001-05-20','171001','Shimla','HP','32D'),('C54','Vikram','Batra',179,'Colonel',62,'1998-08-25','182101','Udhampur','JK','10P'),('C55','Nand','Singh',175,'Major',65,'1996-07-08','226001','Lucknow','UP','11B'),('C56','Navdeep','Singh',180,'Captain',68,'2001-09-09','226001','Lucknow','UP','11A'),('C57','Umrao','Yadav',179,'Lieutenant Gen',62,'2002-11-18','171001','Shimla','HP','12D'),('C58','Deepak','Rao',181,'Captain',64,'1999-12-19','440001','Bhopal','MP','05C'),('C59','Bhandari','Ram',179,'Field Marshal',62,'1998-02-14','440001','Bhopal','MP','90A'),('D50','Gagan','Rathod',188,'Sepoy',86,'1995-12-28','171001','Shimla','HP','12D'),('D51','Mohammed','Usman',184,'Sepoy',87,'1984-01-01','226001','Lucknow','UP','30A');
/*!40000 ALTER TABLE `SOLDIER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Weapon1`
--

DROP TABLE IF EXISTS `Weapon1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Weapon1` (
  `Weapon_ID` varchar(15) NOT NULL,
  `Weapon_Name` varchar(15) NOT NULL,
  `Weapon_Range` int NOT NULL,
  `Inventory_Name` varchar(15) NOT NULL,
  PRIMARY KEY (`Weapon_Name`,`Weapon_ID`),
  KEY `Inventory_Name` (`Inventory_Name`),
  CONSTRAINT `Weapon1_ibfk_1` FOREIGN KEY (`Inventory_Name`) REFERENCES `Inventory` (`Inventory_Name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Weapon1`
--

LOCK TABLES `Weapon1` WRITE;
/*!40000 ALTER TABLE `Weapon1` DISABLE KEYS */;
INSERT INTO `Weapon1` VALUES ('W05','1B1 INSAS',5,'Punj Lloyd'),('W02','Glock 17',171,'DRDO'),('W03','Glock 17',9,'SSS'),('W09','IMI',9,'ISRO'),('W07','Ishapore',234,'UADNL'),('W10','MG 1B',9,'ideaForge'),('W04','Micro-Uzi',9,'UADNL'),('W08','MPi-KM',9,'HAL'),('W06','OFB 1A1',345,'ideaForge'),('W01','Pistol Auto',9,'Punj Lloyd');
/*!40000 ALTER TABLE `Weapon1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Weapon2`
--

DROP TABLE IF EXISTS `Weapon2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Weapon2` (
  `Weapon_ID` varchar(15) NOT NULL,
  `Weapon_Name` varchar(15) NOT NULL,
  `Type` varchar(15) NOT NULL,
  PRIMARY KEY (`Weapon_Name`,`Weapon_ID`,`Type`),
  CONSTRAINT `Weapon2_ibfk_1` FOREIGN KEY (`Weapon_Name`, `Weapon_ID`) REFERENCES `Weapon1` (`Weapon_Name`, `Weapon_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Weapon2`
--

LOCK TABLES `Weapon2` WRITE;
/*!40000 ALTER TABLE `Weapon2` DISABLE KEYS */;
INSERT INTO `Weapon2` VALUES ('W05','1B1 INSAS','gun'),('W02','Glock 17','pistol'),('W03','Glock 17','gun'),('W03','Glock 17','sniper'),('W09','IMI','rifle'),('W07','Ishapore','rifle'),('W10','MG 1B','pistol'),('W04','Micro-Uzi','pistol'),('W08','MPi-KM','rifle'),('W06','OFB 1A1','pistol'),('W01','Pistol Auto','pistol');
/*!40000 ALTER TABLE `Weapon2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Zone`
--

DROP TABLE IF EXISTS `Zone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Zone` (
  `PIN_Code` varchar(15) NOT NULL,
  `Capacity` int DEFAULT NULL,
  `Zone_Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`PIN_Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Zone`
--

LOCK TABLES `Zone` WRITE;
/*!40000 ALTER TABLE `Zone` DISABLE KEYS */;
INSERT INTO `Zone` VALUES ('171001',1150,'Pulwama'),('182101',900,'Ladakh'),('226001',1300,'Delhi'),('440001',1200,'Arunachal Pradesh'),('500057',1150,'Uri');
/*!40000 ALTER TABLE `Zone` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27  4:30:36
