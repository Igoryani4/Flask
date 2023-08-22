""" Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени. """


from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello_page(name = None):
    context = {
        'name' : name or 'Igot'
    }
    return render_template('hello.html', **context)


""" Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений. """


@app.route('/form_page/')
def form_page():
    return render_template ('form_page.html')


""" Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой. """


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'Igot' and password == 'pass':
            return redirect(url_for('hello_page', name = name))
        return render_template ('form_page.html', error = True)
    return render_template ('form_page.html', error = None)


""" Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом. """


@app.route('/input_text/', methods=['POST', 'GET'])
def input_text():
    form1 = """ 
    <form method="post" enctype="multipart/form-data">
    <input type="text" placeholder="input_text" name="text"><br>
    <input type=submit value="Send"> 
    </form>
    """
    if request.method == 'POST':
        text = request.form.get('text')
        len_text = str(len(text.split()))
        return redirect(url_for('result_len', text = text, len_text=len_text))
    return form1


# @app.route('/res_len/<text>-<len_text>')  #вариант 1
# def result_len(text, len_text):
#     return f'{text}, {len_text}'


@app.route('/res_len/')         #вариант 2
def result_len():
    text = request.args.get('text')
    len_text = request.args.get('len_text')
    return f'{text}, {len_text}'


""" Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом. """


@app.route('/input_num/', methods= ['GET', 'POST'])
def input_num():
    form = """ <form method="post" enctype="multipart/form-data">
    <input type="text" placeholder="number1" name="num1"><br>
    <p><input list = "math" name = "option"></p>
        <datalist id = "math">
        <option value = '+'>+</option>
        <option value = '-'>-</option>
        <option value = '/'>/</option>
        <option value = '*'>*</option>
        </datalist>
    <input type="text" placeholder="number2" name="num2"><br>
    <input type=submit value="Send"> 
    </form>
    """

    
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        if request.form.get('option') == '+':
            res = num1 + num2
        elif request.form.get('option') == '-':
            res = num1 - num2
        elif request.form.get('option') == '/':
            res = num1 / num2
        else:
            res = num1 * num2
        return redirect(url_for('res_math', res = str(res)))
    return form

@app.route('/result/<res>')
def res_math(res):
    return res



if __name__ == '__main__':
    app.run(debug=True)