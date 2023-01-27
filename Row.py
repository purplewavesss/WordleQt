from CharBox import CharBox


# Encapsulates a row made out of CharBoxes
class Row:
    def __init__(self, _char_boxes: tuple[CharBox, CharBox, CharBox, CharBox, CharBox], _light_mode: bool):
        self.char_boxes: tuple[CharBox, CharBox, CharBox, CharBox, CharBox] = _char_boxes
        self.__char_list: list = []
        self.__word: str = ""
        self.light_mode = _light_mode

    def add_char(self, char: str):
        if len(char) == 1 and len(self.__char_list) <= 4:
            self.__char_list.append(char)

        # Include char in word and CharBoxes
        self.update_word()
        self.update_char_boxes()

    def remove_char(self):
        if len(self.__char_list) != 0:
            self.__char_list.pop()

        # Include char in word and CharBoxes
        self.update_word()
        self.update_char_boxes()

    def get_word(self) -> str:
        return self.__word

    def update_char_boxes(self):
        # Erase char box text
        for char_box in self.char_boxes:
            char_box.set_text(" ")

        # Fill char boxes with letters
        for letter_num in range(len(self.__char_list)):
            self.char_boxes[letter_num].set_text(self.__char_list[letter_num])

    def clear_row(self):
        for char_box in self.char_boxes:
            char_box.set_text(" ")
            if self.light_mode:
                char_box.set_status("blank")
            else:
                char_box.set_status("blank_dark")

        # Clear all text
        self.__word = ""
        for chars in range(len(self.__char_list)):
            self.remove_char()

    def update_word(self):
        self.__word = ""
        for char in self.__char_list:
            self.__word += char
