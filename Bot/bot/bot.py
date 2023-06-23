import random
import telebot
import webbrowser
from telebot import types
from Bot.инструменти import configure


bot = telebot.TeleBot(configure.config['token'])

answers = ['Я не понял, что ты хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды.', 'Мой разработчик не говорил, что отвечать в такой ситуации... >_<']

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🏠  Снять квартиру')
    button2 = types.KeyboardButton('🏠  Аренда посуточно')


    markup.row(button1,button2)
   

    if message.text == '/start':

        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nУ меня ты сможешь купить некоторые товары!\nКонтакт моего разработчика: https://t.me/Rafo1212', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)


@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')


@bot.message_handler()
def info(message):
    if message.text == '🏠  Снять квартиру':
        goodsChapter(message)
    elif message.text == '🏠  Аренда посуточно':
        settingsChapter(message)
    elif message.text == '🔹 Товар #1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о первом товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар #2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о втором товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар #3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о третьем товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар #4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)

    elif message.text == '💳 Купить' :

        webbrowser.open('https://t.me/Rafo1212')
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)

    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])


def goodsChapter(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Товар #1')
    button2 = types.KeyboardButton('🔹 Товар #2')
    button3 = types.KeyboardButton('🔹 Товар #3')
    button4 = types.KeyboardButton('🔹 Товар #4')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)


    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)


def settingsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Настройки #1')
    button2 = types.KeyboardButton('🔹 Настройки #2')
    button3 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(message.chat.id, 'Раздел настроек.\nВыбери один из вариантов:', reply_markup=markup)


bot.polling(none_stop=True)
