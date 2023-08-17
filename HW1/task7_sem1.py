from flask import Flask, render_template



app = Flask(__name__)


news = [
    {"title": 'Работа с «Ягодой» для новичков: ', "date": '2023-08-16', "text": 'Данная статья создана \
     с ознакомительной целью и служит рекомендацией по работе с Raspberry Pi 4 Model B ("Ягода"), \
     WEMOS WiFi & Bluetooth ESP32 ("ESP32") при настройки Serial Peripheral Interface (SPI).'},
    {"title": 'real-time данные', "date": '2023-05-22', "text": 'The Graph - это децентрализованный \
     протокол, который позволяет получать доступ к данным смарт контрактов на блокчейне, индексируемым \
     децентрализованными так называемыми «индексаторами», курируемым - «кураторами» и\
      спонсируемым - «делегаторами».'},
    {"title": 'DLBI: на продажу ', "date": '2023-08-12', "text": '14 августа 2023 года на одном из\
      теневых форумов на продажу была выставлена база данных зарегистрированных пользователей,\
      а также доступ к серверу Discord.io - стороннему интерфейсу для серверов кроссплатформенной \
     проприетарной системы Discord.'},
    {"title": 'NLP в BI не работает', "date": '2020-04-20', "text": 'Easy Report - это BI-решение,\
      основанное на технологии NLP (обработка запросов, заданных естественным языком) и присылающее\
      мгновенно формирующиеся отчеты в мессенджер. Решение работает с любыми источниками данных и \
     не требует разработок дашбордов и отчетов.'}
]



@app.route('/news/')
def news_page():
    return render_template('news.html', news=news)

if __name__ == '__main__':
    app.run()