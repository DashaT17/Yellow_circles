import sys
from Ui_ui_2 import Ui_MainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow


class Suprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
            col = self.color()
            qp.setBrush(col)
            a = randint(0, 1000)
            qp.drawEllipse(QPoint(randint(0, self.size().width()), randint(0, self.size().height())), a, a)
            qp.end()
        self.do_paint = False
    
    def paint(self):
        self.do_paint = True
        self.repaint()
    
    def color(self):
        return QColor(randint(0, 255), randint(0, 255), randint(0, 255))
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
