""" Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму. """

from flask import Flask


app = Flask(__name__)

@app.route('/about/')
def about():
    return 'About us'


@app.route('/contact/')
def contact():
    return 'Contact us'


@app.route('/sum/<int:num1>-<int:num2>/')
def sum_num(num1, num2):
    res = num1 + num2
    return f'{num1} + {num2} = {num1 +num2}'


@app.route('/')
def hello_world():
    return 'Hello World!'
    


if __name__ == '__main__':
    app.run()