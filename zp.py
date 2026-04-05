import shutil
import os
import sys
from pathlib import Path

def get_base_path():
    """Возвращает путь к папке, где лежат файлы (работает в .exe и без)"""
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    else:
        return os.path.abspath(".")


def __extract():
    base_path = get_base_path()
    zip_path = os.path.join(base_path, "zapret.zip")
    
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Файл zapret.zip не найден! Путь: {zip_path}")

    extract_path = os.path.join(base_path, "zapret")

    if os.path.exists(extract_path):
        shutil.rmtree(extract_path, ignore_errors=True)
    shutil.unpack_archive(zip_path, extract_path)
    
    files = os.listdir(extract_path)
    if not files:
        raise FileNotFoundError("В zapret.zip ничего не найдено!")
    
    zp_path = Path(os.path.join(extract_path, files[0]))
    return zp_path


def read():
    base_path = get_base_path()
    zapret_folder = os.path.join(base_path, "zapret")
    
    if os.path.exists(zapret_folder):
        zz = os.listdir(zapret_folder)
        for item in zz:
            if "zapret" in item.lower():
                path = Path(os.path.join(zapret_folder, item))
                return path
    
    path_2 = __extract()
    return path_2