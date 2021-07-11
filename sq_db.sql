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
INSERT INTO building(title) VALUES('Корпус2');
INSERT INTO building(title) VALUES('Корпус3');
INSERT INTO building(title) VALUES('Территория предприятия');

CREATE TABLE IF NOT EXISTS parlor (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
building_id INTEGER NOT NULL,
FOREIGN KEY (building_id) REFERENCES building(id)
);
INSERT INTO parlor(number, title, building_id) VALUES('101', 'Серверная 1 этаж', '1');
INSERT INTO parlor(number, title, building_id) VALUES('102', 'Серверная 1 этаж', '1');


CREATE TABLE IF NOT EXISTS panel (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
parlor_id INTEGER NOT NULL,
FOREIGN KEY (parlor_id) REFERENCES parlor(id)
);
INSERT INTO panel(number, title, parlor_id) VALUES('5Р7', 'Панель оптических штук1', '1');
INSERT INTO panel(number, title, parlor_id) VALUES('5Р7', 'Панель оптических штук1', '1');
INSERT INTO panel(number, title, parlor_id) VALUES('5Р7', 'Панель оптических штук2', '2');
INSERT INTO panel(number, title, parlor_id) VALUES('5Р7', 'Панель оптических штук2', '2');
INSERT INTO panel(number, title, parlor_id) VALUES('5Р7', 'Панель оптических штук3', '3');



CREATE TABLE IF NOT EXISTS fiber_cross (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
panel_id INTEGER NOT NULL,
FOREIGN KEY (panel_id) REFERENCES panel(id)
);
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('1', 'ОК', '1', 'FC', '1');
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('2', 'ОК', '1', 'SC', '1');
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('3', 'ОК', '1', 'FC', '2');
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('4', 'ОК', '1', 'SC', '2');
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('5', 'ОК', '1', 'SC', '3');
INSERT INTO fiber_cross(number, title, num_of_conn, type_of_conn, panel_id) VALUES('6', 'ОК', '1', 'SC', '3');

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
INSERT INTO cable(title, type, start_of_cable_type, start_of_cable_dev_id, end_of_cable_type, end_of_cable_dev_id, fiber_cross_id) VALUES('ОК1', 'ДПМ-24-ММ', 'cross',  '1', 'cross', '2');
INSERT INTO cable(title, type, start_of_cable, end_of_cable, fiber_cross_id) VALUES('7Р13', 'Панель ЛПОС', '1');
INSERT INTO cable(title, type, start_of_cable, end_of_cable, fiber_cross_id) VALUES('8Р1', 'Панель ПОС', '1');
INSERT INTO cable(title, type, start_of_cable, end_of_cable, fiber_cross_id) VALUES('8Р2', 'Панель ОС', '1');
INSERT INTO cable(title, type, start_of_cable, end_of_cable, fiber_cross_id) VALUES('2Р12', 'Панель ППР', '2');
INSERT INTO cable(title, type, start_of_cable, end_of_cable, fiber_cross_id) VALUES('3Р15', 'Панель НМС', '3');

CREATE TABLE IF NOT EXISTS fiber (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
panel_id INTEGER NOT NULL,
FOREIGN KEY (panel_id) REFERENCES panel(id)
);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('1', 'ОК', '1');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('7Р13', 'Панель ЛПОС', '1');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('8Р1', 'Панель ПОС', '1');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('8Р2', 'Панель ОС', '1');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('2Р12', 'Панель ППР', '2');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('3Р15', 'Панель НМС', '3');

CREATE TABLE IF NOT EXISTS opt_coupler (
id integer PRIMARY KEY AUTOINCREMENT,
number text NOT NULL,
title text NOT NULL,
num_of_conn text NOT NULL,
type_of_conn text NOT NULL,
panel_id INTEGER NOT NULL,
FOREIGN KEY (panel_id) REFERENCES panel(id)
);
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('1', 'ОК', '1');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('7Р13', 'Панель ЛПОС', '1');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('8Р1', 'Панель ПОС', '1');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('8Р2', 'Панель ОС', '1');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('2Р12', 'Панель ППР', '2');
INSERT INTO fiber(number, title, num_of_conn, type_of_conn, parlor_id) VALUES('3Р15', 'Панель НМС', '3');