from flask import Flask, render_template
app = Flask(__name__)

menu = ('Главная', 'Добавить', 'Поиск')
systems = ('АСУП', 'ГГС', 'Громкая')
facility = ('', 'АПК-1', 'АПК-2', 'АПК-3', 'ЩБ')
volokno = ('', '1', 'волокно 1')
@app.route("/")
def index():
    return render_template('index.html', title="Optika-главная", menu=menu, systems=systems, facility=facility)

@app.route("/add", methods=['GET', 'POST'])
def add():
    colours = ['Объект', 'Помещение', 'Панель']
    return render_template('add.html', title="Optika-add", menu=menu, colours=colours)

@app.route("/find")
def find():
    return render_template('find.html', title="Optika-find", menu=menu)

if __name__=="__main__":
    app.run(debug=True)
