CREATE DATABASE IF NOT EXISTS python_console;
USE python_console;

CREATE TABLE IF NOT EXISTS users (
    id INT(25) AUTO_INCREMENT,
    first_name VARCHAR(100),
    second_name VARCHAR(100),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    date DATE NOT NULL,

    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS notes(
    id INT(25) AUTO_INCREMENT,
    user_id INT(25) NOT NULL,
    title VARCHAR(255) NOT NULL,
    content MEDIUMTEXT,
    date DATE NOT NULL,

    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_user_note FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDb;