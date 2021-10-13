create table bandas(
    nombre text
);
drop table bandas;
create table bandas(
    id int PRIMARY KEY AUTO_INCREMENT,
    nombre text
);
alter table bandas
    modify nombre text not null,
    add premios int;
drop table bandas;
create table bandas(
    id int PRIMARY key AUTO_INCREMENT,
    nombre text not NULL,
    premio INT
);
insert into bandas(nombre,premio)
    values("Almendra",28);
insert into bandas(nombre,premio)
    values("Pescado Rabioso",NULL),("Sui Generis",42),("Seru Giran",58);
create table artistas(
    id int primary key AUTO_INCREMENT,
    nombre text,
    apellido text,
    fechaDeNacimiento date
);
insert into artistas(nombre,apellido,fechaDeNacimiento)
    values("Luis Alberto","Spinetta","1950-01-23"),
    ("Charly","Garcia","1951-10-23"),
    ("Pedro","Aznar","1959-07-23"),
    ("David","Lebon","1952-10-05");
create table banda_artista(
    id int primary key AUTO_INCREMENT,
    idBanda int,
    idArtista int,
    FOREIGN key (idBanda) REFERENCES bandas (id),
    FOREIGN key (idArtista) REFERENCES artistas (id)
);
insert into banda_artista(idBanda,idArtista)
    values(3,4),(3,2),(4,2),(1,1),(2,1);
drop table banda_artista;
drop table bandas;
create table bandas(
    id int PRIMARY key AUTO_INCREMENT,
    nombre text not NULL,
    premio INT
);
insert into bandas(nombre,premio)
    values("Pescado Rabioso",NULL),("Sui Generis",42),("Seru Giran",58);
delete from bandas 
    where premio < 30 or premio is NULL;
alter table artistas
    add apodo text;
drop table artistas;
create table artistas(
    id int primary key AUTO_INCREMENT,
    nombre text,
    apellido text,
    fechaDeNacimiento date
);
alter table artistas
    add apodo text;
insert into artistas(nombre,apellido,fechaDeNacimiento)
    values("Luis Alberto","Spinetta","1950-01-23"),
    ("Charly","Garcia","1951-10-23"),
    ("Pedro","Aznar","1959-07-23"),
    ("David","Lebon","1952-10-05");
insert into artistas(nombre,apellido,apodo)
    values("Rodolfo","Paez","Fito");
update artistas
    set fechaDeNacimiento = "1963-03-13"
    where nombre = "Rodolfo";
update artistas
    set apodo = "El Flaco"
    where nombre = "Luis Alberto";
UPDATE artistas
    set apodo = "Sin apodo"
    WHERE apodo is NULL;
insert into artistas(nombre,apellido,fechaDeNacimiento,apodo)
    values("","","","Pappo");
update artistas
    set nombre = "Norberto Anibal",
    apellido = "Napolitano",
    fechaDeNacimiento = "1950-03-10"
    where apodo = "Pappo";