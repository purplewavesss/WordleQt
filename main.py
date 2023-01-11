import sys
from PyQt5 import QtWidgets
from Game import Game
from MainWindow import MainWindow
from Word import Word
from triggers import implement_triggers


# Initializes and displays game
def main():
    # Initialize MainWindow and app
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    # Initialize words
    word1: Word = Word((window.char_box_a1, window.char_box_a2, window.char_box_a3, window.char_box_a4,
                       window.char_box_a5))
    word2: Word = Word((window.char_box_b1, window.char_box_b2, window.char_box_b3, window.char_box_b4,
                       window.char_box_b5))
    word3: Word = Word((window.char_box_c1, window.char_box_c2, window.char_box_c3, window.char_box_c4,
                       window.char_box_c5))
    word4: Word = Word((window.char_box_d1, window.char_box_d2, window.char_box_d3, window.char_box_d4,
                       window.char_box_d5))
    word5: Word = Word((window.char_box_e1, window.char_box_e2, window.char_box_e3, window.char_box_e4,
                       window.char_box_e5))
    word6: Word = Word((window.char_box_f1, window.char_box_f2, window.char_box_f3, window.char_box_f4,
                       window.char_box_f5))

    # Initialize game
    new_game = Game((word1, word2, word3, word4, word5, word6))

    # Implement triggers for menu items
    implement_triggers(window)

    # Open window
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
