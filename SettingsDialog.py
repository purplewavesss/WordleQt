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
        pass

    def change_settings(self):
        was_hard_mode = self.game_window.hard_mode

        self.game_window.hard_mode = self.settings_dict["Hard"]
        self.game_window.light_mode = self.settings_dict["Light"]

        if self.game_window.hard_mode and not was_hard_mode and not self.game_window.first_time:
            self.game_window.reset("random")

        self.write_settings()

        self.accept()

    def write_settings(self):
        with open("settings/settings.txt", "w") as fs:
            settings_str = ""
            for setting in self.settings_dict.keys():
                settings_str += bool_to_binary_char(self.settings_dict[setting])
            fs.write(settings_str)
