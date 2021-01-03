import socket
HEADER=64
PORT=12345
FORMAT='utf-8'
DISCONNECT="!closing connection [DISCONNECT]"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER, PORT))
def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))

send('Hello World ')
input()
send('Ghanshyam S Nair')
input()
send(DISCONNECT)