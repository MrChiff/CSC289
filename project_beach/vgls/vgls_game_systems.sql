-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: vgls
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `game_systems`
--

DROP TABLE IF EXISTS `game_systems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_systems` (
  `system_id` int NOT NULL AUTO_INCREMENT,
  `system_name` varchar(45) NOT NULL,
  `manufacturer` int NOT NULL,
  PRIMARY KEY (`system_id`),
  KEY `manufacturer_idx` (`manufacturer`),
  KEY `fk_manufacturer_idx` (`manufacturer`),
  CONSTRAINT `manufacturer` FOREIGN KEY (`manufacturer`) REFERENCES `manufacturer` (`manufacturer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_systems`
--

LOCK TABLES `game_systems` WRITE;
/*!40000 ALTER TABLE `game_systems` DISABLE KEYS */;
INSERT INTO `game_systems` VALUES (1,'Switch',1),(2,'Nintendo Entertainment System',1),(3,'Game Cube',1),(4,'Super Nintendo',1),(5,'Wii',1),(6,'Wii U',1),(7,'Nintendo 64',1),(8,'Gameboy',1),(9,'Gameboy Color',1),(10,'Gameboy Advance',1),(11,'Gameboy DS',1),(12,'Gameboy 3DS',1),(13,'Xbox One',3),(14,'Xbox 360',3),(15,'Playstation',2),(16,'Playstation 2',2),(17,'Playstation 3',2),(18,'Playstation 4',2),(19,'Playstation 5',2),(20,'Playstation Portable',2),(21,'Playstation Vita',2);
/*!40000 ALTER TABLE `game_systems` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-15 18:24:28
