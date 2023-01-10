from PyQt5 import QtCore, QtGui, QtWidgets


class CharBox(QtWidgets.QLabel):
    def __init__(self, parent: QtWidgets.QWidget, geometry: QtCore.QRect, obj_name: str):
        super().__init__()
        self.setParent(parent)
        self.setGeometry(geometry)
        self.setObjectName(obj_name)
        font = QtGui.QFont()
        try:
            font.setFamily("Bahnschrift")
        except:
            font.setFamily("Arial")
        font.setPointSize(28)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(128, 128, 128);\ncolor: white;")
        self.setText("")
        self.setAlignment(QtCore.Qt.AlignCenter)
