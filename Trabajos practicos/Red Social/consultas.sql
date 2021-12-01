SELECT * FROM usuario

SELECT * FROM tipoposteo

SELECT * FROM amigos

SELECT * FROM pais

SELECT * FROM posteo

SELECT * FROM provincia

SELECT * FROM sentimental 



/*CONSULTAS DE AGREGACION*/

SELECT COUNT(id) AS"CANTIDAD DE USUARIOS",sexo AS "SEXO" FROM usuario
GROUP BY sexo

SELECT MAX(fechaCreacionCuenta) AS "Cuenta mas nueva" FROM usuario

SELECT MIN(fechaCreacionCuenta) AS "Cuenta mas vieja" FROM usuario

SELECT COUNT(id) AS "CANTIDAD DE REGISTROS CON LA LETRA A" FROM usuario
WHERE nombre LIKE "%A%"

/*CONSULTAS DE JOINS*/

SELECT usuario.nombre AS "NOMBRE USUARIO",COUNT(amigos.amigos_ID) AS "CANTIDAD DE AMIGOS" FROM usuario
INNER JOIN amigos 
ON usuario.id = amigos.usuario_ID
GROUP BY amigos.usuario_ID

SELECT posteo.titulo AS "TITULO DEL POSTEO",tipoposteo.nombre AS "TIPO DE POSTEO" FROM posteo
LEFT JOIN tipoposteo
ON posteo.tipoPosteo_ID = tipoposteo.id

SELECT posteo.titulo AS "TITULO DEL POSTEO",tipoposteo.nombre AS "TIPO DE POSTEO" FROM posteo
RIGHT JOIN tipoposteo
ON posteo.tipoPosteo_ID = tipoposteo.id

/*CONSULTAS DE FECHAS*/

SELECT  COUNT(id) AS "CANTIDAD DE REGISTROS", YEAR(fechaCreacionCuenta) AS "AÑO DE REGISTRO" FROM usuario
GROUP BY YEAR(fechaCreacionCuenta)
ORDER BY COUNT(id) DESC 

SELECT CONCAT(nombre,SPACE(1),apellido) AS "NOMBRE Y APELLIDO", DATE_FORMAT(fechaCreacionCuenta,"%Y/%m") AS "FECHA DE REGISTRO" 
FROM usuario

SELECT usuario.nombre AS "NOMBRE", posteo.titulo AS "TITULO POSTEO", DATE_FORMAT(posteo.creacionPosteo, "%Y-%M-%d" ) AS "CREACION DE POSTEO"
FROM posteo
LEFT JOIN usuario
ON posteo.usuario_ID = usuario.id

/*CONSULTAS DE TEXTO*/

SELECT CONCAT(usuario.nombre,SPACE(1),usuario.apellido,SPACE(1), "publicó",SPACE(1),"'",posteo.titulo,"'") AS "TEXTO"FROM usuario
JOIN posteo
ON posteo.usuario_ID = usuario.id 

SELECT CONCAT(usuario.nombre,SPACE(1),"es de",SPACE(1),ciudad.nombre) AS "CIUDAD DEL USUARIO" FROM usuario
JOIN ciudad
ON ciudad.id = usuario.ciudad_id

SELECT CONCAT(provincia.nombre,SPACE(1),"pertenece a",SPACE(1),pais.nombre) AS "PROVINCIA - PAIS" FROM provincia
JOIN pais
ON pais.id = provincia.pais_id

/*CONSULTAS DE CASE IF*/

SELECT usuario.nombre AS "NOMBRE USUARIO", COUNT(amigos.amigos_ID) AS "NUMERO DE AMIGOS",
	CASE
		WHEN COUNT(amigos.amigos_id) > 5 THEN "TIENE MUCHOS AMIGOS"
		WHEN COUNT(amigos.amigos_id) < 5 THEN "TIENE POCO AMIGOS"
		ELSE "TIENE LA CANTIDAD NORMAL DE AMIGOS"
	END AS "CANTIDAD DE AMIGOS"
	FROM usuario
	JOIN amigos
	ON amigos.usuario_ID = usuario.id 
	GROUP BY amigos.usuario_ID

SELECT CONCAT(COUNT(ID),SPACE(1),"PROVINCIAS PERTENECEN A") AS "CANTIDAD DE PROVINCIAS",
	CASE 
		WHEN pais_id = 1 THEN "ARGENTINA"
		WHEN pais_id = 2 THEN "BOLIVIA"
		WHEN pais_id = 3 THEN "BRASIL"
		WHEN pais_id = 4 THEN "ALEMANIA"
		WHEN pais_id = 5 THEN "ESPAÑA"
		WHEN pais_id = 6 THEN "URUGUAY"
		WHEN pais_id = 7 THEN "CHILE"
		WHEN pais_id = 8 THEN "COLOMBIA"
		WHEN pais_id = 9 THEN "ECUADOR"
		WHEN pais_id = 10 THEN "GUYANA"
		WHEN pais_id = 11 THEN "GUYANA FRANCESA"
		WHEN pais_id = 12 THEN "VENEZUELA"
		WHEN pais_id = 13 THEN "MEXICO"
		WHEN pais_id = 14 THEN "PUERTO RICO"
		WHEN pais_id = 15 THEN "PARAGUAY"
		WHEN pais_id = 16 THEN "PERU"
	END AS "PAIS"
	FROM provincia
	GROUP BY pais_id

SELECT usuario.nombre AS "NOMBRE",
CASE 
	WHEN COUNT(posteo.usuario_ID) >= 3 THEN "Tiene 3 o mas posteos"
	WHEN COUNT(posteo.usuario_ID) < 3 AND COUNT(posteo.usuario_ID) > 0 THEN "Tiene entre 1 y 2 posteos"
	ELSE "No tiene posteos"
END
FROM posteo
RIGHT JOIN usuario ON usuario.id = posteo.usuario_ID
GROUP BY usuario.nombre

/*SUBCONSULTAS*/

SELECT usuario.nombre, sentimental.nombre FROM usuario
LEFT JOIN sentimental
ON sentimental.id = usuario.sentimental_ID
WHERE sentimental.nombre IN ( SELECT nombre FROM sentimental WHERE id IN (SELECT DISTINCT(sentimental_ID) FROM usuario))

SELECT provincia.nombre AS "Provincia", pais.nombre AS "Pais" FROM provincia 
LEFT JOIN pais
ON pais.id = provincia.pais_ID
WHERE pais.nombre = (SELECT nombre FROM pais WHERE nombre = "Argentina")

SELECT usuario.nombre AS "Nombre usuario", posteo.titulo AS "Nombre posteo" FROM usuario
JOIN posteo ON posteo.usuario_ID = usuario.id 
WHERE YEAR(posteo.creacionPosteo) = (SELECT DISTINCT(YEAR(creacionPosteo)) FROM posteo WHERE YEAR(creacionPosteo) = 2021)

/*VISTAS*/

CREATE VIEW datos_usuarios AS 
SELECT usuario.nombre,usuario.apellido,sentimental.nombre AS "Situacion Sentimental", COUNT(amigos.usuario_ID) AS "Cantidad de amigos" 
FROM usuario
JOIN sentimental ON sentimental.id = usuario.sentimental_id 
JOIN amigos ON amigos.usuario_id = usuario.id
GROUP BY usuario.nombre 


SELECT * FROM datos_usuarios

CREATE VIEW posteo_informacion as
SELECT posteo.titulo, usuario.nombre AS "nombre usuario", tipoposteo.nombre AS "Tipo de posteo", posteo.creacionPosteo FROM posteo
JOIN usuario ON usuario.id = posteo.usuario_ID 
JOIN tipoposteo ON tipoposteo.id = posteo.tipoposteo_id 

SELECT * FROM posteo_informacion 

CREATE VIEW domicilio_usuarios AS 
SELECT usuario.nombre AS "Nombre usuario", ciudad.nombre AS "Ciudad", provincia.nombre AS "Provincia", pais.nombre AS "Pais" FROM usuario
JOIN ciudad ON ciudad.id = usuario.ciudad_ID
JOIN provincia ON provincia.id = ciudad.provincia_ID
JOIN pais ON pais.id = provincia.pais_ID

SELECT * FROM domicilio_usuarios 