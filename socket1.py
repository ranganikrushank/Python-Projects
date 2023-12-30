import socket

port =3320
host = socket.gethostname()

s = socket.socket()

s.bind((host,port))


s.listen(1)

a,c = s.accept()

while(True):
    msg =input("Enter the message = ")
    a.send(msg.encode())
    if(msg == "bye"):
        break   
    else:
        msg2 = a.recv(1024)
        print(msg2.decode())
        if msg2.decode()=="bye":
            break