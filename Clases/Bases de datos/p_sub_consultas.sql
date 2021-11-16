select apellido, salario from emp
where dept_no = (select dept_no from dept where dnombre = "ventas")

select apellido, salario from emp
inner join dept on emp.Dept_No = dept.dept_no 
where dept.dnombre = "ventas"

/*EJERCICIO 1*/

SELECT Emp_No,Apellido,Fecha_Alt from emp
WHERE Fecha_Alt = (SELECT MIN(Fecha_Alt) FROM emp);

/*EJERCICIO 2*/

SELECT Apellido,Oficio from emp
where Oficio = (select Oficio from emp where Apellido = "Jimenez")

/*EJERCICIO 3*/

SELECT apellido, oficio, salario, dept_no from emp
where salario > (select max(salario) from emp where Dept_No = 30)

/*EJERCICIO 4*/

select apellido,oficio from emp
where dept_no = 20 and oficio in (select oficio from emp 
where dept_no = (select dept_no from dept where dnombre = "ventas"))

/*EJERCICIO 5*/

select apellido,oficio,salario from emp 
where salario in (select avg(salario) from emp where oficio in (select oficio from emp
where oficio <> "presidente") group by oficio) 

select apellido,oficio,salario from emp
where salario > (select avg(salario) from emp where oficio = "director") and oficio not in ("presidente")


/*EJERCICIO 6*/

select apellido,funcion from plantilla
where funcion in (select funcion from plantilla where funcion like "%enfermer%") # = enfermera/o
and hospital_cod = (select hospital_cod from hospital where nombre = "san carlos") # = 45

/*EJERCICIO 7*/
select apellido,funcion,(salario * 12) as "SALARIO ANUAL" from plantilla
where hospital_cod in (
select hospital_cod from hospital
where nombre = "General" or nombre = "provincial") # 18 y 19

/*EJERCICIO 8*/

select apellido,fecha_nac from enfermo
where str_to_Date(fecha_nac,"%d-%M-%Y") < (
SELECT str_to_Date(fecha_nac,"%d-%M-%Y") from enfermo where apellido like "%miller%") #16-sep-45

