"# weather-telebot" 
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
        keyboard2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
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
        bot.send_message(message.chat.id, 'Мне нужна твоя геолокация!', reply_markup=keyboard3)


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        bot.send_message(message.chat.id, forecast(message.location.latitude, message.location.longitude))


bot.infinity_polling()
