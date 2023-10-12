-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.34 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla flask.comments
CREATE TABLE IF NOT EXISTS `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `comment` text,
  `status` tinyint DEFAULT '1',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.comments: ~17 rows (aproximadamente)
DELETE FROM `comments`;
INSERT INTO `comments` (`id`, `username`, `comment`, `status`, `create_date`) VALUES
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
	(17, 'keynerrex', 'uno', 1, '2023-06-08 13:27:28'),
	(18, 'keynerrex', 'uno', 1, '2023-06-08 13:28:35'),
	(19, 'keynerrex', 'ey ola', 1, '2023-10-10 10:53:36');

-- Volcando estructura para tabla flask.medias
CREATE TABLE IF NOT EXISTS `medias` (
  `media_id` smallint NOT NULL,
  `media_name` varchar(100) NOT NULL,
  PRIMARY KEY (`media_id`,`media_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.medias: ~4 rows (aproximadamente)
DELETE FROM `medias`;
INSERT INTO `medias` (`media_id`, `media_name`) VALUES
	(1, 'GITHUB'),
	(2, 'FACEBOOK'),
	(3, 'INSTAGRAM'),
	(4, 'Prefiero no responder');

-- Volcando estructura para tabla flask.messages
CREATE TABLE IF NOT EXISTS `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message_send` text,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.messages: ~0 rows (aproximadamente)
DELETE FROM `messages`;

-- Volcando estructura para tabla flask.registers
CREATE TABLE IF NOT EXISTS `registers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `type_id` smallint NOT NULL,
  `num_id` bigint NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` bigint NOT NULL,
  `media_id` smallint DEFAULT NULL,
  `status` smallint NOT NULL DEFAULT '1',
  `create_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `num_id` (`num_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.registers: ~7 rows (aproximadamente)
DELETE FROM `registers`;
INSERT INTO `registers` (`id`, `fullname`, `type_id`, `num_id`, `email`, `phone`, `media_id`, `status`, `create_date`) VALUES
	(1, 'fgdsgds', 1, 3434, 'fgdfgfd', 4532432, 1, 1, '2023-10-10 15:21:23'),
	(2, 'hgfhgfh', 2, 545, 'gfgr', 3343, 3, 1, '2023-10-10 15:23:48'),
	(3, 'sfds', 2, 2, 'fdd', 3, 3, 1, '2023-10-10 15:25:41'),
	(4, 'santiago', 2, 544454, 'jfrjeiejifj', 4585, NULL, 1, '2023-10-10 20:59:50'),
	(5, 'dfsd', 2, 43243, 'ffdgfd', 42343, NULL, 1, '2023-10-10 21:03:46'),
	(7, 'dfsd', 2, 4324, 'frfr', 34324, 3, 1, '2023-10-10 21:04:53'),
	(8, 'ewrfe', 1, 34324, 'gfgfd', 43243, 1, 1, '2023-10-10 21:05:24'),
	(10, 'fsdfdsfdsf', 1, 45325342543, 'fdf@', 3002453456, 2, 1, '2023-10-10 21:27:09'),
	(11, 'fdsfsdfd', 1, 44443243, 'fdf@', 3303455657, 1, 1, '2023-10-10 21:30:11'),
	(12, 'fdfds', 1, 4234, 'fferfgr@', 3453212321, 2, 1, '2023-10-10 21:30:54'),
	(14, 'gfdgfdg', 1, 434324343434, 'fdf@', 3003003030, 1, 1, '2023-10-10 21:33:25'),
	(15, 'fdfdfdsfdsfef', 1, 90908, 'jefhujkh@', 9877899878, 1, 1, '2023-10-10 21:35:24'),
	(16, 'vdsfsdf', 1, 3434344, 'fdsf@', 4343242323, 1, 1, '2023-10-10 21:35:59'),
	(17, 'gfdsgfdsgf', 1, 1234567, 'dfdsfdsf@', 1234567890, 1, 1, '2023-10-10 21:36:47'),
	(18, '545345', 1, 454354334, '4554354@', 4535435454, 1, 1, '2023-10-10 21:41:45'),
	(20, 'rersdfsdfsd', 1, 343333434, 'rfefe3534@', 3432432411, 3, 1, '2023-10-10 21:42:33'),
	(21, 'kina olir', 1, 67676786, 'fhejkhf@', 6786786778, 1, 1, '2023-10-10 21:43:41'),
	(22, 'hthrthrth', 1, 43432433, 'grththt@', 1233432123, 1, 1, '2023-10-10 21:46:03'),
	(23, 'kina oribesu ', 1, 1009657, 'kdhiwo@', 4564563212, 1, 1, '2023-10-11 01:59:30'),
	(25, 'etrrtgr|1', 1, 75785785, 'hfuiegh@', 1234343212, 1, 1, '2023-10-11 02:01:17'),
	(26, 'kina florez', 5, 7665657, 'jhfkhjeio@gmail.com', 3454567610, 4, 1, '2023-10-11 02:08:05'),
	(27, 'frewfrerf', 1, 455454454, 'frdfgrgrg@', 1233211232, 1, 1, '2023-10-11 02:15:04'),
	(28, 'gfgdrtgrdtg', 1, 45454353, 'ef@', 1234567890, 1, 1, '2023-10-11 02:16:47'),
	(29, 'gdrgdfg', 1, 54543543, 'feg@', 1234567890, 1, 1, '2023-10-11 02:17:11'),
	(30, 'frfgrgertg', 1, 453214345, 'grgrg@', 1234567890, 1, 1, '2023-10-11 02:17:54'),
	(31, 'guacamole', 1, 5627278, 'jfedfio@', 1234567890, 1, 1, '2023-10-11 02:28:23'),
	(32, 'lololol', 1, 7567856756, 'lolool@', 1234567890, 1, 1, '2023-10-11 02:33:12'),
	(33, 'fefsefes', 1, 343243233, 'ojfopje@misena.edu.co', 1234567890, 1, 1, '2023-10-11 14:29:04');

-- Volcando estructura para tabla flask.rol
CREATE TABLE IF NOT EXISTS `rol` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rol` varchar(20) DEFAULT NULL,
  `status` smallint DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rol` (`rol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.rol: ~3 rows (aproximadamente)
DELETE FROM `rol`;
INSERT INTO `rol` (`id`, `rol`, `status`, `create_date`) VALUES
	(1, 'Administrador', 1, '2023-09-27 14:23:12'),
	(2, 'Usuario', 1, '2023-09-27 14:23:15'),
	(3, 'Practicante', 3, '2023-09-27 14:23:18');

-- Volcando estructura para tabla flask.types_id
CREATE TABLE IF NOT EXISTS `types_id` (
  `type_id` smallint NOT NULL AUTO_INCREMENT,
  `name_id` varchar(100) NOT NULL,
  PRIMARY KEY (`type_id`),
  UNIQUE KEY `type_id` (`type_id`),
  UNIQUE KEY `name_id` (`name_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.types_id: ~5 rows (aproximadamente)
DELETE FROM `types_id`;
INSERT INTO `types_id` (`type_id`, `name_id`) VALUES
	(1, 'CEDULA DE CIUDADANIA'),
	(3, 'CEDULA DE EXTRANJERIA'),
	(5, 'NIT'),
	(4, 'PASAPORTE'),
	(2, 'TARJETA DE IDENTIDAD');

-- Volcando estructura para tabla flask.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `rol_id` int DEFAULT '2',
  `status` smallint DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `rol_id` (`rol_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla flask.users: ~21 rows (aproximadamente)
DELETE FROM `users`;
INSERT INTO `users` (`id`, `username`, `email`, `password`, `rol_id`, `status`, `create_date`) VALUES
	(1, 'keynerrex', 'keyneroliveros25@gmail.com', 'scrypt:32768:8:1$SSa2TDTwIYEGgfAw$7ad814f6d353c2a79d159d79982e898699b844333ef9e4b1db9c30767837a918384d6ff133e43d7a17e163ce382d4f360e6cbb180a3b1423f507c80056573438', 1, 1, '2023-05-24 11:55:14'),
	(2, 'kina', 'kina@gmail.com', 'scrypt:32768:8:1$PkgPF1XPiu91l6gb$f8e519e02cce2df96b890b72897a4a482b0d4213016046437de0e153ae1920c7cf999b56d1eb9aade9736e0f8b1148d3400235cfa061a35706f90771c330b150', 2, 1, '2023-05-24 12:09:23'),
	(3, 'keynermo', 'keyneroliveros26@gmail.com', 'scrypt:32768:8:1$Sfm1yr8S8RotSbmM$561fce31d20e15576d4df856a3443a6ce3a6ffec51ecece7988d34a1f32be4ad8c6df6fb26f4e858aeb99a950bcdd558aacbf4655a895656f610da6b2e41e87a', 2, 1, '2023-05-25 07:37:16'),
	(4, 'developer', 'developer@gmail.com', 'pbkdf2:sha256:260000$qpdxJAL7TGFMFDq8$439a95f69f5d8c184da33789603c1cfe635a6e2380268ce1cb90eef7c6fa792c', 2, 2, '2023-05-26 09:02:18'),
	(5, 'programer', 'programer@gmail.com', 'pbkdf2:sha256:260000$ZAUniFFlv7u9DcPY$c5250a5f6cae6daaba2a1155c1624bdca79e2617f66d4b90c9472acc2db33c30', 2, 1, '2023-05-26 09:03:29'),
	(6, 'python', 'keyneroliveros1@gmail.com', 'pbkdf2:sha256:260000$tt94QbtCgMTHJUhQ$5e3bd0167d2257df48f7f730452957f5721674ad309220868d8e88134b5b3bc1', 2, 1, '2023-05-26 09:07:51'),
	(7, 'papalote', 'keyneroliveros27@gmail.com', 'pbkdf2:sha256:260000$iVoIXK93Y8tguEqL$a77db5054768617fbad6531cabd1d8a2a405fb746e4b6e68d3e29532b5fc1548', 2, 0, '2023-06-08 13:37:00'),
	(8, 'papolote', 'keyneroliveros21@gmail.com', 'pbkdf2:sha256:260000$BxY3OpFbZKnHaJSN$641dcad492cc384ef2ea57c2e1bdb1be3b90c9ed079a077db3559c933794af08', 2, 1, '2023-06-08 13:44:40'),
	(11, 'jhon6669_:', 'jhonsantana236@gmail.com', 'scrypt:32768:8:1$1LJzXRSWGkiGCHtw$15ff36f21653658c29f4dce7e3f1fdc369cbba90140d47c0c4e537304552fb4e72af5eaa4a3c3889ed7df123c279b67404966e7b81b879dd00cfa611738bd89d', 2, 1, '2023-10-07 18:55:38'),
	(13, 'nimu', 'keyneroliveros2232@gmail.com', 'scrypt:32768:8:1$ROtRDgISrXwujkcw$e077f549d1160d919a2ab445d3579adc27e52450cb5532ffb685b5d2f0e1a2b912eddd0852976b7c7c36ad8153ed47df6a87cafcc090178d0a8966d53fac20e5', 3, 1, '2023-10-10 11:20:39'),
	(14, 'nimuef', 'keyneroliveros276@gmail.com', 'scrypt:32768:8:1$2BL1bqE04G4uSP0u$ff8f3b24aca66d58f5fd2d54943a81c3654f9e83919fd6e89d8b5ac6929856b6fa73bdb32847c8f310a4a84d76ece9167ca35785c2fb7c45b0b2342f2ca00df4', 3, 1, '2023-10-10 11:59:43'),
	(15, 'fdsfds', 'fdfd@gmail.com', 'scrypt:32768:8:1$AMUSYxBuLKjJXiW2$08dcea7b43ef731b03bd8cb35608394ae95de94229508e03d449fa92900a997cba2a48c2229156947f4ded3a5588647d6ab1b6f2bebf116fac42a25bceb985ad', 2, 1, '2023-10-10 12:01:46'),
	(16, 'kilo', 'keyneroliveros21@gmail.com', 'scrypt:32768:8:1$15A9GtFSafx5PGjS$22f334b600ada8cfdeb6e0410df8d5e2d364f9c0c981bd3000c8138cf7f3519f4e6b5ff503cf144c79d015f3e9b872310bf6edcb285cea4d0ade38b5c4964821', 2, 1, '2023-10-10 12:17:15'),
	(17, 'fdsfsdfg', 'fgdsgrf@gmail.com', 'scrypt:32768:8:1$6mE3uHOtf9TwPFtl$45d75416067d825735448ee143a27900dd63ea32392f8f80bffe110dc678c2c89c5f96d659849258940fd4411d88754b9cb73b19f4251b2c5e31f87f86f4d71b', 2, 1, '2023-10-10 12:19:02'),
	(18, 'DFDSFH', 'iofhdih689@gmail.com', 'scrypt:32768:8:1$vKfhp4b8SWGBEjo2$2f1aa61c49c358caa19c6d7c1bf67c754f03912508292dc78dad689294e354c40059ef7a5007f9c5df33fc94e72f44d9cefb892ca4e2344d1b10d63c9eb40c0b', 2, 1, '2023-10-10 12:19:36'),
	(19, 'fdsfdsff', 'fdf@gmail.com', 'scrypt:32768:8:1$lEBBOMUVQDUVEWSX$1b737585063d2e023b9c149f497f81b9f78e76c99b868376e3d06527d8b858822d6da4aac32ce9366ccf38f0495b5a6fa55c752b9972016a585e42641664b604', 3, 1, '2023-10-10 12:19:47'),
	(20, 'sqa_', 'keyneroliveros24@gmail.com', 'scrypt:32768:8:1$lusaaCF5X0BmMzmT$7b925f378fbfe33343ef13a100166d1d74f4fbf8a80dd8be5093847aee43061f31c375c2fcc01c2892a2fc389c6ae89ebbb3bbc0574ac2a7175fd5a54ea3c740', 1, 1, '2023-10-10 12:20:42'),
	(21, 'SDSD', 'australiayt35@gmail.com', 'scrypt:32768:8:1$35HAlx0HsZVbXmQ5$c077e47946c805f6d64bb51556f7d41fcd49e1f7d08336d5471797c7f7637f46fc249694b88ef0d3a97b25a6f2986714c289ea01eb1c5a5a1ec89ccbaa77585b', 3, 1, '2023-10-10 12:21:46'),
	(22, 'gfddfhioio', 'pollitopioyt@gmail.com', 'scrypt:32768:8:1$eEg9zNuECSJPpmiJ$a46a58562298a5fe6425e215012c144572f3eb40a60b4079b108587544a8c25bd2513136e5da7626fc1b403d8c71a68571a2a7d5e392ef08507a82606cd99d38', 3, 1, '2023-10-10 12:22:11'),
	(23, 'polli', 'pollitopioyt10@gmail.com', 'scrypt:32768:8:1$ByjGP9Oe0YKCavuQ$07919b20e91a3725a72d5fa9042c829b532288629e50ea0ae3f50afe3d8d5b8822db6434cc559ca4f404c366f4a4e41a7f177da4130407d060c07f4fea384a0c', 3, 1, '2023-10-10 12:22:54'),
	(24, 'gretgregreg', 'grgrgherthjtyrghjtr@gmail.com', 'scrypt:32768:8:1$K2NW3EKtCVLbDlkK$4b7c1f6eda31adf0a541801eea64dc3a0fbc772e03667c6409b66e0cfb293bfe6eb9fe502100d463623b7ac480732873a75a6c8a3e6fde593a379ed3067f59ae', NULL, 1, '2023-10-11 14:06:44');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
