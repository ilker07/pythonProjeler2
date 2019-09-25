
import  sys
from PyQt5.QtWidgets import *


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.git()


    def git(self):


        #self.mesajkutusu=QMessageBox()
        #self.mesajkutusu.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #self.mesajkutusu.buttonClicked.connect(self.git)
        self.yazi=QLabel("Yazi")
        self.takvim=QCalendarWidget()
        self.takvim.setGridVisible(True)

        self.button=QPushButton("Aç")

        self.takvim.clicked.connect(self.uygula)
        self.lcd=QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Filled)


        v_box=QVBoxLayout()
        v_box.addWidget(self.takvim)
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.lcd)
        v_box.addWidget(self.button)

        self.button.clicked.connect(self.ac)
        self.setLayout(v_box)





        self.show()
    #def git(self,q):
        #q.text  Tıklanan butonun adı..
        #QMessageBox.warning(self, "Uyarı mesajı", "blablalbalbalball")
        pass
    def ac(self):
        self.dialog=QDialog()
        self.dialog.setWindowTitle("Açılan Pencere")
        v_box=QVBoxLayout()
        self.text2=QTextEdit()
        v_box.addWidget(self.text2)
        self.dialog.setLayout(v_box)
        #self.text=QTextEdit(self.dialog)  text2 ve vbox u kullanmadan sadece bunu da yazabilriz.
        self.dialog.exec()
    def uygula(self,q):
       #self.yazi.setText(q.toString())
       self.deger=q.toString()
       self.yeni_deger=self.deger.split(" ")
       self.yazi.setText(str(self.yeni_deger[2]))
       self.lcd.display(self.yazi.text())

       #self.mdi = QMdiArea()     QMainWindow
       #self.setCentralWidget(self.mdi)

    '''def sekmeEkle(self, q):
           if q.text() == "Sekme Ac":  MenuBardaki menudeki tıklayınca 
               sub = QMdiSubWindow()
               sub.setWindowTitle("Sekme {}".format(self.sayac))
               widget = QWidget()
               v_box = QVBoxLayout()
               v_box.addWidget(QTextEdit())
               v_box.addWidget(QPushButton("Gonder"))
               widget.setLayout(v_box)
               sub.setWidget(widget)
               self.mdi.addSubWindow(sub)
               self.sayac += 1
               sub.show()
           elif q.text() == "Fayansla":  Açılan subwindowları hizalar.
               self.mdi.cascadeSubWindows()
           else:
               self.mdi.tileSubWindows()''' #Açılan subwindowları döşer.


app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())