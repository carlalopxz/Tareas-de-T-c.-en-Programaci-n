#Creacion de una base de datos
CREATE DATABASE pruebaSentencias;
#Uso de una base de datos 
USE pruebasentencias;
#Creacion de tabla
CREATE TABLE nombre_tabla(
columnaID INT PRIMARY KEY
);
#Tabla con primary key
CREATE TABLE productos(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(200) NOT NULL 
);
#Tabla con primary key auto incremental
CREATE TABLE cliente(
clienteID INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(50) NOT NULL 
);
#Tabla con Foreign key 
CREATE TABLE ordenes(
ordenID INT NOT NULL,
ordenNumero INT NOT NULL,
clienteID INT,
PRIMARY KEY(ordenID),
FOREIGN KEY (clienteID) REFERENCES cliente(clienteID)
);
#Borrado de tabla
DROP TABLE nombre_tabla;
#Modificacion de tabla
ALTER TABLE productos
	ADD apellido VARCHAR(50) NOT NULL,
	ADD edad INT,
	MODIFY nombre TEXT;
ALTER TABLE productos
	DROP edad;
#Insertar datos en una tabla 
INSERT INTO productos(nombre,apellido)
sentencias_sql	VALUES("Carla","Lopez"),("Carina","Lopez");
