PRAGMA foreign_keys=on;
CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);
INSERT INTO mainmenu(title, url) VALUES('Главная', '/');
INSERT INTO mainmenu(title, url) VALUES('Добавить', '/add');

CREATE TABLE IF NOT EXISTS building (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL
);
INSERT INTO building(title) VALUES('Корпус1');
INSERT INTO building(title) VALUES('Корпус2');
INSERT INTO building(title) VALUES('Корпус3');
INSERT INTO building(title) VALUES('Корпус4');

CREATE TABLE IF NOT EXISTS parlor (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
building_id INTEGER NOT NULL,
FOREIGN KEY (building_id) REFERENCES building(id)
);
INSERT INTO parlor(number, title, building_id) VALUES('101', 'Серверная 1 этаж', '1');
INSERT INTO parlor(number, title, building_id) VALUES('102', 'Серверная 1 этаж', '1');
INSERT INTO parlor(number, title, building_id) VALUES('201', 'Серверная 2 этаж', '1');
INSERT INTO parlor(number, title, building_id) VALUES('202', 'Серверная 2 этаж', '1');
INSERT INTO parlor(number, title, building_id) VALUES('101', 'Серверная 1 этаж', '2');
INSERT INTO parlor(number, title, building_id) VALUES('101', 'Серверная 1 этаж', '3');