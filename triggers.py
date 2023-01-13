# Creates triggers for menu items
import sys
from PyQt5 import QtWidgets
from GameWindow import GameWindow


def implement_triggers(window: GameWindow):
    window.exit_action.triggered.connect(exit_action_triggers)
    window.credits_action.triggered.connect(credit_action_triggers)
    window.daily_game_action.triggered.connect(not_implemented)
    window.practice_game_action.triggered.connect(not_implemented)
    window.check_streak_action.triggered.connect(not_implemented)
    window.check_stats_action.triggered.connect(not_implemented)
    window.add_words_action.triggered.connect(not_implemented)
    window.mode_action.triggered.connect(not_implemented)


def exit_action_triggers():
    sys.exit()


def credit_action_triggers():
    credits_message_box = QtWidgets.QMessageBox()
    credits_message_box.setWindowTitle("Credits")
    credits_message_box.setIcon(QtWidgets.QMessageBox.Information)
    credits_message_box.setText("Created by Gavin J. Grotegut\nBased on Wordle, a game by Josh Wardle\nCoded in "
                                "Python\nDesigned in Qt, a GUI framework for C++ and Python")
    credits_message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    credits_message_box.exec()


def not_implemented():
    raise NotImplementedError
