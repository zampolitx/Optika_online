class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    ### Метод, возвращающий главное меню ###
    def getMenu(self):
        sql = """SELECT * FROM mainmenu"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения базы данных")
        return [1]

    ### Метод для добавления сущностей в БД (под удаление)###
    def getItems(self):
        try:
            self.__cur.execute("SELECT * FROM items")
            res = self.__cur.fetchall()
            res_list = []
            if res:
                for m in res:
                    res_list.append(m[1])
                return res_list
        except:
            print("Ошибка чтения базы данных")
        return [1]

    ### Метод ###
    def getBuilding(self):
        sql = """SELECT * FROM building"""
        try:
            self.__cur.execute(sql)
            res2=self.__cur.fetchall()
            if res2:
                return res2
        except:
            print("Ошибка чтения базы данных")
        return [1]

    ### Метод ###
    def getParlor(self, building_id):
        sql = "SELECT * FROM parlor where building_id = ?"
        try:
            self.__cur.execute(sql, (building_id, ))
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения базы данных")
        return [1]

    # Метод возвращает
    def getPanel(self, parlor_id):
        sql = "SELECT * FROM panel where parlor_id = ?"
        try:
            self.__cur.execute(sql, (parlor_id, ))
            res = self.__cur.fetchall()
            if res:
                p = {}
                for elem in res:                   #Для каждой строки, извлеченной из БД
                    p[elem[1]] = my_dbase.getCross(elem[0])
                print(p)
                return p
        except:
            print("Ошибка чтения базы данных")
        return [1]