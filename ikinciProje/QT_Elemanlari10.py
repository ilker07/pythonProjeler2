
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.git()

    def git(self):



        self.show()

    def paintEvent(self, olay):

        painter=QPainter()
        painter.begin(self)
        painter.setBrush(QColor(Qt.red))
        painter.setPen(QColor(Qt.blue))
        painter.drawEllipse(50,50,100,50)
        painter.drawLine(10,500,200,10) #x1 y1 x2 y2   drawtext drawrect








        painter.end()









app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())