PRAGMA foreign_keys=on;
CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);
INSERT INTO mainmenu(title, url) VALUES('Главная', '/');
INSERT INTO mainmenu(title, url) VALUES('Добавить', '/add');
INSERT INTO mainmenu(title, url) VALUES('Изменить', '/change');
INSERT INTO mainmenu(title, url) VALUES('Добавить здание', '/add_building');
INSERT INTO mainmenu(title, url) VALUES('Добавить помещение', '/add_room');
INSERT INTO mainmenu(title, url) VALUES('Добавить дверь', '/add_door');
INSERT INTO mainmenu(title, url) VALUES('Добавить панель', '/add_panel');
INSERT INTO mainmenu(title, url) VALUES('Добавить место', '/add_place');
INSERT INTO mainmenu(title, url) VALUES('Добавить кросс', '/add_cross');
INSERT INTO mainmenu(title, url) VALUES('Добавить устройство', '/add_device');
INSERT INTO mainmenu(title, url) VALUES('Оптика', '/optika');
INSERT INTO mainmenu(title, url) VALUES('Пробная', '/proba');


CREATE TABLE IF NOT EXISTS items (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL
);
INSERT INTO items(title) VALUES('Здание');
INSERT INTO items(title) VALUES('Помещение');
INSERT INTO items(title) VALUES('Дверь');
INSERT INTO items(title) VALUES('Панель');
INSERT INTO items(title) VALUES('Кабель');
INSERT INTO items(title) VALUES('Кросс');
INSERT INTO items(title) VALUES('Муфта');
INSERT INTO items(title) VALUES('Устройство');


CREATE TABLE IF NOT EXISTS building (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL
);

CREATE TABLE IF NOT EXISTS parlor (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
par_length INTEGER,
par_width INTEGER,
par_height INTEGER,
building_id INTEGER NOT NULL,
FOREIGN KEY (building_id) REFERENCES building(id)
);

CREATE TABLE IF NOT EXISTS door (
id integer PRIMARY KEY AUTOINCREMENT,
height INTEGER,
width INTEGER,
type text NOT NULL,
parlor_id INTEGER NOT NULL,
positionX INTEGER,
positionY INTEGER,
angle_of_rotation INTEGER,
FOREIGN KEY (parlor_id) REFERENCES parlor(id)
);


CREATE TABLE IF NOT EXISTS panel (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
width INTEGER NOT NULL,
depth INTEGER NOT NULL,
units INTEGER,
positionX INTEGER,
positionY INTEGER,
angle_of_rotation INTEGER,
parlor_id INTEGER NOT NULL,
FOREIGN KEY (parlor_id) REFERENCES parlor(id)
);

CREATE TABLE IF NOT EXISTS place (
id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE IF NOT EXISTS unit (
id INTEGER PRIMARY KEY AUTOINCREMENT,
number INTEGER NOT NULL,
panel_id INTEGER NOT NULL,
place_id INTEGER,
FOREIGN KEY (panel_id) REFERENCES panel(id),
FOREIGN KEY (place_id) REFERENCES place(id)
);

CREATE TABLE IF NOT EXISTS devices (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
description text NOT NULL,
model text NOT NULL,
unit_id INTEGER NOT NULL,
FOREIGN KEY (unit_id) REFERENCES unit(id)
);

CREATE TABLE IF NOT EXISTS fiber_cross (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
panel_id INTEGER NOT NULL,
FOREIGN KEY (panel_id) REFERENCES panel(id)
);

CREATE TABLE IF NOT EXISTS cable (
id integer PRIMARY KEY AUTOINCREMENT,
length_cable integer NOT NULL,
title text NOT NULL,
type text NOT NULL,
start_of_cable_type text NOT NULL,
start_of_cable_dev_id text NOT NULL,
end_of_cable_type text NOT NULL,
end_of_cable_dev_id text NOT NULL,
fiber_cross_id INTEGER NOT NULL,
FOREIGN KEY (fiber_cross_id) REFERENCES fiber_cross(id)
);

CREATE TABLE IF NOT EXISTS fiber (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
cable_id INTEGER NOT NULL,
FOREIGN KEY (cable_id) REFERENCES cable(id)
);

CREATE TABLE IF NOT EXISTS opt_coupler (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
panel_id INTEGER NOT NULL,
FOREIGN KEY (panel_id) REFERENCES panel(id)
);
