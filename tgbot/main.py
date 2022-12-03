import telebot
from telebot import types
import config
import parsing

token = config.token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('📖 Анекдот')
    item2 = telebot.types.KeyboardButton('♌ Гороскоп')
    button.add(item1, item2)
    bot.send_message(message.chat.id, "Привет ✌, этот бот расскажет анекдот.\n"
                                      "Ну или если очень хочется, то выдаст гороскоп", reply_markup=button)


@bot.message_handler(content_types=['text'])
def command_menu(message):
    if message.text == "📖 Анекдот":
        bot.send_message(message.chat.id, f"{parsing.random_joke()}")
    elif message.text == "♌ Гороскоп":
        button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Нет')
        item2 = telebot.types.KeyboardButton('Хочу❕')
        button.add(item1, item2)
        bot.send_message(message.chat.id, 'Точно хочешь?', reply_markup=button)
    elif message.text == "Хочу❕":
        button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Назад')
        item2 = telebot.types.KeyboardButton('ДААААА❗')
        button.add(item1, item2)
        bot.send_message(message.chat.id, 'Точно точно?', reply_markup=button)
    elif message.text == "ДААААА❗":
        markup = telebot.types.InlineKeyboardMarkup(row_width=3)
        item1 = telebot.types.InlineKeyboardButton('Овен ♈', callback_data='Овен')
        item2 = telebot.types.InlineKeyboardButton('Телец ♉', callback_data='Телец')
        item3 = telebot.types.InlineKeyboardButton('Близнецы ♊', callback_data='Близнецы')
        item4 = telebot.types.InlineKeyboardButton('Рак ♋', callback_data='Рак')
        item5 = telebot.types.InlineKeyboardButton('Лев ♌', callback_data='Лев')
        item6 = telebot.types.InlineKeyboardButton('Дева ♍', callback_data='Дева')
        item7 = telebot.types.InlineKeyboardButton('Весы ♎', callback_data='Весы')
        item8 = telebot.types.InlineKeyboardButton('Скорпион ♏', callback_data='Скорпион')
        item9 = telebot.types.InlineKeyboardButton('Стрелец ♐', callback_data='Стрелец')
        item10 = telebot.types.InlineKeyboardButton('Козерог ♑', callback_data='Козерог')
        item11 = telebot.types.InlineKeyboardButton('Водолей ♒', callback_data='Водолей')
        item12 = telebot.types.InlineKeyboardButton('Рыбы ♓', callback_data='Рыбы')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(message.chat.id, 'Выберите знак зодиака!', reply_markup=markup)
    elif message.text == "Назад":
        button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('📖 Анекдот')
        item2 = telebot.types.KeyboardButton('♌ Гороскоп')
        button.add(item1, item2)
        bot.send_message(message.chat.id, "Шутка или гороскоп?", reply_markup=button)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'Овен':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Овен'))
        elif call.data == 'Телец':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Телец'))
        elif call.data == 'Близнецы':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Близнецы'))
        elif call.data == 'Рак':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Рак'))
        elif call.data == 'Лев':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Лев'))
        elif call.data == 'Дева':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Дева'))
        elif call.data == 'Весы':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Весы'))
        elif call.data == 'Скорпион':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Скорпион'))
        elif call.data == 'Стрелец':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Стрелец'))
        elif call.data == 'Козерог':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Козерог'))
        elif call.data == 'Водолей':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Водолей'))
        elif call.data == 'Рыбы':
            bot.send_message(call.message.chat.id, parsing.get_horoscope('Рыбы'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Если хочешь еще один нажми "Да"', reply_markup=None)


bot.infinity_polling()
