

import socket


soket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=8000
soket.bind((host,port))


print("Server başlatıldı..",(host,port))
print("Kullanıcı bekleniyor...")
soket.listen(1)


baglanti,adres=soket.accept()
print("Bağlantı kabul edildi!!!",adres)


mesaj=bytes('Hosgeldiniz Efendim','utf-8')

baglanti.send(mesaj)


data=baglanti.recv(1024)
if len(data)==0:
    #print("Gelen bir mesaj yok..")
    pass
else:

  print("Data:",data)


soket.close()





























