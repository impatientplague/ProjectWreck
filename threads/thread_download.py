from PyQt4.QtCore import QThread
from PyQt4 import QtCore
import pafy
import time , os

class Dwnload(QThread):

    taskFinished = QtCore.pyqtSignal()

    def __init__(self, url):
        QThread.__init__(self)
        self.url = url

    def __del__(self):
        self.wait()

    def run(self):
        v = pafy.new(self.url)
        l = v.getbest()
        print("Size is %s" % l.get_filesize())
        l.download(filepath="Videos")
        time.sleep(5)
        self.taskFinished.emit()




