import os
import sys
from pathlib import Path

def get_base_path():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.abspath(".")

def read():
    base_path = get_base_path()
    # Папка zapret уже будет внутри EXE, ее не надо распаковывать!
    zapret_folder = os.path.join(base_path, "zapret")
    
    if not os.path.exists(zapret_folder):
        raise FileNotFoundError(f"Папка zapret не найдена внутри EXE! Путь: {zapret_folder}")
    
    # Если внутри папки zapret есть еще одна подпапка zapret 
    # (как бывает при кривой архивации) - заходим в нее
    zz = os.listdir(zapret_folder)
    for item in zz:
        if "zapret" in item.lower() and os.path.isdir(os.path.join(zapret_folder, item)):
            return Path(os.path.join(zapret_folder, item))
    
    return Path(zapret_folder)