""" Flash сообщения
Flash сообщения в Flask являются способом передачи информации между запросами. 
Это может быть полезно, например, для вывода сообщений об успешном выполнении 
операции или об ошибках ввода данных.
Для работы с flash сообщениями используется функция flash(). 
Она принимает сообщение и категорию, к которой это сообщение относится, 
и сохраняет его во временном хранилище. """


from flask import Flask, flash, redirect, render_template,request, url_for


""" Секретный ключ
Небольшое отступление. Чтобы не получать ошибки вида при работе с сессией
необходимо добавить в Flask приложение секретный ключ.
Простейший способ генерации такого ключа, выполнить следующие пару строк кода """

# Сгенерировать секретный ключ в командной строке
# >>>import secrets
# >>>secrets.token_hex()


app = Flask(__name__)
app.secret_key =b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/')
def index():
    return 'Hi'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success') 
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)