
import requests
from bs4 import BeautifulSoup

liste=[]

liste2=[]





url="https://www.sinemalar.com/kullanici/ilkeraykut7/listeleri/10055/2016?page=1"
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



index=1
for i in range(0,10):
    print(index,".Film")
    url=liste[i]
    cevap = requests.get(url)
    icerik = cevap.content
    deger = BeautifulSoup(icerik, "html.parser")


    gonderilecek2=deger.find_all("div",{"class":"info-group"})

    for eleman in gonderilecek2:

        eleman.find({"class": "label-title"})

        eleman = eleman.text

        eleman = eleman.replace("\n", " ")
        eleman=eleman.strip()#ilk baştaki boşluklar ve sondakiler silinir.


        if(eleman.startswith("Tür ")):

            eleman=eleman.replace("Tür","Tür:")
            eleman=eleman.replace(" ","")


        if(eleman.startswith("Vizyon Tarihi")):
            eleman=""



        if(eleman.startswith("Yapımı")):
            eleman = eleman.replace("Yapımı", "Yapımı:")
            eleman=eleman.replace(" ","")


        #eleman = eleman.replace(" ","")

        liste2.append(eleman)

        if(eleman!=""):
         print(eleman) #her eklenen bir film için 4 tane eleman olur.yani liste 40 elmanlı olur.0 isim 3 süre 4 isim 7 süre ...



    index+=1
    print("******************************************************")




