from config import *


class State:

    def __init__(self):
        self.user_answers_ = {}
        self.current_question = 0

    def update_action(self, answer=None):
        if answer is not None:
            for i in range(len(answers[self.current_question - 1])):
                if answers[self.current_question - 1][i] == answer:
                    self.user_answers_[self.current_question] = i
                    break

        print(self.user_answers_)

        if len(self.user_answers_) >= len(questions):
            return True, "Зеленый слоник"  # Compute film here
        else:
            self.current_question = self.current_question + 1
            return False, self.current_question - 1

    def __str__(self):
        return str(self.user_answers_)
