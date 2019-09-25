


import sys
import  os

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QFileDialog,QTextEdit,QHBoxLayout

class Notepad(QWidget):
    def __init__(self):


        super().__init__()


        self.git()

    def git(self):


        self.yazi_alani=QTextEdit()
        self.temizle=QPushButton("Temizle")
        self.ac=QPushButton("Aç")
        self.kaydet=QPushButton("Kaydet")


        h_box=QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box=QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)
        self.setLayout(v_box)

        self.temizle.clicked.connect(self.Temizle)
        self.ac.clicked.connect(self.Ac)
        self.kaydet.clicked.connect(self.Kaydet)

        self.show()


    def Temizle(self):
        self.yazi_alani.clear()

    def Ac(self):
        dosya_ismi=QFileDialog.getOpenFileName(self,"Dosya aç",os.getenv("HOME")) #HOME YERİNE DESKTOP DA YAZILABİLİR.

        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())











    def Kaydet(self):


        dosya_ismi=QFileDialog.getSaveFileName(self,"Kaydet",os.getenv("HOME"))

        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())










app=QApplication(sys.argv)
notepad=Notepad()
sys.exit(app.exec_())

