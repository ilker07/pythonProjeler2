

import sys
import serial
from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import  QMediaPlayer,QMediaContent
import time



class Pencere(QTabWidget):
    def __init__(self):
        super().__init__()
        self.sayac=0
        self.i=0
        self.media = QMediaPlayer()
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Asus/Downloads/Payback.mp3")))
        self.tab1=QTabWidget()#1.sekme
        self.tab2=QTabWidget()#2.sekme
        self.tab3=QTabWidget()#3.sekme


        self.tab1_fonksiyon() #1.sekmenin içinin doldurulacağı fonksiyon
        self.tab2_fonksiyon() #2.sekmenin içinin doldurulacağı fonksiyon
        self.tab3_fonksiyon() #3.sekmenin içinin doldurulacağı fonksiyon


        self.addTab(self.tab1,"1.Bölüm") #Ana pencereye 1.sekme eklendi.
        self.addTab(self.tab2,"2.Bölüm") #Ana pencereye 2.sekme eklendi.
        self.addTab(self.tab3,"3.Bölüm") #Ana pencereye 3.sekme eklendi.

        self.setFixedSize(300, 200)

        self.show()

    def tab1_fonksiyon(self):
        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        h_box2=QHBoxLayout()
        h_box3=QHBoxLayout()

        self.pbar=QProgressBar()
        self.pbar.setMaximum(100)
        self.pbar.setMinimum(0)

        self.pbar.setFixedSize(285,20)
        self.sarki_butonu=QPushButton("Çal")
        self.sarki_tekrar_butonu=QPushButton("Tekrardan Çal")
        self.sarki_durum=QLabel("Şarkı Çalmıyor..")

        self.ses_okuma_butonu=QPushButton("Ses Seviyesi")
        self.ses_seviyesi=QLabel("0")
        self.deneme=QLabel()

        h_box.addWidget(self.pbar)

        h_box2.addWidget(self.sarki_butonu)
        h_box2.addWidget(self.sarki_tekrar_butonu)
        h_box2.addWidget(self.sarki_durum)

        h_box3.addWidget(self.ses_okuma_butonu)
        h_box3.addWidget(self.ses_seviyesi)
        h_box3.addWidget(self.deneme)



        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)

        self.sarki_butonu.clicked.connect(self.sarki_baslatma_durdurma)
        self.sarki_tekrar_butonu.clicked.connect(self.tekrar)
        self.ses_okuma_butonu.clicked.connect(self.yap)



        self.tab1.setLayout(v_box)



    def tab2_fonksiyon(self):
        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        h_box2=QHBoxLayout()

        self.ledbuton=QPushButton("Ledi Yak")
        self.ledbutonsondur=QPushButton("Ledi Söndür")
        self.leddurum=QLabel("Led Yanmıyor")

        self.odalambabuton=QPushButton("Lambayı Yak")
        self.odalambabutonsondur=QPushButton("Lambayı Söndür")
        self.lambadurum=QLabel("Lamba Yanmıyor")


        h_box.addWidget(self.ledbuton)
        h_box.addWidget(self.ledbutonsondur)
        h_box.addWidget(self.leddurum)


        h_box2.addWidget(self.odalambabuton)
        h_box2.addWidget(self.odalambabutonsondur)
        h_box2.addWidget(self.lambadurum)


        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)


        self.ledbuton.clicked.connect(self.led_yak_sondur)
        self.ledbutonsondur.clicked.connect(self.led_yak_sondur)

        self.odalambabuton.clicked.connect(self.oda_yak_sondur)
        self.odalambabutonsondur.clicked.connect(self.oda_yak_sondur)


        self.tab2.setLayout(v_box)




    def tab3_fonksiyon(self):
        pass
    def oda_yak_sondur(self):
        sender=self.sender()
        if(sender.text()=="Lambayı Yak"):
            veri_yolu.write(b'2')
            self.lambadurum.setText("Lamba Yanıyor")
        if(sender.text()=="Lambayı Söndür"):
            veri_yolu.write(b'3')
            self.lambadurum.setText("Lamba Yanmıyor")
    def led_yak_sondur(self):
        sender=self.sender()
        if(sender.text()=="Ledi Yak"):
           veri_yolu.write(b'1')
           self.leddurum.setText("Led Yanıyor")
        if(sender.text()=="Ledi Söndür"):
            veri_yolu.write(b'0')
            self.leddurum.setText("Led Yanmıyor")
    def sarki_baslatma_durdurma(self):
        self.sayac +=1
        if(self.sayac %2==1):
         self.sarki_butonu.setText("Durdur..")
         self.media.play()
         self.sarki_durum.setText("Şarkı Çalıyor")
         self.toplam_saniye=round(self.media.duration()/1000) #254 saniye
         self.dakika=int(self.toplam_saniye/60)
         self.saniye=self.toplam_saniye-(self.dakika*60)
         self.deneme.setText(str(self.dakika)+" dakika "+str(self.saniye)+" saniye")
         self.timer=QTimer()
         self.timer.timeout.connect(self.baglan)
         self.timer.start(1000)


        if(self.sayac %2==0):
         self.sarki_butonu.setText("Çal..")
         self.media.pause()
         self.sarki_durum.setText("Şarkı Çalmıyor..")

    def tekrar(self):
        self.media.stop()
        self.sarki_durum.setText("Şarkı Çalıyor")
        self.media.play()

    def baglan(self):

        self.a=int(self.media.position()/1000)
        print(self.a)

        self.pbar.setValue(int(self.a*100/self.toplam_saniye))

    def yap(self):
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.tekrarla)
        self.timer2.start(10)


    def tekrarla(self):
        gelen_deger = veri_yolu.readline()

        gelen_deger = gelen_deger[:-2]

        gelen_deger = gelen_deger.decode("utf-8")
        if (self.i != 0):  # ilk okumada gelen \x ten kaçmak için.bu ifade döndürülemiyor int e.
            #self.ses_seviyesi.setText(gelen_deger)

            self.ses=int(gelen_deger)
            self.a=int(self.ses*100/1024)
            self.ses_seviyesi.setText(str(self.a))
            self.media.setVolume(self.a)


        self.i += 1



app=QApplication(sys.argv)
pencere=Pencere()
try:
 veri_yolu=serial.Serial('COM4',9600)
except:
    print("Port Bulunamadı...")
sys.exit(app.exec_())