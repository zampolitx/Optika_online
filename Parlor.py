import sqlite3
from Panel import Panel
class Parlor:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getParlor(self, building_id):
        my_dbase = Panel(self.__db)
        sql = "SELECT * FROM parlor where building_id = ?"
        try:
            self.__cur.execute(sql, (building_id, ))
            res = self.__cur.fetchall()
            if res:
                l = []
                for elem in res:
                    p = dict(title=elem[2], number=elem[1], child=my_dbase.getPanel(elem[0]))
                    print(p)
                    l.append(p)
                return l
        except:
            print("Ошибка чтения базы данных")
        return [1]

    def addParlor(self, parent_item, room_name, room_number):       # parent_item - запись из чекбокса, остальное из формы добавления кабинета/участка территории
        try:
            self.__cur.execute("SELECT id FROM building WHERE title LIKE ?", (parent_item,))        # из таблицы building получить id записи из чекбокса
            res = self.__cur.fetchall()
            for elem in res:
                print(elem[0])      # в elem[0] находится id здания/территории куда добавляем кабинет
            self.__cur.execute("INSERT INTO parlor(building_id, title, number) VALUES(?, ?, ?)", (elem[0], room_name, room_number))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД: "+str(e))
        return [1]