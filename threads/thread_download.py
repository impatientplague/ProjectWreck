from PyQt4.QtCore import QThread
import pafy

class Dwnload(QThread):

    def __init__(self, url):
        QThread.__init__(self)
        self.url = url

    def __del__(self):
        self.wait()

    def run(self):
        v = pafy.new(self.url)
        l = v.getbest()
        print("Size is %s" % l.get_filesize())
        filename = l.download()