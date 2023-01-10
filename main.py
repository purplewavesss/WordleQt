import sys
from PyQt5 import QtWidgets
from MainWindow import MainWindow


# Initializes and displays game
def main():
    # Initialize MainWindow and app
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    # Open window
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
