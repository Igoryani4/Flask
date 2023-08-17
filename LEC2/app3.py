""" Генерация url адресов """


from flask import Flask, url_for
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi'


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'
    return text


if __name__ == "__main__":
   app.run(debug=True)

   """ А теперь вместо пути, передадим следующую строку:
http://127.0.0.1:5000/<script>alert("I am haсker")</script>/ """


""" При переходе по адресу test_url_for/7/ увидем следующий вывод:
В num лежит 7
Функция url_for("test_url", num=42) = '/test_url_for/42/'
Функция url_for("test_url", num=42, data="new_data") ='/test_url_for/42/?data=new_data'
Функция url_for("test_url", num=42, data="new_data", pi=3.14515)= '/test_url_for/42/?data=new_data&pi=3.14515' """