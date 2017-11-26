from numpy import nan

from config import *
from Predictor import Predictor
from .exceptions import NoSuchAnswerException


class State:

    def __init__(self):
        self.predictor = Predictor("clusters.csv")

    def update_action(self, answer=None):

        answer_id = None

        if answer is not None:
            found = False
            for i in range(len(answers)):
                if answers[i] == answer:
                    answer_id = i
                    found = True
                    break

            if not found:
                raise NoSuchAnswerException("No such answer")

            if answer_id is not None:
                if answer_id == 0:
                    self.predictor.update("yes")
                elif answer_id == 1:
                    self.predictor.update("no")
                elif answer_id == 2:
                    self.predictor.update("probably")

        film = self.predictor.get_film()
        while film[0][2] is nan:
            film = self.predictor.get_film()

        return film

    def __str__(self):
        return str("State")
