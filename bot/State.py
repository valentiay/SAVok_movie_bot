from config import *
from .exceptions import NoSuchAnswerException


class State:

    def __init__(self):
        self.user_answers_ = {}
        self.current_question = 0

    def update_action(self, answer=None):

        if answer is not None:
            found = False
            for i in range(len(answers[self.current_question])):
                if answers[self.current_question][i] == answer:
                    self.user_answers_[self.current_question] = i
                    found = True
                    break

            if not found:
                raise NoSuchAnswerException("No such answer")

        if len(self.user_answers_) >= len(questions):
            return True, "Зеленый слоник"  # Compute film here
        else:
            if answer is not None:
                self.current_question = self.current_question + 1
                return False, self.current_question
            else:
                return False, self.current_question

    def __str__(self):
        return str(self.user_answers_)
