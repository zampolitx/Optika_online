from Parlor import Parlor
class Building:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getBuilding(self):
        my_dbase = Parlor(self.__db)
        sql="""SELECT * FROM building"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                d = {}
                for i in res:
                    print(self.__db)
                    d[i[1]] = my_dbase.getParlor()
                print(d)
                return d
        except:
            print("Ошибка чтения базы данных")
        return [1]
