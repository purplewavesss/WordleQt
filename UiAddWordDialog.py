# Form implementation generated from reading ui file 'C:/Users/School Account/Projects/WordleQt/addword.ui'
from PyQt5 import QtCore, QtGui, QtWidgets


class UiAddWordDialog(object):
    def setup_ui(self, dialog: QtWidgets.QDialog):
        dialog.setObjectName("Dialog")
        dialog.resize(400, 90)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.word_text_edit = QtWidgets.QLineEdit(dialog)
        self.word_text_edit.setGeometry(QtCore.QRect(90, 10, 300, 30))
        self.word_text_edit.setObjectName("plainTextEdit")
        self.ok_button = QtWidgets.QPushButton(dialog)
        self.ok_button.setGeometry(QtCore.QRect(10, 50, 100, 30))
        self.ok_button.setObjectName("ok_button")
        self.apply_button = QtWidgets.QPushButton(dialog)
        self.apply_button.setGeometry(QtCore.QRect(150, 50, 100, 30))
        self.apply_button.setObjectName("apply_button")
        self.cancel_button = QtWidgets.QPushButton(dialog)
        self.cancel_button.setGeometry(QtCore.QRect(290, 50, 100, 30))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslate_ui(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Add Word"))
        self.label.setText(_translate("Dialog", "Add Word:"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.apply_button.setText(_translate("Dialog", "Apply"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
