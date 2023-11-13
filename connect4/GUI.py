from PyQt5.QtWidgets import *
import sys


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
        for i in range(7):
            col = []
            for j in range(6):
                btn = QPushButton("", self)
                btn.setGeometry(100 * i + 10, 100 * j + 10, 80, 80)
                btn.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: white")
                col.append(btn)
            self.btns.append(col)

        for i in range(7):
            for j in range(6):
                self.btns[i][j].clicked.connect(self.clickme)
        self.show()

    def clickme(self):
        for i in range(7):
            for j in range(6):
                if self.sender() == self.btns[i][j]:
                    button = self.btns[i][j]
                    if button.text() != "":
                        return
                    for k in range(5, j, -1):
                        if self.btns[i][k].text() == "":
                            button = self.btns[i][k];
                            break
                    if self.player == 0:
                        button.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: red")
                    else:
                        button.setStyleSheet("border-radius: 40%; border: 2px solid black; background-color: yellow")
                    button.setText(" ")
                    self.player = 1 - self.player


App = QApplication(sys.argv)
g = GUI()
sys.exit(App.exec_())
