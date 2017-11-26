import random

from phrases_list import *


def get_phrase(category):
    try:
        return random.choice(phrases_list[category])
    except KeyError:
        raise Exception("No such phrase")
