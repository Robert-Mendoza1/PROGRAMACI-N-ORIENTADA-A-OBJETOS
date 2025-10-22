

CREATE TABLE usuarios (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    -- VARCHAR(60) es el tamaño mínimo para un hash bcrypt, pero un poco más es seguro
    hashed_password VARCHAR(255) NOT NULL
);