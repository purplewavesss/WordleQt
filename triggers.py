# Creates triggers for menu items
import sys
from PyQt5 import QtWidgets
from GameWindow import GameWindow


def implement_triggers(game_window: GameWindow):
    game_window.exit_action.triggered.connect(exit_action_triggers)
    game_window.credits_action.triggered.connect(credit_action_triggers)
    game_window.daily_game_action.triggered.connect(lambda: daily_action_triggers(game_window))
    game_window.practice_game_action.triggered.connect(lambda: practice_action_triggers(game_window))
    game_window.check_streak_action.triggered.connect(not_implemented)
    game_window.check_stats_action.triggered.connect(not_implemented)
    game_window.add_words_action.triggered.connect(not_implemented)
    game_window.mode_action.triggered.connect(not_implemented)


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


def daily_action_triggers(game_window: GameWindow):
    game_window.reset("daily")


def practice_action_triggers(game_window: GameWindow):
    game_window.reset("random")


def not_implemented():
    raise NotImplementedError
