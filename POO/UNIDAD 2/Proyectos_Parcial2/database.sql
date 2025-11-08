-- Ejecuta esto en tu MySQL para crear la base de datos y tabla
CREATE DATABASE IF NOT EXISTS poo_proyect_p2;
USE poo_proyect_p2;

CREATE TABLE usuarios (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL DEFAULT 'usuario'
);

INSERT INTO usuarios (usuario, password, rol) VALUES ('admin', 'admin', 'administrador');