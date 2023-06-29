# Импортируем класс Flask из модуля flask.
from flask import Flask
# Импортируем модуль render_template для работы шаблонов.
from flask import render_template
# Импортируем модуль url_for для правильной работы html.
from flask import url_for
# Создаем основной объект app класса Flask.
app = Flask(__name__)


## Декоратор, который регистрирует URL-адрес, в котором будет осуществляться представление.
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
@app.route('/user/<string:name>/<int:id>')
# Функция для вывода информации по ссылке.
def user(name, id):
    # Возвращаем на страницу текст.
    return 'User page: ' + name + ' ' + str(id)


# Проверка правильности запуска проекта через файл с названием app.
if __name__ == '__main__':
    # Запуск приложения и отслеживание ошибок.
    app.run(debug=True)
