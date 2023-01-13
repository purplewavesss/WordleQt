import sys
from PyQt5 import QtWidgets
from GameWindow import GameWindow
from triggers import implement_triggers


# Initializes and displays game
def main():
    # Initialize MainWindow and app
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow()

    # Implement triggers for menu items
    implement_triggers(window)

    # Open window
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
