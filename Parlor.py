import sqlite3
from Panel import Panel
class Parlor:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getParlor(self, building_id, parlor_id, ALL=False):    #ALL=True значит нужна полная структура, нет значит вызывают из js
        my_dbase = Panel(self.__db)
        sql_all = "SELECT * FROM parlor where building_id = ?"
        sql_some = "SELECT number, title FROM parlor where building_id = ?"
        sql_one = "SELECT * FROM parlor where id = ?"
        if ALL == False and parlor_id == False:
            try:
                self.__cur.execute(sql_some, (building_id, ))
                res = self.__cur.fetchall()
                if res:
                    l = []
                    for elem in res:
                        l.append(elem[1])
                    return l
            except:
                print("Ошибка чтения базы данных для parlor 1")
            return ['']
        elif ALL == False and parlor_id:
            print("parlor_id in BD is", parlor_id)
            try:
                self.__cur.execute(sql_one, (parlor_id, ))
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
        else:
            try:
                self.__cur.execute(sql_all, (building_id, ))
                res = self.__cur.fetchall()
                if res:
                    l = []
                    for elem in res:
                        p = dict(id=elem[0], title=elem[2], number=elem[1], child=my_dbase.getPanel(elem[0], ALL=True))
                        l.append(p)
                    return l
            except:
                print("Ошибка чтения базы данных для parlor 3")
            return [1]

    def addParlor(self, parent_item, room_name, room_number):       # parent_item - запись из чекбокса, остальное из формы добавления кабинета/участка территории
        try:
            self.__cur.execute("SELECT id FROM building WHERE title=?", (parent_item,))        # из таблицы building получить id записи из чекбокса
            res = self.__cur.fetchall()
            for elem in res:
                print(elem[0])      # в elem[0] находится id здания/территории куда добавляем кабинет
            self.__cur.execute("INSERT INTO parlor(building_id, title, number) VALUES(?, ?, ?)", (elem[0], room_name, room_number))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД: "+str(e))
        return [1]