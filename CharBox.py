from PyQt5 import QtCore, QtGui, QtWidgets


class CharBox(QtWidgets.QLabel):
    def __init__(self, parent: QtWidgets.QWidget, geometry: QtCore.QRect, obj_name: str):
        super().__init__()
        self.setParent(parent)
        self.setGeometry(geometry)
        self.setObjectName(obj_name)
        self.__text: str = " "
        self.set_text(self.__text)
        self.__status: str = ""
        self.set_status("blank")

        # Initialize font
        font = QtGui.QFont()
        try:
            font.setFamily("Bahnschrift")
        except OSError:
            font.setFamily("Arial")
        font.setPointSize(28)

        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def get_text(self) -> str:
        return self.__text

    def set_text(self, _text):
        if len(_text) == 1:
            self.__text = _text
            self.setText(self.__text)
        else:
            raise ValueError("Must be one character long!")

    def get_status(self) -> str:
        return self.__status

    def set_status(self, _status):
        self.__status = _status
        match self.__status:
            # Corresponds to gray color in Wordle
            case "incorrect":
                self.setStyleSheet("background-color: rgb(128, 128, 128);\ncolor: white;")
            # Corresponds to yellow color in Wordle
            case "partial":
                self.setStyleSheet("background-color: rgb(230, 230, 0);\ncolor: white;")
            # Corresponds to green color in Wordle
            case "correct":
                self.setStyleSheet("background-color: rgb(0, 255, 0);\ncolor: white;")
            # Corresponds with the blank color at the start of Wordle
            case "blank":
                self.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: black;")
            case _:
                raise ValueError("Incorrect status used!")
