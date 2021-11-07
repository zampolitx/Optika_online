PRAGMA foreign_keys=on;
CREATE TABLE IF NOT EXISTS mainmenu (
title text NOT NULL UNIQUE,
url text NOT NULL UNIQUE
);
INSERT OR IGNORE INTO mainmenu(title, url) VALUES('Главная', '/');
INSERT OR IGNORE INTO mainmenu(title, url) VALUES('Добавить', '/add');
INSERT OR IGNORE INTO mainmenu(title, url) VALUES('Изменить', '/change');
INSERT OR IGNORE INTO mainmenu(title, url) VALUES('Удалить', '/delete');
INSERT OR IGNORE INTO mainmenu(title, url) VALUES('Найти', '/find');
INSERT OR IGNORE INTO mainmenu(title, url) VALUES('Оптика', '/optika');

CREATE TABLE IF NOT EXISTS AllPagesMenu (
title text NOT NULL UNIQUE,
url text NOT NULL UNIQUE
);
INSERT OR IGNORE INTO AllPagesMenu(title, url) VALUES('Здание', 'building');
INSERT OR IGNORE INTO AllPagesMenu(title, url) VALUES('Помещение', 'room');
INSERT OR IGNORE INTO AllPagesMenu(title, url) VALUES('Дверь', 'door');
INSERT OR IGNORE INTO AllPagesMenu(title, url) VALUES('Панель', 'panel');
INSERT OR IGNORE INTO AllPagesMenu(title, url) VALUES('Место', 'place');
INSERT OR IGNORE INTO AllPagesMenu(title, url) VALUES('Кросс', 'cross');
INSERT OR IGNORE INTO AllPagesMenu(title, url) VALUES('Устройство', 'device');

CREATE TABLE IF NOT EXISTS building (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
UNIQUE(id, title)
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
