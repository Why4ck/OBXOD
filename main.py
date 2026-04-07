import sys
from pathlib import Path
import launcher
import panel
import time
import subprocess
import os
from colorama import init, Fore, Style; init()
import zp

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
OBXOD                  PANEL                               Other
[1] Turn on            [4] Only zapret (Game)              [7] Documentation
[2] Turn off           [5] Only warp (Not for Russia)
[3] Check service      [6] Close programm
"""
print(Fore.CYAN, menu, Style.RESET_ALL, sep="", end='')


zp_path = zp.read() # extracting zip and get path
main = launcher.Launcher(zp_path)
path_now = os.getcwd()

while True:
    try:
            inp = int(input(": "))
            
            
            if inp == 1:
                if main.check_warp_account():
                    main.run_zapret()
                    time.sleep(1)
                    main.run_warp()
                    print(Fore.GREEN, "OBXOD turned up", Style.RESET_ALL, sep='')
                else:
                    print(Fore.RED, "Failed to setup WARP account", Style.RESET_ALL, sep='')

            
            elif inp == 2:
                os.chdir(path_now)
                main.kill(kill_yn=True)
                print(Fore.GREEN, "OBXOD turned off", Style.RESET_ALL, sep='')

            
            elif inp == 3:
                os.chdir(path_now)
                main.check_warp()
                main.check_zapret()
                print(Fore.GREEN, "OBXOD was checked", Style.RESET_ALL, sep='')


            
            elif inp == 4:
                os.chdir(path_now)
                main.kill(True)
                main.run_zapret()
            
            elif inp == 5:
                os.chdir(path_now)
                main.kill(True)
                try:
                    main.run_warp()
                except Exception as e:
                    print(f'Error {e}')
                    main.kill()

            elif inp == 6:
                os.chdir(path_now)
                main.kill(True)
                sys.exit()
            
            elif inp == 7:
                os.chdir(path_now)
                with open('README.md', encoding='utf-8') as f:
                    print(Fore.GREEN, f.read(), Style.RESET_ALL)
                 
                
            else:
                print(Fore.GREEN, "uncorrect number", Style.RESET_ALL, sep="")
    except Exception as e:
        print(Fore.RED, f"Error: {e}", Style.RESET_ALL, sep="")
        main.kill(True)
        sys.exit()