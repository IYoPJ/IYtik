import requests
import json
import time
from colorama import Fore,init
from time import sleep
import random
import random
import os
import random
import string
import itertools
import threading
import time
import sys
 
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rReady to spam!     ')
 
t = threading.Thread(target=animate)
 

 
typeU = 4
length = 1000
file = open('user.txt', 'w')
 
if typeU == 4:
  user = string.ascii_lowercase + string.digits
  le = 1
  while le < length:
    file.write(''.join(random.choice(user) for i in range(4))+'\r\n')
    le += 1
elif typeU == 3:
  user = string.ascii_lowercase + string.digits
  le = 1
  while le < length:
    file.write(''.join(random.choice(user) for i in range(3))+'\r\n')
    le += 1
elif typeU == 2:
  user = string.ascii_lowercase + string.digits
  le = 1
  while le < length:
    file.write(''.join(random.choice(user) for i in range(2))+'\r\n')
    le += 1
file.close()


count=0

print('''

	▀▀█▀▀ 　 ▀█▀ 　 ░█─▄▀ 　 ▀█▀ 　 ░█──░█ 
	─░█── 　 ░█─ 　 ░█▀▄─ 　 ░█─ 　 ░█▄▄▄█ 
	─░█── 　 ▄█▄ 　 ░█─░█ 　 ▄█▄ 　 ──░█──
''')

tok = '1416784792:AAHKAhWBkJx0OV6wScDAqdjZL9-VpJCFfVs'
r = requests.session()
print('''
==========================================
                 
            Hunter bot @IYhunter
                       
''')
time.sleep(2)
falah = input('Press Enter To Start')
print('')

if falah =="1"or " ":
    dd = 'user.txt'
    sessionId = '90fd7b65bcab96c4e44affc1baf91a04'
    myID = input('Tele ID : ')
    if dd =="1"or " ":
        dd="user.txt"
        password = open(dd).read().splitlines()

        # Back up one character, print a space to erase the spinner, then a newline
        # so that the prompt after the program exits isn't on the same line as our
        # message


        for password in password:
              url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+password+"&app_language=ar"
              payload = ""
              headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


        }
              cookies = {'sessionid': sessionId}
              response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
              post = str (response.json ()["status_msg"])
              if post==""or"":
                  count += 1
                  print("[+] {}".format(password.strip())+" --> Available ")
                  Account = (f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={myID}&text=𝙸𝚈𝙷𝚞𝚗𝚝𝚎𝚛 ♫ \n☘︎︎-----------------☘︎︎\n𝙽𝚎𝚠 𝚃𝚒𝚔𝚃𝚘𝚔 𝚄𝚜𝚎𝚛 ✍︎︎ \n☘︎︎-----------------☘︎︎\nꕥ 𝚄𝚜𝚎𝚛 : {password}\nꕥ 𝚃𝚎𝚕𝚎 : @IYoPJ\nꕥ 𝙱𝚘𝚝 : @IYhunterbot\n☘︎︎-----------------☘︎')
                  r.get(Account)
              else:
                  count += 1
                  print("[*] {}".format(password.strip())+" --> Not Available  ")
#24717ebecdb839b489d786e784e8a4ec
#for i in password:
