import sqlite3

class Unit:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getUnit(self, panel_id, unit_id):
        #my_dbase = Panel(self.__db)
        sql_all = "SELECT * FROM unit where panel_id = ?"   # Все юниты в этой панели
        sql_one = "SELECT * FROM unit where id = ?"
        if panel_id:
            try:
                self.__cur.execute(sql_all, (panel_id, ))
                res = self.__cur.fetchall()
                if res:
                    unit_list = []
                    for elem in res:
                        p = dict(id=elem[0], number=elem[1], panel_id=elem[2])
                        unit_list.append(p)
                    return unit_list
            except:
                print("Ошибка чтения базы данных для unit=panel_id", panel_id)
            return ['']
        elif id:
            print("id in BD is", id)
            try:
                self.__cur.execute(sql_one, (unit_id, ))
                res = self.__cur.fetchall()
                print(res)
                if res:
                    for elem in res:
                        print(elem[1])
                        p=dict(number=elem[1], title=elem[2], length=elem[3], width=elem[4], height=elem[5])
                    return p
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