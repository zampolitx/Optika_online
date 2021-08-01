import sqlite3
from Cross import Cross
class Panel:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getPanel(self, parlor_id, ALL=False):
        my_dbase = Cross(self.__db)
        sql_some = "SELECT * FROM panel where parlor_id = ?"
        sql_all = "SELECT * FROM panel where parlor_id = ?"
        if ALL==False: # Если нужно только про шкафы
            try:
                self.__cur.execute(sql_some, (parlor_id, ))
                res = self.__cur.fetchall()
                if res:
                    l = []
                    for elem in res:                   #Для каждой строки, извлеченной из БД
                        l.append(elem)
                    return l
            except:
                print("Ошибка чтения базы данных")
            return [False]
        else:   #Если запрашивает главная страница (полное дерево)
            try:
                self.__cur.execute(sql_all, (parlor_id, ))
                res = self.__cur.fetchall()
                if res:
                    l = []
                    for elem in res:                   #Для каждой строки, извлеченной из БД
                        p = dict(title=elem[2], number=elem[1], child=my_dbase.getCross(elem[0], ALL=True))
                        l.append(p)
                    return l
            except:
                print("Ошибка чтения базы данных")
            return [1]

    # Метод добавляет шкаф, панель или конкретное место на территории
    def addPanel(self, parent_item, panel_name, panel_number, units):       # parent_item - запись из чекбокса, остальное из формы добавления кабинета/участка территории
        try:
            self.__cur.execute("SELECT id FROM parlor WHERE title=?", (parent_item,))        # из таблицы parlor получить id записи из чекбокса
            res = self.__cur.fetchall()
            for elem in res:
                print('parent item=', parent_item)
                #print('element0', elem[0])      # в elem[0] находится id кабинета куда добавляем панель
            self.__cur.execute("INSERT INTO panel(parlor_id, number, title, units) VALUES(?, ?, ?, ?)", (elem[0], panel_name, panel_number, units))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД: "+str(e))
        return [1]