import socket
import threading
HEADER=64
PORT=12345
FORMAT='utf-8'
DISCONNECT="!closing connection [DISCONNECT]"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER, PORT))

def handle_client(conn,addr):
    print(f"[NEW CONNECTION]{addr}connected")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT:
                connected=False

            print(f"[{addr}{msg}]")
            conn.send("Message recieved".encode(FORMAT))

def start():
    server.listen()
    print(f"[LISTENING ] Server is listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        print(f"[Connection]{conn},[ADress]{addr}")
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count()-1}")

print("[STARTING ] server is starting")
start()