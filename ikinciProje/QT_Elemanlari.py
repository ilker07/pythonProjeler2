import sys
from PyQt5.QtWidgets import  QWidget,QPushButton,QLabel,QGridLayout,QApplication,QHBoxLayout,QVBoxLayout,QSpinBox,QDoubleSpinBox,QSlider
from PyQt5.QtGui import *
from  PyQt5.QtCore import *

from PyQt5.QtMultimedia import  QMediaPlayer,QMediaContent


class Pencere(QWidget):


    def __init__(self):

        super().__init__()

        self.git()


    def git(self):

         v_box=QVBoxLayout()

         #SELF.BUTON.setIcon(qıCON(PC DEKİ YERİ))


         self.setAutoFillBackground(True) #ARKAPLAN İÇİN
         self.p=self.palette()
         self.p.setColor(self.backgroundRole(),Qt.blue)
         self.setPalette(self.p)
         self.media=QMediaPlayer()
         self.media.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Asus/Downloads/Payback.mp3")))


         self.sp2=QSpinBox()
         self.buton_muzik=QPushButton("Müzik Çal")
         self.buton_muzik_durdur=QPushButton("Müziği Durdur")
         self.slider=QSlider(Qt.Horizontal)
         self.slider.setTickPosition(QSlider.TicksBelow) #Aralıklar koyar slider a.

         self.slider.setMaximum(100)
         self.slider.setMinimum(0)
         self.slider.setSingleStep(5)

         self.slider.valueChanged.connect(self.Yaz)

         self.slider_yazi=QLabel("Yazı")


         h_box=QHBoxLayout()
         h_box2=QHBoxLayout()
         self.spinbox=QSpinBox()
        # self.spinbox2 = QDoubleSpinBox()   Küsürlü sayılar için.
         self.buton=QPushButton("Tikla")
         self.yazi=QLabel("Yazi")
         #self.spinbox.setRange(0,1000)   Alttaki 2 kod yerine kullanılabilir.
         self.spinbox.setMinimum(0)
         self.spinbox.setMaximum(1000)
         self.spinbox.setSingleStep(5)#5 er 5 er artar.
         self.spinbox.setValue(100) #Program açıldığında 100 değeri ile başlar.
         h_box.addWidget(self.spinbox)
         h_box.addWidget(self.yazi)
         h_box.addWidget(self.buton)
         h_box.addWidget(self.sp2)
         h_box.addWidget(self.buton_muzik)
         h_box.addWidget(self.buton_muzik_durdur)
         h_box2.addStretch()
         h_box2.addWidget(self.slider)
         h_box2.addWidget(self.slider_yazi)
         h_box2.addStretch()
         v_box.addLayout(h_box)
         v_box.addStretch()
         v_box.addLayout(h_box2)
         self.setLayout(h_box)
         self.setLayout(h_box2)
         self.buton.clicked.connect(self.Tikla)
         self.spinbox.valueChanged.connect(self.SP)
         self.yazi.setText(str(self.spinbox.value()))
         self.buton_muzik.clicked.connect(self.sarki_baslat)
         self.buton_muzik_durdur.clicked.connect(self.sarki_durdur)
         self.buton_muzik_durdur.setDisabled(True)
         self.sp2.valueChanged.connect(self.ses_degis)
         self.setLayout(v_box)
         self.show()


    def Tikla(self):

        self.yazi.setText(str(self.spinbox.value()))

    def SP(self):

        self.yazi.setText(str(self.spinbox.value()))


    def ses_degis(self):
        self.media.setVolume(self.sp2.value())

    def sarki_baslat(self):
        #self.sp2.setValue(0)
        self.media.setVolume(self.sp2.value())
        self.media.play()
        self.buton_muzik_durdur.setDisabled(False)
        self.buton_muzik.setDisabled(True)


    def sarki_durdur(self):
        self.media.stop()
        self.buton_muzik_durdur.setDisabled(True)
        self.buton_muzik.setDisabled(False)

    def Yaz(self):
        self.slider_yazi.setText(str(self.slider.value()))

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
