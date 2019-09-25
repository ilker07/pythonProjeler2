

import sys
import serial
from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import  QMediaPlayer,QMediaContent
import time




class Pencere(QWidget):
        def __init__(self):
            super().__init__()
            self.durum=False
            self.i=0

            self.git()
        def git(self):
            v_box=QVBoxLayout()
            h_box=QHBoxLayout()


            self.media=QMediaPlayer()
            self.media.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Asus/Downloads/Payback.mp3")))
            self.buton=QPushButton("Oku")
            self.yazi=QLabel("Gelen Değer: ")
            self.yazi2=QLabel("0")
            self.yazi3=QLabel("1")
            self.ledbuton=QPushButton("Yak")
            self.ledbutonsondur=QPushButton("Sondur")
            self.butonmuzik=QPushButton("Çal")
            h_box.addWidget(self.buton)

            h_box.addWidget(self.yazi)
            h_box.addWidget(self.yazi2)
            h_box.addWidget(self.ledbuton)
            h_box.addWidget(self.ledbutonsondur)
            h_box.addWidget(self.butonmuzik)
            h_box.addWidget(self.yazi3)


            h_box.addStretch()
            v_box.addLayout(h_box)
            v_box.addStretch()
            self.setLayout(v_box)

            self.buton.clicked.connect(self.oku)
            self.ledbuton.clicked.connect(self.Yak)
            self.ledbutonsondur.clicked.connect(self.Sondur)
            self.butonmuzik.clicked.connect(self.cal)

            self.setGeometry(100,100,50,50)
            self.show()

            #veri_yolu.flushInput()
        def oku(self):
            self.timer = QTimer()
            self.timer.timeout.connect(self.tekrarla)
            self.timer.start(10)



        def tekrarla(self):


             gelen_deger = veri_yolu.readline()

             gelen_deger = gelen_deger[:-2]
             #
             gelen_deger = gelen_deger.decode("utf-8")
             if (self.i != 0):#ilk okumada gelen \x ten kaçmak için.bu ifade döndürülemiyor int e.
              self.yazi2.setText(gelen_deger)

              self.ses=int(int(gelen_deger)*100/1024)

              self.media.setVolume(self.ses)

            #self.ses = round(int(self.yazi2.text()) * 100 / 1024)
            #self.media.setVolume(self.ses)
             self.i+=1

        def Yak(self):
            veri_yolu.write(b'1')


        def Sondur(self):
            veri_yolu.write(b'0')


        def cal(self):
            self.media.play()



app=QApplication(sys.argv)
try:
 veri_yolu=serial.Serial('COM4',9600)
except:
    print("Port Bulunamadı...")
pencere=Pencere()
sys.exit(app.exec_())