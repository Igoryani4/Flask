""" Создание ответа
Несколько слов о функции make_response(). 
Во всех прошлых примерах мы возвращали из view функций обычный текст, 
текст форматированный как HTML, динамически сгенерированные страницы через 
render_template и даже запросы переадресации благодаря функциям redirect и url_for. 
Каждый раз Flask неявно формировал объект ответа - response. 
Если же мы хотим внести изменения в ответ,
 можно воспользоваться функцией make_response. """

from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
            'title': 'Главная',
            'name': 'Харитон'
            }
    response = make_response(render_template('main.html',**context))
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response


if __name__ == '__main__':
    app.run(debug=True)