


import sys

from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):


        super().__init__()


        self.git()

    def git(self):

        #QMessage box,status bar.



        # self.qslider1.sliderMoved.connect(self.yap)   Bunlar qscrollBar
        #self.qslider2.sliderMoved.connect(self.yap)
        #self.qslider3.sliderMoved.connect(self.yap)




    #def yap(self):
        #print(self.qslider1.value(),self.qslider2.value(),self.qslider3.value())
        #palette = QPalette()
        #c = QColor(self.qslider1.value(),self.qslider2.value(),self.qslider3.value())
        #palette.setColor(QPalette.Foreground,c)
        #self.yazi.setPalette(palette)
        self.buton=QPushButton("SDFF")
        self.split=QSplitter()
        self.split.addWidget(self.buton)

        self.liste=QListWidget()
        self.liste.insertItem(0,"İlk yer")
        self.liste.insertItem(1,"İkinci yer")
        self.liste.insertItem(2,"Üçüncü yer")

        self.stackwid=QStackedWidget()

        self.w1=QWidget()
        self.w2=QWidget()
        self.w3=QWidget()


        self.w1lay()
        self.w2lay()
        self.w3lay()

        self.stackwid.addWidget(self.w1)   ##stacklere w1 w2 w3 ekle w1 w2 w3 içini aşağıda doldurur.
        self.stackwid.addWidget(self.w2)
        self.stackwid.addWidget(self.w3)


        h_box=QHBoxLayout()
        h_box.addWidget(self.liste)     #solda liste sağda stackwidget olusur.
        h_box.addWidget(self.stackwid)

        self.setLayout(h_box)

        self.liste.currentRowChanged.connect(self.uygula)


        self.show()


    def uygula(self,q):

        self.stackwid.setCurrentIndex(q)
    def w1lay(self):
        v_box=QVBoxLayout()
        self.buton1=QPushButton("Buton")
        self.yazi1=QLabel("Yazi")
        v_box.addWidget(self.buton1)
        v_box.addWidget(self.yazi1)

        self.w1.setLayout(v_box)
    def w2lay(self):
        v_box = QVBoxLayout()

        self.check1 = QCheckBox("CheckBox")
        self.spin1 = QSpinBox()
        v_box.addWidget(self.check1)
        v_box.addWidget(self.spin1)
        self.w2.setLayout(v_box)
    def w3lay(self):
        v_box = QVBoxLayout()
        self.radio1 = QRadioButton("RadioButon")
        self.yazi2 = QLabel("Yazi2")
        v_box.addWidget(self.radio1)
        v_box.addWidget(self.yazi2)
        self.w3.setLayout(v_box)






app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())












