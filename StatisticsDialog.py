from PyQt5 import QtWidgets
from UiStatisticsDialog import UiStatisticsDialog


class StatisticsDialog(QtWidgets.QDialog, UiStatisticsDialog):
    def __init__(self):
        super(StatisticsDialog, self).__init__()
