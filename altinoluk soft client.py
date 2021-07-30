import socket
import threading 

FORMAT='utf-8'
client  =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 123
def davet_et():
        ip2=input("ip adresi:")
        print("altinoluk soft client chate "+nick+" tarafindan davet edildiniz ip adresi:"+ip2)
        main()

def covid():
    print("Covid19:Solunum yollarini etkileyen bir cesit coronavirus")
    print("Belirtiler: Ates,Oksuruk,halsizlik,nefes darligi")
    print("Yakindaki hastaneler 1.Ekin tip merkezi 2.edremit devlet hastanesi")
    print("Alo 185 kovid danisma hatti.")
    main()
    

def baglan(addr):
    port = 123
    server=socket.gethostbyname(socket.gethostname()) 
    header=64
    #addr2=server+port
    client.connect(addr)
    #thread1=threading.Thread(args=(addr),target=recevie_msg)
    #thread1.start()
    # return addr
    while True:
        a=input("Message:")
        send(nick+":"+a)
        recevie_msg(addr)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    #send_length=str(msg_length).encode(FORMAT)
    #send_length += b' '+(header-len(send_length))
    #client.send(send_length)
    client.send(message)

def recevie_msg(addr):
        msg=client.recv(64).decode(FORMAT)
        print(msg)
def main():
    islem=input("islem:")
    if islem=="connect":
        server = input("Server ip:")
        addr=(server,port)
        baglan(addr)
    elif islem=="covid19":
        covid()
    elif islem=="davet":
        davet_et()
    else:
        print("Not selected")
        main()
                
print("welcome to altinoluk software client")
nick=input("nickname:")
password=input("password:")
if password=="aaaa":
     main()
else:
    print("Wrong password")   
