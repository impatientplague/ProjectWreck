# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\BionicDad1\Desktop\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(448, 325)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(448, 325))
        MainWindow.setMaximumSize(QtCore.QSize(448, 325))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(229, 248, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.views = QtGui.QLabel(self.centralwidget)
        self.views.setGeometry(QtCore.QRect(262, 250, 46, 13))
        self.views.setObjectName(_fromUtf8("views"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 267, 31, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.likes = QtGui.QLabel(self.centralwidget)
        self.likes.setGeometry(QtCore.QRect(260, 265, 55, 21))
        self.likes.setObjectName(_fromUtf8("likes"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 286, 44, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.likes_2 = QtGui.QLabel(self.centralwidget)
        self.likes_2.setGeometry(QtCore.QRect(270, 283, 55, 21))
        self.likes_2.setObjectName(_fromUtf8("likes_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(129, 275, 75, 23))
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(-4, -3, 461, 240))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(9, 246, 113, 16))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.push_url = QtGui.QPushButton(self.centralwidget)
        self.push_url.setGeometry(QtCore.QRect(128, 243, 75, 23))
        self.push_url.setObjectName(_fromUtf8("push_url"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(12, 275, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Wreck", None))
        self.label.setText(_translate("MainWindow", "Views:", None))
        self.views.setText(_translate("MainWindow", "0", None))
        self.label_2.setText(_translate("MainWindow", "Likes:", None))
        self.likes.setText(_translate("MainWindow", "0", None))
        self.label_3.setText(_translate("MainWindow", "Dislikes:", None))
        self.likes_2.setText(_translate("MainWindow", "0", None))
        self.pushButton.setText(_translate("MainWindow", "Download", None))
        self.lineEdit.setText(_translate("MainWindow", "URL", None))
        self.push_url.setText(_translate("MainWindow", "Submit", None))

from PyQt4 import QtWebKit
