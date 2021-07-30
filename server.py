import socket
import threading

port = 123
server=socket.gethostbyname(socket.gethostname())

addr=(server,port)

header=64

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

FORMAT='utf-8'

server.bind(addr)

conns=[]

def broadcast(message):
    classic="|"
    message=message.encode(FORMAT)
    classic=classic.encode(FORMAT)
    for conn1 in conns:
        conn1.send(message)
        conn1.send(classic)
        

def handle_client(conn,addr):
    print("New connections....")
    connected=True
    while connected==True:
        msg_length=1
        #msg_length=conn.recv(header).decode(FORMAT)
        if msg_length:
            #msg_length=int(msg_length)
            msg=conn.recv(64).decode(FORMAT)
            if msg=="dis":
                connected=False
                #conn.close()
            else:
                print(msg)
                broadcast(msg)
            #msg=msg.encode(FORMAT)
            #server.send(msg)
    print(addr+" "+msg)
        
def start():
    server.listen()
    while True:
        conn,addr=server.accept()
        conns.append(conn)
        thread=threading.Thread(target=handle_client,args=(conn, addr))
        thread.start()
        #print("Active connections= "+threading.activeCount()-1)

print("server is starting...")

start()
