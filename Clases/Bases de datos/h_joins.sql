/*El INNER JOIN solo me trae registros relacionados*/
SELECT productos.nombre AS "NOMBRE PRODUCTO", marcas.nombre AS "NOMBRE MARCA" FROM productos
INNER JOIN marcas
ON productos.id_marca = marcas.ID;

SELECT productos.nombre, categorias.nombre FROM productos
INNER JOIN categorias
ON productos.id_categoria = categorias.ID;

SELECT COUNT(productos.id) AS "Cantidad de productos", ROUND(AVG(productos.precio),2) AS "Promedio de precio", categorias.nombre FROM productos
INNER JOIN categorias
ON productos.id_categoria = categorias.ID
WHERE precio > 75
GROUP BY categorias.nombre;

SELECT productos.nombre AS "NOMBRE PRODUCTO", marcas.nombre AS "NOMBRE MARCA", categorias.nombre AS "NOMBRE CATEGORIAS" FROM productos
INNER JOIN marcas ON productos.id_marca = marcas.ID
INNER JOIN categorias ON productos.id_categoria = categorias.ID;

/*El LEFT JOIN me devuelve todos los registros de productos y si hay marcas que no tienen coincidencia 
  me devuleve NULL*/
SELECT productos.nombre AS "NOMBRE PRODUCTO", marcas.nombre AS "NOMBRE MARCA" FROM productos
LEFT JOIN marcas
ON productos.id_marca = marcas.ID;

/*El RIGTH JOIN me devuelve todos los registros de marcas y si no hay productos con marca me devuelve
	null*/
SELECT productos.nombre AS "NOMBRE PRODUCTO", marcas.nombre AS "NOMBRE MARCA" FROM productos
RIGHT JOIN marcas
ON productos.id_marca = marcas.ID;

/*UNION ALL = OUTER JOIN, me trae todos los registros en una misma fila*/

SELECT nombre FROM productos
UNION ALL
SELECT nombre FROM marcas;


