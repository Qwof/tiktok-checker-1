#Imports
import requests
from colorama import init, Fore
import time
import os
import ctypes

#Initializing colorama.
init()

#Code for checking...
def checking():
    while True:
        num = 0
        for username in usernames:
            c = requests.Session().get(f'https://www.tiktok.com/@{username}', headers={'Connection': 'keep-alive', 'User-Agent': 'TikTok 17.4.0 rv:174014 (iPhone; iOS 13.6.1; sv_SE) Cronet'}, timeout=60)
            if c.status_code == 404:
                num += 1
                print(f"{Fore.GREEN}[{Fore.WHITE}{num}{Fore.GREEN}] {Fore.GREEN}[{Fore.WHITE}AVALIBLE{Fore.GREEN}]{Fore.WHITE} {username}")
                ctypes.windll.kernel32.SetConsoleTitleW(f"Checked {num} usernames, press ctrl+c to exit.")
                with open('available.txt', "a") as x:
                    x.write(f"{username}"+"\n")
            elif c.status_code == 200 or 204:
                num += 1
                print(f"{Fore.RED}[{Fore.WHITE}{num}{Fore.RED}] [{Fore.WHITE}TAKEN{Fore.RED}] {Fore.WHITE} {username}")
            elif c.status_code == 429:
                print(f'{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Being rate limited, wait 30 seconds.')
                time.sleep(30)
                checking()
                return
            else:
                print(f'{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} Noone knows how we got here, but we are probably fucked.')
    
        print(f"{Fore.GREEN}[{Fore.WHITE}EVENT{Fore.GREEN}]{Fore.WHITE} Done checking usernames, usernames saved in 'generated.txt'")
        os.system("pause>nul")
        break

#Opening file with usernames in them.
with open('Generated.txt', 'r') as file:
    usernames = file.read().splitlines()
    if len(usernames) == 0:
        print(f'{Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.WHITE} No usernames found in "Generated.txt".')
    else:
        checking()
