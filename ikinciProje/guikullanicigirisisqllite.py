import  sys
from PyQt5 import QtWidgets
import  sqlite3

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.git()


    def baglanti_olustur(self):
        baglanti=sqlite3.connect("giris.db")
        self.imlec=baglanti.cursor()
        self.imlec.execute("Create Table if not exists uyeler(Kullanici_Adi TEXT,parola TEXT)")
        baglanti.commit()



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

       adi=self.kullanici_adi.text()
       parolasi=self.parola.text()

       self.imlec.execute("Select * From uyeler where Kullanici_Adi=? and parola=?",(adi,parolasi))

       veri=self.imlec.fetchall()

       if(len(veri)==0):
           self.yazi_alani.setText("Böyle biri yok")
       else:
           self.yazi_alani.setText("Başarılı giriş.. ")





















uyg=QtWidgets.QApplication(sys.argv)

pencere=Pencere()

sys.exit(uyg.exec_())