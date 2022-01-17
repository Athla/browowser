from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    browser: QWebEngineView

    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        # navi
        navi = QToolBar()
        self.addToolBar(navi)
        # back button
        b_button = QAction('Back', self)
        b_button.triggered.connect(self.browser.back)
        navi.addAction(b_button)
        b_button.setStatusTip('Back to the previous page')
        # forward button
        f_button = QAction('Forward', self)
        f_button.triggered.connect(self.browser.forward)
        navi.addAction(f_button)
        f_button.setStatusTip('Forward to the next page.')
        # reset button
        r_button = QAction('Reload', self)
        r_button.triggered.connect(self.browser.reload)
        navi.addAction(r_button)
        r_button.setStatusTip('Reload the page')
        # home
        h_button = QAction('Home', self)
        h_button.triggered.connect(self.navigate_home)
        navi.addAction(h_button)
        h_button.setStatusTip('Return home.')
        # search bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navi.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
        # separator
        navi.addSeparator()
        # stop
        s_button = QAction('Stop', self)
        s_button.triggered.connect(self.browser.stop)
        navi.addAction(s_button)
        s_button.setStatusTip('Stop current page loading')

        self.show()

    def navigate_home(self):
        self.browser.setUrl((QUrl('http://google.com')))

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Browser 1 - test')
window = MainWindow()
app.exec_()
