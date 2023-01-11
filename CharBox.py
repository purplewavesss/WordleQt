from PyQt5 import QtCore, QtGui, QtWidgets


class CharBox(QtWidgets.QLabel):
    def __init__(self, parent: QtWidgets.QWidget, geometry: QtCore.QRect, obj_name: str):
        super().__init__()
        self.setParent(parent)
        self.setGeometry(geometry)
        self.setObjectName(obj_name)
        self.__text: str = " "
        self.set_text(self.__text)
        self.set_status("incorrect")

        # Initialize font
        font = QtGui.QFont()
        try:
            font.setFamily("Bahnschrift")
        except:
            font.setFamily("Arial")
        font.setPointSize(28)

        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignCenter)

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
            case "incorrect":
                self.setStyleSheet("background-color: rgb(128, 128, 128);\ncolor: white;")
            case "partial":
                self.setStyleSheet("background-color: rgb(255, 255, 0);\ncolor: white;")
            case "correct":
                self.setStyleSheet("background-color: rgb(0, 255, 0);\ncolor: white;")
