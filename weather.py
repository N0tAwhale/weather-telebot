from pyowm import *
from pyowm.utils.config import get_default_config
language = get_default_config()
language['language'] = 'ru'
owm = OWM('7bfb9951dd9ef554feb6223cf9c27328', language)
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=53.90, lon=27.55)
city = input('Введи название города ')
while city != 'стоп':
    obs = mgr.weather_at_place(city)
    weather = obs.weather
    print('Сейчас на улице:', weather.detailed_status)
    print(f'Облачность: {weather.clouds}%')
    print(f'Текущая температура: {weather.temperature("celsius").get("temp")} градусов')
    print(f'Максимальная температура: {weather.temperature("celsius").get("temp_max")} градусов')
    print(f'Минимальная температура: {weather.temperature("celsius").get("temp_min")} градусов')
    print(f'Сейчас ощущается: {weather.temperature("celsius").get("feels_like")} градусов')
    if len(weather.rain) == 0:
        rain = 0
    else:
        rain = weather.rain["1h"]
    print(f'За последний час выпало осадков: {rain} mm')
    print(f'Скорость ветра: {weather.wind().get("speed")} м/с')
    city = input('Введи название города ')
# print('Погода на ближайшие семь дней:')
# for i in range(7):
#     print(f'В этот день будет {one_call.forecast_daily[i].detailed_status}, температура воздуха днем {one_call.forecast_daily[i].temperature("celsius").get("day")} градусов')