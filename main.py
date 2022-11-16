import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.btn_show_circle.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        radius = randint(30, 150)
        radius2 = randint(100, 250)
        radius3 = randint(70, 150)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(30, 30, radius, radius)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(200, 250, radius2, radius2)
        qp.drawEllipse(30, 30, radius, radius)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(30, 300, radius3, radius3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wd = MyWidget()
    wd.show()
    sys.exit(app.exec())