

import sys
#from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QPushButton
from PyQt5.QtWidgets import  QWidget,QPushButton,QLabel,QGridLayout,QApplication,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import *


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.git()
    def git(self):
        self.pen=QWidget()

        h_box2=QHBoxLayout()
        v_box=QVBoxLayout()
        self.link=QLabel("<a href=\"https://www.youtube.com\">Youtube</a>")
        self.link.setOpenExternalLinks(True) #linke tıklayınca çalışacak.
        self.izgara=QGridLayout()
        self.yazi_alani=QLabel("Tıklanmadı...")
        self.yazi_alani.setFont(QFont("Arial",35))#QFont.Bold 3. parametre alabilir.
        self.deger=1
        for i in range(0, 4):
            for j in range(0, 4):
                self.buton=QPushButton("Buton"+str(self.deger))
                self.izgara.addWidget(self.buton,i,j)
              #  self.izgara.addWidget(QPushButton("Button" + str(self.deger)), i, j)
                self.deger += 1
                self.buton.clicked.connect(self.Tikla)



        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        v_box.addLayout(self.izgara)
        v_box.addLayout(h_box2)
        h_box2.addStretch()
        h_box2.addWidget(self.yazi_alani)
        h_box2.addStretch()
        v_box.addWidget(self.link)



        #giris=QLineEdit()  giris.setReadOnly()  saddece okuma
        #giris.setInputMask   Telefon noları gibi başı aynı olan yerler 0530 gibi sayıy sabitleme
        #giris.textChanged.connect(self.Tikla)  text değişince fonksiyona git.
        #buton.setIcon( QIcon(PYTHON.JPG))
        #combobox.addItem(""ilker"")
        #combobox.activated(self.uygula)
        #combobox.currentIndexChanged
        #combobo.highlighted.coonnect
        v_box.addStretch()

        self.setLayout(h_box)

        #self.setGeometry(100,100,500,500)




        self.show()
    def Tikla(self):
        sender=self.sender()
        self.yazi_alani.setText(sender.text())

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())








