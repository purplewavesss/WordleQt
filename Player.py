class Player:
    def __init__(self):
        self.__answers: list[str] = []

    def add_answer(self, answer):
        self.__answers.append(answer)
