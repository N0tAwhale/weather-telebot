from telebot import *
import random
from datetime import datetime
from pyowm import *
from pyowm.utils.config import get_default_config
bot = telebot.TeleBot('5551009021:AAHmZGgofzbk4NkA_HdPGPRpYLne6sc1-0s')
language = get_default_config()
language['language'] = 'ru'
owm = OWM('7bfb9951dd9ef554feb6223cf9c27328', language)
mgr = owm.weather_manager()


def weather(city):
    try:
        obs = mgr.weather_at_place(city)
        weather = obs.weather
        if len(weather.rain) == 0:
            rain = 0
        else:
            rain = weather.rain["1h"]
        string = f'Сейчас на улице:{weather.detailed_status}\nОблачность: {weather.clouds}%\nТекущая температура: {weather.temperature("celsius").get("temp")} градусов\nМаксимальная температура: {weather.temperature("celsius").get("temp_max")} градусов\nМинимальная температура: {weather.temperature("celsius").get("temp_min")} градусов\nСейчас ощущается: {weather.temperature("celsius").get("feels_like")} градусов\nСкорость ветра: {weather.wind().get("speed")} м/с\nЗа последний час выпало осадков: {rain} mm'
        return string
    except:
        return None

def forecast(lat, lon):
    one_call = mgr.one_call(lat=lat, lon=lon)
    print('Погода на ближайшие семь дней:')
    a = ''
    for i in range(7):
        a+=f'В этот день будет {one_call.forecast_daily[i].detailed_status}, температура воздуха днем {one_call.forecast_daily[i].temperature("celsius").get("day")} градусов\n'
    return a
def week(numb):
    if numb == 0:
        return 'Понедельник, '
    elif numb == 1:
        return 'Вторник,'
    elif numb == 2:
        return 'Среда,'
    elif numb == 3:
        return 'Четверг,'
    elif numb == 4:
        return 'Пятница,'
    elif numb == 5:
        return 'Суббота, '
    elif numb == 6:
        return 'Воскресенье, '


@bot.message_handler(commands = ['start'])
def start_message(message):
    keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton('Какой сегодня день?')
    button2 = types.KeyboardButton('Погода')
    button2_1 = types.KeyboardButton('Привет!')
    button2_2 = types.KeyboardButton('Пока!')
    keyboard1.add(button)
    keyboard1.add(button2)
    keyboard1.add(button2_1)
    keyboard1.add(button2_2)
    bot.send_message(message.chat.id,'Привет, сыграем в игру?))0) ',  reply_markup=keyboard1)
# @bot.message_handler(commands=['button'])
# def button_message(message):

@bot.message_handler(content_types=['text'])


def message_reply(message):
    if message.text == 'Привет!':
        bot.send_message(message.chat.id, 'И тебе привет!')
    if message.text == 'Пока!':
        bot.send_message(message.chat.id, 'Пока!')
    if message.text == 'Какой сегодня день?':
        text = f'{week(datetime.today().weekday())}  {str(datetime.today())[:10]}'
        bot.send_message(message.chat.id, text)
    if message.text == 'Погода':
        keyboard2= types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button3 = types.KeyboardButton('Погода сейчас в городе...')
        button4 = types.KeyboardButton('Прогноз на 7 дней в вашем городе')
        keyboard2.add(button3)
        keyboard2.add(button4)
        bot.send_message(message.chat.id, 'Выберете ', reply_markup=keyboard2)

    if message.text == 'Погода сейчас в городе...':
        bot.send_message(message.chat.id, 'Ведите название города!')
    if weather(message.text) is not None:
        bot.send_message(message.chat.id, weather(message.text))
    if message.text == 'Прогноз на 7 дней в вашем городе':
        keyboard3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button5 = types.KeyboardButton('Отправить геолокацию', request_location=True)
        keyboard3.add(button5)
        bot.send_message(message.chat.id, 'Мне нужна твоя геолокация!',reply_markup=keyboard3)



@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:

        bot.send_message(message.chat.id, forecast(message.location.latitude, message.location.longitude))

bot.infinity_polling()