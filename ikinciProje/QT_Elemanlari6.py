



 #self.split=QSplitter(qt.vertical) ayraç.   self.split.addwidget(self.buton) ,self.split.setopaqueresize(False)
 #self.split.setSizes([100,200,50])  splitterin 3 tane öğesi varsa sırayla boyutları.
 #self.split.splitterMoved.connect(self.uygula)
 #def  uygula(self,s1,s2)  s1 büyütülen alanın büyüklüğü  s2 hangi indexteki alan büyütüldü.


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class Pencere(QMainWindow):
     def __init__(self):
         self.durum=True
         super().__init__()
         self.setUI()

     def setUI(self):
         menu=self.menuBar()
         dosya=menu.addMenu("Dosya")
         self.liste=QAction(QIcon("C:/Users/Asus/Desktop/messi.jpg"),"liste",self)
         dosya.addAction(self.liste)


         self.array=QListWidget()
         self.array.insertItem(0,"Birinci eleman")
         self.array.insertItem(1,"İkinci eleman")
         self.array.insertItem(2,"Üçüncü eleman")
         self.array.insertItem(3,"Dördüncü eleman")

         self.dock=QDockWidget("Liste Kısmı",self)
         self.dock.setWidget(self.array)
         self.dock.visibilityChanged.connect(self.uygula)

         dosya.triggered.connect(self.yap)


         self.show()

     def yap(self,q):
         if q.text()=="liste":
             if self.durum==True:
                 self.dock.setVisible(False)
             else:
                 self.dock.setVisible(True)
     def uygula(self,q):
         if q:
             self.liste.setIcon(QIcon("C:/Users/Asus/Desktop/messi.jpg"))
             self.durum=True
         else:
             self.liste.setIcon(QIcon())
             self.durum=False








app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())












