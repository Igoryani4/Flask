""" Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!". """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/*/')
def html_text():
    # return """ <h1> My first page </h1><p>Hello world!</p> """
    return """ 
    <title>My first page</title>
    <p>Hello world!</p>
     """

@app.route('/get-sheet/')
def get_sheet():
    sheet = [{'first_name' : 'Ivan', 'last_name' : 'Fedotov', 'age' : 23, 'agv_aver': 4.5},
             {'first_name' : 'Petr', 'last_name' : 'Petrov', 'age' : 21, 'agv_aver': 4.4},
             {'first_name' : 'Vadim', 'last_name' : 'Sidorov', 'age' : 29, 'agv_aver': 4.9}
             ]
    return render_template ('get_sheet.html', students = sheet)

@app.route('/about/')
def about():
    return 'About us'


@app.route('/len/<text>/')
def len_text(text):
    return f'Lenght input text = {len(text)}'


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