CREATE DATABASE b_sentencias_sql;
USE b_sentencias_sql;

DROP TABLE IF EXISTS agenda;

CREATE TABLE agenda(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
	domicilio VARCHAR(30) NOT NULL,
	telefono INT(11)
);
INSERT INTO agenda(nombre,domicilio,telefono)
	VALUES("Alberto Mores","Colon 123","4234567"),
	("Juan Torres","Avellaneda 135","4458787"),
	("Roberto Carlos","Gascon 135","48952233");

DROP TABLE IF EXISTS libros;

CREATE TABLE libros(
	id INT PRIMARY KEY AUTO_INCREMENT,
	titulo VARCHAR(20),
	autor VARCHAR(30),
	editorial VARCHAR(15)
);

INSERT INTO libros(titulo, autor,editorial)
	VALUES("El Aleph","Borges","Planeta"),
	("Martin Fierro","Jose Hernandez","Emece"),
	("Aprenda PHP","Mario Molina","Emece");
	
DROP TABLE IF EXISTS agenda;

CREATE TABLE agenda(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
	domicilio VARCHAR(30) NOT NULL,
	telefono INT(11)
);

INSERT INTO agenda(nombre,domicilio,telefono)
	VALUES("Alberto Mores","Colon 123","4234567"),
	("Juan Torres","Avellaneda 135","4458787"),
	("Roberto Carlos","Gascon 135","4545454"),
	("Lopez Jose","Urquiza 333","4545454");
INSERT INTO agenda(nombre,domicilio,telefono)
	VALUES("Peralta Susana","Gral Paz 1234","4123456");

DELETE FROM agenda
	WHERE nombre = "Juan Torres" OR domicilio = "Urquiza 333";

DELETE FROM agenda
	WHERE telefono = "4545454";
	
DROP TABLE IF EXISTS agenda;

CREATE TABLE agenda(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
	domicilio VARCHAR(30) NOT NULL,
	telefono INT(11)
);

INSERT INTO agenda(nombre,domicilio,telefono)
	VALUES("Alberto Mores","Colon 123","4234567"),
	("Juan Torres","Avellaneda 135","4458787"),
	("Roberto Carlos","Gascon 135","4545454"),
	("Lopez Jose","Urquiza 333","4545454"),
	("Peralta Susana","Gral. Paz 1234","4123456");

UPDATE agenda
	SET nombre = "Juan Pablo"
	WHERE nombre= "Juan Torres";

UPDATE agenda
	SET telefono = "4445566"
	WHERE telefono = "4545454";
	
UPDATE agenda 
	SET nombre = "Juan Jose"
	WHERE nombre = "Juan";

