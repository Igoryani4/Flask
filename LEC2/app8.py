""" Загрузка файлов через POST запрос
Загрузка файлов на сервер является неотъемлемой частью многих веб-приложений. 
В Flask, загрузка файлов может быть выполнена с помощью модуля Flask и объекта request. 
Рассмотрим простейший пример такой загрузки."""


from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads',file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


if __name__ == "__main__":
   app.run(debug=True)

  
