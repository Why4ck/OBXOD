import ctypes
from elevate import elevate
import sys
from pathlib import Path
import launcher
import time


if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    elevate(show_console=True, graphical=False)
    sys.exit(0)


try:
    with open('zp.txt', encoding='utf-8') as f:
        data = f.read().strip()
        print(data)
except FileNotFoundError:
    data = ""


if data == "":
    zp = input("Zapret path: ")
    
    # Правильно: открываем на запись отдельно
    with open('zp.txt', 'w', encoding='utf-8') as f:
        f.write(zp)
    
else:
    zp = data

main = launcher.Launcher(Path(zp))

main.run_zapret()
time.sleep(2)
main.run_warp()

while True:
    time.sleep(1)