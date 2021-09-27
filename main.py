from flask import Flask, render_template, request, flash, g, url_for, json, jsonify
import sqlite3, os, re, json
from FDataBase import FDataBase
from Building import Building
from Parlor import Parlor
from Panel import Panel
from Door import Door
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
    mydbase=Building(db)
    building2=mydbase.getBuilding(build_name=False, ALL=True)       # Возвращает коллекцию из словарей
    print(building2)
    return render_template('index.html', title="Optika-главная", menu=dbase.getMenu(), building=building2)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        if len(request.form['add_items']) > 2:  # Отображение подсказок
            flash('Данные отправлены', category='success')
        else:
            flash('Слишком короткое имя', category='error')
        #print(request.form)
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add.html', title="Optika-add", menu=dbase.getMenu(), add_items=dbase.getItems())

@app.route("/showBuilding<id>", methods=['GET', 'POST'])
def showBuilding(id):
    db = get_db()
    dbase=FDataBase(db)
    mydbase = Parlor(db)
    doorBase = Door(db)
    parlor = mydbase.getParlor(parlor_id=id, ALL=False, building_id=False)
    doors = doorBase.getDoor(parlor_id=id, ALL=False)
    print('it is parlor', parlor)
    if request.method == "POST":
        print('it is parlor', parlor)
    return render_template('showBuilding.html', title="Показать здание", menu=dbase.getMenu(), parlor=parlor, doors=doors)

@app.route("/add_building", methods=['GET', 'POST'])
def add_building():
    db = get_db()
    dbase=FDataBase(db)
    Buld_base=Building(db)
    if request.method == "POST":
        Buld_base.addBuilding(request.form['building_name'])
    return render_template('add_building.html', title="Добавить здание", menu=dbase.getMenu())

@app.route("/add_room", methods=['GET', 'POST'])
def add_room():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Parlor(db)
    parent_item = []                                                          # Пустой список (в него далее добавляем из БД здания и территории предприятия)
    for d in dbase.getBuilding():                                           # В d находятся строки из БД с зданиями
        parent_item.append(d[1])                                              # Список далее передаем на страницу add_room в качестве родителя для комнаты или участка
    if request.method == "POST":
        print(request.form)
        if len(request.form['room_name']) > 1:                          # Отображение подсказок
            res = Par_base.addParlor(request.form['parent_item'], request.form['room_name'], request.form['room_number'])
            if not res:
                flash('Ошибка', category='error')
            else:
                flash('Нет ошибки', category='success')
    return render_template('add_room.html', title="Добавить помещение", menu=dbase.getMenu(), parent_item=parent_item)

@app.route("/add_panel", methods=['GET', 'POST'])
def add_panel():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Panel(db)
    Build_base = Building(db)
    parent_building = []
    print('parent_building', parent_building)
    for d in Build_base.getBuilding():
        parent_building.append(d)
    if request.method == "POST":
        print(request.form)
        if len(request.form['panel_name']) > 1:
            res = Par_base.addPanel(request.form['parent_parlor'], request.form['panel_name'], request.form['panel_number'], request.form['units_number'])
            if not res:
                flash('Ошибка', category='error')
            else:
                flash('Добавлено', category='success')
    return render_template('add_panel.html', title="Добавить панель", menu=dbase.getMenu(), parent_building=parent_building)

@app.route("/add_door", methods=['GET', 'POST'])
def add_door():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Door(db)
    Build_base = Building(db)
    parent_building = []
    for d in Build_base.getBuilding(ALL=True):
        parent_building.append(d)
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
        print('new_building', build_name)
        building_id = mydbase.getBuilding(build_name, ALL=False)
        return retAJAX(building_id)
    elif (request_key=='room_name'):
        mydbase = Parlor(db)
        room_name = request.form['room_name']
        print('new_room', room_name)
        room_id = mydbase.getParlor(room_name, ALL=False)[0]
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
