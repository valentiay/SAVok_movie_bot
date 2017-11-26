import config
import telebot
from telebot import types

from bot import NoSuchAnswerException
from bot.storage import *
from bot.utils import generate_markup

bot = telebot.TeleBot(config.token)


def ask_question_or_give_answer(chat_id, status, result):
    if status:
        keyboard_hider = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, 'Вам точно понравится фильм "%s"' % result, reply_markup=keyboard_hider)
    else:
        markup = generate_markup(answers[result])
        bot.send_message(chat_id, questions[result], reply_markup=markup)


@bot.message_handler(commands=["start"])
def greet_and_ask(message):
    bot.send_message(message.chat.id, "Добро пожаловать. Сейчас я проведу допрос с целью выявления фильма, "
                                      "который вам понравится.")
    create_state(message.chat.id)
    status, result = update_action(message.chat.id)
    ask_question_or_give_answer(message.chat.id, status, result)


@bot.message_handler(content_types=["text"])
def process_message(message):
    try:
        status, result = update_action(message.chat.id, message.text)
        ask_question_or_give_answer(message.chat.id, status, result)
    except NoSuchAnswerException:
        bot.send_message(message.chat.id, "Что-то я не понел, попробуй еще разок.")
        status, result = update_action(message.chat.id)
        ask_question_or_give_answer(message.chat.id, status, result)


if __name__ == '__main__':
    bot.polling(none_stop=True)