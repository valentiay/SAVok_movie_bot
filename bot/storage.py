import shelve

from config import *

from . import State, SurveyNotStartedException


def create_state(chat_id):
    with shelve.open(shelve_name, writeback=True) as storage:
        if str(chat_id) in storage:
            del storage[str(chat_id)]

        storage[str(chat_id)] = State()


def update_action(chat_id, text=None):
    with shelve.open(shelve_name, writeback=True) as storage:
        try:
            state = storage[str(chat_id)]

            if text is not None:
                action = state.update_action(text)
            else:
                action = state.update_action()

            storage[str(chat_id)] = state

            if action[0]:
                del storage[str(chat_id)]

            return action
        except KeyError:
            raise SurveyNotStartedException("Survey not started")
