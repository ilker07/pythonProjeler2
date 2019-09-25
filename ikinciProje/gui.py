

import  sys

from PyQt5 import QtWidgets,QtGui

def Pencere():

    uygulama=QtWidgets.QApplication(sys.argv)

    pencere=QtWidgets.QWidget()

    buton=QtWidgets.QPushButton(pencere)
    buton.setText("Bu bir buton")



    layout_buton1=QtWidgets.QPushButton("Tamam")
    layout_buton2=QtWidgets.QPushButton("İptal")

    layout_buton3 = QtWidgets.QPushButton("Tamam2")
    layout_buton4 = QtWidgets.QPushButton("İptal2")

    horizantol_box=QtWidgets.QHBoxLayout()
    vertical_box=QtWidgets.QVBoxLayout()


    horizantol_box.addWidget(layout_buton1)
    horizantol_box.addWidget(layout_buton2)

    vertical_box.addWidget(layout_buton3)
    vertical_box.addWidget(layout_buton4)



   # horizantol_box.addStretch()

    pencere.setLayout(horizantol_box)
    pencere.setLayout(vertical_box)


    pencere.setWindowTitle("Ders 1")


    etiket1=QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    #etiket2.setPixmap(QtGui.QPixmap("Pyhton.png"))  bu progeye ekle png resim
    etiket1.setText("1. etiket")
    etiket1.move(150,30)
    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(uygulama.exec_())

Pencere()
