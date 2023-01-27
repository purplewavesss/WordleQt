import random
from datetime import date, timedelta

ORIGINAL_DATE = date(2023, 1, 26)


class WordChecker:
    def __init__(self):
        self.word = ""
        self.__game_type = ""
        self.hard_mode = False

        # Open and store potential-answers.txt
        with open("words/potential-answers.txt", "r") as word_file:
            self.word_list: list[str] = word_file.read().split()

        # Open and store real-answers.txt
        with open("words/real-answers.txt", "r") as word_file:
            self.answer_list: list[str] = word_file.read().split()

    def get_game_type(self):
        return self.__game_type

    def set_game_type(self, _game_type: str, _word: str = ""):
        self.__game_type = _game_type
        if self.__game_type != "manual":
            self.get_word()
        else:
            self.word = _word

    def get_word(self):
        # Store random word from list
        if self.__game_type == "random":
            random_word_index: int = random.randint(0, len(self.answer_list))
            self.word = self.answer_list[random_word_index]

        # Store word from daily-answers.txt
        elif self.__game_type == "daily":
            # Calculate time since first word
            elapsed: timedelta = date.today() - ORIGINAL_DATE
            day_num: int = elapsed.days

            # Open and store today's word from daily-answers.txt
            with open("words/daily-answers.txt", "r") as word_file:
                daily_word_list: list[str] = word_file.read().split()
                self.word = daily_word_list[day_num]

    def check_word(self, guess: str) -> dict[int, str]:
        check_word_dict: dict[int, str] = {}
        partial_dict: dict[str, int] = {}
        letter_occurrences: int = 0
        guess = guess.lower()

        for x in range(len(self.word)):
            # Check if word letter and guess letter are the same
            if self.word[x] == guess[x]:
                check_word_dict.update({x + 1: "correct"})
            else:
                # Check if guess letter exists somewhere else in the word
                for y in range(len(self.word)):
                    if self.word[y] == guess[x] and self.word[y] != guess[y]:
                        # Check if partial answer has already been accounted for
                        if self.word[y] in partial_dict.keys():
                            if partial_dict[self.word[y]] > letter_occurrences:
                                partial_dict[self.word[y]] += 1
                            else:
                                check_word_dict.update({x + 1: "incorrect"})
                                break
                        else:
                            # Add letter to partial_dict, to make sure the partial answer isn't accidentally repeated
                            partial_dict.update({self.word[y]: self.letter_count(self.word, self.word[y])})

                        check_word_dict.update({x + 1: "partial"})
                        letter_occurrences += 1
                        break
                    else:
                        check_word_dict.update({x + 1: "incorrect"})
        return check_word_dict

    def hard_valid_check(self, previous_guess: str, guess: str, failed_guesses: list[str]) -> bool:
        if self.valid_check(guess):
            previous_dict = self.check_word(previous_guess)
            current_dict = self.check_word(guess)

            # Checks if partials have been moved, corrects have been kept, and failed guesses removed
            for char in previous_dict.keys():
                if previous_dict[char] == "partial":
                    if previous_dict[char] == current_dict[char] and previous_dict[char] == "partial":
                        if previous_guess[char - 1] == guess[char - 1]:
                            return False

                    if not previous_guess[char - 1] in guess:
                        return False

                if previous_dict[char] != current_dict[char] and previous_dict[char] == "correct":
                    return False

                if guess[char - 1] in failed_guesses:
                    return False

            return True

        else:
            return False

    def valid_check(self, guess) -> bool:
        if guess.lower() in self.word_list:
            return True
        return False

    @staticmethod
    def letter_count(word: str, char: str) -> int:
        value = 0

        if len(char) == 1:
            for letter in range(len(word)):
                if word[letter] == char:
                    value += 1
            return value
        else:
            raise ValueError("Must input a length one character!")
