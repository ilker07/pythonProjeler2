
from  bs4 import BeautifulSoup
import re

'''
icerik=BeautifulSoup("<html><head></head><body><h1 id='ozel' class='sinif'>İlker</h1 ></body></html>","html.parser")


etiket=icerik.h1   #<h1 id='ozel' class="sinif">İlker</h1> Cevabı  bu.

#print(etiket.name) #h1

#print(etiket.text) #İlker
#etiket.name="h2" #h1 etiketi h2 olarak değiştirildi.


#print(icerik.h2) #<h2 class="sinif">İlker</h2>


#print(etiket['id']) #ozel


#print(etiket.attrs) #{'class': ['sinif'], 'id': 'ozel'}


etiket["yeni_eklenen"] ="ilker_yeni_eklenen"

#print(etiket) #<h1 class="sinif" id="ozel" yeni_eklenen="ilker_yeni_eklenen">İlker</h1>

#print(etiket.attrs) #{'id': 'ozel', 'class': ['sinif'], 'yeni_eklenen': 'ilker_yeni_eklenen'}


etiket["class"]=["sinif_degisti","2.sinif_ozelligi"]  #class a 2 tane özellik eklenir.



#del etiket["class"] #class silindi.

#print(etiket) #<h1 class="sinif_degisti 2.sinif_ozelligi" id="ozel" yeni_eklenen="ilker_yeni_eklenen">İlker</h1>

#print(etiket.get_attribute_list("class")) #['sinif_degisti', '2.sinif_ozelligi']


navigable_string=etiket.string

#print(navigable_string) #İlker  .Bu String değil navigable string.

#yazi +=navigable_string

#print(yazi)
etiket.string.replace_with("Değiştimmmm")


#print(etiket)


print(icerik.html)
'''


html_doc="""

<html><head><title>Başlık Kısmı </title></head>

<body>

<p class='sinif1' >Birinci Cumle  </p>
<p class='sinif2' >İkinci Cumle  </p>

<a href==\"https://www.facebook.com\"  id='Facebook'>Facebook</a>

<a href==\"https://www.youtube.com\">Youtube</a>

"""

from  bs4 import BeautifulSoup

icerik=BeautifulSoup(html_doc,"html.parser")

#print(icerik.a.contents[0].string)   #Facebook

#for i in icerik.p.children:
    #print(i)


#for item in icerik.a.descendants:

   # print(item)

#print(len(list(icerik.children)))


#for i in list(icerik.children):
    #print(i)
    #print("************")



#print(len(list(icerik.descendants)))


#for i in list(icerik.descendants):
    #print(i)
    #print("************")



#for i in icerik.strings:  #ya da direkt icerik.stripped_strings
    #if(i!="\n"):
        #print(i)




#print(icerik.p.next_sibling.next_sibling )  #Birinci next_sibling boşluk karakterini getirir.2.next 2.p etiketini getirir.


#print(icerik.find("p",attrs={"class": "sinif2"}).previous_sibling.previous_sibling)


#print(icerik.p.next_element) #Birinci cümle



#re.compile("^b") #b harfiyle başlayanları bulur.