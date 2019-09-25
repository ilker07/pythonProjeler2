
'''
import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server='www.ntvspor.com'


port=80


server_ip=socket.gethostbyname(server)

request="GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server,port))

s.send(request.encode())

sonuc=s.recv(1024)

print(sonuc)

'''

import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server='www.ntvspor.com'


def port_tarama(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False




for i in range(1,26):
    if(port_tarama(i)):
        print("Port ",i,"Açık")

    else:
        print("Port ",i,"Kapalı")







