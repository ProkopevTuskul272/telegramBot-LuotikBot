from config import token
import random
import telebot

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'салам пополам')


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, 'я бот-повторюшочка')


@bot.message_handler(commands=['random'])
def send_random(message):
    bot.reply_to(message, str(random.randint(1,100)))


@bot.message_handler(commands=['otvetNaGlavnyyVoprosZhizniVselennoyIVsegoTakogo'])
def forty_two(message):
    bot.reply_to(message, str(42))

@bot.message_handler(commands=['anekdot'])
def anekdoty(message):
    list = ['пример 1',
            'пример 2',
            'пример 3',
            'пример 4']
    bot.reply_to(message, random.choice(list))

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == 'салам пополам':
        bot.reply_to(message, 'пока')
    else:
        bot.reply_to(message, message.text)


bot.infinity_polling()