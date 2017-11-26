import config
import telebot
from telebot import types

from bot import NoSuchAnswerException, get_phrase
from bot.storage import *
from bot.utils import generate_markup

bot = telebot.TeleBot(config.token)


def ask_question_or_give_answer(chat_id, status, result):
    if status:
        keyboard_hider = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, get_phrase("recommend film") % result, reply_markup=keyboard_hider)
    else:
        markup = generate_markup(answers[result])
        bot.send_message(chat_id, questions[result], reply_markup=markup)


@bot.message_handler(commands=["start"])
def greet_and_ask(message):
    bot.send_message(message.chat.id, get_phrase("greeting"))
    create_state(message.chat.id)
    status, result = update_action(message.chat.id)
    ask_question_or_give_answer(message.chat.id, status, result)


@bot.message_handler(content_types=["text"])
def process_message(message):
    try:
        status, result = update_action(message.chat.id, message.text)
        ask_question_or_give_answer(message.chat.id, status, result)
    except NoSuchAnswerException:
        bot.send_message(message.chat.id, get_phrase("wrong answer"))
        status, result = update_action(message.chat.id)
        ask_question_or_give_answer(message.chat.id, status, result)
    except SurveyNotStartedException:
        bot.send_message(message.chat.id, get_phrase("type start"))


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        finally:
            pass
