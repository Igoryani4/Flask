""" Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!". """



import secrets
from flask import Flask, flash, redirect, render_template, request, url_for
from markupsafe import escape



app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/flas/', methods=['GET', 'POST'])
def flas():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flas'))
    return render_template('flas.html')



if __name__ == '__main__':
    app.run(debug=True)