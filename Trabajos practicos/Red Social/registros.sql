/*CREACION DE REGISTROS */

/*REGISTROS DE TIPO DE POSTEO*/

INSERT INTO tipoposteo (nombre)
	VALUES ("imagen"),("video"),("texto"),("evento"),("publicidad"),
	("contenido de marca"),("encuesta"),("articulo"),("recuerdos"),("historia instantanea");

/*REGISTROS DE SENTIMENTAL*/

INSERT INTO sentimental(nombre)
	VALUES ("soltero/a"),("casado/a"),("en una relacion monogama"),("en una relacion abierta"),
	("es complicado"),("divorciado/a"),("sin apuros"),("desesperao/a"),("viudo/a"),("comprometido/a"),("en union civil");

/*REGISTROS DE PAIS*/

INSERT INTO pais (nombre)
	VALUES ("Argentina"),("Bolivia"),("Brasil"),("Alemania"),("España"),("Uruguay"),("Chile"),("Colombia"),("Ecuador"),
	("Guyana"),("Guyana Francesa"),("Venezuela"),("Mexico"),("Puerto Rico"),("Paraguay"),("Peru");

/*REGISTROS DE PROVINCIA*/

INSERT INTO provincia (nombre, pais_ID)
	VALUES ("CABA",1),("Santa Fe",1),("La Pampa",1),("Cataluña",5),("Colonia",6),("Montevideo",6),("Entre Rios",1),("La Paz",2),
	("Potosi",2),("Beni",2),("Rio de Janeiro",3),("Mato Grosso",3),("Berlin",4),("Hamburgo",4),("Valparaiso",7),("Termuco",7),
	("Antioquia",8),("Santa Elena",9),("Demerara-Mahaica",10),("Bolivar",12),("Guadalajara",13),("San Sebastian",14),
	("San Pedro",15),("Cuzco",16);
	
/*MODIFICACION TABLA PROVINCIA*/

UPDATE provincia
	SET nombre = "Buenos Aires"
	WHERE nombre = "CABA";
	
/*REGISTROS DE CIUDAD*/

INSERT INTO ciudad(nombre,provincia_ID)
	VALUES("CABA",1),("Rosario",2),("General Pico",3),("Cataluña",4),("Carmelo",5),("Montevideo",6),("Concordia",7),
	("La Paz",8),("Potosi",9),("Trinidad",10),("Rio de Janeiro",11),("Cuiaba",11),("Berlin",12),("Hamburgo",13),
	("Valparaiso",14);

/*REGISTROS DE USUARIO*/

INSERT INTO usuario (nombre,apellido,email,contrasenia,sexo,imagenPerfil,imagenPortada,biografia,celular,fechaCreacionCuenta,ciudad_ID,sentimental_ID)
	VALUES ("Carla","Lopez","carlalopez@gmail.com","perro","M","URL1","URL2",NULL,"1139876356",2015/01/01,1,1);

UPDATE usuario
	SET fechaCreacionCuenta = STR_TO_DATE("2015-01-01","%Y-%m-%d")
	WHERE fechaCreacionCuenta = 0000-00-00

INSERT INTO usuario (nombre,apellido,email,contrasenia,sexo,imagenPerfil,imagenPortada,biografia,celular,fechaCreacionCuenta,ciudad_ID,sentimental_ID)
	VALUES ("Carina","Lopez","carinalopez@gmail.com","mueble123","M","URL3","URL4",NULL,"1138765384",STR_TO_DATE("2005-01-01","%Y-%m-%d"),2,2);
	
INSERT INTO usuario (nombre,apellido,email,contrasenia,sexo,imagenPerfil,imagenPortada,biografia,celular,fechaCreacionCuenta,ciudad_ID,sentimental_ID)
	VALUES ("Graciela Gladis","Martinez","gracielaGM@live.com","campo193","M","URL5","URL6",NULL,"1192384826",STR_TO_DATE("1966-01-01","%Y-%m-%d"),3,5),
	("German Alexis", "Gonzalez","germangonzalez187@gmail.com","pueblo987","H","URL7","URL8",NULL,"3454176267",STR_TO_DATE("2013-01-01","%Y-%m-%d"),7,1),
	("Juan Ignacio","Madrid","jimadrid@gmail.com","computadoras","H","URL9","URL10",NULL,"1187364765",STR_TO_DATE("2010-01-01","%Y-%m-%d"),1,3),
	("Rolando","Lopez","rolo@gmail.com","plomeria","H","URL11","URL12",NULL,"1187264564",STR_TO_DATE("1970-01-01","%Y-%m-%d"),9,6),
	("Emiliano","Fernandez","emifernandez@gmail.com","sistemas","H","URL13","URL14",NULL,"872654365",STR_TO_DATE("2001-01-01","%Y-%m-%d"),10,7),
	("Jesus","Aguirre","jesusaguirre@hotmail.com","peluqueria","H","URL15","URL16",NULL,"11873564764",STR_TO_DATE("2010-01-01","%Y-%m-%d"),1,1),
	("Mayra","Monteagudo","mayra@hotmail.com","esculpidas","M","URL17","URL18",NULL,"1189765456", STR_TO_DATE("2015-01-01","%Y-%m-%d"),1,8),
	("Celeste","Dominguez","celesdominguez@hotmail.com","patines","M","URL19","URL20", NULL,"873876356", STR_TO_DATE("2015-01-01","%Y-%m-%d"),1,6),
	("Cintia","Almiron","cintiaalmiron@gmail.com","tortas","M","URL21","URL22", NULL,"871342642",STR_TO_DATE("2005-01-01","%Y-%m-%d"),7,6);

/*REGISTROS DE LA TABLA AMIGOS*/

INSERT INTO amigos(usuario_ID, amigos_ID)
	VALUES (2,3)

INSERT INTO amigos(usuario_ID,amigos_ID)
	VALUES (2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(2,11),(2,12),
	(3,2),(3,4),(3,5),(3,6),(3,7),(3,8),
	(4,2),(4,3),(4,5),(4,9),(4,10),(4,11),(4,12),
	(5,2),(5,3),(5,4),(5,8),(5,7),(5,9),
	(6,2),(6,3),(6,7),(6,12),(6,11),(6,10),(6,9),
	(7,2),(7,3),(7,5),(7,12),(7,11),(7,10),(7,9),
	(8,2),(8,5),(8,11),
	(9,2),(9,4),(9,5),(9,6),(9,12),(9,11),
	(10,2),(10,4),(10,6),(10,7),(10,11),(10,12),
	(11,2),(11,4),(11,6),(11,7),(11,8),(11,9),(11,10),
	(12,2),(12,9),(12,10);

/*REGISTRO DE POSTEO*/

INSERT INTO posteo(titulo, usuario_ID, tipoPosteo_ID,creacionPosteo)
	VALUES ("Nacimiento",2,4,STR_TO_DATE("2021-01-01","%Y-%m-%d")),
	("Casamiento",3,1,STR_TO_DATE("2006-01-01","%Y-%m-%d")),
	("Dia con amigos",5,1,STR_TO_DATE("2010-01-01","%Y-%m-%d")),
	("Baile",6,5,STR_TO_DATE("2015-01-01","%Y-%m-%d")),
	("Comida",12,2,STR_TO_DATE("2019-01-01","%Y-%m-%d")),
	("Recuperandome",8,9,STR_TO_DATE("2021-01-01","%Y-%m-%d")),
	("Navidad",4,2,STR_TO_DATE("2011-01-01","%Y-%m-%d")),
	("Selfie",5,10,STR_TO_DATE("2021-01-01","%Y-%m-%d")),
	("Mi hija",3,2,STR_TO_DATE("2016-01-01","%Y-%m-%d")),
	("Recibido!",8,4,STR_TO_DATE("2010-01-01","%Y-%m-%d"))