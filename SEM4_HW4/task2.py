""" Задание №2
� Написать программу, которая считывает список из 10 URLадресов 
и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте процессы. """


import multiprocessing
import requests


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
    response = requests.get(url)
    with open(name, 'w', encoding='UTF-8') as file:
        file.write(response.text)


processes = []


if __name__ == '__main__':
    for i, url in enumerate(URL_LIST):
        p = multiprocessing.Process(target=parser_url, args=(url, f'process-{i}.txt'))
        processes.append(p)

    for process in processes:
        process.start()

    for process in processes:
        process.join()