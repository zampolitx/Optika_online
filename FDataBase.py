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
    def getItems(self, prefix):
        try:
            self.__cur.execute("SELECT * FROM AllPagesMenu")
            res = self.__cur.fetchall()
            menu_addDict = {}
            if res:
                for m in res:
                    print(m[1])
                    menu_addDict[m[1]] = str(prefix + m[1])     # Если prefix='/add_' то получаем урл типа '/add_building'
                return menu_addDict
        except:
            print("Ошибка чтения базы данных FDataBase getItems")
        return [1]

