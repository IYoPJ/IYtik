import os
import time
import requests
import sys as n
import time as mm
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
os.system('pip install os')
os.system('pip install sys')
os.system('pip install time')
os.system('pip install requests')
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 30)
		
		
green_color = "\033[1;93m"
C = "\033[0m"
W = "\033[96m"
BRed="\033[1;31m"
Green="\033[0;36m"
Yellow="\033[0;33m"

print(green_color+"""
		  Ｔｅｌｏｋ
""")
print(green_color+"""
	 Press Start ~~> @IYhunterbot
""")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
time.sleep(2)
myID = input(BRed+" Tele id : ")
r = requests.session()
jok = 'user.txt'
headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
}

tok = ('1416784792:AAHKAhWBkJx0OV6wScDAqdjZL9-VpJCFfVs')
ok = """
〰️〰️〰️〰️〰️〰️〰️〰️
[•] USER TIKTOK 🥳👇🏻
〰️〰️〰️〰️〰️〰️〰️〰️"""
mon = """〰️〰️〰️〰️〰️〰️〰️〰️
[•] @vv1ck ( JOKER )
"""
file = open(jok, "r")
while True:
	Check = file.readline().split('\n')[0]
	tiklog = f'https://www.tiktok.com/@{Check}'
	rq = requests.get(tiklog, headers=headers)
	if rq.status_code == 404:
		print(green_color+"[+] {}".format(W+Check.strip())+Green+" --> Available  ")
		Account = (f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={myID}&text=𝙸𝚈𝙷𝚞𝚗𝚝𝚎𝚛 ♫ \n☘︎︎-----------------☘︎︎\n𝙽𝚎𝚠 𝚃𝚒𝚔𝚃𝚘𝚔 𝚄𝚜𝚎𝚛 ✍︎︎ \n☘︎︎-----------------☘︎︎\nꕥ 𝚄𝚜𝚎𝚛 : {Check}\nꕥ 𝚃𝚎𝚕𝚎 : @IYoPJ\nꕥ 𝙱𝚘𝚝 : @IYhunterbot\n☘︎︎-----------------☘︎')
		r.get(Account)
		
	elif rq.status_code == 200:
		print(green_color+"[*] {}".format(W+Check.strip())+Green+" --> Not Available  ")
		if (Check == ""):
			break
