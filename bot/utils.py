from telebot import types

from config import answers


def generate_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in answers:
        markup.add(item)
    return markup
