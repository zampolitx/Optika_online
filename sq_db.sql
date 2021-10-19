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
INSERT INTO building(title) VALUES('Помещение-1');
INSERT INTO building(title) VALUES('Помещение-2');
INSERT INTO building(title) VALUES('Помещение-3');
INSERT INTO building(title) VALUES('Помещение-4');
INSERT INTO building(title) VALUES('Помещение-5');
INSERT INTO building(title) VALUES('Помещение-6');
INSERT INTO building(title) VALUES('Помещение-7');


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
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES('К-2', 'Помещение 1', 5520, 2460, 4000, 5);
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES('101-1', 'ЛФА', 5520, 2460, 4000, 1);
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES('101-2', 'Помещение 2', 5520, 2460, 4000, 1);
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES('101-б', 'Помещение 3', 5520, 2460, 4000, 1);
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES('101-5', 'Помещение 4', 5520, 2460, 4000, 1);
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES('4', 'Серверная',1000, 1000, 1000, 1);
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES('3-КП', 'Помещение 5', 5520, 2460, 4000, 6);
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES(' ', 'Левый', 5520, 2460, 4000, 7);
INSERT INTO parlor(number, title, par_length, par_width, par_height, building_id) VALUES(' ', 'Правый', 5520, 2460, 4000, 7);

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
INSERT INTO door(height, width, type, parlor_id, positionX, positionY, angle_of_rotation) VALUES(2000, 1000, 'left', 1, 150, -73, -90);
INSERT INTO door(height, width, type, parlor_id, positionX, positionY, angle_of_rotation) VALUES(2000, 1000, 'right', 1, 150, -13, 90);

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
INSERT INTO panel(number, title, width, depth, units, positionX, positionY, angle_of_rotation, parlor_id) VALUES('ШК1', 'Шкаф связи', 600, 600, 42, 0, 100, 0, 2);
INSERT INTO panel(number, title, width, depth, units, positionX, positionY, angle_of_rotation, parlor_id) VALUES('ШК2', 'Шкаф связи', 1000, 1000, 42, 0, 100, 0, 6);
INSERT INTO panel(number, title, width, depth, units, positionX, positionY, angle_of_rotation, parlor_id) VALUES('ШК3', 'Шкаф связи', 600, 600, 18, 0, 100, 0, 1);
INSERT INTO panel(number, title, width, depth, units, positionX, positionY, angle_of_rotation, parlor_id) VALUES('ШК4', 'Шкаф связи', 600, 600, 10, 0, 100, 0, 1);
INSERT INTO panel(number, title, width, depth, units, positionX, positionY, angle_of_rotation, parlor_id) VALUES('ШК5', 'Шкаф связи', 600, 600, 24, 0, 100, 0, 6);
INSERT INTO panel(number, title, width, depth, units, positionX, positionY, angle_of_rotation, parlor_id) VALUES('ШК6', 'Шкаф связи', 600, 600, 24, 0, 100, 0, 6);

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

INSERT INTO unit(number, panel_id) VALUES(1, 2);
INSERT INTO unit(number, panel_id) VALUES(2, 2);
INSERT INTO unit(number, panel_id) VALUES(3, 2);
INSERT INTO unit(number, panel_id) VALUES(4, 2);
INSERT INTO unit(number, panel_id) VALUES(5, 2);
INSERT INTO unit(number, panel_id) VALUES(6, 2);
INSERT INTO unit(number, panel_id) VALUES(7, 2);
INSERT INTO unit(number, panel_id) VALUES(8, 2);
INSERT INTO unit(number, panel_id) VALUES(9, 2);
INSERT INTO unit(number, panel_id) VALUES(10, 2);
INSERT INTO unit(number, panel_id) VALUES(11, 2);
INSERT INTO unit(number, panel_id) VALUES(12, 2);
INSERT INTO unit(number, panel_id) VALUES(13, 2);
INSERT INTO unit(number, panel_id) VALUES(14, 2);
INSERT INTO unit(number, panel_id) VALUES(15, 2);
INSERT INTO unit(number, panel_id) VALUES(16, 2);

CREATE TABLE IF NOT EXISTS devices (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
description text NOT NULL,
model text NOT NULL,
unit_id INTEGER NOT NULL,
FOREIGN KEY (unit_id) REFERENCES unit(id)
);
INSERT INTO devices(title, description, model, unit_id) VALUES('C1', 'Коммутатор', 'Cisco C3567', 7);

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
