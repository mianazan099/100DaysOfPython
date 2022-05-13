from tokenize import String


class Question:
    def __init__(self, text: String) -> None:
        self.text = text
        self.answer = ''

question = Question()