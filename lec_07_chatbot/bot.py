import config
import telebot
from telebot import types

users = {}

sticker_id = "CAACAgIAAxkBAAIBmV_GKthXR2jNn1m8bXyo6dBqWgapAAIRAgACCTs7E9iC43rBPvyCHgQ"

bot = telebot.TeleBot(config.apikey)

@bot.message_handler(commands=['stop'])
def stop(message):
    print("stoped")
    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)

@bot.message_handler(content_types=['text'])
def start(message):
    global users
    if message.text == '/reg':
        users.update({message.from_user.username: {}})
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
    global users
    users[message.from_user.username].update({"name": message.text})
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global users
    users[message.from_user.username].update({"surname": message.text})
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global users
    global sticker_id
    try:
        users[message.from_user.username].update({"age": int(message.text)})
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_age)
        return
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)

    question = 'Тебе {} лет, тебя зовут {} {}?'.format(users[message.from_user.username]["age"], users[message.from_user.username]["name"], users[message.from_user.username]["surname"])
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    bot.send_sticker(message.from_user.id, sticker_id)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global users
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню :)')
        # сохранение в БД
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Ну, пока, пока!')
        del users[call.message.from_user.username]

bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()
bot.polling(none_stop=True)
