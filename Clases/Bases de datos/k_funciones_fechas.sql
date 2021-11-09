USE d_movies;

SELECT NOW()

SELECT CURDATE()

SELECT YEAR(CURDATE()) AS "AÑO ACTUAL"

SELECT MONTH(CURDATE()) AS "MES ACTUAL"

SELECT DAY(CURDATE()) AS "DIA ACTUAL"

SELECT release_date FROM episodes 

SELECT YEAR(release_date) FROM episodes

SELECT MONTH(release_date) FROM episodes 

SELECT DAY(release_date) FROM episodes

SELECT DATE_FORMAT(release_date,"%d - %M- %Y") AS "DIA - MES - AÑO" FROM episodes

SELECT DATE_FORMAT(release_date,"%d - %m- %y") AS "DIA - MES - AÑO" FROM episodes

SELECT DATE_ADD(release_date, INTERVAL 2 YEAR) AS "AGREGANDO 2 AÑOS", release_date AS "FECHA ORGINAL" FROM episodes 

SELECT DATE_ADD(release_date, INTERVAL -2 YEAR) AS "ELIMINANDO 2 AÑOS", release_date AS "FECHA ORIGINAL" FROM episodes 

SELECT DATE_SUB(release_date, INTERVAL 2 YEAR) AS "ELIMINANDO 2 AÑOS", release_date AS "FECHA ORIGINAL" FROM episodes

SELECT DATEDIFF(CURDATE(),release_date) FROM episodes #diferencia entre hoy y menos la fecha que le pasas 

