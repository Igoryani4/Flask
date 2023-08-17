""" Генерация пути к статике
Один из распространённых способов использования 
url_for является указание пути к файлам статики внутри шаблонов. """


from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi'


@app.route('/about/') 
def about():
    context = {
        'title': 'Обо мне', 
        'name': 'Igoryan',
        }
    return render_template('about.html', **context)



if __name__ == "__main__":
   app.run(debug=True)

  
