# Form implementation generated from reading ui file 'settings.ui'
from PyQt5 import QtCore, QtWidgets


class UiSettingsDialog(object):
    def setup_ui(self, settings_dialog):
        settings_dialog.setObjectName("settings_dialog")
        settings_dialog.resize(370, 140)
        self.button_box = QtWidgets.QDialogButtonBox(settings_dialog)
        self.button_box.setGeometry(QtCore.QRect(10, 100, 350, 30))
        self.button_box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|
                                           QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.button_box.setObjectName("button_box")
        self.hard_mode_box = QtWidgets.QGroupBox(settings_dialog)
        self.hard_mode_box.setGeometry(QtCore.QRect(10, 10, 110, 80))
        self.hard_mode_box.setObjectName("hard_mode_box")
        self.hard_mode_on_option = QtWidgets.QRadioButton(self.hard_mode_box)
        self.hard_mode_on_option.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.hard_mode_on_option.setObjectName("hard_mode_on")
        self.hard_mode_off_option = QtWidgets.QRadioButton(self.hard_mode_box)
        self.hard_mode_off_option.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.hard_mode_off_option.setObjectName("hard_mode_off")
        self.display_mode_box = QtWidgets.QGroupBox(settings_dialog)
        self.display_mode_box.setGeometry(QtCore.QRect(130, 10, 110, 80))
        self.display_mode_box.setObjectName("display_mode_box")
        self.light_mode_option = QtWidgets.QRadioButton(self.display_mode_box)
        self.light_mode_option.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.light_mode_option.setObjectName("light_mode")
        self.dark_mode_option = QtWidgets.QRadioButton(self.display_mode_box)
        self.dark_mode_option.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.dark_mode_option.setObjectName("dark_mode")
        self.reset_streak_box = QtWidgets.QGroupBox(settings_dialog)
        self.reset_streak_box.setGeometry(QtCore.QRect(250, 10, 110, 80))
        self.reset_streak_box.setObjectName("reset_streak_box")
        self.reset_streak_button = QtWidgets.QPushButton(self.reset_streak_box)
        self.reset_streak_button.setGeometry(QtCore.QRect(10, 30, 90, 40))
        self.reset_streak_button.setObjectName("reset_streak_button")
        self.button_box.rejected.connect(settings_dialog.reject)

        self.retranslate_ui(settings_dialog)
        QtCore.QMetaObject.connectSlotsByName(settings_dialog)

    def retranslate_ui(self, settings_dialog):
        _translate = QtCore.QCoreApplication.translate
        settings_dialog.setWindowTitle(_translate("settings_dialog", "Settings"))
        self.hard_mode_box.setTitle(_translate("settings_dialog", "Hard Mode"))
        self.hard_mode_on_option.setText(_translate("settings_dialog", "On"))
        self.hard_mode_off_option.setText(_translate("settings_dialog", "Off"))
        self.display_mode_box.setTitle(_translate("settings_dialog", "Display"))
        self.light_mode_option.setText(_translate("settings_dialog", "Light"))
        self.dark_mode_option.setText(_translate("settings_dialog", "Dark"))
        self.reset_streak_box.setTitle(_translate("settings_dialog", "Reset Streak"))
        self.reset_streak_button.setText(_translate("settings_dialog", "Reset"))
