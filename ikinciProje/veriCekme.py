
import requests
from bs4 import BeautifulSoup

liste=[]


url="https://www.sinemalar.com/film/35917/hachiko-a-dogs-story"

cevap=requests.get(url)
icerik=cevap.content
deger=BeautifulSoup(icerik,"html.parser")

#gonderilecek=deger.find_all("span",{"class":"label"})
gonderilecek=deger.find_all("div",{"class":"info-group"})

#gonderilecek2=gonderilecek.find(("yt-formatted-string",{"id":"subscriber-count"},{"class":"style-scope ytd-c4-tabbed-header-renderer"}))

for eleman in gonderilecek:

  eleman.find({"class":"label-title"})


  eleman=eleman.text
  eleman = eleman + " "
  eleman = eleman.replace("\n", " " )

  eleman=eleman.strip()
  liste.append(eleman)
  #print(eleman)    her eklenen bir eleman 4 tane eleman olur.






a=liste[3]
a=a.strip("Süre ")
a=a.strip("dk")
a=a+" "+"dakika"

b=liste[0]
b=b.strip("Orijinal İsmi ")



print("Filmin adı: {} Süre:{} ".format(b,a))


