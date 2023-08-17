""" Работа с cookie файлами в Flask
Cookie файлы — это небольшие текстовые файлы, которые хранятся в браузере 
пользователя и используются для хранения информации о пользователе и его 
предпочтениях на сайте. В Flask, работа с cookie файлами очень проста и 
может быть выполнена с помощью самого фреймворка, 
без установки дополнительных модулей."""

from flask import Flask, request, make_response


app = Flask(__name__)


@app.route('/')
def index():
    # устанавливаем cookie
    response = make_response("Cookie установлен")
    response.set_cookie('username', 'admin')
    return response


@app.route('/getcookie/')
def get_cookies():
# получаем значение cookie
    name = request.cookies.get('username') 
    return f"Значение cookie: {name}"


if __name__ == '__main__':
    app.run(debug=True)