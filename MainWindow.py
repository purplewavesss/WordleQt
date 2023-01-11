# Form implementation generated from reading ui file 'C:\Users\School Account\Projects\Wordle\wordle.ui'

from PyQt5 import QtCore, QtGui, QtWidgets
from CharBox import CharBox
from Player import Player
from Row import Row


# Encapsulates the UI of a window
class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(310, 460)
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet("")
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.char_box_a1: CharBox = CharBox(self.central_widget, QtCore.QRect(10, 10, 50, 50), "char_box_a1")
        self.char_box_a2: CharBox = CharBox(self.central_widget, QtCore.QRect(70, 10, 50, 50), "char_box_a2")
        self.char_box_a3: CharBox = CharBox(self.central_widget, QtCore.QRect(130, 10, 50, 50), "char_box_a3")
        self.char_box_a4: CharBox = CharBox(self.central_widget, QtCore.QRect(190, 10, 50, 50), "char_box_a4")
        self.char_box_a5: CharBox = CharBox(self.central_widget, QtCore.QRect(250, 10, 50, 50), "char_box_a5")
        self.char_box_b1: CharBox = CharBox(self.central_widget, QtCore.QRect(10, 70, 50, 50), "char_box_b1")
        self.char_box_b2: CharBox = CharBox(self.central_widget, QtCore.QRect(70, 70, 50, 50), "char_box_b2")
        self.char_box_b3: CharBox = CharBox(self.central_widget, QtCore.QRect(130, 70, 50, 50), "char_box_b3")
        self.char_box_b4: CharBox = CharBox(self.central_widget, QtCore.QRect(190, 70, 50, 50), "char_box_b4")
        self.char_box_b5: CharBox = CharBox(self.central_widget, QtCore.QRect(250, 70, 50, 50), "char_box_b5")
        self.char_box_c1: CharBox = CharBox(self.central_widget, QtCore.QRect(10, 130, 50, 50), "char_box_c1")
        self.char_box_c2: CharBox = CharBox(self.central_widget, QtCore.QRect(70, 130, 50, 50), "char_box_c2")
        self.char_box_c3: CharBox = CharBox(self.central_widget, QtCore.QRect(130, 130, 50, 50), "char_box_c3")
        self.char_box_c4: CharBox = CharBox(self.central_widget, QtCore.QRect(190, 130, 50, 50), "char_box_c4")
        self.char_box_c5: CharBox = CharBox(self.central_widget, QtCore.QRect(250, 130, 50, 50), "char_box_c5")
        self.char_box_d1: CharBox = CharBox(self.central_widget, QtCore.QRect(10, 190, 50, 50), "char_box_d1")
        self.char_box_d2: CharBox = CharBox(self.central_widget, QtCore.QRect(70, 190, 50, 50), "char_box_d2")
        self.char_box_d3: CharBox = CharBox(self.central_widget, QtCore.QRect(130, 190, 50, 50), "char_box_d3")
        self.char_box_d4: CharBox = CharBox(self.central_widget, QtCore.QRect(190, 190, 50, 50), "char_box_d4")
        self.char_box_d5: CharBox = CharBox(self.central_widget, QtCore.QRect(250, 190, 50, 50), "char_box_d5")
        self.char_box_e1: CharBox = CharBox(self.central_widget, QtCore.QRect(10, 250, 50, 50), "char_box_e1")
        self.char_box_e2: CharBox = CharBox(self.central_widget, QtCore.QRect(70, 250, 50, 50), "char_box_e2")
        self.char_box_e3: CharBox = CharBox(self.central_widget, QtCore.QRect(130, 250, 50, 50), "char_box_e3")
        self.char_box_e4: CharBox = CharBox(self.central_widget, QtCore.QRect(190, 250, 50, 50), "char_box_e4")
        self.char_box_e5: CharBox = CharBox(self.central_widget, QtCore.QRect(250, 250, 50, 50), "char_box_e5")
        self.char_box_f1: CharBox = CharBox(self.central_widget, QtCore.QRect(10, 310, 50, 50), "char_box_f1")
        self.char_box_f2: CharBox = CharBox(self.central_widget, QtCore.QRect(70, 310, 50, 50), "char_box_f2")
        self.char_box_f3: CharBox = CharBox(self.central_widget, QtCore.QRect(130, 310, 50, 50), "char_box_f3")
        self.char_box_f4: CharBox = CharBox(self.central_widget, QtCore.QRect(190, 310, 50, 50), "char_box_f4")
        self.char_box_f5: CharBox = CharBox(self.central_widget, QtCore.QRect(250, 310, 50, 50), "char_box_f5")
        self.enter_button = QtWidgets.QPushButton(self.central_widget)
        self.enter_button.setGeometry(QtCore.QRect(10, 370, 290, 50))
        self.enter_button.setObjectName("enter_button")
        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 310, 26))
        self.menu_bar.setDefaultUp(False)
        self.menu_bar.setObjectName("menu_bar")
        self.file_menu = QtWidgets.QMenu(self.menu_bar)
        self.file_menu.setObjectName("file_menu")
        self.game_menu = QtWidgets.QMenu(self.menu_bar)
        self.game_menu.setObjectName("game_menu")
        self.new_game_menu = QtWidgets.QMenu(self.game_menu)
        self.new_game_menu.setObjectName("new_game_menu")
        self.settings_menu = QtWidgets.QMenu(self.menu_bar)
        self.settings_menu.setObjectName("settings_menu")
        self.about_menu = QtWidgets.QMenu(self.menu_bar)
        self.about_menu.setObjectName("about_menu")
        main_window.setMenuBar(self.menu_bar)
        self.actionExit = QtWidgets.QAction(main_window)
        self.actionExit.setObjectName("actionExit")
        self.exit_action = QtWidgets.QAction(main_window)
        self.exit_action.setObjectName("exit_action")
        self.check_streak_action = QtWidgets.QAction(main_window)
        self.check_streak_action.setObjectName("check_streak_action")
        self.add_words_action = QtWidgets.QAction(main_window)
        self.add_words_action.setObjectName("add_words_action")
        self.mode_action = QtWidgets.QAction(main_window)
        self.mode_action.setObjectName("mode_action")
        self.check_stats_action = QtWidgets.QAction(main_window)
        self.check_stats_action.setObjectName("check_stats_action")
        self.daily_game_action = QtWidgets.QAction(main_window)
        self.daily_game_action.setObjectName("daily_game_action")
        self.practice_game_action = QtWidgets.QAction(main_window)
        self.practice_game_action.setObjectName("practice_game_action")
        self.credits_action = QtWidgets.QAction(main_window)
        self.credits_action.setObjectName("credits_action")
        self.file_menu.addAction(self.exit_action)
        self.new_game_menu.addAction(self.daily_game_action)
        self.new_game_menu.addAction(self.practice_game_action)
        self.game_menu.addAction(self.new_game_menu.menuAction())
        self.game_menu.addAction(self.check_streak_action)
        self.game_menu.addAction(self.check_stats_action)
        self.settings_menu.addAction(self.add_words_action)
        self.settings_menu.addAction(self.mode_action)
        self.about_menu.addAction(self.credits_action)
        self.menu_bar.addAction(self.file_menu.menuAction())
        self.menu_bar.addAction(self.game_menu.menuAction())
        self.menu_bar.addAction(self.settings_menu.menuAction())
        self.menu_bar.addAction(self.about_menu.menuAction())
        # Initialize rows
        self.row1: Row = Row((self.char_box_a1, self.char_box_a2, self.char_box_a3, self.char_box_a4,
                              self.char_box_a5))
        self.row2: Row = Row((self.char_box_b1, self.char_box_b2, self.char_box_b3, self.char_box_b4,
                              self.char_box_b5))
        self.row3: Row = Row((self.char_box_c1, self.char_box_c2, self.char_box_c3, self.char_box_c4,
                              self.char_box_c5))
        self.row4: Row = Row((self.char_box_d1, self.char_box_d2, self.char_box_d3, self.char_box_d4,
                              self.char_box_d5))
        self.row5: Row = Row((self.char_box_e1, self.char_box_e2, self.char_box_e3, self.char_box_e4,
                              self.char_box_e5))
        self.row6: Row = Row((self.char_box_f1, self.char_box_f2, self.char_box_f3, self.char_box_f4,
                              self.char_box_f5))
        self.current_row = self.row1
        self.rows: tuple[Row, Row, Row, Row, Row, Row] = (self.row1, self.row2, self.row3, self.row4, self.row5, self.row6)
        self.row_indice = 0

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Wordle"))
        self.enter_button.setText(_translate("main_window", "Enter"))
        self.file_menu.setTitle(_translate("main_window", "File"))
        self.game_menu.setTitle(_translate("main_window", "Game"))
        self.new_game_menu.setTitle(_translate("main_window", "New Game"))
        self.settings_menu.setTitle(_translate("main_window", "Settings"))
        self.about_menu.setTitle(_translate("main_window", "Help"))
        self.actionExit.setText(_translate("main_window", "Add Words"))
        self.exit_action.setText(_translate("main_window", "Exit"))
        self.check_streak_action.setText(_translate("main_window", "Check Streak"))
        self.add_words_action.setText(_translate("main_window", "Add Words"))
        self.mode_action.setText(_translate("main_window", "Mode"))
        self.check_stats_action.setText(_translate("main_window", "Check Stats"))
        self.daily_game_action.setText(_translate("main_window", "Daily"))
        self.practice_game_action.setText(_translate("main_window", "Practice"))
        self.credits_action.setText(_translate("main_window", "Credits"))


# Encapsulates a main window
class MainWindow(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self, _player: Player, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.player: Player = _player
        self.setup_ui(self)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.key_parse(a0)

    def key_parse(self, keyboard: QtGui.QKeyEvent):
        match keyboard.key():
            case QtCore.Qt.Key_A:
                self.current_row.add_char("A")
            case QtCore.Qt.Key_B:
                self.current_row.add_char("B")
            case QtCore.Qt.Key_C:
                self.current_row.add_char("C")
            case QtCore.Qt.Key_D:
                self.current_row.add_char("D")
            case QtCore.Qt.Key_E:
                self.current_row.add_char("E")
            case QtCore.Qt.Key_F:
                self.current_row.add_char("F")
            case QtCore.Qt.Key_G:
                self.current_row.add_char("G")
            case QtCore.Qt.Key_H:
                self.current_row.add_char("H")
            case QtCore.Qt.Key_I:
                self.current_row.add_char("I")
            case QtCore.Qt.Key_J:
                self.current_row.add_char("J")
            case QtCore.Qt.Key_K:
                self.current_row.add_char("K")
            case QtCore.Qt.Key_L:
                self.current_row.add_char("L")
            case QtCore.Qt.Key_M:
                self.current_row.add_char("M")
            case QtCore.Qt.Key_N:
                self.current_row.add_char("N")
            case QtCore.Qt.Key_O:
                self.current_row.add_char("O")
            case QtCore.Qt.Key_P:
                self.current_row.add_char("P")
            case QtCore.Qt.Key_Q:
                self.current_row.add_char("Q")
            case QtCore.Qt.Key_R:
                self.current_row.add_char("R")
            case QtCore.Qt.Key_S:
                self.current_row.add_char("S")
            case QtCore.Qt.Key_T:
                self.current_row.add_char("T")
            case QtCore.Qt.Key_U:
                self.current_row.add_char("U")
            case QtCore.Qt.Key_V:
                self.current_row.add_char("V")
            case QtCore.Qt.Key_W:
                self.current_row.add_char("W")
            case QtCore.Qt.Key_X:
                self.current_row.add_char("X")
            case QtCore.Qt.Key_Y:
                self.current_row.add_char("Y")
            case QtCore.Qt.Key_Z:
                self.current_row.add_char("Z")
            case QtCore.Qt.Key_Backspace:
                self.current_row.remove_char()
            case QtCore.Qt.Key_Return:
                if len(self.current_row.get_word()) == 5:
                    if self.row_indice < 5:
                        self.row_indice += 1
                    self.player.add_answer(self.current_row.get_word())
                    self.current_row = self.rows[self.row_indice]

        self.current_row.update_char_boxes()
