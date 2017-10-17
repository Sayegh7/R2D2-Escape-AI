import sys
from collections import deque
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QComboBox,
    QLabel, QApplication)

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
import Visualizer as v

class App(QWidget):

    def __init__(self, results, size):
        super(App, self).__init__()
        self.title = 'R2D2 Escape'
        self.results = results
        self.index = 0
        self.left = 20
        self.size = size
        self.top = 20
        self.strategy = "BFS"
        self.width = 1000
        self.height = 1000
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        btn1 = QPushButton("Next", self)
        btn2 = QPushButton("Previous", self)
        btn1.clicked.connect(self.next)
        btn2.clicked.connect(self.prev)

        combo = QComboBox(self)
        combo.addItem("BFS")
        combo.addItem("DFS")
        combo.addItem("UC")
        combo.addItem("G")
        combo.addItem("A*")
        combo.addItem("ID")
        combo.activated[str].connect(self.onActivated)
        hbox.addWidget(combo)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        self.refresh()
        self.show()

    def onActivated(self, text):
        self.strategy = text
        self.index = 0
        self.refresh()

    def next(self):
        if self.index == len(self.results[self.strategy])-1:
            return
        self.index+=1
        self.refresh()

    def prev(self):
        if self.index == 0:
            return
        self.index-=1
        self.refresh()

    def refresh(self):
        v.renderGrid(self.results[self.strategy][self.index], self.size)
        pixmap = QPixmap('out.png')
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
