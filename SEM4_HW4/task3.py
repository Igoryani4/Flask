""" Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте асинхронный подход. """


import asyncio
import aiohttp
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


async def parser_url(url: str, name: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(name, 'w', encoding='UTF-8') as file:
                r = await response.text()
                file.write(r)


if __name__ == '__main__':
    tasks = []
    for i, url in enumerate(URL_LIST):
        task = asyncio.ensure_future(parser_url(url, f'aiohttp-{i}.txt'))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))