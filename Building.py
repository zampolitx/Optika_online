from Parlor import Parlor
class Building:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getBuilding(self):
        sql="""SELECT * FROM building"""
        try:
            self.__cur.execute(sql)
            res=self.__cur.fetchall()
            if res:
                d={}
                for i in res:
                    d[i[1]]=Parlor.getParlor(i[0], i[1])
                    print(d)
                return res
        except:
            print("Ошибка чтения базы данных")
        return [1]
