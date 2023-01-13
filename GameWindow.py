from PyQt5 import QtWidgets, QtGui, QtCore
from Player import Player
from UiMainWindow import UiMainWindow
from WordChecker import WordChecker


# Encapsulates a main window and the functions of its items
class GameWindow(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self, _player: Player, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        self.player: Player = _player
        self.setup_ui(self)
        self.__game_type = ""
        self.word_checker = WordChecker()
        self.set_game_type("daily")
        self.word_dict: dict[int, str] = {}

    def get_game_type(self) -> str:
        return self.__game_type

    def set_game_type(self, _game_type: str):
        self.__game_type = _game_type
        self.word_checker.set_game_type(self.__game_type)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.key_parse(a0)

    def key_parse(self, keyboard: QtGui.QKeyEvent):
        # Switch on key entered
        match keyboard.key():
            case QtCore.Qt.Key_A:
                self.current_row.add_char("A")
            case QtCore.Qt.Key_B:
                self.current_row.add_char("B")
            case QtCore.Qt.Key_C:
                self.current_row.add_char("C")
            case QtCore.Qt.Key_D:
                self.current_row.add_char("D")
            case QtCore.Qt.Key_E:
                self.current_row.add_char("E")
            case QtCore.Qt.Key_F:
                self.current_row.add_char("F")
            case QtCore.Qt.Key_G:
                self.current_row.add_char("G")
            case QtCore.Qt.Key_H:
                self.current_row.add_char("H")
            case QtCore.Qt.Key_I:
                self.current_row.add_char("I")
            case QtCore.Qt.Key_J:
                self.current_row.add_char("J")
            case QtCore.Qt.Key_K:
                self.current_row.add_char("K")
            case QtCore.Qt.Key_L:
                self.current_row.add_char("L")
            case QtCore.Qt.Key_M:
                self.current_row.add_char("M")
            case QtCore.Qt.Key_N:
                self.current_row.add_char("N")
            case QtCore.Qt.Key_O:
                self.current_row.add_char("O")
            case QtCore.Qt.Key_P:
                self.current_row.add_char("P")
            case QtCore.Qt.Key_Q:
                self.current_row.add_char("Q")
            case QtCore.Qt.Key_R:
                self.current_row.add_char("R")
            case QtCore.Qt.Key_S:
                self.current_row.add_char("S")
            case QtCore.Qt.Key_T:
                self.current_row.add_char("T")
            case QtCore.Qt.Key_U:
                self.current_row.add_char("U")
            case QtCore.Qt.Key_V:
                self.current_row.add_char("V")
            case QtCore.Qt.Key_W:
                self.current_row.add_char("W")
            case QtCore.Qt.Key_X:
                self.current_row.add_char("X")
            case QtCore.Qt.Key_Y:
                self.current_row.add_char("Y")
            case QtCore.Qt.Key_Z:
                self.current_row.add_char("Z")
            case QtCore.Qt.Key_Backspace:
                self.current_row.remove_char()
            case QtCore.Qt.Key_Return:
                # Check if word is proper length and not last word
                if len(self.current_row.get_word()) == 5 and len(self.player.get_answers()) < 6:
                    self.player.add_answer(self.current_row.get_word())

                    # Generate dictionary for CharBox color statuses
                    self.word_dict = self.word_checker.check_word(self.current_row.get_word())

                    # Color row
                    for x in range(len(self.current_row.char_boxes)):
                        self.current_row.char_boxes[x].set_status(self.word_dict[x + 1])

                    # If not last row, switch to next row
                    if self.row_indice < 5:
                        self.row_indice += 1
                        self.current_row = self.rows[self.row_indice]
