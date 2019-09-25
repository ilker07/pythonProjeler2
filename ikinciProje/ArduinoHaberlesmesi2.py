
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMessageBox

import requests
from bs4 import BeautifulSoup
import  serial
import  sys
import  time

url="https://www.youtube.com/user/greatscottlab/featured"

cevap=requests.get(url)
icerik=cevap.content
deger=BeautifulSoup(icerik,"html.parser")
gonderilecek=deger.find_all("yt-formatted-string",{"id":"subscriber-count","class":"style-scope ytd-c4-tabbed-header-renderer"})
for eleman in gonderilecek:
    gonderilecek1=eleman.text
    if(len(gonderilecek1)>0):
        print(gonderilecek1)
    else:
        print("hata")




class haberlesme(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()





        #self.gonder()


    def gonder(self):
        self.buton1=QtWidgets.QPushButton("Buton1")
        self.buton2=QtWidgets.QPushButton("Buton2")
        self.yazi_alani=QtWidgets.QLineEdit()
        self.buton1.setStyleSheet("background-color: red")
        self.buton2.setStyleSheet("background-color: blue")
        self.yazi_alani.setStyleSheet(
            """QLineEdit { background-color: black; color: white }""")


        dikey=QtWidgets.QVBoxLayout()
        yatay1 = QtWidgets.QHBoxLayout()
        yatay=QtWidgets.QHBoxLayout()
        yatay.addStretch()
        yatay.addLayout(dikey)
        dikey.addLayout(yatay1)
        yatay.addStretch()







        yatay1.addWidget(self.buton1)
        yatay1.addWidget(self.buton2)
        dikey.addWidget(self.yazi_alani)



        self.setLayout(yatay)


        self.buton1.clicked.connect(self.Tikla1)
        self.buton2.clicked.connect(self.Tikla2)

        self.show()

    def Tikla1(self):

          b=self.yazi_alani.text()
          if(b !=""):
           a=bytes(b,'utf-8')
           #veri.write(a)
           #veri.write(b" ")




          else:
              QMessageBox.about(self, "Hata", "Boşluk bırakma..")

          self.yazi_alani.clear()




    def Tikla2(self):



        self.yazi_alani.setText(gonderilecek1)
        #a = bytes(gonderilecek.text, 'utf-8')
        #veri.write(a)





















uyg=QtWidgets.QApplication(sys.argv)
#veri = serial.Serial('COM3', 9600)
dosya=haberlesme()

sys.exit(uyg.exec_())




