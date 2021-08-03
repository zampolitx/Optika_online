PRAGMA foreign_keys=on;
CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);
INSERT INTO mainmenu(title, url) VALUES('Главная', '/');
INSERT INTO mainmenu(title, url) VALUES('Добавить', '/add');
INSERT INTO mainmenu(title, url) VALUES('Добавить здание', '/add_building');
INSERT INTO mainmenu(title, url) VALUES('Добавить помещение', '/add_room');
INSERT INTO mainmenu(title, url) VALUES('Добавить панель', '/add_panel');
INSERT INTO mainmenu(title, url) VALUES('Добавить кросс', '/add_cross');

CREATE TABLE IF NOT EXISTS items (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL
);
INSERT INTO items(title) VALUES('Здание');
INSERT INTO items(title) VALUES('Помещение');
INSERT INTO items(title) VALUES('Панель');
INSERT INTO items(title) VALUES('Кабель');
INSERT INTO items(title) VALUES('Кросс');
INSERT INTO items(title) VALUES('Муфта');

CREATE TABLE IF NOT EXISTS building (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL
);
INSERT INTO building(title) VALUES('Корпус1');


CREATE TABLE IF NOT EXISTS parlor (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
building_id INTEGER NOT NULL,
FOREIGN KEY (building_id) REFERENCES building(id)
);
INSERT INTO parlor(number, title, building_id) VALUES('101', 'Серверная 1 этаж', 1);
INSERT INTO parlor(number, title, building_id) VALUES('102', 'Серверная 2 этаж', 1);


CREATE TABLE IF NOT EXISTS panel (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
units INTEGER,
parlor_id INTEGER NOT NULL,
FOREIGN KEY (parlor_id) REFERENCES parlor(id)
);
INSERT INTO panel(number, title, units, parlor_id) VALUES('5Р7', 'Панель оптических штук1', 42, 2);
INSERT INTO panel(number, title, units, parlor_id) VALUES('5Р7', 'Панель оптических штук1', 42, 2);
INSERT INTO panel(number, title, units, parlor_id) VALUES('5Р7', 'Панель оптических штук2', 42, 2);
INSERT INTO panel(number, title, units, parlor_id) VALUES('5Р7', 'Панель оптических штук2', 42, 2);
INSERT INTO panel(number, title, units, parlor_id) VALUES('5Р7', 'Панель оптических штук3', 42, 2);



CREATE TABLE IF NOT EXISTS fiber_cross (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
panel_id INTEGER NOT NULL,
FOREIGN KEY (panel_id) REFERENCES panel(id)
);
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('1', 'Оптический Кросс', '1', 'FC', 1);
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('2', 'Оптический Кросс', '1', 'SC', 1);
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('3', 'Оптический Кросс', '1', 'FC', 2);
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('4', 'Оптический Кросс', '1', 'SC', 3);
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('5', 'Оптический Кросс', '1', 'SC', 4);
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('6', 'Оптический Кросс', '1', 'SC', 5);

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
INSERT INTO cable(length_cable, title, type, start_of_cable_type, start_of_cable_dev_id, end_of_cable_type, end_of_cable_dev_id, fiber_cross_id) VALUES(1000, 'Опт. кабель', 'ДПМ-24-ММ', 'cross',  '1', 'cross', '1', 1);


CREATE TABLE IF NOT EXISTS fiber (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
cable_id INTEGER NOT NULL,
FOREIGN KEY (cable_id) REFERENCES cable(id)
);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa11111111111111122222222222', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, cable_id) VALUES('1', 'Moxa1', '1', 'LC', 1);

CREATE TABLE IF NOT EXISTS opt_coupler (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
panel_id INTEGER NOT NULL,
FOREIGN KEY (panel_id) REFERENCES panel(id)
);
