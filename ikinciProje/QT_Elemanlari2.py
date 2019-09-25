

import sys
from PyQt5.QtWidgets import QAction, QWidget,QPushButton,QLabel,QGridLayout,QApplication,QHBoxLayout,QVBoxLayout,QSpinBox,QDoubleSpinBox,QSlider,QMenuBar,QMainWindow,QLineEdit,QFileDialog
from PyQt5.QtGui import *
from  PyQt5.QtCore import *



class Pencere(QMainWindow):

    def __init__(self):

        super().__init__()
        self.git()

    def git(self):

        menubar=self.menuBar()
        dosya=menubar.addMenu("Dosya")
        self.label=QLabel()
        self.setCentralWidget(self.label)

        self.statusBar()



        toolbar=self.addToolBar("File")

        new=QAction(QIcon("C:/Users/Asus/Desktop/messi.jpg"),"YENİ",self)
        new.setStatusTip("Resim açma işlemi...")
        toolbar.addAction(new)

        self.ara=QLineEdit()
        self.ara.setPlaceholderText("Ara") #Arama işlemi yapmak için.

        toolbar.addWidget(self.ara)

        toolbar.setMovable(False)
        toolbar.setOrientation(Qt.Horizontal)
        toolbar.actionTriggered.connect(self.uygula)






        yeni=dosya.addMenu("Yeni")
        proje=QAction("Proje",self)
        klasor=QAction("Klasör",self)
        yeni.addAction(proje)
        yeni.addAction(klasor)

        ac=QAction("Aç",self)
        ac.setShortcut("Ctrl+B")

        kapat=QAction("Kapat",self)
        kapat.setShortcut("Q")


        dosya.addAction(ac)
        dosya.addAction(kapat)




        kapat.triggered.connect(self.Kapat)
        new.triggered.connect(self.resim)





        self.show()

    def Kapat(self):
        sys.exit()

    def uygula(self,q):
        print(q.text())

    def resim(self):

        file=QFileDialog.getOpenFileName(self,"Dosya Aç","C:/Users/Asus/Desktop","Resim dosyaları(*.jpg *.png)")
        self.label.setPixmap(QPixmap(file[0]))

















app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())