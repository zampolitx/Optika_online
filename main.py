from flask import Flask, render_template, request, flash, g, url_for, json, jsonify, redirect
import sqlite3, os, re, json
from FDataBase import FDataBase
from Building import Building
from Parlor import Parlor
from Panel import Panel
from Place import Place
from Device import Device
from Door import Door
from Unit import Unit
from ALL import ALL
# Конфигурация приложения
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = ';askldjfa;skdljfas;kldfj'
# Конец конфигурации
app = Flask(__name__)
app.config.from_object(__name__)                                                # Загружаем конфигурацию из текущего модуля
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))      # Переопределяем путь к БД
# Функция подключения к БД
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn
# Функция для создания БД
def create_db():
    db=connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db

@app.route("/")
def index():
    db = get_db()
    dbase=FDataBase(db)                 #FDataBase - это класс, dbase - экземляр класса FDataBase
    ALLdbase=ALL(db)
    mydbase=Building(db)
    building2=mydbase.getBuilding(build_name=False)       # Возвращает коллекцию из словарей
    building3 = ALLdbase.getALL()
    print('it is building3', building3)
    if(building3):  #Если база данных уже заполнена
        print(building3)
        return render_template('index.html', title="Optika-главная", menu=dbase.getMenu(), building=building3)
    else:   #Если база данных пустая
        return render_template('index.html', title="Optika-главная", menu=dbase.getMenu(), building=building3)

@app.route("/optika")
def optika():
    db = get_db()
    dbase=FDataBase(db)                 #FDataBase - это класс, dbase - экземляр класса FDataBase
    ALLdbase=ALL(db)
    mydbase=Building(db)
    building2=mydbase.getBuilding(build_name=False)       # Возвращает коллекцию из словарей
    building3 = ALLdbase.getALL()
    print(building3)
    return render_template('index.html', title="Optika-главная", menu=dbase.getMenu(), building=building3)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        if len(request.form['add_items']) > 2:  # Отображение подсказок
            flash('Данные отправлены', category='success')
            return redirect(url_for(request.form['add_items']))     # Если выбрали пункт в меню, делаем редирект
        else:
            flash('Слишком короткое имя', category='error')
        print(request.form['add_items'])
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add.html', title="Optika-add", menu=dbase.getMenu(), add_items=dbase.getItems(prefix='/add_'))

@app.route("/change", methods=['GET', 'POST'])
def change():
    if request.method == "POST":
        print(request.form)
        if (request.form['change_items']) == 'change_building':  # Если выбрали изменить здание
            return redirect('/change_building')  # Редирект
        elif (request.form['change_items']) == 'change_room':  # Если выбрали изменить помещение
            return redirect('/change_parlor')  # Редирект
        elif (request.form['change_items']) == 'change_door':  # Если выбрали изменить дверь
            return redirect('/change_door')  # Редирект
    db = get_db()
    dbase = FDataBase(db)
    return render_template('change.html', title="change", menu=dbase.getMenu(), add_items=dbase.getItems(prefix='/change_'))

@app.route("/change_building", methods=['GET', 'POST'])
def change_building():
    db = get_db()
    dbase = FDataBase(db)
    Build_base = Building(db)
    if request.method == "POST":
        print(request.form)
        Build_base.changeBuilding(request.form['old_name'], request.form['new_name'])
    building = Build_base.getBuilding(build_name=False)     # Список всех зданий
    print('it is building in change_building', building)
    return render_template('change_building.html', title="change_building", menu=dbase.getMenu(), old_name=building)

@app.route("/change_parlor", methods=['GET', 'POST'])
def change_parlor():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Building(db)
    if request.method == "POST":
        print(request.form)
        Par_base.changeBuilding(request.form['old_name'], request.form['new_name'])
    building = Par_base.getBuilding(build_name=False)     # Список всех зданий
    print('it is building in change_building', building)
    return render_template('change_parlor.html', title="change_parlor", menu=dbase.getMenu(), old_name=building)

@app.route("/change_door", methods=['GET', 'POST'])
def change_door():
    db = get_db()
    dbase = FDataBase(db)
    Door_base = Door(db)
    if request.method == "POST":
        print(request.form)
        Door_base.changeBuilding(request.form['old_name'], request.form['new_name'])
    door = Door_base.getDoor(door_name=False)     # Список всех дверей
    print('it is building in change_building', door)
    return render_template('change_door.html', title="change_door", menu=dbase.getMenu(), old_door=door)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        print(request.form)
        if (request.form['delete_items']) == 'deletebuilding':  # Если выбрали изменить здание
            return redirect('/delete_building')  # Редирект
        elif (request.form['change_items']) == 'change_parlor':  # Если выбрали изменить помещение
            return redirect('/change_parlor')  # Редирект

    return render_template('delete.html', title="delete", menu=dbase.getMenu(), add_items=dbase.getItems(prefix='/delete'))

@app.route("/delete_building", methods=['GET', 'POST'])
def delete_building():
    db = get_db()
    dbase = FDataBase(db)
    Build_base = Building(db)
    if request.method == "POST":
        print(request.form)
        Build_base.deleteBuilding(request.form['building'])
    building = Build_base.getBuilding(build_name=False)     # Список всех зданий
    print('it is building in delete_building', building)
    return render_template('delete_building.html', title="delete_building", menu=dbase.getMenu(), building=building)

@app.route("/showBuilding<id>", methods=['GET', 'POST'])
def showBuilding(id):
    db = get_db()
    dbase=FDataBase(db)
    parBase = Parlor(db)
    doorBase = Door(db)
    panelBase = Panel(db)
    parlor = parBase.getParlor(parlor_id=id, ALL=False, building_id=False)
    doors = doorBase.getDoor(parlor_id=id, ALL=False)
    panel = panelBase.getPanel(parlor_id=id, ALL=False) # Список строк панелей из БД
    print('it is parlor', parlor)
    print('it is a panel', panel)
    if request.method == "POST":
        print('it is parlor', parlor)
    return render_template('showBuilding.html', title="Показать здание", menu=dbase.getMenu(), parlor=parlor, doors=doors, panel=panel)

@app.route("/add_building", methods=['GET', 'POST'])
def add_building():
    db = get_db()
    dbase=FDataBase(db)     #Используется для получения меню
    Build_base=Building(db)
    if request.method == "POST":
        Build_base.addBuilding(request.form['building_name'])
    return render_template('add_building.html', title="Добавить здание", menu=dbase.getMenu())

@app.route("/add_room", methods=['GET', 'POST'])
def add_room():
    db = get_db()
    dbase = FDataBase(db)
    Build_base = Building(db)
    Par_base = Parlor(db)
    parent_item = []                                                          # Пустой список (в него далее добавляем из БД здания и территории предприятия)
    if Build_base.getBuilding()==False:
        return redirect('add_building')
    for d in Build_base.getBuilding():                                        # В d находятся строки из БД с зданиями
        parent_item.append(d[1])                                              # Список далее передаем на страницу add_room в качестве родителя для комнаты или участка
    if request.method == "POST":
        print(request.form)
        if len(request.form['room_name']) > 1:                          # Отображение подсказок
            res = Par_base.addParlor(request.form['parent_item'], request.form['room_name'], request.form['room_number'], request.form['par_length'], request.form['par_width'], request.form['par_height'])
            if not res:
                flash('Ошибка', category='error')
            else:
                flash('Нет ошибки', category='success')
    return render_template('add_room.html', title="Добавить помещение", menu=dbase.getMenu(), parent_item=parent_item)

@app.route("/showPanel<id>", methods=['GET', 'POST'])
def showPanel(id):
    db = get_db()
    dbase=FDataBase(db)
    panelBase = Panel(db)
    unitBase = Unit(db)
    deviceBase = Device(db)
    panel = panelBase.getPanel(panel_id=id, ALL=False, parlor_id=False)
    print('panel in showPanel main.py', panel)
    listOfUnit = unitBase.getUnit(panel_id=id, unit_id=False)   #Вычисляем id всех юнитов для этой панели. Получаем список словарей
    print('unit in showPanel main.py', listOfUnit)
    unit=[]
    for elem in listOfUnit:
        unit.append(elem['id']) # список всех id юнитов для данной панели
    print('list of units is', unit)
    device = deviceBase.getDevice(unit_id=unit, device_id=False) # Мы передаем unit_id всех юнитов в этой панели и должны получить.
    print('it is panel', panel)
    print('it is device in panel', device)
    if request.method == "POST":
        print('it is parlor', panel)
    return render_template('showPanel.html', title="Показать панель", menu=dbase.getMenu(), panel=panel)

@app.route("/add_panel", methods=['GET', 'POST'])
def add_panel():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Panel(db)
    Build_base = Building(db)
    unitBase = Unit(db)
    parent_building = []
    print('parent_building', parent_building)
    for d in Build_base.getBuilding():
        parent_building.append(d[1])
    if request.method == "POST":
        print(request.form)
        if len(request.form['panel_name']) > 1:
            res = Par_base.addPanel(request.form['parent_parlor'], request.form['panel_name'], request.form['panel_number'], request.form['units_number'], request.form['width'], request.form['depth'])
            print('Это res из add_panel', res)      # id последней добавленной панели
            if not res:
                flash('Ошибка', category='error')
            else:
                unitBase.addUnit(panel_id=res, numOfUnits=request.form['units_number'])
                flash('Добавлено', category='success')
    return render_template('add_panel.html', title="Добавить панель", menu=dbase.getMenu(), parent_building=parent_building)

@app.route("/showUnit<id>", methods=['GET', 'POST'])
def showUnit(id):
    db = get_db()
    dbase=FDataBase(db)
    unitBase = Unit(db)
    unit = unitBase.getUnit(panel_id=id)
    print('it is unit', unit)
    if request.method == "POST":
        print('it is parlor', unit)
    return render_template('showUnit.html', title="Показать юнит", menu=dbase.getMenu(), unit=unit)

@app.route("/add_place", methods=['GET', 'POST'])   # Новый, переделать
def add_place():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Panel(db)
    Build_base = Building(db)
    Place_base = Place(db)
    unitBase = Unit(db)
    parent_building = []
    print('parent_building', parent_building)
    for d in Build_base.getBuilding():
        parent_building.append(d[1])
    if request.method == "POST":
        print('requst.form in add place:', request.form)
        print('requst.form.getlist in add place:', request.form.getlist('check'))
        if len(request.form['parent_panel']) > 1:
            res = Par_base.addPlace(request.form['parent_parlor'])
            print('Это res из add_panel', res)      # id последней добавленной панели
            if not res:
                flash('Ошибка', category='error')
            else:
                unitBase.addUnit(panel_id=res, numOfUnits=request.form['units_number'])
                flash('Добавлено', category='success')
    return render_template('add_place.html', title="Добавить панель", menu=dbase.getMenu(), parent_building=parent_building)



@app.route("/add_door", methods=['GET', 'POST'])
def add_door():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Door(db)
    Build_base = Building(db)
    parent_building = []
    for d in Build_base.getBuilding():
        parent_building.append(d[1])
    if request.method == "POST":
        print(request.form)
        res = Par_base.addDoor(request.form['parent_parlor'], request.form['door_width'], request.form['door_height'], request.form['type'])
        print('res', res)
    return render_template('add_door.html', title="Добавить дверь", menu=dbase.getMenu(), parent_building=parent_building)


@app.route("/add_cross", methods=['GET', 'POST'])
def add_cross():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        print(request.form)
    return render_template('add_cross.html', title="Добавить кросс", menu=dbase.getMenu())

@app.route("/add_cable", methods=['GET', 'POST'])
def add_cable():
    if request.method == "POST":
        print(request.form)
    return render_template('add_cable.html', title="Добавить кабель", menu=menu)

@app.route("/add_opt_coupler", methods=['GET', 'POST'])
def add_opt_coupler():
    if request.method == "POST":
        print(request.form)
    return render_template('add_opt_coupler.html', title="Добавить муфту", menu=menu)

@app.route("/find")
def find():
    return render_template('find.html', title="Optika-find", menu=menu)

@app.route("/proba", methods=['GET', 'POST'])
def proba():
    return render_template('proba.html')

@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    print(request.form)
    name = request.form['parent_building']
    return json.dumps({'len': len(name)})

# Обработчик функции AJAX add_panel.js
@app.route('/get_parlor', methods=['GET', 'POST'])
def get_parlor():
    print(request.form)
    par_building = request.form['parent_building']  #Из js получаем название здания, в котором находится кабинет
    db = get_db()
    mydbase = Building(db)
    building_id = mydbase.getBuilding(par_building)  # Обращаемся к БД и получаем id здания, в котором находится кабинет
    print('b_id is', building_id)
    mydbase_par = Parlor(db)
    parlor_list = mydbase_par.getParlor(building_id, parlor_id=False, ALL=False)
    print('par_list', parlor_list)
    return json.dumps({'par_buld_resp': parlor_list})

# Обработчик функции AJAX get_panels.js
# Получаем все панели для этого здания/территории
@app.route('/get_panels', methods=['GET', 'POST'])
def get_panels():
    print(request.form)
    par_parlor = request.form['parent_parlor']  #Из js получаем название кабинета, в котором находится панель
    db = get_db()
    Par_base = Parlor(db)
    Pan_base = Panel(db)
    parlor_id = []
    for d in Par_base.getParlor(parlor_name=par_parlor):  # Обращаемся к БД и получаем id кабинета, в котором находится панель
        parlor_id.append(d[0])
    print('parlor_id is', parlor_id)
    panel_list = []
    li = Pan_base.getPanel(parlor_id[0], ALL=False)
    print('li is', li)
    for l in li:
        print('l is ', l)
        panel_list.append(l['title'])   # Список с названиями панелей в AJAX функцию, например: par_list ['Шкаф связи', '1234']
    print('par_list', panel_list)
    return json.dumps({'par_par_resp': panel_list})

# Обработчик функции AJAX get_units.js
# Получаем все юниты для этой панели
# Должна возвращать так же уже занятые места (существующие)
@app.route('/get_units', methods=['GET', 'POST'])
def get_units():
    db = get_db()
    Pan_base = Panel(db)
    parlor_id = []
    for d in Par_base.getParlor(parlor_name=par_parlor):  # Обращаемся к БД и получаем id кабинета, в котором находится панель
        parlor_id.append(d[0])
    print('parlor_id is', parlor_id)
    panel_list = []
    li = Pan_base.getPanel(parlor_id[0], ALL=False)
    print('li is', li)
    for l in li:
        print('l is ', l)
        panel_list.append(l['title'])   # Список с названиями панелей в AJAX функцию, например: par_list ['Шкаф связи', '1234']
    print('par_list', panel_list)
    return json.dumps({'par_par_resp': panel_list})

# Обработчик функции AJAX add_building.js
# Проверяет введенные данные в форму и то, что есть в базе данных
def retAJAX(response):
    if (response):
        print('oldsss')
        return json.dumps({'resp': 'Old'})
    else:
        print('Newwww')
        return json.dumps(({'resp': 'New'}))


@app.route('/get_AJAX', methods=['GET', 'POST'])
def get_building():
    db = get_db()
    request_key = list(request.form.keys())[0]      # Ключ в запросе AJAX (building_name, room_name ...)
    if (request_key=='building_name'):             # Если в запросе AJAX есть building_name
        mydbase = Building(db)
        build_name = request.form['building_name']
        if (build_name=='all'):                     # Если нужно вывести список всех зданий (например в change_building)
            pass
        else:                                       # Если нужен id конкретного здания:
            print('new_building', build_name)
            building_id = mydbase.getBuilding(build_name)
            return retAJAX(building_id)
    elif (request_key=='room_name'):
        mydbase = Parlor(db)
        parlor_name = request.form['room_name']
        print('new_room', parlor_name)
        room_id = mydbase.getParlor(parlor_name=parlor_name)
        print(type(room_id))
        print('room_id', room_id)
        return retAJAX(room_id)


#Закрываем соединение с БД
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__=="__main__":
    app.run(debug=True)
