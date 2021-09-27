import sqlite3
from Cross import Cross
# Предусмотреть защиту от одинаковых названий, чтобы не добавлялось в одно и то же здание
class Panel:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getPanel(self, parlor_id=False, panel_id=False, ALL=False):
        my_dbase = Cross(self.__db)
        sql_some = "SELECT * FROM panel where parlor_id = ?"
        sql_all = "SELECT * FROM panel where parlor_id = ?"
        sql_one = "SELECT * FROM panel where id = ?"
        if ALL==False and parlor_id: # Если нужно только про шкафы
            try:
                self.__cur.execute(sql_all, (parlor_id, ))
                res = self.__cur.fetchall()
                print('Это res in panel', res)
                if res:
                    return res
            except:
                print("Ошибка чтения базы данных panel (только шкафы)")
            return [False]

        elif ALL==False and panel_id: # Если нужно только один шкаф
            print('Это panel_id одного шкафа', panel_id)
            try:
                self.__cur.execute(sql_one, (panel_id, ))
                res = self.__cur.fetchall()
                print('Это res одного шкафа', res)
                if res:
                    for elem in res:
                        print(elem[1])
                        p = dict(number=elem[1], title=elem[2], width=elem[3], depth=elem[4], units=elem[5], positionX=elem[6], positionY=elem[7], angle_of_rotate=elem[8])
                    return p
            except:
                print("Ошибка чтения базы данных panel (только один шкаф)")
            return [False]

        else:   #Если запрашивает главная страница (полное дерево)
            try:
                self.__cur.execute(sql_all, (parlor_id, ))
                res = self.__cur.fetchall()
                if res:
                    l = []
                    for elem in res:                   #Для каждой строки, извлеченной из БД
                        p = dict(id=elem[0], title=elem[2], number=elem[1], child=my_dbase.getCross(elem[0], ALL=True))
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