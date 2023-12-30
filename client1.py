import socket

port =3320
host = socket.gethostname()

s = socket.socket()
s.connect((host,port))

while(True):
    msg = s.recv(1024)
    
    print(msg.decode())

    if(msg.decode()=='bye'):
        break
    else:
        msg =input("Enter the message = ")
        s.send(msg.encode())
        if msg=="bye":
            break