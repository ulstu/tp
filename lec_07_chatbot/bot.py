import config
import telebot
from telebot import types

name = ''
surname = ''
age = 0
sticker_id = "CAACAgIAAxkBAAIBmV_GKthXR2jNn1m8bXyo6dBqWgapAAIRAgACCTs7E9iC43rBPvyCHgQ"

bot = telebot.TeleBot(config.apikey)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

@bot.message_handler(content_types=['sticker'])
def print_sticker_id(message):
    global sticker_id
    bot.send_message(message.from_user.id, message.sticker.file_id)
    sticker_id = message.sticker.file_id


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    global sticker_id
    try:
        age = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_age)
        return
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')
    bot.send_sticker(message.from_user.id, sticker_id)

bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()
bot.polling(none_stop=True)
