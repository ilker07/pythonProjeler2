


from datetime import datetime

import  locale         #TÜRKİYE BİLGİSİ İÇİN
locale.setlocale(locale.LC_ALL,"")


print(datetime.now())
print(datetime.now().year)
print(datetime.ctime(datetime.now()))

print("*************************")

print(datetime.strftime(datetime.now(),"%A"))  #Y :YIL ,B :AY,A:GÜN, X:SAAT,D:TAM GÜN


saniye=datetime.timestamp(datetime.now()) #saniye bilgisi
print(saniye)



tarih=datetime(2018,12,4)  #DATETİME NESNESİ OLUŞTURULDU.4 ARALIK 2018
su_an=datetime.now()
print(tarih-su_an) #GİRİLEN TARİH İLE ŞİMDİKİ ZAMAN ARASINDAKİ FARK

