from PyQt5 import QtWidgets
from GameWindow import GameWindow
from UiSettingsDialog import UiSettingsDialog
from conversions import *


class SettingsDialog(QtWidgets.QDialog, UiSettingsDialog):
    def __init__(self, _game_window: GameWindow):
        super(SettingsDialog, self).__init__()
        self.setup_ui(self)
        self.game_window = _game_window
        self.settings_dict: dict[str, bool] = {"Hard": False, "Light": True}
        self.read_settings()
        self.hard_mode_on_option.toggled.connect(lambda: self.register_settings_change(self.hard_mode_on_option))
        self.hard_mode_off_option.toggled.connect(lambda: self.register_settings_change(self.hard_mode_off_option))
        self.light_mode_option.toggled.connect(lambda: self.register_settings_change(self.light_mode_option))
        self.dark_mode_option.toggled.connect(lambda: self.register_settings_change(self.dark_mode_option))
        self.reset_streak_button.clicked.connect(self.reset_streak)
        self.button_box.accepted.connect(self.change_settings)
        self.reset = False

    def read_settings(self):
        # Parse settings.txt
        with open("settings/settings.txt", "r") as fs:
            settings: str = fs.read()
            self.settings_dict["Hard"] = binary_char_to_bool(settings[0])
            self.settings_dict["Light"] = binary_char_to_bool(settings[1])

        # Change toggle defaults
        self.hard_mode_on_option.setChecked(self.settings_dict["Hard"])
        self.hard_mode_off_option.setChecked(not self.settings_dict["Hard"])
        self.light_mode_option.setChecked(self.settings_dict["Light"])
        self.dark_mode_option.setChecked(not self.settings_dict["Light"])

    def register_settings_change(self, radio_button: QtWidgets.QRadioButton):
        match radio_button.objectName():
            case "hard_mode_on":
                self.settings_dict["Hard"] = True

            case "hard_mode_off":
                self.settings_dict["Hard"] = False

            case "light_mode":
                self.settings_dict["Light"] = True

            case "dark_mode":
                self.settings_dict["Light"] = False

    def reset_streak(self):
        streak_message_box = QtWidgets.QMessageBox()
        streak_message_box.setWindowTitle("Do you want to reset your streak?")
        streak_message_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        streak_message_box.setText("This will also reset your statistics.")

        # Create buttons
        yes_button = QtWidgets.QPushButton()
        yes_button.setText("Yes")
        no_button = QtWidgets.QPushButton()
        no_button.setText("No")
        yes_button.clicked.connect(lambda: self.yes_reset(streak_message_box, True))
        no_button.clicked.connect(streak_message_box.reject)

        streak_message_box.addButton(yes_button, QtWidgets.QMessageBox.ButtonRole.YesRole)
        streak_message_box.addButton(no_button, QtWidgets.QMessageBox.ButtonRole.NoRole)

        streak_message_box.exec()

        if self.reset:
            self.game_window.stats.clear_file("stats/daily_stats.txt")
            self.game_window.stats.clear_file("stats/random_stats.txt")
            self.game_window.stats.clear_file("stats/dates.txt")
            self.game_window.stats.streak = 0
            self.game_window.stats.daily_stats_dict = {}
            self.game_window.stats.random_stats_dict = {}
            self.game_window.stats.gen_combined_dict()
            self.reset = False

    def change_settings(self):
        was_hard_mode = self.game_window.get_hard_mode()
        was_light_mode = self.game_window.get_light_mode()

        self.game_window.set_hard_mode(self.settings_dict["Hard"])
        self.game_window.set_light_mode(self.settings_dict["Light"])

        if self.game_window.get_light_mode() != was_light_mode:
            self.light_mode_reset()

        if self.game_window.get_hard_mode() and not was_hard_mode and not self.game_window.first_time:
            self.game_window.reset("random")

        self.write_settings()

        self.accept()

    def write_settings(self):
        with open("settings/settings.txt", "w") as fs:
            settings_str = ""
            for setting in self.settings_dict.keys():
                settings_str += bool_to_binary_char(self.settings_dict[setting])
            fs.write(settings_str)

    def yes_reset(self, msg_box: QtWidgets.QMessageBox, _reset: bool):
        self.reset = _reset
        msg_box.accept()

    @staticmethod
    def light_mode_reset():
        QtWidgets.qApp.exit(GameWindow.EXIT_CODE_REBOOT)
