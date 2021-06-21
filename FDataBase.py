class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql="""SELECT * FROM mainmenu"""
        try:
            self.__cur.execute(sql)
            res=self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения базы данных")
        return [1]

    def getBuilding(self):
        sql="""SELECT * FROM building"""
        try:
            self.__cur.execute(sql)
            res2=self.__cur.fetchall()
            if res2:
                return res2
        except:
            print("Ошибка чтения базы данных")
        return [1]

    def getParlor(self):
        sql = """SELECT * FROM parlor"""
        try:
            self.__cur.execute(sql)
            res3 = self.__cur.fetchall()
            if res3:
                return res3
        except:
            print("Ошибка чтения базы данных")
        return [1]