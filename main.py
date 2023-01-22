import sys
from PyQt5 import QtWidgets
from GameWindow import GameWindow
from SettingsDialog import SettingsDialog
from triggers import implement_triggers


# Initializes and displays game
def main():
    # Initialize MainWindow and app
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow()

    # Initialize settings
    settings_dialog = SettingsDialog(window)
    settings_dialog.read_settings()
    settings_dialog.change_settings()

    # Implement triggers for menu items
    implement_triggers(window, settings_dialog)

    # Open window
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
