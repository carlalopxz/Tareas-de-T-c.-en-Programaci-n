/*EJERCICIO 1*/

SELECT productos.nombre AS "NOMBRE DE PRODUCTO", marcas.nombre AS "NOMBRE DE MARCA" FROM productos
INNER JOIN marcas
ON productos.id_marca = marcas.ID;

/*EJERCICIO 2*/

SELECT productos.nombre AS "NOMBRE DE PRODUCTO", marcas.nombre AS "NOMBRE DE MARCA" FROM productos
LEFT JOIN marcas
ON productos.id_marca = marcas.ID;

/*EJERCICIO 3*/

SELECT productos.nombre AS "NOMBRE PRODUCTO", marcas.nombre AS "NOMBRE DE MARCA", productos.puntuacion FROM productos
LEFT JOIN marcas
ON productos.id_marca = marcas.id
WHERE puntuacion > 3;

/*EJERCICIO 4*/

SELECT CONCAT(clientes.nombre, " " ,clientes.apellido) AS "NOMBRE Y APELLIDO CLIENTE", productos.nombre AS "NOMBRE PRODUCTO" FROM ventas
LEFT JOIN productos ON ventas.id_producto = productos.id
LEFT JOIN clientes ON ventas.id_cliente = clientes.id;

/*EJERCICIO 5*/

SELECT CONCAT(clientes.nombre, " " ,clientes.apellido) AS "NOMBRE Y APELLIDO CLIENTE", productos.nombre AS "NOMBRE PRODUCTO", marcas.nombre AS "NOMBRE DE MARCA" FROM ventas
LEFT JOIN productos ON ventas.id_producto = productos.id 
LEFT JOIN clientes ON ventas.id_cliente = clientes.id
LEFT JOIN marcas ON marcas.ID = productos.id_marca;

/*EJERCICIO 6*/

SELECT CONCAT(clientes.nombre, " ", clientes.apellido) AS "NOMBRE Y APELLIDO CLIENTE", productos.nombre AS "NOMBRE PRODUCTO" FROM ventas
LEFT JOIN productos ON ventas.id_producto = productos.id 
LEFT JOIN clientes ON ventas.id_cliente = clientes.id
WHERE productos.nombre LIKE "%fideos%";

SELECT CONCAT(clientes.nombre, " ", clientes.apellido) AS "NOMBRE Y APELLIDO CLIENTE", productos.nombre AS "NOMBRE PRODUCTO" FROM ventas
LEFT JOIN productos ON ventas.id_producto = productos.id 
LEFT JOIN clientes ON ventas.id_cliente = clientes.id
WHERE productos.nombre LIKE "%iphone%"
ORDER BY clientes.apellido ASC;

/*EJERCICIO 7*/

SELECT productos.nombre AS "NOMBRE PRODUCTO", COALESCE(productos.modelo, "NO APLICA") AS "MODELO" FROM productos;

/*EJERCICIO 8*/

SELECT REPLACE(nombre, "TV", "TELEVISOR") FROM productos;

/*EJERCICIO 9*/

SELECT COUNT(id) AS "CANTIDAD", MAX(puntuacion) AS "PUNTUACION MAXIMA", MIN(precio) AS "PRECIO MINIMO", ROUND(AVG(puntuacion),2) AS "PROMEDIO PUNTUACION", SUM(precio) AS "SUMA PRECIOS" 
FROM productos;

/*EJERCICIO 10*/

SELECT marcas.nombre AS "NOMBRE MARCA", COUNT(productos.id_marca) AS "CANTIDAD" FROM marcas
LEFT JOIN productos
ON productos.id_marca = marcas.id
GROUP BY marcas.nombre;

/*EJERCICIO 11*/

SELECT marcas.nombre AS "NOMBRE MARCA", categorias.nombre AS "NOMBRE CATEGORIA",COUNT(productos.id_marca) AS "CANTIDAD" FROM marcas
LEFT JOIN productos
ON productos.id_marca = marcas.id
LEFT JOIN categorias
ON categorias.ID = productos.id_categoria
GROUP BY marcas.nombre, categorias.nombre;
