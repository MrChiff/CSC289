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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consoles`
--

LOCK TABLES `consoles` WRITE;
/*!40000 ALTER TABLE `consoles` DISABLE KEYS */;
INSERT INTO `consoles` VALUES (1,'Playstation',2),(2,'Xbox 360',3),(3,'Xbox One',3),(4,'SNES',1),(5,'NES',1),(6,'Switch',1),(7,'Playstation 2',2),(8,'GameCube',1),(9,'Wii',1),(10,'Atari',7),(11,'Playstation 5',2),(12,'Playstation 3',2),(13,'Playstation 4',2),(14,'Xbox Series S',3),(15,'Xbox Series X',3),(16,'Wii U',1),(17,'Jaguar',7),(18,'SEGA Saturn',4),(19,'Dreamcast',4),(20,'SG-1000',4),(21,'SEGA Master System',4),(22,'Genesis',4),(23,'Game Gear',4),(24,'SEGA CD',4),(25,'Pico',4),(26,'SEGA 32X',4),(27,'Advanced Pico Beena',4),(28,'Genesis Mini',4),(29,'Game Gear Micro',4),(30,'Genesis Mini 2',4),(31,'Nintendo 64',1),(32,'Game Boy',1),(33,'Game Boy Color',1),(34,'Game Boy Advance',1),(35,'Nintendo DS',1),(36,'Nintendo 3DS',1),(37,'Virtual Boy',1),(38,'PSP',2),(39,'PS Vita',2),(40,'PS One',2),(41,'Xbox',3),(42,'Xbox One',3),(43,'iOS',17),(44,'Android',18),(45,'Nintendo DSi',1),(46,'macOS',17),(47,'Commodore / Amiga',19),(48,'Atari 7800',7),(49,'Atari 5200',7),(50,'Atari 2600',7),(51,'Atari Flashback',7),(52,'Atari 8-bit',7),(53,'Atari ST',7),(54,'Atari Lynx',7),(55,'Atari XEGS',7),(56,'3DO',20),(57,'Neo Geo',21),(60,'PC',0),(61,'Xbox Series S/X',0),(62,'Nintendo Switch',0),(63,'Linux',0),(64,'Web',0);
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
  `price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `console_fk_idx` (`console_id`),
  KEY `creator_id_fk_idx` (`creator_id`),
  CONSTRAINT `console_fk` FOREIGN KEY (`console_id`) REFERENCES `consoles` (`id`),
  CONSTRAINT `creator_fk` FOREIGN KEY (`creator_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=320 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'Final Fantasy XIV: Dawntrail',13,6,NULL),(2,'Final Fantasy XIV: Dawntrail',11,6,NULL),(3,'Final Fantasy XIV: Dawntrail',15,6,NULL),(4,'Visions of Mana',13,6,NULL),(5,'Visions of Mana',11,6,NULL),(6,'Visions of Mana',15,6,NULL),(7,'Final Fantasy VII Rebirth',11,6,NULL),(8,'Foamstars',11,6,NULL),(9,'Foamstars',13,6,NULL),(10,'Star Ocean: The Second Story',11,6,NULL),(11,'Star Ocean: The Second Story',13,6,NULL),(12,'Front Mission 2: Remake',11,6,NULL),(13,'Front Mission 2: Remake',13,6,NULL),(14,'Front Mission 2: Remake',3,6,NULL),(15,'Front Mission 2: Remake',15,6,NULL),(16,'Marble Madness',10,7,NULL),(17,'Paperboy',10,7,NULL),(18,'Star Wars: The Empire Strikes Back',10,7,NULL),(19,'Peter Pack Rat',10,7,NULL),(20,'Indiana Jones and the Temple of Doom',10,7,NULL),(21,'Gauntlet',10,7,NULL),(22,'Super Sprint',10,7,NULL),(23,'Road Runner',10,7,NULL),(24,'Gauntlet II',10,7,NULL),(25,'Championship Sprint',10,7,NULL),(26,'720 Degrees',10,7,NULL),(27,'Pac Man',10,7,NULL),(28,'E.T. The Extra Terrestrial',10,7,NULL),(29,'R.B.I. Baseball',10,7,NULL),(30,'Super Mario Brothers / Duck Hunt',5,1,NULL),(31,'Abe\'s Odysee',1,8,NULL),(32,'Parasite Eve',1,8,NULL),(33,'Gran Tursimo 2',1,9,NULL),(34,'Gran Turismo',1,2,NULL),(35,'Crash Bandicoot Warped',1,2,NULL),(36,'Animal Crossing New Horizions',6,1,NULL),(37,'Assassins Creed IV Black Flag',3,10,NULL),(38,'Spyro the Dragon',3,3,NULL),(39,'Grand Theft Auto V',60,0,-99.00),(40,'Grand Theft Auto V',11,0,-99.00),(41,'Grand Theft Auto V',61,0,-99.00),(42,'Grand Theft Auto V',13,0,-99.00),(43,'Grand Theft Auto V',12,0,-99.00),(44,'Grand Theft Auto V',2,0,-99.00),(46,'The Witcher 3: Wild Hunt',61,0,9.99),(47,'The Witcher 3: Wild Hunt',11,0,9.99),(48,'The Witcher 3: Wild Hunt',46,0,9.99),(49,'The Witcher 3: Wild Hunt',13,0,9.99),(50,'The Witcher 3: Wild Hunt',62,0,9.99),(51,'The Witcher 3: Wild Hunt',60,0,9.99),(52,'The Witcher 3: Wild Hunt',3,0,9.99),(53,'Portal 2',12,0,2.79),(54,'Portal 2',60,0,2.79),(55,'Portal 2',2,0,2.79),(56,'Portal 2',63,0,2.79),(57,'Portal 2',46,0,2.79),(58,'Portal 2',3,0,2.79),(59,'Counter-Strike: Global Offensive',60,0,0.00),(60,'Counter-Strike: Global Offensive',63,0,0.00),(61,'Counter-Strike: Global Offensive',2,0,0.00),(62,'Counter-Strike: Global Offensive',12,0,0.00),(63,'Tomb Raider (2013)',13,0,0.00),(64,'Tomb Raider (2013)',46,0,0.00),(65,'Tomb Raider (2013)',60,0,0.00),(66,'Tomb Raider (2013)',3,0,0.00),(67,'Tomb Raider (2013)',2,0,0.00),(68,'Tomb Raider (2013)',12,0,0.00),(69,'Portal',46,0,0.85),(70,'Portal',60,0,0.85),(71,'Portal',44,0,0.85),(72,'Portal',12,0,0.85),(73,'Portal',2,0,0.85),(74,'Portal',63,0,0.85),(75,'Portal',62,0,0.85),(76,'Left 4 Dead 2',46,0,9.99),(77,'Left 4 Dead 2',63,0,9.99),(78,'Left 4 Dead 2',60,0,9.99),(79,'Left 4 Dead 2',2,0,9.99),(80,'The Elder Scrolls V: Skyrim',60,0,12.59),(81,'The Elder Scrolls V: Skyrim',61,0,12.59),(82,'The Elder Scrolls V: Skyrim',11,0,12.59),(83,'The Elder Scrolls V: Skyrim',3,0,12.59),(84,'The Elder Scrolls V: Skyrim',13,0,12.59),(85,'The Elder Scrolls V: Skyrim',62,0,12.59),(86,'The Elder Scrolls V: Skyrim',2,0,12.59),(87,'The Elder Scrolls V: Skyrim',12,0,12.59),(88,'Red Dead Redemption 2',60,0,17.59),(89,'Red Dead Redemption 2',13,0,17.59),(90,'Red Dead Redemption 2',3,0,17.59),(91,'BioShock Infinite',13,0,2.62),(92,'BioShock Infinite',2,0,2.62),(93,'BioShock Infinite',62,0,2.62),(94,'BioShock Infinite',63,0,2.62),(95,'BioShock Infinite',60,0,2.62),(96,'BioShock Infinite',12,0,2.62),(97,'BioShock Infinite',3,0,2.62),(98,'Life is Strange',60,0,5.52),(99,'Life is Strange',63,0,5.52),(100,'Life is Strange',12,0,5.52),(101,'Life is Strange',46,0,5.52),(102,'Life is Strange',43,0,5.52),(103,'Life is Strange',2,0,5.52),(104,'Life is Strange',44,0,5.52),(105,'Life is Strange',13,0,5.52),(106,'Life is Strange',3,0,5.52),(107,'Borderlands 2',12,0,3.24),(108,'Borderlands 2',46,0,3.24),(109,'Borderlands 2',60,0,3.24),(110,'Borderlands 2',44,0,3.24),(111,'Borderlands 2',63,0,3.24),(112,'Borderlands 2',39,0,3.24),(113,'Borderlands 2',2,0,3.24),(114,'Half-Life 2',60,0,7.99),(115,'Half-Life 2',46,0,7.99),(116,'Half-Life 2',2,0,7.99),(117,'Half-Life 2',63,0,7.99),(118,'Half-Life 2',41,0,7.99),(119,'Half-Life 2',44,0,7.99),(120,'BioShock',12,0,5.00),(121,'BioShock',46,0,5.00),(122,'BioShock',60,0,5.00),(123,'BioShock',2,0,5.00),(124,'Destiny 2',13,0,0.00),(125,'Destiny 2',3,0,0.00),(126,'Destiny 2',60,0,0.00),(127,'Destiny 2',64,0,0.00),(128,'Destiny 2',61,0,0.00),(129,'Destiny 2',11,0,0.00),(130,'God of War (2018)',60,0,0.00),(131,'God of War (2018)',13,0,0.00),(132,'Limbo',44,0,2.49),(133,'Limbo',39,0,2.49),(134,'Limbo',13,0,2.49),(135,'Limbo',12,0,2.49),(136,'Limbo',2,0,2.49),(137,'Limbo',63,0,2.49),(138,'Limbo',46,0,2.49),(139,'Limbo',60,0,2.49),(140,'Limbo',43,0,2.49),(141,'Limbo',3,0,2.49),(142,'Limbo',62,0,2.49),(143,'Fallout 4',3,0,12.59),(144,'Fallout 4',60,0,12.59),(145,'Fallout 4',13,0,12.59),(146,'DOOM (2016)',13,0,0.00),(147,'DOOM (2016)',62,0,0.00),(148,'DOOM (2016)',60,0,0.00),(149,'DOOM (2016)',3,0,0.00),(150,'PAYDAY 2',63,0,1.43),(151,'PAYDAY 2',60,0,1.43),(152,'PAYDAY 2',3,0,1.43),(153,'Crysis',60,0,NULL),(154,'Crysis',2,0,NULL),(155,'Crysis',12,0,NULL),(156,'Crysis 2 - Maximum Edition',60,0,NULL),(157,'Crysis 3',60,0,NULL),(158,'Crysis 3',3,0,NULL),(159,'Crysis 3',2,0,NULL),(160,'Crysis 3',12,0,NULL),(161,'Crysis Warhead',60,0,NULL),(162,'Crysis 2',60,0,NULL),(163,'Crysis 2',2,0,NULL),(164,'Crysis 2',12,0,NULL),(165,'Crysis Remastered',60,0,NULL),(166,'Crysis Remastered',3,0,NULL),(167,'Crysis Remastered',13,0,NULL),(168,'Crysis Remastered',62,0,NULL),(169,'Crysis 3 Remastered',60,0,NULL),(170,'Crysis 3 Remastered',11,0,NULL),(171,'Crysis 3 Remastered',3,0,NULL),(172,'Crysis 3 Remastered',13,0,NULL),(173,'Crysis 3 Remastered',61,0,NULL),(174,'Crysis 3 Remastered',62,0,NULL),(175,'Crysis 2 Remastered',60,0,NULL),(176,'Crysis 2 Remastered',11,0,NULL),(177,'Crysis 2 Remastered',3,0,NULL),(178,'Crysis 2 Remastered',13,0,NULL),(179,'Crysis 2 Remastered',61,0,NULL),(180,'Crysis 2 Remastered',62,0,NULL),(181,'Dino Crisis',60,0,NULL),(182,'Dino Crisis',1,0,NULL),(183,'Dino Crisis',19,0,NULL),(184,'Dino Crisis 2',60,0,NULL),(185,'Dino Crisis 2',1,0,NULL),(186,'Crisis in the Kremlin',60,0,NULL),(187,'Crisis in the Kremlin',46,0,NULL),(188,'Crisis in the Kremlin',63,0,NULL),(189,'Crisis Core: Final Fantasy VII',38,0,NULL),(190,'Crysis 3: The Lost Island',60,0,NULL),(191,'Crysis 3: The Lost Island',2,0,NULL),(192,'Crysis 3: The Lost Island',12,0,NULL),(193,'Time Crisis',1,0,NULL),(194,'Coffee Crisis',60,0,NULL),(195,'Coffee Crisis',3,0,NULL),(196,'Coffee Crisis',13,0,NULL),(197,'Coffee Crisis',62,0,NULL),(198,'Coffee Crisis',46,0,NULL),(199,'Coffee Crisis',63,0,NULL),(200,'Cuban Missile Crisis: Ice Crusade',60,0,NULL),(201,'Infinite Crisis',60,0,NULL),(202,'Crisis Core: Final Fantasy VII Reunion',60,0,NULL),(203,'Crisis Core: Final Fantasy VII Reunion',11,0,NULL),(204,'Crisis Core: Final Fantasy VII Reunion',3,0,NULL),(205,'Crisis Core: Final Fantasy VII Reunion',13,0,NULL),(206,'Crisis Core: Final Fantasy VII Reunion',61,0,NULL),(207,'Crisis Core: Final Fantasy VII Reunion',62,0,NULL),(208,'Crystal Crisis',60,0,NULL),(209,'Crystal Crisis',13,0,NULL),(210,'Crystal Crisis',62,0,NULL),(212,'Soda Crisis',60,0,NULL),(213,'Spyro: A Hero\'s Tail',41,0,NULL),(214,'Spyro: A Hero\'s Tail',7,0,NULL),(215,'Spyro: A Hero\'s Tail',8,0,NULL),(216,'Spyro: Enter the Dragonfly',7,0,NULL),(217,'Spyro: Enter the Dragonfly',8,0,NULL),(218,'Spyro 2: Ripto\'s Rage!',1,0,NULL),(219,'Spyro: Year of the Dragon',1,0,NULL),(220,'Skylanders Spyro\'s Adventure',60,0,NULL),(221,'Skylanders Spyro\'s Adventure',36,0,NULL),(222,'Skylanders Spyro\'s Adventure',46,0,NULL),(223,'Skylanders Spyro\'s Adventure',2,0,NULL),(224,'Skylanders Spyro\'s Adventure',12,0,NULL),(225,'Skylanders Spyro\'s Adventure',16,0,NULL),(226,'Skylanders Spyro\'s Adventure',9,0,NULL),(227,'Spyro Reignited Trilogy',60,0,NULL),(228,'Spyro Reignited Trilogy',3,0,NULL),(229,'Spyro Reignited Trilogy',13,0,NULL),(230,'Spyro Reignited Trilogy',62,0,NULL),(231,'Spyro: Shadow Legacy',35,0,NULL),(232,'The Legend of Spyro: Dawn of the Dragon',2,0,NULL),(233,'The Legend of Spyro: Dawn of the Dragon',12,0,NULL),(234,'The Legend of Spyro: Dawn of the Dragon',7,0,NULL),(235,'The Legend of Spyro: Dawn of the Dragon',9,0,NULL),(236,'The Legend of Spyro: A New Beginning',2,0,NULL),(237,'The Legend of Spyro: A New Beginning',41,0,NULL),(238,'The Legend of Spyro: A New Beginning',7,0,NULL),(239,'The Legend of Spyro: A New Beginning',8,0,NULL),(240,'The Legend of Spyro: A New Beginning',34,0,NULL),(241,'Spyro: Attack of the Rhynocs',34,0,NULL),(242,'Spyro: Season of Ice',34,0,NULL),(243,'Spiro, Spero',60,0,NULL),(244,'Spyro 2: Season of Flame',34,0,NULL),(245,'Spyro Orange: The Cortex Conspiracy',34,0,NULL),(246,'spyro dragon',64,0,NULL),(247,'Spyrox',60,0,NULL),(248,'Spyro The Dragon (itch)',60,0,NULL),(249,'Spyro Dating Sim (Prototype)',60,0,NULL),(250,'Spyro Dating Sim (Prototype)',44,0,NULL),(251,'Spyro Dating Sim (Prototype)',64,0,NULL),(252,'Pyro-Mite',60,0,NULL),(253,'Pyro-Mite',46,0,NULL),(254,'Arma 3',60,0,NULL),(255,'DOOM 3',60,0,NULL),(256,'DOOM 3',13,0,NULL),(257,'DOOM 3',3,0,NULL),(258,'DOOM 3',62,0,NULL),(259,'DOOM 3',46,0,NULL),(260,'DOOM 3',63,0,NULL),(261,'DOOM 3',41,0,NULL),(262,'Blitzkrieg 3',60,0,NULL),(263,'Blitzkrieg 3',46,0,NULL),(264,'Caesar 3',60,0,NULL),(265,'MegaRace 3',60,0,NULL),(266,'MegaRace 3',46,0,NULL),(267,'YORG.io 3',60,0,NULL),(268,'YORG.io 3',46,0,NULL),(269,'F.E.A.R. 3',60,0,NULL),(270,'F.E.A.R. 3',2,0,NULL),(271,'F.E.A.R. 3',12,0,NULL),(272,'Cossacks 3',60,0,NULL),(273,'Cossacks 3',63,0,NULL),(274,'Tropico 3',60,0,NULL),(275,'Tropico 3',2,0,NULL),(276,'Syphon Filter',11,0,NULL),(277,'Syphon Filter',13,0,NULL),(278,'Syphon Filter',1,0,NULL),(279,'Syphon Filter 3',1,0,NULL),(280,'Syphon Filter 2',11,0,NULL),(281,'Syphon Filter 2',13,0,NULL),(282,'Syphon Filter 2',1,0,NULL),(283,'Syphon Filter: Logan\'s Shadow',7,0,NULL),(284,'Syphon Filter: Logan\'s Shadow',38,0,NULL),(285,'Syphon Filter: Dark Mirror',7,0,NULL),(286,'Syphon Filter: Dark Mirror',38,0,NULL),(287,'Syphon Filter: The Omega Strain',7,0,NULL),(288,'Prey: Typhon Hunter',60,0,NULL),(289,'Prey: Typhon Hunter',3,0,NULL),(290,'Prey: Typhon Hunter',13,0,NULL),(291,'Songbird Symphony',60,0,NULL),(292,'Songbird Symphony',13,0,NULL),(293,'Songbird Symphony',62,0,NULL),(294,'Songbird Symphony',64,0,NULL),(295,'Killzone: Liberation and Syphon Filter: Logan\'s Shadow',38,0,NULL),(296,'Symphony',60,0,NULL),(297,'Symphony',46,0,NULL),(298,'Symphony',63,0,NULL),(299,'Castlevania: Symphony of the Night',43,0,NULL),(300,'Castlevania: Symphony of the Night',44,0,NULL),(301,'Castlevania: Symphony of the Night',2,0,NULL),(302,'Castlevania: Symphony of the Night',1,0,NULL),(303,'Castlevania: Symphony of the Night',18,0,NULL),(304,'Symphony of War: The Nephilim Saga',60,0,NULL),(305,'SOCOM: Fireteam Bravo and Syphon Filter: Dark Mirror',38,0,NULL),(306,'Blade Symphony',60,0,NULL),(307,'Jay Fighter: Remastered',60,0,NULL),(308,'Rumble Fighter: Unleashed',60,0,NULL),(309,'Queen\'s Quest 5: Symphony of Death',60,0,NULL),(310,'Queen\'s Quest 5: Symphony of Death',46,0,NULL),(311,'Queen\'s Quest 5: Symphony of Death',63,0,NULL),(312,'Color Symphony',60,0,NULL),(313,'Color Symphony',43,0,NULL),(314,'Eurofighter Typhoon',60,0,NULL),(315,'Street Fighter IV',60,0,NULL),(316,'Street Fighter IV',3,0,NULL),(317,'Street Fighter IV',43,0,NULL),(318,'Street Fighter IV',2,0,NULL),(319,'Street Fighter IV',12,0,NULL);
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
  `console_id` int NOT NULL,
  `quantity` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `game_fk_idx` (`videogame_id`),
  KEY `console_fk_idx` (`console_id`),
  KEY `library_user_fk_idx` (`user_id`),
  CONSTRAINT `game_fk` FOREIGN KEY (`videogame_id`) REFERENCES `games` (`id`),
  CONSTRAINT `library_console_fk` FOREIGN KEY (`console_id`) REFERENCES `consoles` (`id`),
  CONSTRAINT `library_user_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library`
--

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;
INSERT INTO `library` VALUES (1,1,13,1,2),(2,8,13,2,2),(3,157,60,1,2),(4,278,1,1,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,'Amazing Website','2024-03-15 22:19:53','I love the way that I can create my own video game library and then be able to see how much the collection is possibly worth.',1),(2,'I love this site','2024-03-15 22:21:12','I am looking forward to possibly selling my video game collection to other video game enthusiasts in the future.',2),(3,'Really good site','2024-03-15 22:23:23','I forgot my password, so I was happy to be able to change my password without having to contact the site\'s administrators.',3),(4,'blah blah blah','2024-05-06 01:19:23','bllllllaaaaaahhhhhh',6);
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'niatheangel','Brenda','Beach','$2b$12$8ZRKlA58QA7pdFHaUMpzWOdhpSiM0PgHJWyHCyDR00sdxSZtSOvTm','default.jpg','Admin'),(2,'testuser','Test','User','$2b$12$LUjfP38q6PLv7BB86RWmnuz42nNexNW1cQAnRz3jI58tIQsIinYby','default.jpg','Admin'),(3,'dragon2peer','David','North','$2b$12$.azK9JwUerZQ15bCkVfVveby9eBu3VwSp/dPPP75YigRPTUCYSe/W','default.jpg','User'),(4,'testuser2','test','user2','$2b$12$wswCbOB/4A9d/cQeR5hRMe8cwLVNQS8s3Rs9pz5ImDfJFoRrGM3ji','default.jpg','User'),(6,'buddy','buddy','buddy','$2b$12$LNp/GN7idDGJqFKDR06QsOymm6810uzxbnubCdK2xTBgcNg5tkMgq','default.jpg','User');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vw_consolidated`
--

DROP TABLE IF EXISTS `vw_consolidated`;
/*!50001 DROP VIEW IF EXISTS `vw_consolidated`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_consolidated` AS SELECT 
 1 AS `games_id`,
 1 AS `videogame`,
 1 AS `console`,
 1 AS `manufacturer`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vw_consolidated`
--

/*!50001 DROP VIEW IF EXISTS `vw_consolidated`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_consolidated` AS select `games`.`id` AS `games_id`,`games`.`videogame` AS `videogame`,`consoles`.`console` AS `console`,`manufacturer`.`manufacturer` AS `manufacturer` from ((`games` left join `consoles` on((`games`.`id` = `consoles`.`id`))) left join `manufacturer` on((`games`.`creator_id` = `manufacturer`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-06  0:12:40
