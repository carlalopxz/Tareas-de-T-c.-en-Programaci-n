/*EJERCICIO 1*/
select nombre, apellidos from contactos
	where cabello="castaño" and ojos_color = "marrones";
/*EJERCICIO 2*/
select count(nombre)from contactos
  where ojos_color="marrones" and (cabello = "castaño" or cabello = "rubio");
/*
SELECT COUNT(id) FROM contactos
	WHERE cabello IN ("castaño", "rubio") AND ojos_color = "marrones";
*/
/*EJERCICIO 3*/
select COUNT(id),localidad, cabello FROM contactos GROUP BY localidad,cabello;
/*EJERCICIO 4*/
select localidad,count(id),cabello from contactos 
	where sexo = "F"
	group by cabello,localidad;
/*EJERCICIO 5*/
select nombre,apellidos,localidad,dirección,teléfono from contactos
	where nombre like "%J%O%"
	order by localidad,nombre ASC;
/*EJERCICIO 6*/
select localidad,count(nombre) AS "Cantidad de personas",avg(peso_kg)AS "Promedio de peso", avg(altura) AS "Promedio Altura",avg(hijos) AS "Promedio de Hijos" from contactos
	group by localidad;
/*EJERCICIO 7*/
SELECT nombre,apellidos FROM contactos
	WHERE (cabello = "pelirrojo" AND  altura > 1.70 AND sexo = "F") OR (cabello = "castaño" AND sexo = "M" AND localidad = "Madrid");
/*EJERCICIO 8*/
SELECT cabello, ojos_color,COUNT(id) AS "Cantidad de personas",round(avg(altura),2) AS "Promedio de altura" FROM contactos
	GROUP BY cabello,ojos_color;

SELECT cabello, ojos_color,COUNT(id) AS "Cantidad de personas",round(avg(altura),2) AS "Promedio de altura" FROM contactos
	WHERE altura > 1.70
	GROUP BY cabello,ojos_color;


SELECT cabello, ojos_color,COUNT(id) AS "Cantidad de personas",round(avg(altura),2) AS "Promedio de altura" FROM contactos
	GROUP BY cabello, ojos_color
	HAVING ROUND(AVG(altura),2 > 1.70);