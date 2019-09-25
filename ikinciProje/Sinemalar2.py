

import requests
from bs4 import BeautifulSoup
from SinemalarSql import *


liste=[]

liste2=[]
bos_liste=[]
orjinal_isim=0
sure=0
degisken=True
birinci_deger=0
ikinci_deger=10
index=1
for i in range(1,14):

 url="https://www.sinemalar.com/kullanici/ilkeraykut7/listeleri/10055/2016?page="+str(i)
 cevap = requests.get(url)
 icerik = cevap.content
 deger = BeautifulSoup(icerik, "html.parser")


 gonderilecek=deger.find_all("div",{"class":"all-favorites-feed"})


 for film in gonderilecek:

    #print(film)
    film=film.find("a")

    #print(film.get("href"))
    liste.append(film.get("href"))

    #print("*********************************************************************************************")





 for i in range(birinci_deger,ikinci_deger):
  #print(index,".Film")
  if(i==len(liste)):
        print("liste sonu...")
        degisken=False



  #else:
  if(degisken):

    #print(index, ".Film")
    url = liste[i]
    cevap = requests.get(url)
    icerik = cevap.content
    deger = BeautifulSoup(icerik, "html.parser")


    gonderilecek2=deger.find_all("div",{"class":"info-group"})

    for eleman in gonderilecek2:

        eleman.find({"class": "label-title"})

        eleman = eleman.text

        eleman = eleman.replace("\n", " ")
        eleman=eleman.strip()#ilk baştaki boşluklar ve sondakiler silinir.
        if(eleman.startswith("Orijinal İsmi")):
            orjinal_isim=1
            eleman=eleman.replace("Orijinal İsmi","Orijinal İsmi:")
            bos_liste.append(eleman)

        if(eleman.startswith("Tür ")):

            eleman=eleman.replace("Tür","Tür:")
            eleman=eleman.replace(" ","")
            if(orjinal_isim==1):
                bos_liste.append(eleman)


        if(eleman.startswith("Vizyon Tarihi")):
            eleman=""



        if(eleman.startswith("Yapımı")):
            eleman = eleman.replace("Yapımı", "Yapımı:")
            eleman=eleman.replace(" ","")

        if(eleman.startswith("Yapımı")):
            eleman=""
        #eleman = eleman.replace(" ","")


        if(eleman.startswith("Süre")):
           sure=1
           bos_liste.append(eleman)
           dakika=eleman.strip("Süre")
           dakika=dakika.strip("dk")
           dakika=int(dakika)


        #liste2.append(eleman)


        #if(eleman!=""):
         #print(eleman)

    if (len(bos_liste) == 3):
      if(dakika<100):

        print(index, ".Film")
        for i in range(0, 3):
            print(bos_liste[i])
        sinema = SinemaVeriTabani()
        bos_liste[0]=bos_liste[0].strip("Orijinal İsmi:")
        bos_liste[1]=bos_liste[1].strip("Tür:")
        bos_liste[2]=bos_liste[2].strip("Süre ")
        eklenecek_film=Film(bos_liste[0],bos_liste[1],bos_liste[2])

        sinema.Film_Ekle(eklenecek_film)
        time.sleep(1)
        print("******************************************************")
        index += 1
    bos_liste = []
    dakika=""
    #index+=1
    #print("******************************************************")



 birinci_deger+=10
 ikinci_deger+=10










