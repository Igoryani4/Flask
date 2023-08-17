""" Перенаправления
Перенаправления в Framework Flask позволяют перенаправлять пользователя с одной 
страницы на другую. Это может быть полезно, например, для перенаправления пользователя 
после успешной отправки формы или для перенаправления пользователя на страницу авторизации 
при попытке доступа к защищенной странице без авторизации.
Для перенаправления в Flask используется функция redirect(). Она принимает URL-адрес, 
на который нужно перенаправить пользователя, и возвращает объект ответа, 
который перенаправляет пользователя на указанный адрес."""

from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external')
def external_redirect():
    return redirect('https://yandex.ru')


@app.route('/hello/<name>') 
def hello(name):
    return f'Привет, {name}!'


@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))

""" В этом примере мы определяем маршрут '/hello/<name>', 
который принимает параметр 'name', и маршрут '/redirect/<name>', 
который использует функцию redirect() для перенаправления пользователя на 
маршрут '/hello/<name>' с передачей параметра 'name'. 
Функция url_for() возвращает URL-адрес для указанного маршрута с передачей параметров. """


if __name__ == "__main__":
   app.run(debug=True)

  
