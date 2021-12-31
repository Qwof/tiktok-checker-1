#imports
import random, string, time, ctypes
from colorama import init, Fore

init()

#Opening file to save usernames in.
with open("Generated.txt","r+") as file:
    file.truncate(0)
    file.close()

#Code for generating.
def generating():
    num = 0
    while True:
        try:
            if onl.lower() == 'y':
                usr = random.choices(string.ascii_letters, k=len)
            else:
                usr = ''.join(random.choices(string.ascii_letters + string.digits, k=len))
            with open('Generated.txt', 'a+') as f:
                num += 1
                print(f"{Fore.RED}[{Fore.WHITE}{num}{Fore.RED}]{Fore.LIGHTBLACK_EX} {''.join(usr)}")
                f.write(''.join(usr)+'\n')
                ctypes.windll.kernel32.SetConsoleTitleW(f"Generated {num} Usernames, press ctrl+c to exit.")
                time.sleep(0.005)
        except KeyboardInterrupt:
            print(f"{Fore.RED}Exited.")
            break
            
#Setup.
onl = input("Only letters? (y/n) > ")
len = int(input("Length? > "))
generating()
