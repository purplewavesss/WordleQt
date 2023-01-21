from PyQt5 import QtWidgets
from UiSettingsDialog import UiSettingsDialog


class SettingsDialog(QtWidgets.QDialog, UiSettingsDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.setup_ui(self)
        self.settings_dict: dict[str, bool] = {"Hard": False, "Dark": False}
        self.hard_mode_on_option.toggled.connect(lambda: self.register_settings_change(self.hard_mode_on_option,
                                                                                       "Hard"))
        self.hard_mode_off_option.toggled.connect(lambda: self.register_settings_change(self.hard_mode_off_option,
                                                                                        "Easy"))
        self.light_mode_option.toggled.connect(lambda: self.register_settings_change(self.light_mode_option, "Light"))
        self.dark_mode_option.toggled.connect(lambda: self.register_settings_change(self.dark_mode_option, "Dark"))
        self.reset_streak_button.clicked.connect(self.reset_streak)

    def register_settings_change(self, radio_button: QtWidgets.QRadioButton, setting: str):
        pass

    def reset_streak(self):
        pass

    def change_settings(self):
        pass
