-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.22


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema bd1
--

CREATE DATABASE IF NOT EXISTS bd1;
USE bd1;

--
-- Definition of table `contactos`
--

DROP TABLE IF EXISTS `contactos`;
CREATE TABLE `contactos` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `apellidos` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `dirección` varchar(255) DEFAULT NULL,
  `localidad` varchar(255) DEFAULT NULL,
  `teléfono` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `hijos` int(10) unsigned DEFAULT NULL,
  `peso_kg` int(10) unsigned DEFAULT NULL,
  `altura` double(15,5) DEFAULT NULL,
  `cabello` varchar(255) DEFAULT NULL,
  `ojos_color` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contactos`
--

/*!40000 ALTER TABLE `contactos` DISABLE KEYS */;
INSERT INTO `contactos` (`ID`,`apellidos`,`nombre`,`dirección`,`localidad`,`teléfono`,`email`,`sexo`,`hijos`,`peso_kg`,`altura`,`cabello`,`ojos_color`) VALUES 
 (1,'AROCAS PASADAS','ESTEFANIA','PADRÓ , 109','Zaragoza','938205580','africa@altecom.es','F',1,73,1.62000,'Castaño','Marrones'),
 (2,'VISO GILABERT','QUERALT','CASA CORDELLAS ,','Barcelona','936545115','agata@hotmail.com','F',0,98,1.55000,'Negro','Marrones'),
 (3,'AYALA FERRERAS','JOAN','DOCTOR FLEMING , 11','Zaragoza','938202768',NULL,'M',0,61,1.67000,'Negro','Otro'),
 (4,'BAEZ TEJADO','JUAN','BERTRAND I SERRA , 11, 3R.','Zaragoza','938727844','albatros@wandoo.es','M',1,70,1.82000,'Otros','Marrones'),
 (5,'BASTARDES SOTO','MARC','CARRIÓ , 12, 5È A','Tarragona','938350521','albert@intercom.es','M',3,91,1.80000,'Negro','Azules'),
 (6,'ANGUERA VILAFRANCA','JOSEP','PIRINEUS , 10','Valencia','938755645','alien@intercom.es','M',1,53,1.66000,'Negro','Verdes'),
 (7,'PASCUAL ALOY','ESTHER','JACINT VERDAGUER , 43','Girona','936520547','amores@hotmail.com','F',0,60,1.60000,'Calvo','Otro'),
 (8,'VALLÉS GIRVENT','LAURA','NOU , 9, 2N.','Tarragona','936565656','anabel@altecom.es','F',1,70,1.70000,'Pelirrojo','Verdes'),
 (9,'RAYA GARCIA','RAQUEL','JACINT VERDAGUER , 52, 3R, 1A.','Barcelona','936752156','antiga@minorisa.es','F',1,65,1.89000,'Rubio','Azules'),
 (10,'ANDREU CRUZ','JOAN','JOAN MIRÓ , 10','Tarragona','938300025','ballador@hotmail.com','M',1,99,1.65000,'Castaño','Otro'),
 (11,'BARALDÉS COMAS','MARIA ISABEL','JAUME GALOBART , 12','Lleida','938385567','balladora@altecom.es','F',0,87,1.69000,'Otros','Otro'),
 (12,'BERENGUERAS CULLERÉS','ADRIÀ','PINTOR SERT , 12, 1R., 1A.','Valencia','937809812','barbilla@hotmail.com','M',0,92,1.78000,'Calvo','Marrones'),
 (13,'LÓPEZ DE PABLO GARCIA UCEDA','GERARD','BELLAVISTA , 30','Zaragoza','936520741','besugo@minorisa.es','M',0,66,1.87000,'Negro','Otro'),
 (14,'ARNAU MORENO','ELIOT','MONTURIOL , 10, 1R.','Girona','938202456','bogart@terra.es','M',2,53,1.79000,'Negro','Negros'),
 (15,'RAYA GAVILAN','JORDI','JACINT VERDAGUER , 52, 2N., 4A.','Lleida','938754554','bond@terra.es','M',1,101,1.67000,'Castaño','Otro'),
 (16,'ZAMBUDIO FIGULS','LLUÍS','CASA NOVA ,','Lleida','936875544',NULL,'M',1,104,1.74000,'Rubio','Verdes'),
 (17,'BIDAULT CULLERÉS','LAURA','DE LA CAÇA , 12, 1R., C','Valencia','935880712','cabeza larga@cataloniamail.com','F',0,74,1.91000,'Pelirrojo','Negros'),
 (18,'BIOSCA FONTANET','JORDI','PINTOR SERT , 12, 2N., 1A.','Zaragoza','936875255',NULL,'M',3,107,1.78000,'Calvo','Azules'),
 (19,'ZAFRA FIGULS','DOUNYA','CASA SARA ,','Tarragona','936542775',NULL,'F',1,107,1.78000,'Otros','Marrones'),
 (20,'ALEU ICART','JULIO','ARTÈS , 1, 1R, 1A.','Barcelona','938773545','cangur@intercom.es','M',0,79,1.90000,'Castaño','Azules'),
 (21,'BADIA TORNÉ','ANDREU','GENERAL PRIM , 11, 2N.','Valencia','938200022',NULL,'M',1,106,1.80000,'Rubio','Verdes'),
 (22,'MORALES GESE','RAMON','CAU DE LA GUINEU , 4','Tarragona','936512545',NULL,'M',0,70,1.86000,'Calvo','Verdes'),
 (23,'BLANCO FONTANET','DAVID-JESE','JOAN SANMARTÍ , 12, 2N., 2A.','Lleida','937785655','caparranas@altecom.es','M',1,61,1.65000,'Negro','Azules'),
 (24,'ALVAREZ FERNÁNDEZ','ARAN','PROL. PADRÓ , 1, 3R. 1A.','Madrid','938300385',NULL,'M',2,85,1.64000,'Castaño','Marrones'),
 (25,'GARCIA ALMOGUERA','GEMMA','SALLENT , 22, 2N.','Barcelona','936520471',NULL,'F',0,75,1.75000,'Pelirrojo','Azules'),
 (26,'LIBORI FIGUERAS','IVAN','JOAN MIRÓ , 3','Girona','936012445','carretero@intercom.es','M',0,88,1.60000,'Otros','Otro'),
 (27,'BIDAULT PUEYO','DAVID','LLUÍS CASTELLS , 12, 2N.','Barcelona','934500611','cela@altecom.es','M',0,102,1.54000,'Rubio','Otro'),
 (28,'BENITEZ JOSE','XAVIER','SANT VALENTÍ , 12, 1R.','Girona','937885544','coco@hotmail.com','M',2,69,1.70000,'Rubio','Azules'),
 (29,'PASCUAL FLORES','MARIO','ÀNGEL GUIMERÀ , 43, 2N','Girona','936512105','conejo@minorisa.es','M',1,73,1.59000,'Castaño','Verdes'),
 (30,'AYALA TORNÉ','JESUS','JAUME GALOBART , 11','Girona','938202200','corcel@altecom.es','M',1,71,1.88000,'Negro','Marrones'),
 (31,'LISTAN FIGUERAS','GEMMA','AVINGUDA TRES , 3, 1R., 1A.','Madrid','939965585',NULL,'F',0,77,1.75000,'Negro','Negros'),
 (32,'RASERO GAVILAN','SILVIA','JACINT VERDAGUER , 52, 2N., 1A.','Barcelona','936541235','curie@minorisa.es','F',1,104,1.76000,'Negro','Marrones'),
 (33,'ARNALOT PUIG','ALBERT','DIPUTACIÓ , 10','Lleida','938204054','dalí@wandoo.es','M',0,59,1.70000,'Pelirrojo','Verdes'),
 (34,'MOLINER GARRIDO','MARIA','VIC , 39, 1R., 2A.','Tarragona','936584541',NULL,'F',1,106,1.65000,'Pelirrojo','Azules'),
 (35,'GALOBART GARCIA','BERTA','GERMAN DURAN , 21','Zaragoza','934111475','dolça@cidet.com','F',0,58,1.63000,'Pelirrojo','Negros'),
 (36,'LÓPEZ GARRIGASSAIT','BERTA','BELLAVISTA , 30','Zaragoza','935687444','dorada@intercom.es','F',0,80,1.99000,'Otros','Verdes'),
 (37,'SÁNCHEZ GÓMEZ','MIREIA','NOU , 7, 2N.','Lleida','936658711','elisa@altecom.es','F',0,66,1.72000,'Rubio','Otro'),
 (38,'ALAVEDRA SUNYÉ','GEMMA','MANELIC , 1','Barcelona','938773941','encarna@hotmail.com','F',1,66,1.69000,'Otros','Negros'),
 (39,'ALIGUÉ BONVEHÍ','MARIA ISABEL','DE LA PESCA , 1, 1R., 1A.','Lleida','938305295','entesa@altecom.es','F',0,68,1.83000,'Pelirrojo','Otro'),
 (40,'MAS FRANCH','TONI','PIRINEUS , 34','Lleida','936524446',NULL,'M',1,54,1.60000,'Otros','Marrones'),
 (41,'ALOY COMPTE','ALEJANDRO','PROL. JACINT VERDAGUER , 1, 2N., 2A.','Madrid','938305551',NULL,'M',0,78,1.80000,'Negro','Otro'),
 (42,'ASENSIO VEGA','JOAN MARTÍ','MALLORCA , 11','Zaragoza','938206097','et@altecom.es','M',2,91,1.71000,'Rubio','Negros'),
 (43,'BIDAULT PÉREZ','INGRID','SANT BENET , 12, 2N.','Lleida','934500644',NULL,'F',0,53,1.89000,'Castaño','Marrones'),
 (44,'ALOY CODINACHS','OLIVER','PROL. PADRÓ , 1, 2N., 2A.','Lleida','938305594',NULL,'M',1,79,1.76000,'Castaño','Negros'),
 (45,'ALTIMIRAS ARMENTEROS','SANDRA','ARTÈS , 1, 2N., 2A.','Barcelona','938300422','experta@wandoo.es','F',1,110,1.62000,'Calvo','Verdes'),
 (46,'BELMONTE SÁNCHEZ','JORDI','JOAN XXIII , 12, 1R, 2A.','Madrid','938350511','f5@wandoo.es','M',1,105,1.70000,'Castaño','Azules'),
 (47,'BAJONA GARCIA','MARC','BERTRAND I SERRA , 11, 3R.','Zaragoza','938727589',NULL,'M',2,60,1.70000,'Rubio','Verdes'),
 (48,'AGUILAR RODRIGUEZ','JORDINA','LA SARDANA , 1','Barcelona','938208488',NULL,'F',0,87,1.64000,'Calvo','Marrones'),
 (49,'BARRIGA SOTO','MARIA JOSÉ','GALILEU , 12','Tarragona','938320587','fina@hotmail.com','F',2,70,1.86000,'Otros','Negros'),
 (50,'AVILA MASJUAN','RAQUEL','SANT VALENTÍ , 11','Girona','938203095','fuego@altecom.es','F',0,70,1.80000,'Negro','Otro'),
 (51,'PARRAMON FLORES','ENRIC','JOAN XXIII , 43','Barcelona','934555455',NULL,'M',0,78,1.90000,'Castaño','Otro'),
 (52,'AGUILAR RAMOS','MARTA','DE LA PAU , 1','Tarragona','938208502','garota@hotmail.com','F',2,62,1.72000,'Otros','Otro'),
 (53,'AYALA ALSINA','CARLA','SANT ANTONI MARIA CLARET , 11','Zaragoza','938205245',NULL,'F',0,103,1.70000,'Otros','Verdes'),
 (54,'ALVAREZ TROYANO','MARIA NOELIA','AVINGUDA TRES , 1, 3R., 1A.','Tarragona','938300374','gateta@cataloniamail.com','F',0,66,1.65000,'Rubio','Azules'),
 (55,'ALINS GONZÁLEZ','CRISTINA','PROL. PADRÓ , 1, 2N., 1A.','Barcelona','938305576',NULL,'F',1,102,1.78000,'Negro','Azules'),
 (56,'ACUÑA TORT','CARLOS','SANT JOAN , 0, C, 3R. A','Valencia','938208614','groucho@intercom.es','M',1,79,1.80000,'Rubio','Negros'),
 (57,'ALGUÉ TRANCHO','DAVID','PROL. JACINT VERDAGUER , 1, 1R., 1A.','Madrid','938770077','harpo@hotmail.com','M',1,82,1.70000,'Castaño','Marrones'),
 (58,'BADIA CASTILLO','CRISTIAN','JOAN XXIII , 11, 1R., 1A.','Girona','938200713','hispa@cataloniamail.com','M',1,103,1.70000,'Rubio','Marrones'),
 (59,'BENITEZ FLORES','JULIO ALBERTO','LLUÍS CASTELLS , 12, 1R.','Barcelona','938270685',NULL,'M',0,54,1.70000,'Negro','Negros'),
 (60,'TORRUELLA GARCIA','SERGI','PADRÓ , 83','Zaragoza','936021048','huevo@terra.es','M',0,66,1.80000,'Negro','Verdes'),
 (61,'ALBERICH RODRIGUEZ','ALEIX','SANT ISCLE , 1','Tarragona','938773933','james dean@intercom.es','M',2,64,1.70000,'Calvo','Negros'),
 (62,'ARMENCOT PUIG','VERÒNICA','MONTSERRAT , 10','Zaragoza','938206766','jéssica@hotmail.com','F',1,104,1.80000,'Calvo','Azules'),
 (63,'ALIGUÉ RIVERA','MARIONA','PROL. JACINT VERDAGUER , 1, 1R., 2A.','Zaragoza','938305223',NULL,'F',0,48,1.80000,'Calvo','Azules'),
 (64,'BARRIGA RIU','MARC','TRABUCAIRES , 12','Zaragoza','938325565',NULL,'M',1,89,1.80000,'Rubio','Negros'),
 (65,'PORTELLA GISPETS','GEMMA','JACINT VERDAGUER , 49, 4T., 2A.','Girona','936565448',NULL,'F',1,98,1.60000,'Otros','Marrones'),
 (66,'AGUILERA BAENA','RICARD','MANELIC , 1','Madrid','938208360',NULL,'M',0,82,1.70000,'Negro','Verdes'),
 (67,'RODRIGUEZ GARCÍA','JUAN','VERGE DE FÀTIMA , 6, BX., 2A.','Madrid','936549889','llus@hotmail.com','M',0,94,1.60000,'Calvo','Otro'),
 (68,'AGUILAR SUNYÉ','MARTA','SANT JOAN , 0, D, 3R. A','Tarragona','938208677',NULL,'F',0,91,1.70000,'Calvo','Verdes'),
 (69,'BARRIGA TARDÀ','NATÀLIA','GALILEU , 12','Madrid','938325558','madonna@wandoo.es','F',1,95,1.90000,'Calvo','Otro'),
 (70,'BARCONS LARA','MARTA','ESPORTS , 12','Barcelona','938360281','mata hari@intercom.es','F',0,110,1.90000,'Otros','Otro'),
 (71,'AGUILERA TATJÉ','LAURA','JOSEP BOIXADERAS , 1','Valencia','938208380','melanie@minorisa.es','F',1,96,1.90000,'Castaño','Azules'),
 (72,'ALEU PRAT','JOAN','CERVANTES , 1, 1R.','Girona','938770878','melquíades@hotmail.com','M',2,93,1.80000,'Calvo','Azules'),
 (73,'VALLÉS GIRVENT','ALEXIA','CERVANTES , 9, 1R.','Valencia','936874511','merche@terra.es','F',0,53,1.70000,'Calvo','Azules'),
 (74,'MOLINA GARRIDO','FERRAN','JOAN XXIII , 39','Girona','936548745','midas@cataloniamail.com','M',0,59,1.80000,'Calvo','Otro'),
 (75,'ARISSA HERMOSO','CRISTINA','DOCTOR BARNARD , 10','Tarragona','938755512','mona lisa@minorisa.es','F',0,75,1.70000,'Castaño','Azules'),
 (76,'BARALDÉS PARDO','JOSÉ ANTONIO','ESPORTS , 12','Barcelona','938722096','moro@minorisa.es','M',0,97,1.60000,'Calvo','Otro'),
 (77,'SUAREZ GARZÓN','JORDI','DE LA PAU , 8','Valencia','934512544','mozart@wandoo.es','M',1,108,1.90000,'Castaño','Negros'),
 (78,'ARPA MORENO','BEGONYA','SANT VALENTÍ , 11','Lleida','938205011',NULL,'F',1,106,1.80000,'Castaño','Verdes'),
 (79,'ALOY FARRANDO','INGRID','PROL. PADRÓ , 1, 2N., 2A.','Barcelona','938300864',NULL,'F',1,93,1.80000,'Pelirrojo','Otro'),
 (80,'LUQUE GARRIGASAIT','MIQUEL','VIC , 30 (TORROELLA)','Lleida','933256844','napoleon@cidet.com','M',0,93,1.60000,'Rubio','Azules'),
 (81,'RIDÓ GÓMEZ','AGUSTÍ','SANT ISCLE , 6','Tarragona','936528779','orondo@altecom.es','M',2,79,1.60000,'Pelirrojo','Negros'),
 (82,'SANTAMARIA FLOTATS','ANTONI','JAUME BALMES , 70, 3R, 1A.','Girona','931021886','papagayo@altecom.es','M',0,89,1.80000,'Otros','Otro'),
 (83,'HERMS GÓMEZ','JOAN','GERMAN DURAN , 27, 3R., 1A.','Zaragoza','936201457',NULL,'M',1,81,1.70000,'Pelirrojo','Otro'),
 (84,'ARTIGAS MATURANO','MÒNICA','SANT JOAN , 11','Lleida','938207515','pasión@altecom.es','F',3,100,1.90000,'Otros','Otro'),
 (85,'AGUILAR MASANA','GERARD','PUIG , 1','Madrid','938208558',NULL,'M',2,83,1.80000,'Rubio','Marrones'),
 (86,'ALTIMIRAS SERAROLS','GEMMA','PROL. JACINT VERDAGUER , 1, 2N., 2A.','Valencia','938300496','pelusa@hotmail.com','F',4,89,1.80000,'Calvo','Azules'),
 (87,'TORRESCASANA GARCIA','MARIA','RAMON I CAJAL , 81, 2N.','Lleida','930120545','perla@cataloniamail.com','F',0,63,1.80000,'Pelirrojo','Negros'),
 (88,'ARIZA PUIGBÓ','ORIOL','MORAGUES , 10','Girona','938207095',NULL,'M',1,79,1.70000,'Negro','Negros'),
 (89,'ALVAREZ ARMENTEROS','VIRGINIA','PROL. PADRÓ , 1, 3R., 2A.','Barcelona','938300214',NULL,'F',0,66,1.80000,'Negro','Marrones'),
 (90,'BARALDÉS TARRAGÓ','DAMIÀ','FRANCESC DE VITÒRIA , 11, 4T 2A','Tarragona','938727244','psicosis@intercom.es','M',0,101,1.60000,'Castaño','Negros'),
 (91,'GARCIA GARCÍA','VALENTÍ','ALBÉNIZ , 22, 2N.','Barcelona','936565874',NULL,'M',1,108,1.70000,'Otros','Azules'),
 (92,'AROCA GÓMEZ','AINA','TRES ROURES , 10, 4T 2A','Tarragona','938205782','rebeca@cataloniamail.com','F',0,95,1.80000,'Pelirrojo','Otro'),
 (93,'ALONSO RODRIGUEZ','DAVID','PROL. PADRÓ , 1, 2N., 1A.','Girona','938305551','rebelde@intercom.es','M',2,83,1.70000,'Calvo','Verdes'),
 (94,'CANO GÓMEZ','GERARD','ALBÉNIZ , 13, 2N., 1A.','Zaragoza','936577225',NULL,'M',1,69,1.70000,'Otros','Verdes'),
 (95,'ALCAIDE MOLINA','MARTA','FONT DEL GAT , 1','Lleida','938773647',NULL,'F',0,73,1.70000,'Castaño','Marrones'),
 (96,'AGUILERA PRAT','MIREIA','MONTCAU , 1','Lleida','938208054','rene@intercom.es','F',1,90,1.60000,'Negro','Marrones'),
 (97,'ALAPONT ICART','ELOI','MONTURIOL , 1','Lleida','938208054',NULL,'M',1,58,1.60000,'Rubio','Marrones'),
 (98,'RIVERO FLORIDO','ANNA','VILATORRADA , 6','Valencia','930712563','rica@terra.es','F',0,102,1.80000,'Otros','Marrones'),
 (99,'AVILA MASJUAN','ALBA','JAUME GALOBART , 11','Valencia','938204078','rockera@terra.es','F',2,76,1.60000,'Otros','Negros'),
 (100,'GRANADOS ANDRÉS','SANDRA','SANT GENÍS , 25','Barcelona','936871045',NULL,'F',1,51,1.60000,'Calvo','Marrones'),
 (101,'FERRER GASSET','ERIC','VERGE DE FÀTIMA , 2, 3R., 1A.','Valencia','938745211','roman@wandoo.es','M',0,62,1.70000,'Castaño','Negros'),
 (102,'AMIGO MODREGO','LLUÍS','JAUME I , 10','Zaragoza','938300065',NULL,'M',1,98,1.80000,'Rubio','Azules'),
 (103,'ABDIN TATJÈ','CRISTIAN','SANT JOAN , 0, C, 1R., B','Girona','938208674','romeo@intercom.es','M',0,76,1.60000,'Calvo','Marrones'),
 (104,'CANELLAS GOMEZ','GUILLEM','JACINT VERDAGUER , 13','Zaragoza','930214054',NULL,'M',0,68,1.90000,'Calvo','Verdes'),
 (105,'HIDALGO ALTIMIRAS','DIMAS','SANT BENET , 28, 2N., 2A.','Barcelona','936521404','ronc@cataloniamail.com','M',0,89,1.60000,'Rubio','Marrones'),
 (106,'BASTARDAS FRANCH','ANA INÉS','FONERIA , 12','Zaragoza','938350593','sabrosa@hotmail.com','F',0,96,1.80000,'Negro','Marrones'),
 (107,'ABADIAS MASANA','IVET','ALFONS XII , 9, 4T 1A','Zaragoza','939962045','salsa@cataloniamail.com','F',0,105,1.60000,'Castaño','Azules'),
 (108,'AREVALO SANCHEZ','JÚLIA','JAUME I , 10','Valencia','938755603',NULL,'F',0,99,1.60000,'Castaño','Marrones'),
 (109,'ALINS MULET','DANIEL','DE LA PESCA , 1, 1R., 2A.','Barcelona','938305524',NULL,'M',2,86,1.60000,'Rubio','Verdes'),
 (110,'GARCIA GONZÁLEZ','ABEL','PIRINEUS , 22','Valencia','936571974','sincer@altecom.es','M',0,83,1.90000,'Pelirrojo','Azules'),
 (111,'ALVAREZ PARCERISA','IRENE','PROL. JACINT VERDAGUER , 1, 3R., 2A.','Girona','938300036','sincera@hotmail.com','F',1,98,1.70000,'Otros','Azules'),
 (112,'CASAS ANDRÉS','ADRIÀ','JAUME GALOBART , 14','Madrid','936505455','suau@hotmail.com','M',1,100,1.80000,'Castaño','Negros'),
 (113,'MORALES GESE','JAIRO','SANT JOAN, EDIFICI D , 3R A','Barcelona','936587454','superman@altecom.es','M',0,85,1.80000,'Pelirrojo','Negros'),
 (114,'BARALDÉS MARTORELL','CRISTINA','VIC , 119, 3R., 2A.','Valencia','938725845','superwoman@wandoo.es','F',0,101,1.90000,'Calvo','Azules'),
 (115,'AROCA GÓMEZ','DAVID','CARLES BUÏGAS , 10, 1R., 1A.','Barcelona','938205730','tablon@hotmail.com','M',0,58,1.80000,'Otros','Negros'),
 (116,'RUEDA ALVAREZ','ADRIÀ','JAUME BALMES , 67, 2N.','Madrid','936828258','tendre@terra.es','M',1,76,1.70000,'Pelirrojo','Verdes'),
 (117,'ALVAREZ DOMENECH','LUCIA','PROL. PADRÓ , 1, 3R., 2A.','Valencia','938300045','teta@intercom.es','F',0,62,1.60000,'Otros','Otro'),
 (118,'BOIX GONZÁLEZ','CARLA','DE LA CAÇA , 12, 2N., C','Tarragona','936521452','tomasa@hotmail.com','F',0,49,1.60000,'Castaño','Marrones'),
 (119,'BARALDÉS MONRÓS','ADRIÀ','VIC , 119, 2N., 1A.','Valencia','938725885',NULL,'M',0,62,1.60000,'Calvo','Marrones'),
 (120,'AGUILERA MERINO','MARTA','MORAGUES , 1','Valencia','938208303','tremenda@altecom.es','F',1,75,1.80000,'Pelirrojo','Otro'),
 (121,'BAREA D\'HAENE','MARC','TRABUCAIRES , 12','Valencia','938360213','tripa@intercom.es','M',0,74,1.60000,'Pelirrojo','Marrones'),
 (122,'BARROSO D\'HAENE','ALEX','FONERIA , 12','Valencia','938320537','verruga@hotmail.com','M',0,76,1.70000,'Calvo','Verdes');
/*!40000 ALTER TABLE `contactos` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
