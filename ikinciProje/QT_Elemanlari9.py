
import sys
from PyQt5.QtWidgets import *

class Buton(QPushButton):
    def __init__(self,yazi):
        super().__init__(yazi)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if(e.mimeData().hasText()) :
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.git()

    def git(self):
      self.buton=Buton("Sürükle")
      self.label=QLineEdit("Yazi")
      self.label.setDragEnabled(True)
      h_box=QHBoxLayout()
      h_box.addWidget(self.buton)
      h_box.addWidget(self.label)
      self.setLayout(h_box)


      self.show()






app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())