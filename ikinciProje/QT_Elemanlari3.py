

import  sys
from  PyQt5.QtWidgets import  *




class Pencere(QWidget):


   def __init__(self):

       super().__init__()

       self.git()

   def git(self):
       self.buton=QPushButton("Buton")
       self.buton2=QPushButton("Tamam")
       self.buton3=QPushButton("Font")
       self.yazi=QLabel("Yazı Alanı")
       self.line_edit=QLineEdit()
       h_box=QHBoxLayout()

       h_box.addStretch()
       h_box.addWidget(self.buton)
       h_box.addWidget(self.yazi)
       h_box.addWidget(self.buton2)
       h_box.addWidget(self.line_edit)
       h_box.addWidget(self.buton3)
       h_box.addStretch()

       self.setLayout(h_box)

       self.setWindowTitle("İki Class")
       self.buton.clicked.connect(self.Tikla)
       self.buton2.clicked.connect(self.Tikla2)
       self.buton3.clicked.connect(self.Tikla3)

   def Tikla(self):

       diller=("Pyhton","C","C++","C#","Java")
       secilen,tamam=QInputDialog.getItem(self,"Sevdiğiniz Dil","Dili Seçin",diller,0,False)
       if tamam:
           self.yazi.setText(str(secilen))


   def Tikla2(self):
       yazilan,tamam=QInputDialog.getText(self,"İsminiz","Yazın..")
       if tamam:
          self.line_edit.setText(str(yazilan))
       else:
           print("Hata")
   def Tikla3(self):

       secilen,tamam=QFontDialog.getFont()
       if tamam:
           self.yazi.setFont(secilen)
class MenuElemanlari(QMainWindow):

    def __init__(self):

        super().__init__()
        self.pencere=Pencere()
        self.setCentralWidget(self.pencere)
        self.git2()

    def git2(self):

        menubar=self.menuBar()

        dosya=menubar.addMenu("Dosya")

        yeni=QAction("Yeni",self)
        kaydet=QAction("Kaydet",self)
        kapat=QAction("Kapat",self)

        dosya.addAction(yeni)
        dosya.addAction(kaydet)
        dosya.addAction(kapat)
        print("sadds")
        self.show()








app=QApplication(sys.argv)
menu=MenuElemanlari()
sys.exit(app.exec_())
