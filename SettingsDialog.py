from PyQt5 import QtWidgets
from UiSettingsDialog import UiSettingsDialog


class SettingsDialog(QtWidgets.QDialog, UiSettingsDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.setup_ui(self)
