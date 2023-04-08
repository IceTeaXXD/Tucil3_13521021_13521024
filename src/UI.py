from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a QWebEngineView instance
        self.webview = QWebEngineView(self)

        # set the URL to the HTML content
        html = open("src/maptest.html", "r").read()
        self.webview.setHtml(html)

        # add the QWebEngineView to the main window
        self.setCentralWidget(self.webview)

        # set the size of the main window
        self.resize(1280, 720)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
