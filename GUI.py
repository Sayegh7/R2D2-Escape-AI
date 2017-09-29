import sys
import threading
from collections import deque
import index
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
gui = None

class ThreadClass(QtCore.QThread):

    def __init__(self, app, parent=None):
        super(ThreadClass, self).__init__(parent)


    def run(self):
        index.run(gui)
class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.title = 'R2D2 Escape'
        self.left = 20
        self.top = 20
        self.width = 1000
        self.height = 1000
        self.initUI()
        self.mythread=ThreadClass(self)
        self.mythread.start()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        self.label = QLabel(self)

        self.refresh()
        self.show()

    def refresh(self):
        pixmap = QPixmap('out.png')
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    gui = ex
    sys.exit(app.exec_())
