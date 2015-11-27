# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\BionicDad1\Desktop\download.ui'
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

class Ui_downloadWindow(object):
    def setupUi(self, downloadWindow):
        downloadWindow.setObjectName(_fromUtf8("downloadWindow"))
        downloadWindow.resize(250, 66)
        self.centralwidget = QtGui.QWidget(downloadWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(13, 22, 230, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        downloadWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(downloadWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        downloadWindow.setStatusBar(self.statusbar)

        self.retranslateUi(downloadWindow)
        QtCore.QMetaObject.connectSlotsByName(downloadWindow)

    def retranslateUi(self, downloadWindow):
        downloadWindow.setWindowTitle(_translate("downloadWindow", "Download", None))

