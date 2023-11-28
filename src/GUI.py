import threading
import time
from multiprocessing import Process

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
from minimax import *
from state_utils import *

class GUI(QMainWindow):

    def __init__(self,k, minimaxAlgorithm):
        super().__init__()
        cell = 100
        labelheigt = 80
        height = cell * 6 + labelheigt
        width = cell * 7
        self.maxk=k
        self.minimaxxx=minimaxAlgorithm
        self.setWindowTitle('Connect 4')
        center = QDesktopWidget().availableGeometry().center()
        self.setGeometry(center.x() - width // 2, center.y() - height // 2, width, height)
        self.layout2 = QGridLayout()

        self.label = QLabel("", self)
        self.label.setStyleSheet("background-color: blue")
        self.label.setGeometry(0, labelheigt, width, height - labelheigt)

        self.label2 = QLabel(f"Computer: 0                    Player: 0", self)
        self.label2.setGeometry(0, 0, width, labelheigt)
        font = QFont("Arial", 30, QFont.Bold)
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet(
            "background-color: black; color: red; font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;")

        self.btns = []
        self.player = 0
        self.remainingGames=42
        self.state = 2**14 - 1
        self.state <<= 7 * 3 + 1

        self.computerscore = 0
        self.playerscore = 0

        for i in range(6):
            row = []
            for j in range(7):
                btn = QPushButton("", self)
                btn.setGeometry(100 * j + 10, 100 *i + 10 + labelheigt, 80, 80)
                btn.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: white")
                row.append(btn)
            self.btns.append(row)

        for i in range(6):
            for j in range(7):
                self.btns[i][j].clicked.connect(self.thread)

        self.changeboard(self.minimaxxx( self.state, 0, self.maxk)[1]-1)
        self.show()

    def thread(self):
        t1 = threading.Thread(target=self.play)
        t1.start()
        
    def play(self):
        if self.player == 0:
            return
        for i in range(6):
            for j in range(7):
                if self.sender() == self.btns[i][j]:
                    self.remainingGames-=1
                    self.changeboard(j, i)

        if self.player == 0:
            self.remainingGames-=1
            self.changeboard(self.minimaxxx(self.state, 0, min(self.maxK,self.remainingGames))[1] - 1)


    def changeboard(self, col, row=0):
        button = self.btns[row][col]
        if button.text() != "":
            return
        for k in range(5, row, -1):
            if self.btns[k][col].text() == "":
                button = self.btns[k][col]
                row = k
                break
        if self.player == 0:
            button.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: red")
        else:
            button.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: yellow")
            time.sleep(1)
        button.setText((self.player+1)*" ")

        

        self.scores(row, col)
        self.state = next_state(self.state, col+1)
        self.player = 1 - self.player
        self.label2.setText(f"Computer: {self.computerscore}                    Player: {self.playerscore}")

    def scores(self, row, col):
        str = self.btns[row][col].text()
        score = 0

        count = 0
        for i in range(row, 6):
            if self.btns[i][col].text() != str:
                break
            count += 1
        if count >= 4: score += 1

        count = 0
        for i in range(4):
            if col < i: break
            if col > i + 3: continue
            for j in range(i, i + 4):
                if self.btns[row][j].text() != str:
                    break
                count += 1
            if count == 4: score += 1
            count = 0

        mn = min(row, col)
        i = row - mn
        j = col - mn
        while i < 3 and j < 4:
            if row < i:
                break
            if row > i + 3:
                i += 1
                j += 1
                continue
            for k in range(4):
                if self.btns[i+k][j+k].text() != str:
                    break
                count += 1
            if count == 4: score += 1
            count = 0
            i += 1
            j += 1

        mn = min(row, 6 - col)
        i = row - mn
        j = col + mn
        while i < 3 and j > 2:
            if row < i:
                break
            if row > i + 3:
                i += 1
                j -= 1
                continue
            for k in range(4):
                if self.btns[i + k][j - k].text() != str:
                    break
                count += 1
            if count == 4: score += 1
            count = 0
            i += 1
            j -= 1

        if self.player == 0: self.computerscore += score
        else: self.playerscore += score







App = QApplication(sys.argv)
g = GUI()
sys.exit(App.exec_())
