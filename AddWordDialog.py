from PyQt5 import QtWidgets
from UiAddWordDialog import UiAddWordDialog


class AddWordDialog(QtWidgets.QDialog, UiAddWordDialog):
    def __init__(self):
        super(AddWordDialog, self).__init__()
        self.setup_ui(self)