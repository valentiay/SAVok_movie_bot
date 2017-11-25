from random import shuffle

from telebot import types


def generate_markup(answers):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    shuffle(answers)
    for item in answers:
        markup.add(item)
    return markup
