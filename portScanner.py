import sys
import socket
from datetime import datetime
import threading


def port_scanner(target,ports):
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)
    print()
    
    socket.setdefaulttimeout(1)
    
    for port in ports:
        t = threading.Thread(target=connection_scan,args=(target,int(port)))
        t.start()
        
        
def connection_scan(target, port):
    screen_lock = threading.Semaphore()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((target,port))
            s.send(b'Hello\r\n')
            results = s.recv(100).decode('utf-8')
            screen_lock.acquire()
            print(f'[+] {port}/tcp open')
        except OSError:
            screen_lock.acquire()
            print(f'[-] {port}/tcp closed')
        finally:
            screen_lock.release()
            
    