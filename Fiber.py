class Fiber:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getFiber(self, cable_id, ALL=False):
        sql = "SELECT * FROM fiber where cable_id = ?"
        try:
            self.__cur.execute(sql, (cable_id, ))
            res = self.__cur.fetchall()
            if res:
                p = []
                for i in res:                   #Для каждой строки, извлеченной из БД
                    p.append(i[1])
                print(p)
                return p
        except:
            print("Ошибка чтения базы данных Fiber.py")
        return [1]