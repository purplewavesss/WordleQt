import sys
from PyQt5 import QtWidgets
from Player import Player
from Game import Game
from MainWindow import MainWindow
from triggers import implement_triggers


# Initializes and displays game
def main():
    # Create player
    player: Player = Player()

    # Initialize MainWindow and app
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(player)

    # Initialize game
    new_game = Game(window)

    # Implement triggers for menu items
    implement_triggers(window)

    # Open window
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
