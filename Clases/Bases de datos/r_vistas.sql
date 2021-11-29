/*VISTAS*/


CREATE VIEW vistasalarios AS 
SELECT plantilla.apellido,plantilla.funcion,(plantilla.salario * 13) as "SALARIO ANUAL",hospital.nombre AS "NOMBRE HOSPITAL" 	FROM plantilla
JOIN hospital ON plantilla.hospital_cod = hospital.hospital_cod
WHERE plantilla.hospital_cod IN ( select hospital_cod from hospital
WHERE nombre IN("general","provincial"))

SELECT * FROM vistasalarios

SELECT apellido FROM vistasalarios 

SELECT `SALARIO ANUAL` FROM vistasalarios