from colorama import init, Fore, Back, Style
import sys, os, time, platform, psutil, random, string, ctypes
from os import system, name
from bs4 import BeautifulSoup as BS
import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
btcpric = response.json()

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()

time.sleep(1.2)
print("")
time.sleep(0.07)
print(Fore.CYAN + "                                    ╔════════════╗                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ║────────────║                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ║─╦╩╩═╩╩══╗──║                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ║─╣─╔═══╗─║──║                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ║─║─╚═══╝─╚╗─║                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ║─║─╔════╗─║─║                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ║─╣─╚════╝─║─║                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ║─╩╦╦═╦╦═══╝─║                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ║────────────║                       ")
time.sleep(0.07)
print(Fore.CYAN + "                                    ╚════════════╝                       ")
time.sleep(0.07)

welcome = Fore.CYAN + "\n                                    Feeling lucky?"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.4)

version = Fore.CYAN + "\n                                    EASYMONEY V1.2"
for char in version:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.4)

btcprice = Fore.CYAN + "\n                                    BTC PRICE:" + btcpric["bpi"]["USD"]["rate"] + " USD" + "\n"
for char in btcprice:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1)

def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_pswd = ''.join(random.choice(letters) for i in range(8))
    print(Fore.WHITE + "[" + Fore.CYAN + "EASYMONEY" + Fore.WHITE + "]" + Fore.CYAN +"  WALLET: " + Fore.WHITE + Fore.LIGHTRED_EX + result_str + Fore.CYAN + " | "  + Fore.CYAN +"PASSWORD: " + Fore.WHITE + Fore.LIGHTRED_EX + result_pswd )

def get_random_password(length):
    letters = string.ascii_uppercase + string.digits
    result_pass = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.CYAN + "EASYMONEY" + Fore.WHITE + "]" + Fore.CYAN +"  WALLET: " + Fore.WHITE + Fore.LIGHTGREEN_EX + "4CP1G5J1SSFUKI1294LZ043SB6QXOQV8ZQG" + Fore.CYAN + " | "  + Fore.CYAN +"PASSWORD: " + Fore.WHITE + Fore.LIGHTRED_EX + result_pass )


def btc_logo():
    print("")
    print(Fore.CYAN + "                                    ╔════════════╗                       ")
    print(Fore.CYAN + "                                    ║────────────║                       ")
    print(Fore.CYAN + "                                    ║─╦╩╩═╩╩══╗──║                       ")
    print(Fore.CYAN + "                                    ║─╣─╔═══╗─║──║                       ")
    print(Fore.CYAN + "                                    ║─║─╚═══╝─╚╗─║                       ")
    print(Fore.CYAN + "                                    ║─║─╔════╗─║─║                       ")
    print(Fore.CYAN + "                                    ║─╣─╚════╝─║─║                       ")
    print(Fore.CYAN + "                                    ║─╩╦╦═╦╦═══╝─║                       ")
    print(Fore.CYAN + "                                    ║────────────║                       ")  
    print(Fore.CYAN + "                                    ╚════════════╝                       ")
    print(Fore.CYAN + "\n                                    Feeling lucky?")
    print(Fore.CYAN + "                                    EASYMONEY V1.2")
    print(Fore.CYAN + "                                    BTC PRICE:" + btcpric["bpi"]["USD"]["rate"] + " USD" + "")
    print("")

print("\n                                    Start now? y/n")
Start = input(Fore.GREEN + ">>> " + Fore.MAGENTA)
if Start == ("y"):
    print(Fore.CYAN + "Starting...")
    time.sleep(1.5)
    clear()
    btc_logo()
    for i in range(100):
        get_random_string(35)
        time.sleep(0.1)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    get_random_password(8)
    time.sleep(1.2)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")    
    for i in range(100):
        get_random_password(8)
        time.sleep(0.1)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        
elif Start == ("n"):
    print(Fore.CYAN + "Bye...")
    time.sleep(1)
    print(Fore.RESET)
    exit()
else:
    print(Fore.CYAN + "Wrong answer, closing...")
    time.sleep(1)
    print(Fore.RESET)
    exit()

print(Fore.WHITE + "[" + Fore.CYAN + "EASYMONEY" + Fore.WHITE + "]" + Fore.CYAN +"  WALLET: " + Fore.WHITE + Fore.LIGHTGREEN_EX + "4CP1G5J1SSFUKI1294LZ043SB6QXOQV8ZQG" + Fore.CYAN + " | "  + Fore.CYAN +"PASSWORD: " + Fore.WHITE + Fore.LIGHTGREEN_EX + "XJWSKIQL" )
time.sleep(1.3)
finish = Fore.WHITE + "[" + Fore.CYAN + "EASYMONEY" + Fore.WHITE + "]" + Fore.CYAN +"  BALANCE: " + Fore.LIGHTGREEN_EX + "1.24BTC"
for char in finish:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

fintwo = Fore.WHITE + "\n[" + Fore.CYAN + "EASYMONEY" + Fore.WHITE + "]" + Fore.CYAN +"  SAVING IN:" + Fore.WHITE + " WALLET.TXT"
for char in fintwo:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

finthree = Fore.WHITE + "\n[" + Fore.CYAN + "EASYMONEY" + Fore.WHITE + "]" + Fore.CYAN + "  Closing... "
for char in finthree:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

finfour = Fore.WHITE + "\n[" + Fore.CYAN + "EASYMONEY" + Fore.WHITE + "]" + Fore.CYAN + "  Have a nice day! "
for char in finfour:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)
print(Fore.RESET)
time.sleep(1.5)
