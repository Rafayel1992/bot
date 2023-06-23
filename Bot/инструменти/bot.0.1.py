import telebot
import webbrowser
from Bot.инструменти import configure
from telebot import types


bot = telebot.TeleBot(configure.config['token'])


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)

    button1 = types.KeyboardButton("Снять квартиру")
    button2 = types.KeyboardButton('Аренда посуточно')
    button3 = types.KeyboardButton('dlya branirovanya najmite suda')

    keyboard.add(button1, button2, button3)

    bot.reply_to(message, "Привет! Я бот. "
                          "\n.Այստեղ դուկ կարողեք վարձակալել բնակարան"
                          "\n.Գնել  բնակարան"
                          "\n.Ինչպես նաև վարձակալել օրավարձով:\n"
                          "\n.Здесь можно снять квартиру."
                          "\n.Купить квартиру."
                          "\n.A так же аренда посуточно.\n"
                          '\n.Here you can rent an apartment.'
                          "\n.Buy an apartment as well as daily", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Снять квартиру")
def handle_button1(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    button1 = types.InlineKeyboardButton("Кнопка 1", callback_data='button1')
    button2 = types.InlineKeyboardButton("Кнопка 2", callback_data='button2')
    button3 = types.InlineKeyboardButton("Кнопка 3", callback_data='button3')

    keyboard.add(button1, button2, button3)
    bot.reply_to(message, "Привет! Выберите одну из кнопок:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 1")
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 2")
    elif call.data == 'button3':
        bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 3")


@bot.message_handler(func=lambda message: message.text == "Аренда посуточно")
def handle_button2(message):
    key_board = types.InlineKeyboardMarkup(row_width=1)

    button1 = types.InlineKeyboardButton("Кнопка 1", callback_data='button1')
    button2 = types.InlineKeyboardButton("Кнопка 2", callback_data='button2')
    button3 = types.InlineKeyboardButton("Кнопка 3", callback_data='button3')

    key_board.add(button1, button2, button3)
    bot.reply_to(message, "Привет! Выберите одну из кнопок:", reply_markup=key_board)


@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 1")
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 2")
    elif call.data == 'button3':
        bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 3")


@bot.message_handler(func=lambda message: message.text == "dlya branirovanya najmite suda")
def handle_button3(message):
    bot.reply_to(message)


bot.polling(none_stop=True)