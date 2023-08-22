""" Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени. """


from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello_page(name = None):
    context = {
        'name' : name or 'Igot'
    }
    return render_template('hello.html', **context)



@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        print(name, password)
        if name == 'Igot' and password == 'pass':
            return redirect(url_for('hello_page', name = name))
        return render_template ('form_page.html', error = True)
    return render_template ('form_page.html', error = None)


if __name__ == '__main__':
    app.run()