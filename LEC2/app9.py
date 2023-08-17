""" Декоратор errorhandler
Flask предоставляет возможности для обработки ошибок и способен заменить 
стандартный текст на симпатичную страницу в стиле вашего сайта.
Обработка ошибок в Flask происходит с помощью декоратора errorhandler(). 
Этот декоратор позволяет определить функцию-обработчик ошибок, 
которая будет вызываться в случае возникновения ошибки в приложении.
Например, чтобы обработать ошибку 404 (страница не найдена), 
необходимо определить функцию, которая будет вызываться при возникновении этой ошибки:"""


import logging
from flask import Flask, render_template, request


app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


if __name__ == "__main__":
   app.run(debug=True)

  
