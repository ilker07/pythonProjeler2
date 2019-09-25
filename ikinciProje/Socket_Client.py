
import socket

soket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=8000

soket.connect((host,port))

data=soket.recv(1024)
data=data.decode("utf-8")


print("Data: ",data)


#soket.send("Hoşbulduk....")


soket.close()

























