import ctypes
from elevate import elevate
import sys
from pathlib import Path
import launcher
import panel
import time
import subprocess
from colorama import init, Fore, Style; init()

if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    elevate(show_console=True, graphical=False)
    sys.exit(0)


name_title = f"""{Fore.GREEN}
 █     █░ ██░ ██▓██   ██▓ ▄████▄   ██ ▄█▀    ▒█████   ▄▄▄▄   ▒██   ██▒ ▒█████  ▓█████▄ 
▓█░ █ ░█░▓██░ ██▒▒██  ██▒▒██▀ ▀█   ██▄█▒    ▒██▒  ██▒▓█████▄ ▒▒ █ █ ▒░▒██▒  ██▒▒██▀ ██▌
▒█░ █ ░█ ▒██▀▀██░ ▒██ ██░▒▓█    ▄ ▓███▄░    ▒██░  ██▒▒██▒ ▄██░░  █   ░▒██░  ██▒░██   █▌
░█░ █ ░█ ░▓█ ░██  ░ ▐██▓░▒▓▓▄ ▄██▒▓██ █▄    ▒██   ██░▒██░█▀   ░ █ █ ▒ ▒██   ██░░▓█▄   ▌
░░██▒██▓ ░▓█▒░██▓ ░ ██▒▓░▒ ▓███▀ ░▒██▒ █▄   ░ ████▓▒░░▓█  ▀█▓▒██▒ ▒██▒░ ████▓▒░░▒████▓ 
░ ▓░▒ ▒   ▒ ░░▒░▒  ██▒▒▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░ ▒░▒░▒░ ░▒▓███▀▒▒▒ ░ ░▓ ░░ ▒░▒░▒░  ▒▒▓  ▒ 
  ▒ ░ ░   ▒ ░▒░ ░▓██ ░▒░   ░  ▒   ░ ░▒ ▒░     ░ ▒ ▒░ ▒░▒   ░ ░░   ░▒ ░  ░ ▒ ▒░  ░ ▒  ▒ 
  ░   ░   ░  ░░ ░▒ ▒ ░░  ░        ░ ░░ ░    ░ ░ ░ ▒   ░    ░  ░    ░  ░ ░ ░ ▒   ░ ░  ░ 
    ░     ░  ░  ░░ ░     ░ ░      ░  ░          ░ ░   ░       ░    ░      ░ ░     ░    
                 ░ ░     ░                                 ░                    ░      

Why4ck OBXOD
Github: >>> https://github.com/why4ck <<<
{Style.RESET_ALL}"""

print(name_title)

s = "Menu"
print(f"{Fore.RED}{s:.^86}{Style.RESET_ALL}", end="\n\n")

menu = """
OBXOD                  PANEL
[1] Turn on            [4] Clear zapret path (zp.txt)
[2] Turn off           [5] Close programm
[3] Check service
"""
print(Fore.CYAN, menu, Style.RESET_ALL, sep="", end='')


zp = ""
def zappret():
    global zp
    try:
        with open('zp.txt', encoding='utf-8') as f:
            data = f.read().strip()

    except FileNotFoundError:
        data = ""



    if data == "":
        zp = input("(zapret by FLOWSEAL)Zapret path: ")
        
        with open('zp.txt', 'w', encoding='utf-8') as f:
            f.write(zp)

    else:
        zp = data
    
    zp = Path(zp)

zappret()


main = launcher.Launcher(zp)

while True:
    try:
            inp = int(input(": "))
            
            
            if inp == 1:
                if main.check_warp_account():
                    main.run_zapret()
                    time.sleep(3)
                    main.run_warp()
                    print(Fore.GREEN, "OBXOD turned up", Style.RESET_ALL, sep='')
                else:
                    print(Fore.RED, "Failed to setup WARP account", Style.RESET_ALL, sep='')

            
            elif inp == 2:
                main.kill(kill_yn=True)
                print(Fore.GREEN, "OBXOD turned off", Style.RESET_ALL, sep='')

            
            elif inp == 3:
                main.check_warp()
                main.check_zapret()
                print(Fore.GREEN, "OBXOD was checked", Style.RESET_ALL, sep='')

            
            elif inp == 4:
                panel.clear_txt()
                zappret()
                main = launcher.Launcher(zp)
            
            elif inp == 5:
                print("Bye")
                main.kill(True)
                time.sleep(1)
                break

            
            else:
                print(Fore.GREEN, "uncorrect number", Style.RESET_ALL, sep="")
    except:
        print(Fore.RED, "Uncorrect number", Style.RESET_ALL, sep="")
