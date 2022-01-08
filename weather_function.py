import requests as r
from my_token import token
import datetime


def get_weather(city, token=token):
    try:
        request = r.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
        data = request.json()

        text = f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}****\n" \
               f"Город : {data['name']}\n" \
               f"Температура сейчас : {data['main']['temp']}\n" \
               f"Максимальная температура в течении дня : {data['main']['temp_max']}\n" \
               f"Минимальная температура в течении дня : {data['main']['temp_min']}\n" \
               f"Cкорость ветра : {data['wind']['speed']} м/с\n" \
               f"Восход солнца : {datetime.datetime.fromtimestamp(data['sys']['sunrise'])}\n" \
               f"Закат : {datetime.datetime.fromtimestamp(data['sys']['sunset'])}\n" \
               f"Продолжительность дня : {datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])}"
        return text

    except Exception as ex:

        return "\U00002628 Something_wrong \U00002628"


def main():
    city = input("Введите ваш город - ")
    get_weather(city, token)


if __name__ == '__main__':
    main()
