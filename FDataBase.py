class FDataBase:
    def __init__(self, db, my):
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

    def getFacility(self):
        sql="""SELECT * FROM building"""
        try:
            self.__cur.execute(sql)
            res2=self.__cur.fetchall()
            if res2:
                return res2
        except:
            print("Ошибка чтения базы данных")
        return [1]

    def getParlor(self, my_id):
        sql="""SELECT * FROM parlor where (?)"""
        try:
            for m in my_id:
                print(m)
            self.__cur.execute(sql, my_id)
            res3=self.__cur.fetchall()
            print(res3)
            if res3:
                return res3
        except:
            print("Ошибка чтения базы данных")
        return [1]