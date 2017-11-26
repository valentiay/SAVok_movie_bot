
class NoSuchAnswerException(BaseException):
    def __init__(self, error):
        self.error = error
