from CharBox import CharBox


# Encapsulates a row made out of CharBoxes
class Row:
    def __init__(self, _char_boxes: tuple[CharBox, CharBox, CharBox, CharBox, CharBox]):
        self.char_boxes = _char_boxes
        self.__char_list: list = []
        self.__word: str = ""

    def add_char(self, char: str):
        if len(char) == 1 and len(self.__char_list) <= 4:
            self.__char_list.append(char)
        self.update_word()

    def remove_char(self):
        if len(self.__char_list) != 0:
            self.__char_list.pop()
        self.update_word()

    def get_word(self) -> str:
        return self.__word

    def update_char_boxes(self):
        for char_box in self.char_boxes:
            char_box.set_text(" ")
        for letter_num in range(len(self.__char_list)):
            self.char_boxes[letter_num].set_text(self.__char_list[letter_num])

    def update_word(self):
        self.__word = ""
        for char in self.__char_list:
            self.__word += char
