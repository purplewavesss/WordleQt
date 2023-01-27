# Form implementation generated from reading ui file 'statistics.ui'
from PyQt5 import QtCore, QtGui, QtWidgets
from HistogramBar import HistogramBar


class UiStatisticsDialog(object):
    def setup_ui(self, stats_dialog):
        stats_dialog.setObjectName("stats_dialog")
        stats_dialog.resize(400, 330)

        # Initialize font
        font = QtGui.QFont()
        try:
            font.setFamily("Bahnschrift")
        except OSError:
            font.setFamily("Arial")
        font.setPointSize(16)

        self.buttonBox = QtWidgets.QDialogButtonBox(stats_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(310, 290, 80, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.one_guess_label = QtWidgets.QLabel(stats_dialog)
        self.one_guess_label.setGeometry(QtCore.QRect(10, 10, 20, 25))
        self.one_guess_label.setFont(font)
        self.one_guess_label.setObjectName("one_guess_label")
        self.two_guess_label = QtWidgets.QLabel(stats_dialog)
        self.two_guess_label.setGeometry(QtCore.QRect(10, 50, 20, 25))
        self.two_guess_label.setFont(font)
        self.two_guess_label.setObjectName("two_guess_label")
        self.three_guess_label = QtWidgets.QLabel(stats_dialog)
        self.three_guess_label.setGeometry(QtCore.QRect(10, 90, 20, 25))
        self.three_guess_label.setFont(font)
        self.three_guess_label.setObjectName("three_guess_label")
        self.four_guess_label = QtWidgets.QLabel(stats_dialog)
        self.four_guess_label.setGeometry(QtCore.QRect(10, 130, 20, 25))
        self.four_guess_label.setFont(font)
        self.four_guess_label.setObjectName("four_guess_label")
        self.five_guess_label = QtWidgets.QLabel(stats_dialog)
        self.five_guess_label.setGeometry(QtCore.QRect(10, 170, 20, 25))
        self.five_guess_label.setFont(font)
        self.five_guess_label.setObjectName("five_guess_label")
        self.six_guess_label = QtWidgets.QLabel(stats_dialog)
        self.six_guess_label.setGeometry(QtCore.QRect(10, 210, 20, 25))
        self.six_guess_label.setFont(font)
        self.six_guess_label.setObjectName("six_guess_label")
        self.fail_label = QtWidgets.QLabel(stats_dialog)
        self.fail_label.setGeometry(QtCore.QRect(10, 250, 20, 25))
        self.fail_label.setFont(font)
        self.fail_label.setObjectName("fail_label")
        self.one_histogram_bar = HistogramBar(stats_dialog, 10, font)
        self.two_histogram_bar = HistogramBar(stats_dialog, 50, font)
        self.three_histogram_bar = HistogramBar(stats_dialog, 90, font)
        self.four_histogram_bar = HistogramBar(stats_dialog, 130, font)
        self.five_histogram_bar = HistogramBar(stats_dialog, 170, font)
        self.six_histogram_bar = HistogramBar(stats_dialog, 210, font)
        self.x_histogram_bar = HistogramBar(stats_dialog, 250, font)
        self.histogram_bars: list[HistogramBar] = [self.one_histogram_bar, self.two_histogram_bar,
                                                   self.three_histogram_bar, self.four_histogram_bar,
                                                   self.five_histogram_bar, self.six_histogram_bar, self.x_histogram_bar
                                                   ]

        self.retranslate_ui(stats_dialog)
        self.buttonBox.accepted.connect(stats_dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(stats_dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(stats_dialog)

    def retranslate_ui(self, stats_dialog):
        _translate = QtCore.QCoreApplication.translate
        stats_dialog.setWindowTitle(_translate("stats_dialog", "Statistics"))
        self.one_guess_label.setText(_translate("stats_dialog", "1:"))
        self.two_guess_label.setText(_translate("stats_dialog", "2:"))
        self.three_guess_label.setText(_translate("stats_dialog", "3:"))
        self.four_guess_label.setText(_translate("stats_dialog", "4:"))
        self.five_guess_label.setText(_translate("stats_dialog", "5:"))
        self.six_guess_label.setText(_translate("stats_dialog", "6:"))
        self.fail_label.setText(_translate("stats_dialog", "X:"))
