CREATE TABLE user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL
);

CREATE TABLE address (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    address_description TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE user_type (
    user_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_type_name TEXT NOT NULL,
        user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

INSERT INTO "user" (user_name)
values ("Ana"),
("Maria"),
("Fernanda"),
("Vanessa"),
("Bia");

INSERT INTO user_type (user_id, user_type_name)
values (1, "Casual");
INSERT INTO user_type (user_id, user_type_name)
values (2, "Casual");
INSERT INTO user_type (user_id, user_type_name)
values (3, "Casual");
INSERT INTO user_type (user_id, user_type_name)
values (4, "Frequente");
INSERT INTO user_type (user_id, user_type_name)
values (5, "Frequente");

INSERT INTO address (user_id, address_description)
values (1, "Av. Vasconcelos Costa, 270 - Martins, Uberlândia - MG, 38400-448");
INSERT INTO address (user_id, address_description)
values (2, "R. Álvares Cabral, 40 - Tabajaras, Uberlândia - MG, 38400-294");
INSERT INTO address (user_id, address_description)
values (3, "Av. Pres. Médici, 1001 - Morada da Colina, Uberlândia - MG, 38411-012");
INSERT INTO address (user_id, address_description)
values (4, "Av. Paulo Gracindo, 15 - 19-A - Morada da Colina, Uberlândia - MG, 38411-145");
INSERT INTO address (user_id, address_description)
values (5, "Rua João Balbino 1164 - Sala 09, CEP 38.408-262 - Santa Mônica, Uberlândia - MG");


SELECT u.user_name, ut.user_type_name, a.address_description 
from user u
inner join user_type ut 
on u.user_id = ut.user_id
inner join address a 
on u.user_id = a.user_id;