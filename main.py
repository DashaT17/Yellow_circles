import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.click)
    
    def click(self):
        self.paint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            col = QColor(255,255,0)
            qp.setBrush(col)
            a = randint(0, 1000)
            qp.drawEllipse(QPoint(randint(0, self.size().width()), randint(0, self.size().height())), a, a)
            qp.end()
        self.do_paint = False
    
    def paint(self):
        self.do_paint = True
        self.repaint()
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
