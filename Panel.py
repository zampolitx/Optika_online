import sqlite3
from Cross import Cross
class Panel:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getPanel(self, parlor_id):
        my_dbase = Cross(self.__db)
        sql = "SELECT * FROM panel where parlor_id = ?"
        try:
            self.__cur.execute(sql, (parlor_id, ))
            res = self.__cur.fetchall()
            print(res)
            if res:
                l = []
                for elem in res:                   #Для каждой строки, извлеченной из БД
                    p = dict(title=elem[2], number=elem[1], child=my_dbase.getCross(elem[0]))
                    l.append(p)
                return l
        except:
            print("Ошибка чтения базы данных")
        return [1]

    # Метод добавляет шкаф, панель или конкретное место на территории
    def addPanel(self, parent_item, panel_name, panel_number):       # parent_item - запись из чекбокса, остальное из формы добавления кабинета/участка территории
        try:
            self.__cur.execute("SELECT id FROM building WHERE title LIKE ?", (parent_item,))        # из таблицы parlor получить id записи из чекбокса
            res = self.__cur.fetchall()
            for elem in res:
                print(elem[0])      # в elem[0] находится id здания/территории куда добавляем кабинет
            self.__cur.execute("INSERT INTO parlor(building_id, title, number) VALUES(?, ?, ?)", (elem[0], panel_name, panel_number))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД: "+str(e))
        return [1]