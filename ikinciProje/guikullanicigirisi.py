

import  sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.git()
    def git(self):

        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)

        self.giris=QtWidgets.QPushButton("Giriş")
        self.yazi_alani=QtWidgets.QLabel("k")

        vertical_box=QtWidgets.QVBoxLayout()

        vertical_box.addWidget(self.kullanici_adi)
        vertical_box.addWidget(self.parola)
        vertical_box.addWidget(self.yazi_alani)

        vertical_box.addStretch()

        vertical_box.addWidget(self.giris)

        self.setLayout(vertical_box)


        self.giris.clicked.connect(self.Tikla)

        self.show()

    def Tikla(self):

        if(self.kullanici_adi.text()=="İlker" and self.parola.text()=="1234"):
            self.yazi_alani.setText("TEBRİKLER")

        else:
            self.yazi_alani.setText("Hatali giriş")

















uyg=QtWidgets.QApplication(sys.argv)

pencere=Pencere()

sys.exit(uyg.exec_())