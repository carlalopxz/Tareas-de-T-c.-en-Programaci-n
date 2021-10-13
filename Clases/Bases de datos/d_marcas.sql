-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.1.38-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win32
-- HeidiSQL Versión:             10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para marcas
CREATE DATABASE IF NOT EXISTS `marcas` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `marcas`;

-- Volcando estructura para tabla marcas.categorias
CREATE TABLE IF NOT EXISTS `categorias` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` text NOT NULL,
  `id_categoria_padre` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla marcas.categorias: ~22 rows (aproximadamente)
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` (`ID`, `nombre`, `id_categoria_padre`) VALUES
	(1, 'Electrodomesticos', 0),
	(2, 'Consolas y videojuegos', 0),
	(3, 'Celulares', 0),
	(4, 'Aires Acondicionados', 0),
	(5, 'Informatica', 0),
	(6, 'Comida', 0),
	(7, 'Bebida', 0),
	(8, 'Fruta', 6),
	(9, 'Carnes', 6),
	(10, 'Gaseosa', 7),
	(11, 'Bebidas Alcoholicas', 7),
	(12, 'Aguas saborizadas', 7),
	(13, 'Aguas', 7),
	(14, 'Portatiles', 2),
	(15, 'Hornos', 1),
	(16, 'Lavarropas', 1),
	(17, 'Heladeras', 1),
	(18, 'Microndas', 1),
	(19, 'Aires Acondicionados frio', 4),
	(20, 'Aires acondicionados frio/calor', 4),
	(21, 'Computadoras', 5),
	(22, 'Impresoras', 5),
	(23, 'Notebooks', 5),
	(24, 'Televisores', 0),
	(25, 'Pasta', 6);
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;

-- Volcando estructura para tabla marcas.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` tinytext,
  `apellido` tinytext,
  `email` tinytext,
  `telefono` tinytext,
  `celular` tinytext,
  `fecha_de_nacimiento` datetime DEFAULT NULL,
  `id_producto_preferido` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `producto` (`id_producto_preferido`),
  CONSTRAINT `producto` FOREIGN KEY (`id_producto_preferido`) REFERENCES `productos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla marcas.clientes: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`id`, `nombre`, `apellido`, `email`, `telefono`, `celular`, `fecha_de_nacimiento`, `id_producto_preferido`) VALUES
	(1, 'Sacha', 'Lifszyc', 'sacha.lifzyc@gmail.com', '46319613', '1153980907', '1990-08-12 18:52:29', 27),
	(4, 'Dario ', 'Ramirez', 'dario.Ramirez@gmail.com', '49968901', '1130315490', '1990-10-03 18:59:16', 22),
	(7, 'Javier', 'Herrera', 'javier.herrera@gmail.com', '43562718', '1123657890', '1990-04-08 19:17:53', 24),
	(9, 'Lucas', 'Croci', 'lucas.croci@gmail.com', '45672310', '1132567845', '1990-04-10 19:20:40', 8),
	(11, 'Martina', 'Zapata', 'martina.zapata@gmail.com', '478902345', '1123450970', '1992-10-08 19:21:57', 17),
	(14, 'Laura', 'Cortez', 'Laura.Cortez@gmail.com', '42678901', '1123657808', '1991-12-08 19:26:29', 21);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla marcas.marcas
CREATE TABLE IF NOT EXISTS `marcas` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` tinytext,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla marcas.marcas: ~17 rows (aproximadamente)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` (`ID`, `nombre`) VALUES
	(1, 'HP'),
	(2, 'Samsung'),
	(3, 'Toshiba'),
	(4, 'TP Link'),
	(5, 'Sony'),
	(6, 'Nintendo'),
	(7, 'Microsoft'),
	(8, 'Apple'),
	(9, 'Motorola'),
	(10, 'Sanyo'),
	(11, 'Phillips'),
	(12, 'Philco'),
	(13, 'LG'),
	(14, 'Panasonic'),
	(15, 'Coca-Cola'),
	(16, 'Sprite'),
	(17, 'Ser'),
	(18, 'Quilmes'),
	(19, 'Stella Artois'),
	(20, 'Patagonia');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;

-- Volcando estructura para tabla marcas.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` text,
  `modelo` text,
  `descripcion` text,
  `precio` float DEFAULT NULL,
  `puntuacion` float DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `id_marca` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `categoria` (`id_categoria`),
  KEY `marca` (`id_marca`),
  CONSTRAINT `categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `marca` FOREIGN KEY (`id_marca`) REFERENCES `marcas` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla marcas.productos: ~27 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id`, `nombre`, `modelo`, `descripcion`, `precio`, `puntuacion`, `id_categoria`, `id_marca`) VALUES
	(1, 'TV LED 32', 'SY-XFJQLP', 'Este televisior tiene una pantalla grande', 8000, 3.1, 1, 10),
	(2, 'Manzana roja', NULL, 'manzana roja orifen nacional', 5, 2.5, 8, NULL),
	(3, 'Manzana verde', NULL, 'Manzana verde origen nacional', 5, 2.5, 8, NULL),
	(4, '1kg de bife', NULL, NULL, 129, 3.4, 10, NULL),
	(5, '1kg de lechuga de pollo', NULL, NULL, 105, 3, 10, NULL),
	(6, 'fideos tricolor', NULL, 'fideos de zapallo zanahoria y acelga', 40, 1.9, 6, NULL),
	(7, 'caja de ravioles de verdura', NULL, 'los mejores ravioles de argentina', 64, 2.4, 6, NULL),
	(8, 'caracolitos', NULL, 'rica pasta', 38, 0.9, 6, NULL),
	(9, 'Playsation 3', 'slim', 'con 2 jostick', 7000, 3.6, 2, 5),
	(10, 'Playstation 4', NULL, 'con 1 solo jostick', 8000, 4.1, 2, 5),
	(11, 'Playstation 4 Slim', 'slim', 'ultimo modelo, mas finita', 8500, 4.3, 2, 5),
	(12, 'Wii', 'blanca 250gb', 'Nintendo Wii excelente para jugar en familia', 7000, 3.2, 2, 6),
	(13, 'wii-U', 'con mando externo tipo iPad', 'buena wii', 8000, 3.6, 2, 6),
	(14, 'Nintendo Switch', 'la ultima consola de Nintendo', 'mama mia', 12000, 4.6, 2, 14),
	(15, 'TV Samsung 3D ', 'smg-3d', 'alta tele', 25000, 3.7, 24, 14),
	(16, 'Smart TV Panasonic', 'PNSC-SMJ', 'excelente para mirar futbol', 26000, 4, 24, 8),
	(17, 'iphone 6s', '64gb negro', 'nice', 14000, 4, 14, 8),
	(18, 'iphone 6s', '128 gb negro', 'buena capacidad', 17000, 4.5, 14, 8),
	(19, 'iphone 7', '128 gb negro', 'buena capacidad', 24000, 4.8, 14, 15),
	(20, 'Coca-cola', '1.5lts', 'coca', 75, 4.2, 7, 15),
	(21, 'Coca-cola', '2.25lts', 'coca grande', 100, 3.8, 7, 16),
	(22, 'Sprite', '1.5lts', 'sprite', 100, 3.6, 7, 17),
	(23, 'Agua sabor pomelo', '1.5lts', 'agua copada', 75, 3.4, 12, 17),
	(24, 'agua sabor naranja', '1.5lts', 'agua saborizada', 75, 3.5, 12, 17),
	(25, 'Cerveza quilmes', '1lt', 'el sabor del encuentro', 65, 2.2, 11, 18),
	(26, 'Cerveza stella artois', '1lt', 'ella es unica', 85, 3.2, 11, 19),
	(27, 'Cerveza artesanal patagonia', '750cc', 'la mas rica', 100, 4.3, 11, 20);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla marcas.ventas
CREATE TABLE IF NOT EXISTS `ventas` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `cliente` (`id_cliente`),
  KEY `productos` (`id_producto`),
  CONSTRAINT `cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productos` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla marcas.ventas: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` (`ID`, `id_cliente`, `id_producto`) VALUES
	(1, 14, 7),
	(2, 14, 21),
	(3, 1, 6),
	(4, 4, 26),
	(6, 9, 4),
	(7, 11, 2),
	(8, 14, 10),
	(9, 11, 16),
	(10, 7, 6),
	(11, 1, 7),
	(12, 9, 23),
	(13, 7, 6);
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
