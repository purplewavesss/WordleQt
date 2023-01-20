from PyQt5 import QtWidgets
from GameWindow import GameWindow
from UiAddWordDialog import UiAddWordDialog


class AddWordDialog(QtWidgets.QDialog, UiAddWordDialog):
    def __init__(self, _game_window: GameWindow):
        super(AddWordDialog, self).__init__()
        self.setup_ui(self)
        self.game_window = _game_window
        self.ok_button.clicked.connect(self.ok)
        self.apply_button.clicked.connect(self.apply)
        self.cancel_button.clicked.connect(self.reject)

    def ok(self):
        self.apply()
        self.accept()

    def apply(self):
        if len(self.word_text_edit.text()) == 5:
            # Append word
            with open("words/real-answers.txt", "a") as fs:
                fs.write("\n" + self.word_text_edit.text())

            # Ask to set word to newly added word
            self.gen_set_word_message_box()

            # Clear text edit
            self.word_text_edit.setText("")

        elif len(self.word_text_edit.text()) != 0:
            self.game_window.gen_message_box("Not five letters!", "The word you added was not five letters long.",
                                             QtWidgets.QMessageBox.Icon.Warning)

    def gen_set_word_message_box(self):
        # Create message box
        set_word_message_box = QtWidgets.QMessageBox()
        set_word_message_box.setWindowTitle("Add Word")
        set_word_message_box.setIcon(QtWidgets.QMessageBox.Icon.Question)
        set_word_message_box.setText(f'Do you want the next word to be "{self.word_text_edit.text()}"?')

        # Create buttons
        yes_button = QtWidgets.QPushButton()
        yes_button.setText("Yes")
        yes_button.clicked.connect(lambda: self.game_window.reset("manual", self.word_text_edit.text()))
        no_button = QtWidgets.QPushButton()
        no_button.setText("No")
        no_button.clicked.connect(set_word_message_box.reject)

        # Add buttons
        set_word_message_box.addButton(yes_button, QtWidgets.QMessageBox.ButtonRole.YesRole)
        set_word_message_box.addButton(no_button, QtWidgets.QMessageBox.ButtonRole.NoRole)

        # Display message box
        set_word_message_box.exec()
