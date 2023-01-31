from PyQt5 import QtWidgets, QtCore, QtGui


class HistogramBar(QtWidgets.QLabel):
    def __init__(self, parent: QtWidgets.QDialog, y: int, _label_font: QtGui.QFont):
        super().__init__()
        self.setParent(parent)
        self.setGeometry(QtCore.QRect(50, y, 350, 25))
        self.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.__percentage: float = 0.0

    def get_percentage(self) -> float:
        return self.__percentage

    def set_percentage(self, _percentage: float):
        self.__percentage = _percentage
        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw_bar(painter)
        painter.end()

    def draw_bar(self, painter: QtGui.QPainter):
        if self.get_percentage() > 0:
            painter.setBrush(QtGui.QColor(0, 255, 0))
            painter.setPen(QtGui.QColor(0, 255, 0))
            painter.drawRect(0, 0, int(350 * self.get_percentage()), self.height())
