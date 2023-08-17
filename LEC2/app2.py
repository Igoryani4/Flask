""" Для повышения безопасности необходимо экранировать пользовательский ввод. 
Для этого используйте функцию escape из модуля markupsafe. """


from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


@app.route('/<path:file>/')
def get_file(file):
   print(file)
   return f'Ваш файл находится в: {escape(file)}!'


if __name__ == "__main__":
   app.run(debug=True)

   """ А теперь вместо пути, передадим следующую строку:
http://127.0.0.1:5000/<script>alert("I am haсker")</script>/ """
