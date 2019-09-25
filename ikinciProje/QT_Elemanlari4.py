

import  sys
from PyQt5.QtWidgets import *




class TabWidgetPencere(QTabWidget):

    def __init__(self):

        super().__init__()


        self.tab1=QTabWidget() #widget da olabilir.
        self.tab2=QTabWidget()
        self.tab3=QTabWidget()

        self.Tablo1()
        self.Tablo2()
        self.Tablo3()


        self.addTab(self.tab1,"Bilgiler")
        self.addTab(self.tab2,"Kişisel")
        self.addTab(self.tab3,"Hakkında")

        self.setWindowTitle("QTabWidget")


        self.setTabPosition(QTabWidget.North)
        self.setTabShape(QTabWidget.Triangular)
        self.setTabsClosable(True)

        self.setTabToolTip(0,"Bilgiler Bölümü")
        self.setTabToolTip(1, "Kişisel Bölümü")
        self.setTabToolTip(2, "Hakkında Bölümü")

        self.setMovable(True)


        self.tabCloseRequested.connect(self.kapat)



        self.show()

    def kapat(self, q):
        self.removeTab(q)

    def Kapat(self):
        sender=self.sender()
        self.removeTab(sender)



    def Tablo1(self):

        h_box=QHBoxLayout()
        h_box2=QHBoxLayout()
        v_bov= QVBoxLayout()

        self.adLabel=QLabel("Ad:   ")
        self.soyadLabel=QLabel("Soyad:")
        self.lineEdit1=QLineEdit()
        self.lineEdit2=QLineEdit()

        h_box.addWidget(self.adLabel)
        h_box.addWidget(self.lineEdit1)

        h_box2.addWidget(self.soyadLabel)
        h_box2.addWidget(self.lineEdit2)

        v_bov.addStretch()
        v_bov.addLayout(h_box)
        v_bov.addLayout(h_box2)
        v_bov.addStretch()


        self.tab1.setLayout(v_bov)






    def Tablo2(self):

        h_box = QHBoxLayout()
        h_box2 = QHBoxLayout()
        v_bov = QVBoxLayout()

        self.yasLabel = QLabel("Yaş:   ")
        self.lineEdit1 = QSpinBox()
        self.buton = QPushButton("Gönder")

        h_box.addWidget(self.yasLabel)
        h_box.addWidget(self.lineEdit1)


        h_box2.addWidget(self.buton)

        v_bov.addStretch()
        v_bov.addLayout(h_box)
        v_bov.addLayout(h_box2)
        v_bov.addStretch()

        self.tab1.setLayout(v_bov)
        self.tab2.setLayout(v_bov)


    def Tablo3(self):

        h_box=QHBoxLayout()

        self.label=QLabel()
        self.label.setText("İlker Mustafa Aykut")

        h_box.addWidget(self.label)

        self.tab3.setLayout(h_box)






app=QApplication(sys.argv)
tab=TabWidgetPencere()
sys.exit(app.exec_())
