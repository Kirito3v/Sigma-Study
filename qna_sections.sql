-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: qna
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sections`
--

DROP TABLE IF EXISTS `sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sections` (
  `sect` int DEFAULT NULL,
  `Saturday` varchar(255) DEFAULT NULL,
  `Sunday` varchar(255) DEFAULT NULL,
  `Monday` varchar(255) DEFAULT NULL,
  `Tuesday` varchar(255) DEFAULT NULL,
  `Wednesday` varchar(255) DEFAULT NULL,
  `Thursday` varchar(255) DEFAULT NULL,
  `Friday` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sections`
--

LOCK TABLES `sections` WRITE;
/*!40000 ALTER TABLE `sections` DISABLE KEYS */;
INSERT INTO `sections` VALUES (1,'nothing','DS','TW','nothing','nothing','nothing','nothing'),(1,'nothing','nothing','nothing','PM','nothing','nothing','nothing'),(1,'nothing','nothing','IS','PM','nothing','nothing','nothing'),(2,'DS','nothing',' nothing','nothing','nothing','nothing','nothing'),(2,'nothing','nothing','nothing','PM','nothing','nothing','nothing'),(2,'nothing','nothing','IS','PM','nothing','nothing','nothing'),(3,'nothing','DS','TW','nothing','nothing','nothing','nothing'),(3,'nothing','TW','IS','PM','nothing','nothing','nothing'),(3,'nothing','PM','nothing','nothing','nothing','nothing','nothing'),(4,'nothing','DS','TW','nothing','nothing','nothing','nothing'),(4,'nothing','nothing','nothing','PM','nothing','nothing','nothing'),(4,'nothing','nothing','IS','nothing','nothing','nothing','nothing'),(5,'nothing','DS','TW','nothing','nothing','nothing','nothing'),(5,'nothing','nothing','nothing','PM','nothing','nothing','nothing'),(5,'nothing','nothing','IS','nothing','nothing','nothing','nothing'),(6,'PM','DS','TW','IS','nothing','nothing','nothing'),(6,'DS','nothing','nothing','PM','nothing','nothing','nothing'),(6,'nothing','TW','IS','nothing','nothing','nothing','nothing'),(7,'nothing','DS','TW','nothing','nothing','nothing','nothing'),(7,'nothing','nothing','nothing','PM','nothing','nothing','nothing'),(7,'nothing','nothing','IS','nothing','nothing','nothing','nothing'),(8,'IS','DS','TW','PM','nothing','nothing','nothing'),(8,'nothing','PM','nothing','nothing','nothing','nothing','nothing'),(8,'TW','nothing','IS','nothing','nothing','nothing','nothing');
/*!40000 ALTER TABLE `sections` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-06 20:08:11
