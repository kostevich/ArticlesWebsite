# Импортируем класс Flask из модуля flask.
from flask import Flask
# Импортируем модуль render_template для работы шаблонов.
from flask import render_template
# Импортируем модуль SQLAlchemy для работы с базой данных.
from flask_sqlalchemy import SQLAlchemy
# Импортируем модуль datetime для работы с полем дата базы данных.
from datetime import datetime

# Создаем основной объект app класса Flask.
app = Flask(__name__)
# Настройки бд c названием sqlite:///blog.bd.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.bd'
# Создание бд.
db = SQLAlchemy(app)


# Создадим класс, на основе которого, будет создаваться таблица
class Article(db.Model):
    # Добавим поле id, уникальное.
    id = db.Column(db.Integer, primary_key=True)
    # Добавим поле тег, не может быть пустым.
    tag = db.Column(db.String(20), nullable=False)
    # Добавим поле название, не может быть пустым.
    title = db.Column(db.String(50), nullable=False)
    # Добавим поле вводный текст, не может быть пустым.
    intro = db.Column(db.String(200), nullable=False)
    # Добавим поле основного текста артикула, не может быть пустым.
    text = db.Column(db.Text, nullable=False)
    # Добавим поле время создания, значение по умолчанию время сейчас.
    create_on = db.Column(db.DateTime, default=datetime.utcnow)
    # Добавим поле время изменения, значение по умолчанию время сейчас, и оно обновляется при обновлении информации в базе данных.
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    # Получение данных объетка базы данных в виде строки.
    def __repr__(self):
        return '<Article %r>' % self.id


# /Декоратор, который регистрирует URL-адрес, # в котором будет осуществляться представление.
@app.route('/')
@app.route('/home')
# Функция для вывода информации по ссылке.
def index():
    # Возвращаем на страницу текст.
    return render_template("index.html")


@app.route('/about')
# Функция для вывода информации по ссылке.
def about():
    # Возвращаем на страницу текст.
    return render_template("about.html")


# Декоратор, который регистрирует URL-адрес, в котором будет осуществляться представление.
@app.route('/create_articles')
# Функция для вывода информации по ссылке.
def creation_articles():
    # Возвращаем на страницу текст.
    return render_template("create_articles.html")


# Проверка правильности запуска проекта через файл с названием app.
if __name__ == '__main__':
    # Запуск приложения и отслеживание ошибок.
    app.run(debug=True)
