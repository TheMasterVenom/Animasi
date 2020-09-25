import os,sys,random,string,time


p = '\x1b[1;97m'
m = '\x1b[1;91m'
b = '\x1b[1;93m'
h = '\033[1;92m'

def muat():
    m = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
    print
    for oppai in m:
        sys.stdout.write('\r['+oppai+'% Working]')
        sys.stdout.flush()
        time.sleep(0.1)
    akbar()

def akbar():
	list = ['\x1b[1;91m', '\x1b[30;1m']
	while True:
		warna = random.choice(list)
		try:
			os.system("clear")
			print "              By TheMasterVenom_1St ~ Akbar Nasuha\n"
			print (p+""+b+"           [-] You have come out of this sad word [-] ")
			sys.stdout.write(warna + "\r                  error . error . error . error					")
			print (p+""+b+"            [-] You have come out of this sad word [-] ")
			sys.stdout.write(warna + "\r                  error . error . error . error					")
			print (p+""+b+"            [-] You have come out of this sad word [-] ")
			sys.stdout.write(warna + "\r                  error . error . error . error					")
			print(p+""+b+"            [-] You have come out of this sad word [-] ")
			time.sleep(0.09)
			sys.stdout.flush()
			akbar()
		except KeyboardInterrupt:
			exit()

def mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)

def terminal():
        os.system('clear')
        print '               By TheMasterVenom_1St|4kb4rn4suh4 \n'
        mengetik(p+""+b+"root@terminal: ~# "+p+"love")
        mengetik(p+""+h+"~bash: "+p+"love : "+m+"command not found")
        mengetik(p+""+b+"root@terminal: ~# "+p+"happyness")
        mengetik(p+""+h+"~bash: "+p+"happyness : "+m+"command not found")
        mengetik(p+""+b+"root@terminal: ~# "+p+"kill")
        mengetik(p+""+p+"Do you Want To Kill (Y/N): "+p+"N")
        mengetik(p+""+b+"root@terminal: ~# "+p+"exit")
        muat()#terserah mau pake yang ini apa yang lain
        titik = ['10% Working]', '20% Working]', '30% Working]', '40% Working]', '50% Working]', '60% Working]', '70% Working]', '80% Working]', '90% Working]', '100% Working]','Process completed-press Enter]']
        for o in titik:
		print '\r[' + o,
		sys.stdout.flush()
		time.sleep(1)

terminal()
