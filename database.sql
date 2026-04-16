DROP DATABASE IF EXISTS seu_banco;
CREATE DATABASE seu_banco;
USE seu_banco;

CREATE TABLE usuarios (
   id INT PRIMARY KEY AUTO_INCREMENT,
   email VARCHAR(100) UNIQUE NOT NULL,
   senha VARCHAR(255) NOT NULL,
   ativo TINYINT(1) DEFAULT 1,
   tentativas_login INT DEFAULT 0,
   ultimo_login DATETIME NULL
);

INSERT INTO usuarios (email, senha, ativo, tentativas_login, ultimo_login)
VALUES ('admin@gmail.com', 'scrypt:32768:8:1$BIt9kMKh6PGTWZFl$85e1b4ded0b3c6afd811e5664828038857fd40e4814c3b1bdf7974b5dd0df8a894f0348c3f48eea4da2bdee5c2efa8f14532c7d8e80e6d4fdbc0cb7f9dbb92e2', 1, 0, NULL);