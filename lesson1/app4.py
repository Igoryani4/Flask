""" В примере выше мы передали через name строковое значение. Это действие по умолчанию. Помимо этого можно передавать следующие данные:
● string — (по умолчанию) принимает текст без слеша
● int — принимает позитивные целые числа
● float — принимает позитивные числа с плавающей точкой
● path — как string, но принимает слеши
● uuid — принимает строки UUID """


from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return f'Привет, {name.capitalize()}!'


@app.route('/file/<path:file>/')
def set_path(file):
   print(type(file))
   return f'Путь до файла "{file}"'


@app.route('/number/<float:num>/')
def set_number(num):
   print(type(num))
   return f'Передано число {num}'


if __name__ == "__main__":
   app.run(debug=True)
