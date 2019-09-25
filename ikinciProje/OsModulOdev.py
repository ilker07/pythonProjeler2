


import  os


liste=[]
liste2=[]
liste3=[]
for dosya in os.walk("C:\\Users\Asus\Downloads"):

     for i in range(0,len(dosya[2])):

       #print(dosya[2][i])
        if(dosya[2][i].endswith(".txt")):
            #print(dosya[2][i])
            liste.append(dosya[2][i]+"\n")

        elif(dosya[2][i].endswith(".pdf")):
            liste2.append(dosya[2][i]+"\n")


        elif (dosya[2][i].endswith(".mp3")):
            liste3.append(dosya[2][i]  +"\n")

with open("tum_dosyalar.txt","w",encoding="utf-8") as file:

    for i in liste:
        file.write(i)



with open("pdf_dosyalari.txt","w",encoding="utf-8") as file2:

    for i in liste2:
        file2.write(i)

with open("mp3_dosyalari.txt", "w", encoding="utf-8") as file3:
    for i in liste3:
        file3.write(i)