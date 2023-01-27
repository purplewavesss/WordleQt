# Form implementation generated from reading ui file 'ui/share.ui'


from PyQt5 import QtCore, QtWidgets


class UiShareDialog(object):
    def setup_ui(self, share_dialog):
        share_dialog.setObjectName("share_dialog")
        share_dialog.resize(210, 250)
        self.label = QtWidgets.QLabel(share_dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 190, 15))
        self.label.setObjectName("label")
        self.share_text = QtWidgets.QPlainTextEdit(share_dialog)
        self.share_text.setGeometry(QtCore.QRect(18, 35, 175, 165))
        self.share_text.setPlainText("")
        self.share_text.setObjectName("share_text")
        self.ok_button = QtWidgets.QPushButton(share_dialog)
        self.ok_button.setGeometry(QtCore.QRect(18, 210, 175, 30))
        self.ok_button.setText("OK")

        self.retranslate_ui(share_dialog)
        QtCore.QMetaObject.connectSlotsByName(share_dialog)

    def retranslate_ui(self, share_dialog):
        _translate = QtCore.QCoreApplication.translate
        share_dialog.setWindowTitle(_translate("share_dialog", "Share"))
        self.label.setText(_translate("share_dialog", "Copy and share the code below:"))
