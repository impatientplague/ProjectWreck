import pafy , sys , logging
from PyQt4 import QtGui
from PyQt4.QtWebKit import QWebView, QWebSettings
from gui.ui_youtube import Ui_MainWindow
from workers.watch_video import Watch

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
logging.disable(logging.DEBUG)

class ProjectWreck(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(ProjectWreck,self).__init__(parent)
        self.setupUi(self)
        self.push_url.clicked.connect(self.url_handler)


    def url_handler(self):
        self.webView.settings().setAttribute(QWebSettings.PluginsEnabled,True)
        self.url_fetch()
        self.set_html()


    def url_fetch(self):
        video = Watch(self.lineEdit.text())
        fetched = video.get_url()
        return fetched


    def set_html(self):
        catch = self.url_fetch()
        self.webView.setHtml('''<html>
<body>

<iframe width="440" height="220"
src="%s">
</iframe>

</body>
</html>''' % catch)
        logging.info('[Debug]: Watching Video')


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = ProjectWreck()
    myapp.show()
    app.exec_()


if __name__ == '__main__':
    main()