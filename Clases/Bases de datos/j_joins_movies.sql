/*EJERCICIO 1*/
SELECT genres.name AS "NOMBRE GENERO", movies.title AS "TITULO PELICULA" FROM genres
	LEFT JOIN movies
	ON movies.genre_id = genres.id
	ORDER BY NAME ASC ;

/*EJERCICIO 2*/

SELECT movies.title AS "TITULO PELICULA", genres.name AS "GENERO PELICULA",CONCAT(actors.first_name, " ",actors.last_name) AS "NOMBRE COMPLETO ACTOR"FROM movies
	LEFT JOIN genres
	ON genres.id = movies.genre_id
	LEFT JOIN actor_movie
	ON (actor_movie.movie_id = movies.id)
	LEFT JOIN actors
	ON actors.id = actor_movie.actor_id;

/*EJERCICIO 3*/

SELECT CONCAT(actors.first_name, " ", actors.last_name) AS "NOMBRE COMPLETO ACTOR", movies.title AS "TITULO PELICULA" FROM actors
	LEFT JOIN actor_movie 
	ON actor_movie.actor_id = actors.id
	LEFT JOIN movies
	ON actor_movie.movie_id = movies.id
	ORDER BY actors.first_name, actors.last_name ASC;

/*EJERCICIO 4*/
SELECT movies.title AS "TITULO PELICULA", genres.name AS "GENERO" FROM movies
	LEFT JOIN genres
	ON genres.id = movies.genre_id;
	
SELECT movies.title AS "TITULO PELICULA", genres.name AS "GENERO" FROM movies
	LEFT JOIN genres
	ON genres.id = movies.genre_id
	ORDER BY movies.title ASC;
	
SELECT movies.title AS "TITULO PELICULA", genres.name AS "GENERO" FROM movies
	LEFT JOIN genres
	ON genres.id = movies.genre_id
	ORDER BY genres.name ASC;
	
/*EJERCICIO 5*/

SELECT episodes.title AS "NOMBRE EPISODIO", seasons.number AS "NUMERO DE TEMPORADA", series.title AS "TITULO DE LA SERIE", genres.name AS "GENERO", COUNT(actor_episode.id) AS "CANTIDAD DE ACTORES" FROM episodes
	LEFT JOIN seasons ON seasons.id = episodes.season_id
	LEFT JOIN series ON series.id = seasons.serie_id
	LEFT JOIN genres ON genres.id = series.genre_id
	LEFT JOIN actor_episode ON actor_episode.episode_id = episodes.id 
	LEFT JOIN actors ON actor_episode.actor_id = actors.id
	GROUP BY  episodes.title
	
/*EJERCICIO 6*/

SELECT genres.name AS "GENERO", ROUND(AVG(movies.rating),2) AS "PROMEDIO DE RATING" FROM genres
	LEFT JOIN movies
	ON movies.genre_id = genres.id
	WHERE movies.rating > 5
	GROUP BY genres.name;

/*EJERCICIO 7*/

SELECT series.title AS "SERIE", COUNT(episodes.id) AS "CANTIDAD DE EPISODIOS" FROM episodes
	LEFT JOIN seasons
	ON episodes.season_id = seasons.id
	LEFT JOIN series
	ON series.id = seasons.serie_id
	WHERE YEAR(episodes.release_date) = '2016'
	GROUP BY series.title

/*EJERCICIO 8*/

SELECT series.title AS "SERIE", COUNT(episodes.id) AS "CANTIDAD DE EPISODIOS" FROM episodes
	LEFT JOIN seasons ON episodes.season_id = seasons.id
	LEFT JOIN series ON series.id = seasons.serie_id
	WHERE YEAR(episodes.release_date) = YEAR(CURDATE())
 	GROUP BY series.title

