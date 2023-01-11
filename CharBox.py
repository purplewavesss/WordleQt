from PyQt5 import QtCore, QtGui, QtWidgets


class CharBox(QtWidgets.QLabel):
    def __init__(self, parent: QtWidgets.QWidget, geometry: QtCore.QRect, obj_name: str):
        super().__init__()
        self.setParent(parent)
        self.setGeometry(geometry)
        self.setObjectName(obj_name)
        self.__text: str = " "
        self.change_text(self.__text)
        font = QtGui.QFont()
        try:
            font.setFamily("Bahnschrift")
        except:
            font.setFamily("Arial")
        font.setPointSize(28)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(128, 128, 128);\ncolor: white;")
        self.setAlignment(QtCore.Qt.AlignCenter)

    def get_text(self) -> str:
        return self.__text

    def change_text(self, _text):
        if len(_text) == 1:
            self.__text = _text
            self.setText(self.__text)
        else:
            raise ValueError("Must be one character long!")
