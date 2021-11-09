USE d_movies;

SELECT title FROM movies 

SELECT INSERT(title, 2, 3, "***") FROM movies

SELECT LPAD(title, 60, "*") FROM movies 

SELECT RPAD(title,60,"***") FROM movies 

SELECT TRIM(title) FROM movies 

SELECT RTRIM(title) FROM movies 

SELECT LTRIM(title) FROM movies 

SELECT CONCAT(first_name, SPACE(7),last_name) FROM actors

SELECT repeat(title, 3) FROM movies 

SELECT REPLACE(title, "a", "*") FROM movies 

SELECT REVERSE(title) FROM movies 

SELECT LEFT(title,3) FROM movies 

SELECT RIGHT(title,3) FROM movies 

SELECT LENGTH(title) FROM movies 

SELECT LOWER(title) FROM movies 

SELECT REPLACE(LOWER(title),"a","*") FROM movies 