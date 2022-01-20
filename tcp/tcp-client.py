import socket 

tagret_host = '127.0.0.1'
tagret_port = 9090
try:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating the socket object
    # AF_INET => IPv4 adress or hostname
    # SOCK_STREAM => TCP client
    client.connect((tagret_host,tagret_port)) # connecting the client
    print(client)
    client.send(b"GET / HTTP1.1\r\nHost: 0.0.0.0\r\n\r\n")
    response = client.recv(1024)
except KeyboardInterrupt :
    print('goodbye')

client.close()

print(response)