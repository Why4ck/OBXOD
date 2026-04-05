# panel
import sys
from colorama import Fore, Style, init
init()

def clear_txt():
    with open('zp.txt', encoding='utf-8') as f:
        data = f.read()
    while True:
        a = input("Want to clear txt [y/n]: ")
        if a == 'y':
            with open('zp.txt',mode="w", encoding='utf-8') as f:
                pass # mode='w' -> file now clear!
            print(Fore.CYAN, "Txt was clear", Style.RESET_ALL, sep="")
            break
        elif a == 'n':
            break

def read_txt():
    with open('zp.txt', encoding='utf-8') as f:
        data = f.read()
        print(data)