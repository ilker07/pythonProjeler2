

import requests
import sys


url="https://api.fixer.io/latest?base="
birinci_doviz=input("Birinci döviz:")
ikinci_doviz=input("İkinci döviz:")

cevap=requests.get(url+birinci_doviz)


json_verisi=cevap.json() #girilen dövize göre bütün paraların o dövizdeki karşılığı çekildi.
try:
 print(json_verisi["rates"][ikinci_doviz])
except:
    sys.stderr.write("Doğru para birimi girin..")




