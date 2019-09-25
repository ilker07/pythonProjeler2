

import requests
from bs4 import BeautifulSoup
birinci_skor=""
ikinci_skor=""
a=""
b=""
while True:
 url="http://www.mackolik.com/Basket-Mac/3088638/Saski-Baskonia-SAD-Fenerbahce"
 cevap = requests.get(url)
 icerik = cevap.content
 deger = BeautifulSoup(icerik, "html.parser")


 gonderilecek=deger.find_all("div",{"class":"match-score"})




 for eleman in gonderilecek:


        eleman.find({"id": "dvScoreText"})

        eleman=eleman.text
        eleman = eleman.replace("\n", " ")
        eleman=eleman.replace(" ","")
        eleman = eleman.strip()
        eleman=eleman.split("-")
        birinci_skor=eleman[0]
        ikinci_skor=eleman[1]

        if(birinci_skor != a or ikinci_skor != b):
            a=birinci_skor
            b=ikinci_skor
            print("BASKONİA: "+a+"-"+b+" FB")












