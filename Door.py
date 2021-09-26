import sqlite3
class Door:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getDoor(self, parlor_id, ALL=False):
        sql_some = "SELECT * FROM door where parlor_id = ?"
        sql_all = "SELECT * FROM door where parlor_id = ?"
        if ALL==False: # Если нужно двери только одного помещения
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
    def addDoor(self, parent_item, door_height, door_width, type):       # parent_item - запись из чекбокса, остальное из формы добавления кабинета/участка территории
        try:
            self.__cur.execute("SELECT id FROM parlor WHERE title=?", (parent_item,))        # из таблицы parlor получить id записи из чекбокса
            res = self.__cur.fetchall()
            for elem in res:
                print('parent item=', parent_item)
                print('element0', elem[0])      # в elem[0] находится id кабинета куда добавляем панель
                positionX=123
                positionY=124
                angle_of_rotation = 90
                self.__cur.execute("INSERT INTO door(parlor_id, height, width, type, positionX, positionY, angle_of_rotation) VALUES(?, ?, ?, ?, ?, ?, ?)", (elem[0], door_height, door_width, type, positionX, positionY, angle_of_rotation))
                self.__db.commit()
                print('Запись двери добавлена')
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД: "+str(e))
        return [1]
