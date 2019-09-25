

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.sayac=0
        self.durum=False

        self.git()

    def git(self):



       # self.dial=QDial()  #YUVARLAK POT GİBİ BİR ALET
        #self.dial.setMaximum(100)
        #self.dial.setMinimum(0)
        #self.dial.setNotchesVisible(True)
        #self.dial.valueChanged.connect(self.degistir)



        self.button=QPushButton("Başla")
        self.button2=QPushButton("Durdur")
        self.button3=QPushButton("Devam Et")
        self.label=QLabel("Zaman: ")
        self.label2=QLabel(str(self.sayac))
        self.label.setFont(QFont("Helvetica", 20,QFont.Bold))
        self.label2.setFont(QFont("Helvetica", 20,QFont.Bold))

        h_box=QHBoxLayout()
        h_box.addWidget(self.label)
        h_box.addWidget(self.label2)


        h_box2=QHBoxLayout()
        h_box2.addWidget(self.button)
        h_box2.addWidget(self.button3)
        h_box2.addWidget(self.button2)

        v_box=QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.button.clicked.connect(self.basla)
        self.button2.clicked.connect(self.dur)
        self.button3.clicked.connect(self.devam)
        self.setLayout(v_box)








        self.show()

    def basla(self):
        self.sayac=0
        self.timer = QTimer()
        self.timer.timeout.connect(self.arttir)
        self.timer.start(1000)


    def arttir(self):
        self.label2.setText(str(self.sayac))
        self.sayac += 1

    def dur(self):
        self.timer.stop()



    def devam(self):

       if self.timer.timerId() ==-1:#Timer durduysa.
           self.timer.start(1000)

    #def degistir(self, q):

        #self.dial.setValue(q)


app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
