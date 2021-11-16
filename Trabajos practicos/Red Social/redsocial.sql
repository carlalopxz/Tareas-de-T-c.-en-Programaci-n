/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ redsocial /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE redsocial;

DROP TABLE IF EXISTS amigos;
CREATE TABLE `amigos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_ID` int(11) DEFAULT NULL,
  `amigos_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_ID` (`usuario_ID`),
  KEY `amigos_ID` (`amigos_ID`),
  CONSTRAINT `amigos_ibfk_1` FOREIGN KEY (`usuario_ID`) REFERENCES `usuario` (`id`),
  CONSTRAINT `amigos_ibfk_2` FOREIGN KEY (`amigos_ID`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS ciudad;
CREATE TABLE `ciudad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `provincia_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `provincia_ID` (`provincia_ID`),
  CONSTRAINT `ciudad_ibfk_1` FOREIGN KEY (`provincia_ID`) REFERENCES `provincia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS pais;
CREATE TABLE `pais` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS posteo;
CREATE TABLE `posteo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) NOT NULL,
  `usuario_ID` int(11) DEFAULT NULL,
  `tipoPosteo_ID` int(11) DEFAULT NULL,
  `creacionPosteo` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tipoPosteo_ID` (`tipoPosteo_ID`),
  KEY `usuario_ID` (`usuario_ID`),
  CONSTRAINT `posteo_ibfk_1` FOREIGN KEY (`tipoPosteo_ID`) REFERENCES `tipoposteo` (`id`),
  CONSTRAINT `posteo_ibfk_2` FOREIGN KEY (`usuario_ID`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS provincia;
CREATE TABLE `provincia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `pais_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pais_ID` (`pais_ID`),
  CONSTRAINT `provincia_ibfk_1` FOREIGN KEY (`pais_ID`) REFERENCES `pais` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS sentimental;
CREATE TABLE `sentimental` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS tipoposteo;
CREATE TABLE `tipoposteo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS usuario;
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `celular` varchar(15) DEFAULT NULL,
  `contrasenia` varchar(50) NOT NULL,
  `sexo` varchar(2) DEFAULT NULL,
  `imagenPerfil` varchar(255) DEFAULT NULL,
  `imagenPortada` varchar(255) DEFAULT NULL,
  `biografia` text DEFAULT NULL,
  `fechaCreacionCuenta` date NOT NULL,
  `sentimental_ID` int(11) DEFAULT NULL,
  `ciudad_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sentimental_ID` (`sentimental_ID`),
  KEY `ciudad_ID` (`ciudad_ID`),
  CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`sentimental_ID`) REFERENCES `sentimental` (`id`),
  CONSTRAINT `usuario_ibfk_3` FOREIGN KEY (`ciudad_ID`) REFERENCES `ciudad` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

INSERT INTO amigos(id,usuario_ID,amigos_ID) VALUES(6,2,3),(7,2,3),(8,2,4),(9,2,5),(10,2,6),(11,2,7),(12,2,8),(13,2,9),(14,2,10),(15,2,11),(16,2,12),(17,3,2),(18,3,4),(19,3,5),(20,3,6),(21,3,7),(22,3,8),(23,4,2),(24,4,3),(25,4,5),(26,4,9),(27,4,10),(28,4,11),(29,4,12),(30,5,2),(31,5,3),(32,5,4),(33,5,8),(34,5,7),(35,5,9),(36,6,2),(37,6,3),(38,6,7),(39,6,12),(40,6,11),(41,6,10),(42,6,9),(43,7,2),(44,7,3),(45,7,5),(46,7,12),(47,7,11),(48,7,10),(49,7,9),(50,8,2),(51,8,5),(52,8,11),(53,9,2),(54,9,4),(55,9,5),(56,9,6),(57,9,12),(58,9,11),(59,10,2),(60,10,4),(61,10,6),(62,10,7),(63,10,11),(64,10,12),(65,11,2),(66,11,4),(67,11,6),(68,11,7),(69,11,8),(70,11,9),(71,11,10),(72,12,2),(73,12,9),(74,12,10);

INSERT INTO ciudad(id,nombre,provincia_ID) VALUES(1,'CABA',1),(2,'Rosario',2),(3,'General Pico',3),(4,'Cataluña',4),(5,'Carmelo',5),(6,'Montevideo',6),(7,'Concordia',7),(8,'La Paz',8),(9,'Potosi',9),(10,'Trinidad',10),(11,'Rio de Janeiro',11),(12,'Cuiaba',11),(13,'Berlin',12),(14,'Hamburgo',13),(15,'Valparaiso',14);

INSERT INTO pais(id,nombre) VALUES(1,'Argentina'),(2,'Bolivia'),(3,'Brasil'),(4,'Alemania'),(5,'España'),(6,'Uruguay'),(7,'Chile'),(8,'Colombia'),(9,'Ecuador'),(10,'Guyana'),(11,'Guyana Francesa'),(12,'Venezuela'),(13,'Mexico'),(14,'Puerto Rico'),(15,'Paraguay'),(16,'Peru');

INSERT INTO posteo(id,titulo,usuario_ID,tipoPosteo_ID,creacionPosteo) VALUES(1,'Nacimiento',2,4,'2021-01-01'),(2,'Casamiento',3,1,'2006-01-01'),(3,'Dia con amigos',5,1,'2010-01-01'),(4,'Baile',6,5,'2015-01-01'),(5,'Comida',12,2,'2019-01-01'),(6,'Recuperandome',8,9,'2021-01-01'),(7,'Navidad',4,2,'2011-01-01'),(8,'Selfie',5,10,'2021-01-01'),(9,'Mi hija',3,2,'2016-01-01'),(10,'Recibido!',8,4,'2010-01-01');

INSERT INTO provincia(id,nombre,pais_ID) VALUES(1,'Buenos Aires',1),(2,'Santa Fe',1),(3,'La Pampa',1),(4,'Cataluña',5),(5,'Colonia',6),(6,'Montevideo',6),(7,'Entre Rios',1),(8,'La Paz',2),(9,'Potosi',2),(10,'Beni',2),(11,'Rio de Janeiro',3),(12,'Mato Grosso',3),(13,'Berlin',4),(14,'Hamburgo',4),(15,'Valparaiso',7),(16,'Termuco',7),(17,'Antioquia',8),(18,'Santa Elena',9),(19,'Demerara-Mahaica',10),(20,'Bolivar',12),(21,'Guadalajara',13),(22,'San Sebastian',14),(23,'San Pedro',15),(24,'Cuzco',16);

INSERT INTO sentimental(id,nombre) VALUES(1,'soltero/a'),(2,'casado/a'),(3,'en una relacion monogama'),(4,'en una relacion abierta'),(5,'es complicado'),(6,'divorciado/a'),(7,'sin apuros'),(8,'desesperao/a'),(9,'viudo/a'),(10,'comprometido/a'),(11,'en union civil');

INSERT INTO tipoposteo(id,nombre) VALUES(1,'imagen'),(2,'video'),(3,'texto'),(4,'evento'),(5,'publicidad'),(6,'contenido de marca'),(7,'encuesta'),(8,'articulo'),(9,'recuerdos'),(10,'historia instantanea');
INSERT INTO usuario(id,nombre,apellido,email,celular,contrasenia,sexo,imagenPerfil,imagenPortada,biografia,fechaCreacionCuenta,sentimental_ID,ciudad_ID) VALUES(2,'Carla','Lopez','carlalopez@gmail.com','1139876356','perro','M','URL1','URL2',NULL,'2015-01-01',1,1),(3,'Carina','Lopez','carinalopez@gmail.com','1138765384','mueble123','M','URL3','URL4',NULL,'2005-01-01',2,2),(4,'Graciela Gladis','Martinez','gracielaGM@live.com','1192384826','campo193','M','URL5','URL6',NULL,'1966-01-01',5,3),(5,'German Alexis','Gonzalez','germangonzalez187@gmail.com','3454176267','pueblo987','H','URL7','URL8',NULL,'2013-01-01',1,7),(6,'Juan Ignacio','Madrid','jimadrid@gmail.com','1187364765','computadoras','H','URL9','URL10',NULL,'2010-01-01',3,1),(7,'Rolando','Lopez','rolo@gmail.com','1187264564','plomeria','H','URL11','URL12',NULL,'1970-01-01',6,9),(8,'Emiliano','Fernandez','emifernandez@gmail.com','872654365','sistemas','H','URL13','URL14',NULL,'2001-01-01',7,10),(9,'Jesus','Aguirre','jesusaguirre@hotmail.com','11873564764','peluqueria','H','URL15','URL16',NULL,'2010-01-01',1,1),(10,'Mayra','Monteagudo','mayra@hotmail.com','1189765456','esculpidas','M','URL17','URL18',NULL,'2015-01-01',8,1),(11,'Celeste','Dominguez','celesdominguez@hotmail.com','873876356','patines','M','URL19','URL20',NULL,'2015-01-01',6,1),(12,'Cintia','Almiron','cintiaalmiron@gmail.com','871342642','tortas','M','URL21','URL22',NULL,'2005-01-01',6,7);