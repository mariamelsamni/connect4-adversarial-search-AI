import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
from minimax import *
from state_utils import *

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        cell = 100
        height = cell * 6
        width = cell * 7
        self.setWindowTitle('Connect 4')
        center = QDesktopWidget().availableGeometry().center()
        self.setGeometry(center.x() - width // 2, center.y() - height // 2, width, height)
        self.layout2 = QGridLayout()
        self.label = QLabel("", self)
        self.label.setStyleSheet("background-color: blue")
        self.label.setGeometry(0, 0, width, height)
        self.btns = []
        self.player = 0
        self.state = 2**14 - 1
        self.state <<= 7 * 3 + 1
        for i in range(6):
            row = []
            for j in range(7):
                btn = QPushButton("", self)
                btn.setGeometry(100 * j + 10, 100 *i + 10, 80, 80)
                btn.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: white")
                row.append(btn)
            self.btns.append(row)

        for i in range(6):
            for j in range(7):
                self.btns[i][j].clicked.connect(self.play)

        self.changeboard(value(None, self.state, 0, 2)[1]-1)
        self.show()

    def play(self):
        if self.player == 0:
            return
        for i in range(6):
            for j in range(7):
                if self.sender() == self.btns[i][j]:
                    self.changeboard(j, i)
        if self.player == 0:self.changeboard(value(None, self.state, 0, 2)[1] - 1)


    def changeboard(self, col, row=0):
        button = self.btns[row][col]
        print(self.player)
        print(row, col)
        if button.text() != "":
            return
        for k in range(5, row, -1):
            if self.btns[k][col].text() == "":
                button = self.btns[k][col]
                break
        if self.player == 0:
            button.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: red")
        else:
            button.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: yellow")
        button.setText(" ")
        self.state = next_state(self.state, col+1)
        self.player = 1 - self.player



App = QApplication(sys.argv)
g = GUI()
sys.exit(App.exec_())
