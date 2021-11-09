/*EJERCICIO 1*/

SELECT nombre,precio,
CASE
	WHEN precio >= 10000 THEN "MUY COSTOSO"
	WHEN precio >= 5000 THEN "COSTOSO"
	ELSE "NORMAL"
END AS "CLASIFICACION"
FROM productos;

/*EJERCICIO 2*/

SELECT nombre,
CASE
	WHEN puntuacion >= 4 THEN "MUY BUENO"
	WHEN puntuacion >= 2 THEN "BUENO"
	ELSE "REGULAR"
END AS "CLASIFICACION" 
FROM productos;

/*EJERCICIO 3*/

SELECT Apellido, Salario,Oficio, DATE_FORMAT(Fecha_Alt, "%d-%m-%Y") AS "FECHA DE ALTA", Dept_no,
CASE
	WHEN (emp.Dept_No = 10) OR (emp.Dept_No = 30) THEN "DEPARTAMENTO ELIMINADO"
	ELSE "NO SE ELIMINA"
END AS "DEPARTAMENTO"
FROM emp;

SELECT Apellido, Salario,Oficio, DATE_FORMAT(Fecha_Alt, "%d-%m-%Y") AS "FECHA DE ALTA",Dept_no,
CASE
	WHEN Dept_no IN(10,30) THEN "DEPARTAMENTO ELIMINADO"
	ELSE "NO SE ELIMINA"
END AS "DEPARTAMENTO"
FROM emp;


/*EJERCICIO 4*/

SELECT A.Apellido AS "APELLIDO",A.Salario AS "SALARIO",
CASE
	WHEN A.Salario < 100000 THEN "SE SUBE SUELDO"
	WHEN 100000 <= A.Salario >= 250000 THEN "MANTENEMOS SALARIO" 
	ELSE "SE BAJA SALARIO"
END AS "DECISION SALARIO"
FROM (SELECT Apellido, Salario FROM emp UNION ALL SELECT Apellido,Salario FROM plantilla)A;

/*EJERCICIO 5*/

SELECT T AS "TURNO",
CASE
	WHEN T = "N" THEN "NOCHE"
	WHEN T = "M" THEN "MAÑANA"
	ELSE "TARDE"
END	
FROM plantilla;

/*EJERCICIO 6*/       
/*DATE_FORMAT(STR_TO_DATE(Fecha_Nac, "%d-%b-%Y"),'%Y')*/
SELECT Apellido,Direccion, STR_TO_DATE(Fecha_Nac, "%d-%b-%Y") FROM enfermo;

SELECT CONCAT(DATE_FORMAT(Fecha_Nac,'%d-'),
CASE 
	WHEN MONTH(Fecha_Nac) = "ene" THEN 

)



SELECT 
CONCAT(
DATE_FORMAT(Fecha_Nac, '%d'), " ",(
CASE
WHEN DATE_FORMAT(Fecha_Nac, '%b') = 'ene' THEN 'jan'
WHEN DATE_FORMAT(Fecha_Nac, '%b') = 'dic' THEN 'dec'
END), " ",
DATE_FORMAT(Fecha_Nac, '%Y'))
FROM enfermo;



