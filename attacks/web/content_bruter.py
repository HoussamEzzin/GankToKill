# this is a spider that crawls
# the target website in order to discover as much
# of the web app as possible
import os
import queue
import threading
import urllib.error
import urllib.parse
import urllib.request
import socket

threads = 50
resume = None
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0)" \
             "Gecko/20100101" \
             "Firefox/94.0" 

def build_wordlist(wordlist_file):
    file_wordlist = open(wordlist_file, "r")
    raw_words = [line.rstrip('\n') for line in file_wordlist]
    file_wordlist.close()

    found_resume = False
    words = queue.Queue()
    
    for word in raw_words:
        if resume:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print("Resuming wordlist from : %s" % resume)
        else:
            words.put(word)
    return words


def dir_bruter(word_queue,target_url,extensions=None):
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        
        #check for file or directory
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s" % attempt)
        
        #brute force extensions
        if extensions:
            for extension in extensions:
                attempt_list.append("/%s%s" % (attempt,extension))
        
        for brute in attempt_list:
            # target url will be given from input in main.py
            url = "%s%s" % (target_url, urllib.parse.quote(brute))
            try:
                headers = {'User-Agent': user_agent}
                r = urllib.request.Request(url, headers=headers)
                response = urllib.request.urlopen(r)
                if len(response.read()):
                    print("[%d] => %s" % (response.code, url))
            except urllib.error.HTTPError as e:
                if e.code != 404:
                    print("!!! %d => %s " % (e.code,url))
                pass
            except KeyboardInterrupt:
                os.exit()

def content_bruter(wordlist_file,target_url):
    word_queue = build_wordlist(wordlist_file)
    file_extensions = ['.php','.bak','.orig','.inc']

    
    for i in range(threads):
        t = threading.Thread(target=dir_bruter, args=(word_queue,target_url,file_extensions,))
        t.start()
                    
