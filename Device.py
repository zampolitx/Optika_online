import sqlite3

class Device:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getDevice(self, unit_id, device_id):
        #my_dbase = Panel(self.__db)
        sql_all = "SELECT * FROM devices where unit_id = ?"
        sql_one = "SELECT * FROM devices where id = ?"
        if id:
            try:
                self.__cur.execute(sql_one, (device_id, ))
                res = self.__cur.fetchall()
                if res:
                    return res  # Возвращаем строку из БД
            except:
                print("Ошибка чтения базы данных для id", id)
            return ['']
        elif unit_id:   # Нужены девайсы, которые установлены в конкретный unit. Должен быть список словарей
            print("id in BD is", unit_id)
            try:
                self.__cur.execute(sql_all, (unit_id, ))
                res = self.__cur.fetchall()
                print('Это res in Device.py/getDevice/unit_id=', unit_id)
                if res:     # Список строк из БД
                    dev_list = []
                    for elem in res:
                        p=dict(id=elem[0], title=elem[1], description=elem[2], model=elem[3], unit_id=elem[4])
                        dev_list.append(p)
                    return dev_list
            except:
                print("Ошибка чтения базы данных для parlor 2")
            return ['']

    def addUnit(self, parent_item, room_name, room_number, par_length, par_width, par_height):       # parent_item - запись из чекбокса, остальное из формы добавления кабинета/участка территории
        try:
            self.__cur.execute("SELECT id FROM building WHERE title=?", (parent_item,))        # из таблицы building получить id записи из чекбокса
            res = self.__cur.fetchall()
            for elem in res:
                print(elem[0])      # в elem[0] находится id здания/территории куда добавляем кабинет
            self.__cur.execute("INSERT INTO parlor(building_id, title, number, par_length, par_width, par_height) VALUES(?, ?, ?, ?, ?, ?)", (elem[0], room_name, room_number, par_length, par_width, par_height))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД: "+str(e))
        return [1]