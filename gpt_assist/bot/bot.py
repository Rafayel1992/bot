import telebot
from telebot import types


bot = telebot.TeleBot("6216739188:AAGI1LRLGG_CSeqCHgdGaq8lYkZr31omDTY")



@bot.message_handler(commands=['start'])
def handle_start(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=2)


    button1 = types.KeyboardButton("'.Վարձակալել բնակարան''\n.Снять квартиру''\n.To rent an apartment'")
    button2 = types.KeyboardButton('.Ամրագրեք''\n.Зарезервировать\n''\n.Make a reservation')
    button3 = types.KeyboardButton('.Զամբյուղ''\n.Корзина''\n.Cart')
    button4 = types.KeyboardButton( 'Հետ'"\nНазад"'\nBack')


    keyboard.add(button1, button2, button3,button4)


    bot.reply_to(message, "Привет! Я бот. "
                                                                    "\n.Այստեղ դուկ կարողեք վարձակալել բնակարան"
                                                                    "\n.Գնել  բնակարան"
                                                                    "\n.Ինչպես նաև վարձակալել օրավարձով:\n"
                                                                    "\n.Здесь можно снять квартиру."
                                                                    "\n.Купить квартиру."
                                                                    "\n.A так же аренда посуточно.\n"
                                                                    '\n.Here you can rent an apartment.'
                                                                    "\n.Buy an apartment as well as daily", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Кнопка 1")
def handle_button1(message):
    bot.reply_to(message, "Вы нажали на Кнопку 1")


@bot.message_handler(func=lambda message: message.text == "Кнопка 2")
def handle_button2(message):
    bot.reply_to(message, "Вы нажали на Кнопку 2")



@bot.message_handler(func=lambda message: message.text == "Кнопка 3")
def handle_button3(message):
    bot.reply_to(message, "Вы нажали на Кнопку 3")

@bot.message_handler(func=lambda message: message.text == "Кнопка 4")
def handle_button4(message):
    bot.reply_to(message, "Вы нажали на Кнопку 4")


bot.polling()
