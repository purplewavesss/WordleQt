from PyQt5 import QtWidgets
from UiSettingsDialog import UiSettingsDialog


class SettingsDialog(QtWidgets.QDialog, UiSettingsDialog):
    def __init__(self):
        super(UiSettingsDialog, self).__init__()
