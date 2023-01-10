from PyQt5 import QtWidgets
import CharBox


# Encapsulates a word made out of CharBoxes
class Word:
    def __init__(self, _char_boxes: tuple[CharBox, CharBox, CharBox, CharBox, CharBox]):
        self.char_boxes = _char_boxes
        self.value: str = ""

    def add_char(self, char: str):
        if len(char) == 1:
            self.value += char
        else:
            raise ValueError("Must be one character long!")

    def remove_char(self):
        if len(self.value) > 0:
            self.value = self.value[1:len(self.value) - 1]

    def update_word(self):
        self.value = ""
        for char_box in self.char_boxes:
            self.value += char_box.text
