import socket
import threading
from sys import exit
# multi-threaded TCP server
import time
import signal

 


bind_ip = "127.0.0.1"
bind_port = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))

server.listen(5) #max backlog connections set to 5

print("[*] Listening on %s:%d" % (bind_ip,bind_port))

def handle_client(client_socket):
 
    request = client_socket.recv(1024)

    print("[*] Recieved: %s" % request)

    client_socket.send(b"ACK!")
    print(client_socket.getpeername())
    client_socket.close()

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)
 
signal.signal(signal.SIGINT, handler)        

while True:
    client, addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()


