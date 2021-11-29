CREATE TABLE libros(
	codigo INT PRIMARY KEY,
	titulo VARCHAR(50),
	autor VARCHAR(50),
	editorial VARCHAR(50),
	precio FLOAT
);

CREATE TABLE editoriales(
	nombre VARCHAR(50)
);


INSERT INTO libros (codigo, titulo, autor, editorial,precio)
	VALUES (1,'El aleph','Borges','Emece',23.5),
	(2,'Alicia en el pais de las maravillas','Lewis Carroll','Planeta',15),
	(3,'Matematica estas ahi','Paenza','Emece',34.6),
	(4,'Martin Fierro','Jose Hernandez','Paidos',43.5),
	(5,'Martin Fierro','Jose Hernandez','Planeta',12),
	(6,'Aprenda PHP','Mario Molina','Paidos',21.8),
	(7,'Aprenda Java','Mario Molina','Paidos',55.4),
	(8,'Alicia a traves del espejo','Lewis Carroll','Emece',18),
	(9,'Antologia poetica','Borges','Paidos',47.9);
	
INSERT INTO editoriales (nombre)
SELECT DISTINCT(editorial) FROM libros

CREATE TABLE cantidadEditorial(
	nombre VARCHAR(50),
	cantidad int
);


INSERT INTO cantidadeditorial (nombre,cantidad)
SELECT editorial, COUNT(codigo) FROM libros
GROUP BY editorial

CREATE TABLE facturas(
	numero INT AUTO_INCREMENT,
	numero_item SMALLINT,
	descripcion VARCHAR(100),
	precio_por_unidad FLOAT,
	cantidad INT,
	PRIMARY KEY(numero,numero_item)
);


INSERT INTO facturas(numero,numero_item,descripcion,precio_por_unidad,cantidad)
	VALUES (100,1,'escuadra 20 cm.',2.50,20),
	(100,2,'escuadra 50 cm.',5,30),
	(100,3,'goma lapiz-tinta',0.35,100),
	(102,1,'lapices coloresx6',4.40,50),
	(102,2,'lapices coloresx12',8,60),
	(255,1,'lapices coloresx24',12.35,100),
	(567,1,'compas plastico',12,50),
	(567,2,'compas metal',18.90,80);


CREATE TABLE montoFacturas(
	numero INT,
	total float
);

INSERT INTO montoFacturas
SELECT numero, SUM(ROUND(precio_por_unidad * cantidad,2)) FROM facturas
GROUP BY numero




