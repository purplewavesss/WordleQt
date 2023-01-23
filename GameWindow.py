LOSE_SCORE: int = 7


from PyQt5 import QtWidgets, QtGui, QtCore
from Row import Row
from GameStats import GameStats
from UiMainWindow import UiMainWindow
from WordChecker import WordChecker


# Encapsulates a main window and the functions of its items
class GameWindow(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self, _stats: GameStats, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        self.setup_ui(self)
        self.__game_type: str = ""
        self.word_checker = WordChecker()
        self.stats = _stats
        self.set_game_type("daily")
        self.hard_mode: bool = False
        self.light_mode: bool = True
        self.guesses: list[str] = []
        self.won: bool = False
        self.__game_end: bool = False
        self.current_row: Row = self.row1
        self.row_index: int = 0
        self.first_time: bool = True
        self.enter_button.clicked.connect(self.enter_case)

    def get_game_type(self) -> str:
        return self.__game_type

    def set_game_type(self, _game_type: str, _word: str = ""):
        self.__game_type = _game_type
        self.word_checker.set_game_type(self.__game_type, _word)
        self.stats.game_type = self.__game_type

    def get_game_end(self) -> bool:
        return self.__game_end

    def set_game_end(self, _game_end: bool):
        self.__game_end = _game_end
        if self.__game_end:
            self.stats.add_score(len(self.guesses))
            self.enter_case()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.key_parse(a0)

    def key_parse(self, keyboard: QtGui.QKeyEvent):
        # Switch on key entered
        match keyboard.key():
            case QtCore.Qt.Key.Key_A:
                self.current_row.add_char("A")
            case QtCore.Qt.Key.Key_B:
                self.current_row.add_char("B")
            case QtCore.Qt.Key.Key_C:
                self.current_row.add_char("C")
            case QtCore.Qt.Key.Key_D:
                self.current_row.add_char("D")
            case QtCore.Qt.Key.Key_E:
                self.current_row.add_char("E")
            case QtCore.Qt.Key.Key_F:
                self.current_row.add_char("F")
            case QtCore.Qt.Key.Key_G:
                self.current_row.add_char("G")
            case QtCore.Qt.Key.Key_H:
                self.current_row.add_char("H")
            case QtCore.Qt.Key.Key_I:
                self.current_row.add_char("I")
            case QtCore.Qt.Key.Key_J:
                self.current_row.add_char("J")
            case QtCore.Qt.Key.Key_K:
                self.current_row.add_char("K")
            case QtCore.Qt.Key.Key_L:
                self.current_row.add_char("L")
            case QtCore.Qt.Key.Key_M:
                self.current_row.add_char("M")
            case QtCore.Qt.Key.Key_N:
                self.current_row.add_char("N")
            case QtCore.Qt.Key.Key_O:
                self.current_row.add_char("O")
            case QtCore.Qt.Key.Key_P:
                self.current_row.add_char("P")
            case QtCore.Qt.Key.Key_Q:
                self.current_row.add_char("Q")
            case QtCore.Qt.Key.Key_R:
                self.current_row.add_char("R")
            case QtCore.Qt.Key.Key_S:
                self.current_row.add_char("S")
            case QtCore.Qt.Key.Key_T:
                self.current_row.add_char("T")
            case QtCore.Qt.Key.Key_U:
                self.current_row.add_char("U")
            case QtCore.Qt.Key.Key_V:
                self.current_row.add_char("V")
            case QtCore.Qt.Key.Key_W:
                self.current_row.add_char("W")
            case QtCore.Qt.Key.Key_X:
                self.current_row.add_char("X")
            case QtCore.Qt.Key.Key_Y:
                self.current_row.add_char("Y")
            case QtCore.Qt.Key.Key_Z:
                self.current_row.add_char("Z")
            case QtCore.Qt.Key.Key_Backspace:
                self.current_row.remove_char()
            case QtCore.Qt.Key.Key_Return:
                self.enter_case()

    def enter_word(self):
        # Check if word is proper length, not past last word, and valid
        if len(self.current_row.get_word()) == 5 and len(self.guesses) < 6 and self.word_checker.valid_check(
                self.current_row.get_word()):
            self.guesses.append(self.current_row.get_word())
            self.first_time = False

            # Generate dictionary for CharBox color statuses
            word_dict = self.word_checker.check_word(self.current_row.get_word())

            # Color row
            for x in range(len(self.current_row.char_boxes)):
                self.current_row.char_boxes[x].set_status(word_dict[x + 1])

            # Check if game was won
            self.won = True
            for letter in word_dict.keys():
                if word_dict[letter] != "correct":
                    self.won = False
                    break

            # Loss scenario
            if self.row_index == 5 and not self.won:
                self.gen_message_box("Loser", f'You lost! The word was {self.word_checker.word.upper()}.',
                                     QtWidgets.QMessageBox.Icon.NoIcon)
                self.stats.add_score(LOSE_SCORE)
                self.set_game_end(True)

            else:
                # If not last row, switch to next row
                if self.row_index < 5 and not self.won:
                    self.row_index += 1
                    self.current_row = self.rows[self.row_index]

                # If won, display win message
                elif self.won:
                    self.gen_message_box("Winner", f'You won after {len(self.guesses)} guesses!',
                                         QtWidgets.QMessageBox.Icon.NoIcon)
                    self.set_game_end(True)

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
        self.set_game_end(False)
        self.current_row = self.row1
        self.row_index = 0

    def enter_case(self):
        if not self.get_game_end():
            self.enter_word()
        else:
            self.reset("random")

    @staticmethod
    def gen_message_box(title: str, message: str, icon: QtWidgets.QMessageBox.Icon):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setIcon(icon)
        message_box.setText(message)
        message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        message_box.exec()
