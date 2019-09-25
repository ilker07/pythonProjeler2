
import sqlite3

import time
class Film():
    def __init__(self,isim,tur,sure):
        self.isim=isim
        self.tur=tur
        self.sure=sure

    def __str__(self):
        return "Film ismi:{}\nFilm Tur: {}\nFilm Sure:{}".format(self.isim, self.tur, self.sure)


class SinemaVeriTabani():


    def __init__(self):
        self.baglanti_olustur()


    def baglanti_olustur(self):

        self.baglanti=sqlite3.connect("Sinemalar_yeni.db")
        self.ayrac=self.baglanti.cursor()


        sorgu="Create Table If not exists sinemalar_yeni (Film_Ismi TEXT,Tur TEXT,Sure INT)"
        self.ayrac.execute(sorgu)
        self.baglanti.commit()


    def Film_Ekle(self,film_isim):

        sorgu="Insert into Sinemalar values(?,?,?)"
        #self.ayrac.execute(sorgu,(film_isim,film_tur,film_sure))
        self.ayrac.execute(sorgu,(film_isim.isim,film_isim.tur,film_isim.sure))
        self.baglanti.commit()






#sinema=SinemaVeriTabani()