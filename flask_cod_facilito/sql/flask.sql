-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.32 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para flask
CREATE DATABASE IF NOT EXISTS `flask` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `flask`;

-- Volcando estructura para tabla flask.comments
CREATE TABLE IF NOT EXISTS `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `comment` text,
  `active` tinyint DEFAULT '1',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.comments: ~17 rows (aproximadamente)
INSERT INTO `comments` (`id`, `username`, `comment`, `active`, `create_date`) VALUES
	(1, 'keynerrex', 'Ya falta poco', 1, '2023-05-24 11:56:05'),
	(2, 'keynerrex', 'Bienvenido', 1, '2023-05-24 12:06:07'),
	(3, 'kina', 'Hola soy kina', 1, '2023-05-24 12:10:11'),
	(4, 'kina', 'adios', 1, '2023-05-24 12:39:21'),
	(5, 'keynerrex', 'Ya falta poco', 1, '2023-05-24 14:10:47'),
	(6, 'keynerrex', 'Y esta parte bien', 1, '2023-05-24 14:10:54'),
	(7, 'keynerrex', 'todo OK', 1, '2023-05-24 14:18:36'),
	(8, 'keynerrex', 'Bye', 1, '2023-05-24 14:18:40'),
	(9, 'keynerrex', 'web total', 1, '2023-05-25 07:24:41'),
	(10, 'keynerrex', 'terminado el web total', 1, '2023-05-25 07:38:28'),
	(11, 'keynermo', 'Hola a todos', 1, '2023-05-25 14:57:21'),
	(12, 'keynermo', 'y mi primera web fue con python', 1, '2023-05-25 14:58:53'),
	(13, 'python', 'Hola Mundo', 1, '2023-05-26 09:08:58'),
	(14, 'python', 'Hola Flask', 1, '2023-05-26 09:19:55'),
	(15, 'keynerrex', '𝐄𝐧 𝐜𝐮𝐚𝐧𝐭𝐨 𝐚𝐥 𝐭𝐞𝐦𝐚 𝐝𝐞 𝐦𝐢𝐬 𝐩𝐫𝐞𝐟𝐞𝐫𝐞𝐧𝐜𝐢𝐚𝐬 𝐞𝐧 𝐫𝐞𝐥𝐚𝐜𝐢𝐨𝐧𝐞𝐬 𝐚𝐦𝐨𝐫𝐨𝐬𝐚𝐬, 𝐝𝐞𝐛𝐨 𝐝𝐞𝐜𝐢𝐫 𝐪𝐮𝐞 𝐦𝐞 𝐚𝐭𝐫𝐚𝐞𝐧 𝐦𝐮𝐜𝐡𝐨 𝐥𝐚𝐬 𝐦𝐮𝐣𝐞𝐫𝐞𝐬 𝐦𝐚𝐲𝐨𝐫𝐞𝐬 𝐪𝐮𝐞 𝐲𝐨. 𝐍𝐨 𝐩𝐮𝐞𝐝𝐨 𝐞𝐯𝐢𝐭𝐚𝐫 𝐬𝐞𝐧𝐭𝐢𝐫 𝐮𝐧𝐚 𝐠𝐫𝐚𝐧 𝐟𝐚𝐬𝐜𝐢𝐧𝐚𝐜𝐢ó𝐧 𝐩𝐨𝐫 𝐥𝐚 𝐚𝐝𝐫𝐞𝐧𝐚𝐥𝐢𝐧𝐚 𝐪𝐮𝐞 𝐩𝐫𝐨𝐝𝐮𝐜𝐞 𝐞𝐥 𝐡𝐞𝐜𝐡𝐨 𝐝𝐞 𝐭𝐞𝐧𝐞𝐫 𝐮𝐧𝐚 𝐩𝐚𝐫𝐞𝐣𝐚 𝐪𝐮𝐞 𝐬𝐨𝐛𝐫𝐞𝐩𝐚𝐬𝐚 𝐦𝐢 𝐞𝐝𝐚𝐝. 𝐈𝐧𝐜𝐥𝐮𝐬𝐨 𝐬𝐢 𝐞𝐥𝐥𝐚𝐬 𝐬𝐞 𝐬𝐢𝐞𝐧𝐭𝐞𝐧 𝐢𝐧𝐬𝐞𝐠𝐮𝐫𝐚𝐬 𝐩𝐨𝐫 𝐚𝐥𝐠𝐮𝐧𝐨𝐬 𝐫𝐚𝐬𝐠𝐨𝐬 𝐟í𝐬𝐢𝐜𝐨𝐬 𝐪𝐮𝐞 𝐜𝐨𝐧𝐬𝐢𝐝𝐞𝐫𝐚𝐧 "𝐝𝐞𝐟𝐞𝐜𝐭𝐮𝐨𝐬𝐨𝐬", 𝐜𝐨𝐦𝐨 𝐭𝐞𝐧𝐞𝐫 𝐮𝐧 𝐜𝐮𝐞𝐫𝐩𝐨 𝐢𝐫𝐫𝐞𝐠𝐮𝐥𝐚𝐫, 𝐧𝐨 𝐜𝐮𝐦𝐩𝐥𝐢𝐫 𝐜𝐨𝐧 𝐥𝐨𝐬 𝐞𝐬𝐭á𝐧𝐝𝐚𝐫𝐞𝐬 𝐝𝐞 𝐛𝐞𝐥𝐥𝐞𝐳𝐚 𝐢𝐦𝐩𝐮𝐞𝐬𝐭𝐨𝐬 𝐩𝐨𝐫 𝐥𝐚 𝐬𝐨𝐜𝐢𝐞𝐝𝐚𝐝, 𝐭𝐞𝐧𝐞𝐫 𝐩𝐞𝐜𝐡𝐨𝐬 𝐩𝐥𝐚𝐧𝐨𝐬 𝐨 𝐜𝐚í𝐝𝐨𝐬, 𝐞𝐬𝐨 𝐧𝐨 𝐚𝐟𝐞𝐜𝐭𝐚 𝐩𝐚𝐫𝐚 𝐧𝐚𝐝𝐚 𝐦𝐢 𝐚𝐭𝐫𝐚𝐜𝐜𝐢ó𝐧 𝐡𝐚𝐜𝐢𝐚 𝐞𝐥𝐥𝐚𝐬.  𝐃𝐞 𝐡𝐞𝐜𝐡𝐨, 𝐝𝐢𝐬𝐟𝐫𝐮𝐭𝐨 𝐦𝐮𝐜𝐡𝐨 𝐢𝐧𝐭𝐞𝐫𝐚𝐜𝐭𝐮𝐚𝐫 𝐜𝐨𝐧 𝐞𝐥𝐥𝐚𝐬, 𝐞𝐬𝐜𝐮𝐜𝐡𝐚𝐫 𝐬𝐮𝐬 𝐡𝐢𝐬𝐭𝐨𝐫𝐢𝐚𝐬 𝐝𝐞 𝐯𝐢𝐝𝐚 𝐲 𝐚𝐩𝐫𝐞𝐧𝐝𝐞𝐫 𝐝𝐞 𝐬𝐮 𝐞𝐱𝐩𝐞𝐫𝐢𝐞𝐧𝐜𝐢𝐚. 𝐒𝐞𝐠𝐮𝐫𝐚𝐦𝐞𝐧𝐭𝐞, 𝐞𝐬𝐭𝐨 𝐬𝐞 𝐝𝐞𝐛𝐞 𝐚 𝐪𝐮𝐞 𝐬𝐢𝐞𝐧𝐭𝐨 𝐪𝐮𝐞 𝐩𝐮𝐞𝐝𝐨 𝐚𝐩𝐫𝐞𝐧𝐝𝐞𝐫 𝐦𝐮𝐜𝐡𝐨 𝐦á𝐬 𝐝𝐞 𝐮𝐧𝐚 𝐦𝐮𝐣𝐞𝐫 𝐦𝐚𝐲𝐨𝐫 𝐪𝐮𝐞 𝐝𝐞 𝐮𝐧𝐚 𝐦𝐮𝐣𝐞𝐫 𝐝𝐞 𝐦𝐢 𝐦𝐢𝐬𝐦𝐚 𝐞𝐝𝐚𝐝. 𝐀𝐝𝐞𝐦á𝐬, 𝐞𝐥 𝐡𝐞𝐜𝐡𝐨 𝐝𝐞 𝐪𝐮𝐞 𝐞𝐥𝐥𝐚𝐬 𝐬𝐞𝐚𝐧 𝐦𝐚𝐲𝐨𝐫𝐞𝐬 𝐪𝐮𝐞 𝐲𝐨 𝐦𝐞 𝐝𝐚 𝐮𝐧𝐚 𝐬𝐞𝐧𝐬𝐚𝐜𝐢ó𝐧 𝐝𝐞 𝐬𝐞𝐠𝐮𝐫𝐢𝐝𝐚𝐝 𝐲 𝐩𝐫𝐨𝐭𝐞𝐜𝐜𝐢ó𝐧 𝐪𝐮𝐞 𝐦𝐞 𝐫𝐞𝐬𝐮𝐥𝐭𝐚 𝐦𝐮𝐲 𝐚𝐭𝐫𝐚𝐜𝐭𝐢𝐯𝐚.  𝐀𝐬í 𝐪𝐮𝐞, 𝐞𝐧 𝐫𝐞𝐬𝐮𝐦𝐞𝐧, 𝐩𝐚𝐫𝐚 𝐦𝐚𝐧𝐭𝐞𝐧𝐞𝐫 𝐮𝐧𝐚 𝐫𝐞𝐥𝐚𝐜𝐢ó𝐧 𝐚𝐦𝐨𝐫𝐨𝐬𝐚 𝐜𝐨𝐧 𝐮𝐧𝐚 𝐦𝐮𝐣𝐞𝐫, 𝐦𝐢 ú𝐧𝐢𝐜𝐨 𝐫𝐞𝐪𝐮𝐢𝐬𝐢𝐭𝐨 𝐬𝐞𝐫í𝐚 𝐪𝐮𝐞 𝐬𝐞𝐚 𝐦𝐚𝐲𝐨𝐫 𝐪𝐮𝐞 𝐲𝐨. 𝐌𝐞 𝐞𝐧𝐜𝐚𝐧𝐭𝐚 𝐥𝐚 𝐢𝐝𝐞𝐚 𝐝𝐞 𝐞𝐬𝐭a', 1, '2023-06-06 10:59:11'),
	(16, NULL, 'uno', 1, '2023-06-08 13:26:10'),
	(17, 'keynerrex', 'uno', 1, '2023-06-08 13:27:28'),
	(18, 'keynerrex', 'uno', 1, '2023-06-08 13:28:35');

-- Volcando estructura para tabla flask.messages
CREATE TABLE IF NOT EXISTS `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message_send` text,
  `active` tinyint DEFAULT '1',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.messages: ~0 rows (aproximadamente)

-- Volcando estructura para tabla flask.rol
CREATE TABLE IF NOT EXISTS `rol` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rol` varchar(20) DEFAULT NULL,
  `active` tinyint(1) DEFAULT '1',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rol` (`rol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.rol: ~3 rows (aproximadamente)
INSERT INTO `rol` (`id`, `rol`, `active`, `create_date`) VALUES
	(1, 'Administrador', 1, '2023-09-27 14:23:12'),
	(2, 'Usuario', 1, '2023-09-27 14:23:15'),
	(3, 'Practicante', 1, '2023-09-27 14:23:18');

-- Volcando estructura para tabla flask.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `rol_id` int DEFAULT '0',
  `active` tinyint(1) DEFAULT '1',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `rol_id` (`rol_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.users: ~8 rows (aproximadamente)
INSERT INTO `users` (`id`, `username`, `email`, `password`, `rol_id`, `active`, `create_date`) VALUES
	(1, 'keynerrex', 'keyneroliveros25@gmail.com', 'pbkdf2:sha256:260000$HhYNsZBBA5Xu0tAW$f5314e11436a65330b600f4c4e3437b5736c3c01d9dd3e17c04b4d22c0296b21', 1, 1, '2023-05-24 11:55:14'),
	(2, 'kina', 'kina@gmail.com', 'pbkdf2:sha256:260000$eVYIsgUPLIyLDI7c$b94cb7ba2f894f51452ce3215bed2efea5aac1451c6e4c24efd3c42f40883f45', 2, 1, '2023-05-24 12:09:23'),
	(3, 'keynermo', 'keyneroliveros26@gmail.com', 'pbkdf2:sha256:260000$0t7b0wGHOWMjJ6Lg$b27baa6d01b62f554dd334245c54d244e42a269798761cc19ec23fc388ccf6b2', 2, 1, '2023-05-25 07:37:16'),
	(4, 'developer', 'developer@gmail.com', 'pbkdf2:sha256:260000$qpdxJAL7TGFMFDq8$439a95f69f5d8c184da33789603c1cfe635a6e2380268ce1cb90eef7c6fa792c', 2, 1, '2023-05-26 09:02:18'),
	(5, 'programer', 'programer@gmail.com', 'pbkdf2:sha256:260000$ZAUniFFlv7u9DcPY$c5250a5f6cae6daaba2a1155c1624bdca79e2617f66d4b90c9472acc2db33c30', 2, 1, '2023-05-26 09:03:29'),
	(6, 'python', 'keyneroliveros1@gmail.com', 'pbkdf2:sha256:260000$tt94QbtCgMTHJUhQ$5e3bd0167d2257df48f7f730452957f5721674ad309220868d8e88134b5b3bc1', 2, 1, '2023-05-26 09:07:51'),
	(7, 'papalote', 'keyneroliveros27@gmail.com', 'pbkdf2:sha256:260000$iVoIXK93Y8tguEqL$a77db5054768617fbad6531cabd1d8a2a405fb746e4b6e68d3e29532b5fc1548', 2, 1, '2023-06-08 13:37:00'),
	(8, 'papolote', 'keyneroliveros24@gmail.com', 'pbkdf2:sha256:260000$BxY3OpFbZKnHaJSN$641dcad492cc384ef2ea57c2e1bdb1be3b90c9ed079a077db3559c933794af08', 2, 1, '2023-06-08 13:44:40');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
