import sys, io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class tester(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.btn = QPushButton(self)
        self.btn.clicked.connect(self.run)

    def run(self):
        print("кружочек рандомного размера")
        print("кружочек рандомного цвета")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = tester()
    ex.show()
    sys.exit(app.exec())
