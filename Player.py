class Player:
    def __init__(self):
        self.__answers: list[str] = []

    def get_answers(self) -> list[str]:
        return self.__answers

    def add_answer(self, answer):
        self.__answers.append(answer)
