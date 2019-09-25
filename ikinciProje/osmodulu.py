

import os
from  datetime import  datetime


print(os.getcwd())  #Bulunduğumuz yer C nin altında untitled1

os.chdir("C:\\Users\Asus\Downloads") #Dizini değiştir .

print(os.listdir())  #Bulunduğumuz dizinin altında bulunan dosyalar


for i in os.listdir():
    print(i)



os.mkdir("Deneme1") #Klasör oluşturur.

os.makedirs("Deneme2/Deneme3") #Önce Deneme2 yi oluşturur.Sonra Deneme3 ü oluşturur.

os.rmdir("Deneme2/Deneme3")  #Deneme2  altındaki Deneme3 ü siler.
os.removedirs("Deneme2/Deneme3") #İkisini de siler.

os.rename("text.txt","text2.txt")  #text.txt adında oluşturulan textin adını değiştirir.






print(os.stat("text.txt")) #Bütün özelliklerini görürüz.

print(os.stat("text.txt").st_mtime) #Değiştirilme zamanı.


print(datetime.fromtimestamp(os.stat("text.txt").st_mtime)) #Değiştirilme zamanı.



for i in os.walk("C:\\Users\Asus\Downloads"):  #Masaüstünün altındaki herşeyi verir.
    print(i)


for klasor_yolu,klasor_isimleri,dosya_ismleri in os.walk("C:\\Users\Asus\Downloads"):  #Masaüstünün altındaki herşeyi verir.
    print("Klasör yolu",klasor_yolu)
    print("Klasör isimleri",klasor_isimleri)
    print("Dosya isimleri",dosya_ismleri)
    print("***********************")

