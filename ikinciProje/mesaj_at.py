import  smtplib
from email.mime.multipart import  MIMEMultipart
from  email.mime.text import  MIMEText
import  sys






isim_liste=[]
mail_liste=[]

def isimle_maili_ayir(deger):


   liste=deger.split(",")


   isim=liste[0]
   mail=liste[1]

   isim_liste.append(isim)

   mail_liste.append(mail)







with open("mail.txt","r",encoding="utf-8") as file:

  for i in file:
      i=i.strip()
      a=isimle_maili_ayir(i)
      #print(i)

  file.close()


sayi=1
for i in mail_liste:

    mesaj = MIMEMultipart()
    mesaj["From"] = "ilkeraykut8@gmail.com"
    mesaj["To"] = i
    mesaj["Subject"] ="{}.mailim".format(sayi)  # Mailimizin Konusu
    sayi +=1




    yazi = """

    Merhaba, Python ile mail gönderiyorum.    

    İLKER MUSTAFA AYKUT


     """


    mesaj_govdesi = MIMEText(yazi, "plain")  # Mailimizin gövdesini bu sınıftan oluşturuyoruz.

    mesaj.attach(mesaj_govdesi)  # Mailimizin gövdesini mail yapımıza ekliyoruz.


    try:
      mail = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP objemizi oluşturuyoruz ve gmail smtp server'ına bağlanıyoruz.

      mail.ehlo()  # SMTP serverına kendimizi tanıtıyoruz.

      mail.starttls()  # Adresimizin ve Parolamızın şifrelenmesi için gerekli

      mail.login("ilkeraykut8@gmail.com",
               "250250i7")  # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz.

      mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  # Mailimizi gönderiyoruz.

      mail.close()  # Smtp serverımızın bağlantısını koparıyoz.

    except:
         sys.stderr.write(
        "Mail göndermesi başarısız oldu...")  # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
         sys.stderr.flush()