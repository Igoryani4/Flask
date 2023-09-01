""" Написать программу, которая считывает список из 
10 URLадресов и одновременно загружает данные с каждого
адреса.
После загрузки данных нужно записать их в отдельные
файлы.
Используйте потоки. """


import threading
from flask import Flask, request
import requests
# import pandas as pd


app = Flask(__name__)


URL_LIST = ["https://gb.ru",
            "https://ya.ru",
            "https://google.com",
            "https://mail.ru",
            "https://vk.ru",
            "https://rambler.ru",
            "https://stackoverflow.com",
            "https://metanit.com/python",
            "https://pypi.org/project/requests/",
            "https://github.com/"
            "https://tproger.ru",
            "https://habr.com/ru/articles/"]


def parser_url(url: str, name: str):
    with app.test_request_context():
        from flask import request
        response = requests.get(url) 
        with open(name, 'w', encoding='UTF-8') as file:
            file.write(response.text)


threads = []


if __name__ == '__main__':
    for i, url in enumerate(URL_LIST):
        t = threading.Thread(target=parser_url, args=(url, f'thread-{i}.txt'))
        threads.append(t)
    print(*threads)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()