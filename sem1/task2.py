""" Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше вебприложение:
○ страницу "about"
○ страницу "contact". """

from flask import Flask


app = Flask(__name__)

@app.route('/about/')
def about():
    return 'About us'


@app.route('/contact/')
def contact():
    return 'Contact us'


@app.route('/')
def hello_world():
    return 'Hello World!'
    


if __name__ == '__main__':
    app.run()