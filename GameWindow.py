from PyQt5 import QtWidgets, QtGui, QtCore
from Row import Row
from GameStats import GameStats
from UiGameWindow import UiMainWindow
from WordChecker import WordChecker

LOSE_SCORE: int = 7


# Encapsulates a main window and the functions of its items
class GameWindow(QtWidgets.QMainWindow, UiMainWindow):
    EXIT_CODE_REBOOT = -123456

    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        self.setup_ui(self)
        self.__game_type: str = ""
        self.word_checker = WordChecker()
        self.stats = GameStats()
        self.set_game_type("daily")
        self.__hard_mode: bool = False
        self.__light_mode: bool = True
        self.guesses: list[str] = []
        self.won: bool = False
        self.__game_end: bool = False
        self.current_row: Row = self.row1
        self.row_index: int = 0
        self.first_time: bool = True
        self.played_today: bool = self.stats.played_today()
        self.enter_button.clicked.connect(self.enter_case)
        self.failed_guesses: list[str] = []

    def get_game_type(self) -> str:
        return self.__game_type

    def set_game_type(self, _game_type: str, _word: str = ""):
        self.__game_type = _game_type
        self.word_checker.set_game_type(self.__game_type, _word)
        self.stats.game_type = self.__game_type

    def get_game_end(self) -> bool:
        return self.__game_end

    def set_game_end(self, _game_end: bool, lose: bool):
        self.__game_end = _game_end
        if self.__game_end:
            if self.get_game_type() != "daily" or not self.played_today:
                if not lose:
                    self.stats.add_score(len(self.guesses))
                else:
                    self.stats.add_score(7)

                if not self.played_today and self.get_game_type() == "daily":
                    self.add_to_streak()

            self.enter_case()

    def get_hard_mode(self) -> bool:
        return self.__hard_mode

    def set_hard_mode(self, _hard_mode: bool):
        self.__hard_mode = _hard_mode
        self.stats.hard_mode = _hard_mode

    def get_light_mode(self) -> bool:
        return self.__light_mode

    def set_light_mode(self, _light_mode: bool):
        self.__light_mode = _light_mode
        for row in self.rows:
            row.light_mode = self.get_light_mode()
        self.set_dark()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.key_parse(a0)

    def key_parse(self, keyboard: QtGui.QKeyEvent):
        # Switch on key entered
        match keyboard.key():
            case QtCore.Qt.Key.Key_A:
                self.add_char("A")
            case QtCore.Qt.Key.Key_B:
                self.add_char("B")
            case QtCore.Qt.Key.Key_C:
                self.add_char("C")
            case QtCore.Qt.Key.Key_D:
                self.add_char("D")
            case QtCore.Qt.Key.Key_E:
                self.add_char("E")
            case QtCore.Qt.Key.Key_F:
                self.add_char("F")
            case QtCore.Qt.Key.Key_G:
                self.add_char("G")
            case QtCore.Qt.Key.Key_H:
                self.add_char("H")
            case QtCore.Qt.Key.Key_I:
                self.add_char("I")
            case QtCore.Qt.Key.Key_J:
                self.add_char("J")
            case QtCore.Qt.Key.Key_K:
                self.add_char("K")
            case QtCore.Qt.Key.Key_L:
                self.add_char("L")
            case QtCore.Qt.Key.Key_M:
                self.add_char("M")
            case QtCore.Qt.Key.Key_N:
                self.add_char("N")
            case QtCore.Qt.Key.Key_O:
                self.add_char("O")
            case QtCore.Qt.Key.Key_P:
                self.add_char("P")
            case QtCore.Qt.Key.Key_Q:
                self.add_char("Q")
            case QtCore.Qt.Key.Key_R:
                self.add_char("R")
            case QtCore.Qt.Key.Key_S:
                self.add_char("S")
            case QtCore.Qt.Key.Key_T:
                self.add_char("T")
            case QtCore.Qt.Key.Key_U:
                self.add_char("U")
            case QtCore.Qt.Key.Key_V:
                self.add_char("V")
            case QtCore.Qt.Key.Key_W:
                self.add_char("W")
            case QtCore.Qt.Key.Key_X:
                self.add_char("X")
            case QtCore.Qt.Key.Key_Y:
                self.add_char("Y")
            case QtCore.Qt.Key.Key_Z:
                self.add_char("Z")
            case QtCore.Qt.Key.Key_Backspace:
                self.remove_char()
            case QtCore.Qt.Key.Key_Return:
                self.enter_case()

    def add_char(self, char: str):
        self.current_row.add_char(char)
        if char in self.failed_guesses:
            self.current_row.char_boxes[len(self.current_row.get_word()) - 1].set_status("incorrect")

    def remove_char(self):
        old_char: str = self.current_row.char_boxes[len(self.current_row.get_word()) - 1].get_text()
        self.current_row.remove_char()
        if old_char in self.failed_guesses:
            self.current_row.char_boxes[len(self.current_row.get_word())].set_status("blank")

    def enter_word(self):
        # Check if word is proper length, not past last word, and valid
        if len(self.current_row.get_word()) == 5 and len(self.guesses) < 6 and self.word_checker.valid_check(
                self.current_row.get_word()):
            if not self.get_hard_mode() or self.first_time or self.word_checker.hard_valid_check(
                                                              self.guesses[len(self.guesses) - 2],
                                                              self.current_row.get_word(), self.failed_guesses):
                self.guesses.append(self.current_row.get_word())
                self.first_time = False

                # Generate dictionary for CharBox color statuses
                word_dict = self.word_checker.check_word(self.current_row.get_word())

                # Color row
                for x in range(len(self.current_row.char_boxes)):
                    self.current_row.char_boxes[x].set_status(word_dict[x + 1])
                    if self.current_row.char_boxes[x].get_status() == "incorrect" and not \
                            self.current_row.char_boxes[x].get_text() in self.failed_guesses:
                        self.failed_guesses.append(self.current_row.char_boxes[x].get_text())

                # Check if game was won
                self.won = True
                for letter in word_dict.keys():
                    if word_dict[letter] != "correct":
                        self.won = False
                        break

                # Loss scenario
                if self.row_index == 5 and not self.won:
                    self.lose()

                else:
                    # If not last row, switch to next row
                    if self.row_index < 5 and not self.won:
                        self.row_index += 1
                        self.current_row = self.rows[self.row_index]

                    # If won, display win message
                    elif self.won:
                        self.win()

            elif not self.word_checker.hard_valid_check(self.guesses[len(self.guesses) - 2],
                                                        self.current_row.get_word(), self.failed_guesses):
                self.gen_message_box("Invalid guess!", f'Your guess "{self.current_row.get_word()}" did not meet the '
                                                       f'rules for hard mode.', QtWidgets.QMessageBox.Icon.Warning)

        # Invalid word
        elif len(self.current_row.get_word()) == 5 and len(self.guesses) < 6 and not self.word_checker.valid_check(
                self.current_row.get_word()):
            self.gen_message_box("Invalid guess!", f'Your guess "{self.current_row.get_word()}" was not in the word '
                                                   f'list.', QtWidgets.QMessageBox.Icon.Warning)

        elif len(self.current_row.get_word()) != 5:
            self.gen_message_box("Invalid guess!", f'Your guess was not five letters long!',
                                 QtWidgets.QMessageBox.Icon.Warning)

    def reset(self, _game_type: str, _word: str = ""):
        # Resets all game variables to their initial values
        self.set_game_type(_game_type, _word)
        for row in self.rows:
            row.clear_row()
        self.guesses = []
        self.won = False
        self.current_row = self.row1
        self.row_index = 0

    def enter_case(self):
        if not self.get_game_end():
            self.enter_word()
        else:
            self.reset("random")
            self.set_game_end(False, False)

    def add_to_streak(self):
        if not self.played_today:
            self.played_today = True
            self.stats.add_to_streak()

    def lose(self):
        # First play message
        if not self.played_today or self.get_game_type() != "daily":
            self.gen_message_box("Loser", f'You lost! The word was {self.word_checker.word.upper()}.',
                                 QtWidgets.QMessageBox.Icon.NoIcon)
            self.set_game_end(True, True)

        # Post-first play message
        elif self.played_today and self.get_game_type() == "daily":
            self.gen_message_box("Loser", f'You lost! The word was {self.word_checker.word.upper()}. Thankfully'
                                          f', this won\'t count, as you\'ve already played today.',
                                 QtWidgets.QMessageBox.Icon.NoIcon)
            self.set_game_end(True, True)

    def win(self):
        # First play message
        if not self.played_today or self.get_game_type() != "daily":
            self.gen_message_box("Winner", f'You won after {len(self.guesses)} guesses!',
                                 QtWidgets.QMessageBox.Icon.NoIcon)
            self.set_game_end(True, False)

        # Post-first play message
        elif self.played_today and self.get_game_type() == "daily":
            self.gen_message_box("Winner", f'You won after {len(self.guesses)} guesses! You\'ve already '
                                           f'played today, so this game won\'t count.',
                                 QtWidgets.QMessageBox.Icon.NoIcon)
            self.set_game_end(True, False)

    def set_dark(self):
        for row in self.rows:
            for char_box in row.char_boxes:
                if self.get_light_mode():
                    char_box.set_status("blank")
                else:
                    char_box.set_status("blank_dark")

    @staticmethod
    def gen_message_box(title: str, message: str, icon: QtWidgets.QMessageBox.Icon):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setIcon(icon)
        message_box.setText(message)
        message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        message_box.exec()
