# Creates triggers for menu items
import sys
from PyQt5 import QtWidgets
from AddWordDialog import AddWordDialog
from GameWindow import GameWindow
from SettingsDialog import SettingsDialog


def implement_triggers(game_window: GameWindow, settings_dialog: SettingsDialog):
    game_window.exit_action.triggered.connect(exit_action_triggers)
    game_window.credits_action.triggered.connect(credit_action_triggers)
    game_window.daily_game_action.triggered.connect(lambda: daily_action_triggers(game_window))
    game_window.practice_game_action.triggered.connect(lambda: practice_action_triggers(game_window))
    game_window.check_streak_action.triggered.connect(not_implemented)
    game_window.check_stats_action.triggered.connect(not_implemented)
    game_window.add_words_action.triggered.connect(lambda: add_words_action_triggers(game_window))
    game_window.settings_action.triggered.connect(settings_dialog.exec)


def exit_action_triggers():
    sys.exit()


def credit_action_triggers():
    GameWindow.gen_message_box("Credits", "Created by Gavin J. Grotegut\nBased on Wordle, a game by Josh Wardle\n"
                               "Coded in Python\nDesigned in Qt, a GUI framework for C++ and Python",
                               QtWidgets.QMessageBox.Icon.Information)


def daily_action_triggers(game_window: GameWindow):
    game_window.reset("daily")


def practice_action_triggers(game_window: GameWindow):
    game_window.reset("random")


def add_words_action_triggers(game_window: GameWindow):
    add_word_dialog = AddWordDialog(game_window)
    add_word_dialog.exec()


def not_implemented():
    raise NotImplementedError
