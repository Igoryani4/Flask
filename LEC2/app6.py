""" Обработка POST запросов
POST запросы используются для отправки данных на сервер. 
Они отличаются от GET запросов тем, что данные, передаваемые в POST запросах, не видны в URL. 
Также POST запросы могут содержать большее количество данных, чем GET.
Для того, чтобы передать данные в POST запросе, обычно используют HTML форму. 
У формы нужно указать атрибут method="post" для правильной обработки сервером. """


from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi'


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == "__main__":
   app.run(debug=True)

  
