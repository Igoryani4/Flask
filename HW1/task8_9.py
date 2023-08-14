from flask import Flask, render_template

app = Flask(__name__)

category = [
    {"title": 'Одежда', "func_name": 'dress'},
    {"title": 'Обувь', "func_name": 'shoes'},
    {"title": 'Куртка', "func_name": 'jacket'}
]

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', category=category)


@app.route('/info/')
def info():
    return render_template('info.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/dress/')
def dress():
    return render_template('dress.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')



@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')



if __name__ == '__main__':
    app.run()