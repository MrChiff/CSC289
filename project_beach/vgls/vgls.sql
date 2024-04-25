CREATE DATABASE  IF NOT EXISTS `vgls` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `vgls`;
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
-- Table structure for table `consoles`
--

DROP TABLE IF EXISTS `consoles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consoles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `console` varchar(100) NOT NULL,
  `manufacturer_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manufacturer_fk_idx` (`manufacturer_id`),
  CONSTRAINT `manufacturer_fk` FOREIGN KEY (`manufacturer_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consoles`
--

LOCK TABLES `consoles` WRITE;
/*!40000 ALTER TABLE `consoles` DISABLE KEYS */;
INSERT INTO `consoles` VALUES (1,'Playstation',2),(2,'Xbox 360',3),(3,'Xbox One',3),(4,'SNES',1),(5,'NES',1),(6,'Switch',1),(7,'Playstation 2',2),(8,'GameCube',1),(9,'Wii',1),(10,'Atari',7),(11,'Playstation 5',2),(12,'Playstation 3',2),(13,'Playstation 4',2),(14,'Xbox Series S',3),(15,'Xbox Series X',3),(16,'Wii U',1),(17,'Jaguar',7),(18,'SEGA Saturn',4),(19,'Dreamcast',4),(20,'SG-1000',4),(21,'SEGA Master System',4),(22,'Genesis',4),(23,'Game Gear',4),(24,'SEGA CD',4),(25,'Pico',4),(26,'SEGA 32X',4),(27,'Advanced Pico Beena',4),(28,'Genesis Mini',4),(29,'Game Gear Micro',4),(30,'Genesis Mini 2',4),(31,'Nintendo 64',1),(32,'Game Boy',1),(33,'Game Boy Color',1),(34,'Game Boy Advance',1),(35,'Nintendo DS',1),(36,'Nintendo 3DS',1),(37,'Virtual Boy',1),(38,'PSP',2),(39,'PS Vita',2),(40,'PS One',2),(41,'Xbox',3),(42,'Xbox One',3),(43,'iOS',17),(44,'Android',18),(45,'Nintendo DSi',1),(46,'macOS',17),(47,'Commodore / Amiga',19),(48,'Atari 7800',7),(49,'Atari 5200',7),(50,'Atari 2600',7),(51,'Atari Flashback',7),(52,'Atari 8-bit',7),(53,'Atari ST',7),(54,'Atari Lynx',7),(55,'Atari XEGS',7),(56,'3DO',20),(57,'Neo Geo',21);
/*!40000 ALTER TABLE `consoles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `id` int NOT NULL AUTO_INCREMENT,
  `videogame` varchar(100) NOT NULL,
  `console_id` int NOT NULL,
  `creator_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `console_fk_idx` (`console_id`),
  KEY `creator_id_fk_idx` (`creator_id`),
  CONSTRAINT `console_fk` FOREIGN KEY (`console_id`) REFERENCES `consoles` (`id`),
  CONSTRAINT `creator_fk` FOREIGN KEY (`creator_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'Final Fantasy XIV: Dawntrail',13,6),(2,'Final Fantasy XIV: Dawntrail',11,6),(3,'Final Fantasy XIV: Dawntrail',15,6),(4,'Visions of Mana',13,6),(5,'Visions of Mana',11,6),(6,'Visions of Mana',15,6),(7,'Final Fantasy VII Rebirth',11,6),(8,'Foamstars',11,6),(9,'Foamstars',13,6),(10,'Star Ocean: The Second Story',11,6),(11,'Star Ocean: The Second Story',13,6),(12,'Front Mission 2: Remake',11,6),(13,'Front Mission 2: Remake',13,6),(14,'Front Mission 2: Remake',3,6),(15,'Front Mission 2: Remake',15,6),(16,'Marble Madness',10,7),(17,'Paperboy',10,7),(18,'Star Wars: The Empire Strikes Back',10,7),(19,'Peter Pack Rat',10,7),(20,'Indiana Jones and the Temple of Doom',10,7),(21,'Gauntlet',10,7),(22,'Super Sprint',10,7),(23,'Road Runner',10,7),(24,'Gauntlet II',10,7),(25,'Championship Sprint',10,7),(26,'720 Degrees',10,7),(27,'Pac Man',10,7),(28,'E.T. The Extra Terrestrial',10,7),(29,'R.B.I. Baseball',10,7),(30,'Super Mario Brothers / Duck Hunt',5,1),(31,'Abe\'s Odysee',1,8),(32,'Parasite Eve',1,8),(33,'Gran Tursimo 2',1,9),(34,'Gran Turismo',1,2),(35,'Crash Bandicoot Warped',1,2),(36,'Animal Crossing New Horizions',6,1),(37,'Assassins Creed IV Black Flag',3,10),(38,'Spyro the Dragon',3,3);
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library`
--

DROP TABLE IF EXISTS `library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library` (
  `id` int NOT NULL AUTO_INCREMENT,
  `videogame_id` int NOT NULL,
  `machine_id` int NOT NULL,
  `quantity` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `game_fk_idx` (`videogame_id`),
  KEY `console_fk_idx` (`machine_id`),
  KEY `library_user_fk_idx` (`user_id`),
  CONSTRAINT `game_fk` FOREIGN KEY (`videogame_id`) REFERENCES `games` (`id`),
  CONSTRAINT `library_console_fk` FOREIGN KEY (`machine_id`) REFERENCES `consoles` (`id`),
  CONSTRAINT `library_user_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library`
--

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;
/*!40000 ALTER TABLE `library` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturer`
--

DROP TABLE IF EXISTS `manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `manufacturer` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturer`
--

LOCK TABLES `manufacturer` WRITE;
/*!40000 ALTER TABLE `manufacturer` DISABLE KEYS */;
INSERT INTO `manufacturer` VALUES (0,'unknown'),(1,'Nintendo'),(2,'Sony'),(3,'Microsoft'),(4,'Sega'),(5,'Namco'),(6,'Square Enix'),(7,'Atari SA'),(8,'Square'),(9,'Sony Interactive Entertainment America'),(10,'Ubisoft'),(11,'Epic Games'),(12,'Capcom'),(13,'Activisionblizzard'),(14,'PopCap Games'),(15,'Konami'),(16,'Apple'),(17,'Google'),(18,'Android'),(19,'Commodore'),(20,'3DO'),(21,'SNK Corporation');
/*!40000 ALTER TABLE `manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `date_posted` datetime NOT NULL,
  `content` longtext NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_fk_idx` (`user_id`),
  CONSTRAINT `user_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,'Amazing Website','2024-03-15 22:19:53','I love the way that I can create my own video game library and then be able to see how much the collection is possibly worth.',1),(2,'I love this site','2024-03-15 22:21:12','I am looking forward to possibly selling my video game collection to other video game enthusiasts in the future.',2),(3,'Really good site','2024-03-15 22:23:23','I forgot my password, so I was happy to be able to change my password without having to contact the site\'s administrators.',3);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `password` longtext NOT NULL,
  `image_file` varchar(20) NOT NULL,
  `admin_user` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'niatheangel','Brenda','Beach','$2b$12$8ZRKlA58QA7pdFHaUMpzWOdhpSiM0PgHJWyHCyDR00sdxSZtSOvTm','default.jpg','Admin'),(2,'testuser','Test','User','$2b$12$LUjfP38q6PLv7BB86RWmnuz42nNexNW1cQAnRz3jI58tIQsIinYby','default.jpg','Admin'),(3,'dragon2peer','David','North','$2b$12$.azK9JwUerZQ15bCkVfVveby9eBu3VwSp/dPPP75YigRPTUCYSe/W','default.jpg','User'),(4,'testuser2','test','user2','$2b$12$wswCbOB/4A9d/cQeR5hRMe8cwLVNQS8s3Rs9pz5ImDfJFoRrGM3ji','default.jpg','User');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'vgls'
--

--
-- Dumping routines for database 'vgls'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-24 21:40:25
