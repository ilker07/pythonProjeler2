

import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()


        self.git()
    def git(self):

        self.buton=QtWidgets.QPushButton("Tıkla")
        self.yazi_alani=QtWidgets.QLabel("Tıklanılmadı...")
        self.sayac=0
        self.textbox=QtWidgets.QLineEdit()
        v_box = QtWidgets.QVBoxLayout()

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()




        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        self.setLayout(h_box)

        self.buton.clicked.connect(self.Tikla)
        self.show()
    def Tikla(self):

        self.sayac +=1
        self.yazi_alani.setText(str(self.sayac)+" defa tıklandi...")

       #sender=self.sender           self.yazı_alanı.clear();  print(self.yazı_alanı.text())
       #if sender.text()=="Tıkla":

uyg=QtWidgets.QApplication(sys.argv)

pencere=Pencere()

sys.exit(uyg.exec_())


