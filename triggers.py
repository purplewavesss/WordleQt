# Creates triggers for menu items
import sys
from PyQt5 import QtWidgets
from AddWordDialog import AddWordDialog
from GameStats import GameStats
from GameWindow import GameWindow
from SettingsDialog import SettingsDialog
from StatisticsDialog import StatisticsDialog


def implement_triggers(game_window: GameWindow, settings_dialog: SettingsDialog):
    game_window.exit_action.triggered.connect(exit_action_triggers)
    game_window.credits_action.triggered.connect(credit_action_triggers)
    game_window.daily_game_action.triggered.connect(lambda: daily_action_triggers(game_window))
    game_window.practice_game_action.triggered.connect(lambda: practice_action_triggers(game_window))
    game_window.check_streak_action.triggered.connect(lambda: check_streak_triggers(game_window.stats))
    game_window.check_daily_stats_action.triggered.connect(lambda: create_statistics_dialog(game_window.stats,
                                                                                            game_window, "Daily"))
    game_window.check_practice_stats_action.triggered.connect(lambda: create_statistics_dialog(game_window.stats,
                                                                                               game_window, "Practice"))
    game_window.check_combined_stats_action.triggered.connect(lambda: create_statistics_dialog(game_window.stats,
                                                                                               game_window, "Combined"))
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
    game_window.daily_game_action.setChecked(True)
    game_window.practice_game_action.setChecked(False)


def practice_action_triggers(game_window: GameWindow):
    game_window.reset("random")
    game_window.daily_game_action.setChecked(False)
    game_window.practice_game_action.setChecked(True)


def create_statistics_dialog(game_stats: GameStats, game_window: GameWindow, data_type: str):
    statistics_dialog = StatisticsDialog(game_stats, data_type)
    if statistics_dialog.histogram_generated:
        statistics_dialog.exec()


def add_words_action_triggers(game_window: GameWindow):
    add_word_dialog = AddWordDialog(game_window)
    add_word_dialog.exec()


def check_streak_triggers(game_stats: GameStats):
    if game_stats.streak != 1:
        GameWindow.gen_message_box("Streak", f'You have a streak of {game_stats.streak} days!',
                                   QtWidgets.QMessageBox.Icon.NoIcon)
    else:
        GameWindow.gen_message_box("Streak", f'You have a streak of {game_stats.streak} day!',
                                   QtWidgets.QMessageBox.Icon.NoIcon)
