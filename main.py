import sys

import config
import telebot

from bot import NoSuchAnswerException, get_phrase
from bot.storage import *
from bot.utils import generate_markup

bot = telebot.TeleBot(config.token)


def recommend_film(chat_id, result):
    markup = generate_markup()
    bot.send_message(chat_id, "\"" + str(result[0][2]) + "\"\n Рейтинг: " + str(result[0][4]) + "\n" + str(result[0][3]) + "\n" + str(result[0][5]), reply_markup=markup)


@bot.message_handler(commands=["start"])
def greet_and_ask(message):
    bot.send_message(message.chat.id, get_phrase("greeting"))
    create_state(message.chat.id)
    result = update_action(message.chat.id)
    recommend_film(message.chat.id, result)


@bot.message_handler(content_types=["text"])
def process_message(message):
    try:
        print("[%d] %s" % (message.chat.id, message.text), file=sys.stderr)
        result = update_action(message.chat.id, message.text)
        recommend_film(message.chat.id, result)
    except NoSuchAnswerException:
        bot.send_message(message.chat.id, get_phrase("wrong answer"))
        result = update_action(message.chat.id)
        recommend_film(message.chat.id, result)
    except SurveyNotStartedException:
        bot.send_message(message.chat.id, get_phrase("type start"))


if __name__ == '__main__':
    print("Bot is now running")
    while True:
        try:
            bot.polling(none_stop=True)
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            print("Restarted bot")
