import sys
import qdarkstyle
from PyQt5 import QtWidgets
from GameWindow import GameWindow
from SettingsDialog import SettingsDialog
from triggers import implement_triggers


# Initializes and displays game
def main():
    current_exit_code = GameWindow.EXIT_CODE_REBOOT
    while current_exit_code == GameWindow.EXIT_CODE_REBOOT:
        # Initialize windows/apps
        app = QtWidgets.QApplication(sys.argv)
        window = GameWindow()

        # Initialize settings
        settings_dialog = SettingsDialog(window, app)
        settings_dialog.read_settings()
        settings_dialog.change_settings()

        # Set stylesheet
        if not settings_dialog.settings_dict["Light"]:
            app.setStyleSheet(qdarkstyle.load_stylesheet())

        else:
            app.setStyleSheet("")

        # Implement triggers for menu items
        implement_triggers(window, settings_dialog)

        # Open window
        window.show()
        current_exit_code = app.exec()
        window.close()
        app = None
        settings_dialog = None


if __name__ == '__main__':
    main()
