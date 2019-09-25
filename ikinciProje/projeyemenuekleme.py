


import sys
import os

from  PyQt5.QtWidgets import  QWidget,QApplication,QTextEdit,QLabel,QPushButton,QBoxLayout,QVBoxLayout,QFileDialog,QHBoxLayout


from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QWidget):

    def __init__(self):
        super().__init__()

        menubar=self.menuBar()

        dosya=menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac=QAction("Dosya Aç",self)

        dosya_kaydet= QAction("Dosya kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis=QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)


        ara_ve_degistir=duzenle.addMenu("Ara ve Değiştir")
        ara=QAction("Ara",self)
        degistir=QAction("Değiştir")

        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)

        temizle=QAction("Temizle",self)
        duzenle.addAction(temizle)


        cikis.triggered.connect(self.cikis_yap)
        dosya.triggered.connect(self.dosya_islemi)








        self.show()

    def cikis_yap(self):
        qApp.quit()


    def dosya_islemi(self,action):
        if(action.text=="Dosya Aç"):
            print("ffsd")





app=QApplication(sys.argv)

menu=Menu()

sys.exit(app.exec_())

