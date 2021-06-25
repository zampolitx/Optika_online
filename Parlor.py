class Parlor:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getParlor(self):
        sql="""SELECT * FROM parlor where building_id = '1'"""
        print(id)
        try:
            self.__cur.execute(sql)
            res=self.__cur.fetchall()
            if res:
                a=[]
                for elem in res:
                    a.append(elem[1])
                return a
        except:
            print("Ошибка чтения базы данных")
        return [1]
