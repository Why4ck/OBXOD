# 🚀 Why4ck_OBXOD

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

Утилита для удобного управления и обхода блокировок с использованием **Zapret** и **Cloudflare WARP (warp-cli)**. Скомпилировано с помощью **Nuitka** для максимальной производительности и мгновенного запуска.

---

## ✨ Особенности

* **⚡ Мгновенный старт:** Никаких ожиданий распаковки (в отличие от PyInstaller)
* **🛡️ Авто-админ:** Программа сама запрашивает права администратора при запуске (UAC)
* **🛠️ Все в одном:** Интеграция `Zapretq и `warp-cli` в одном интерфейсе
* **🧹 Чистота:** Быстрое завершение всех фоновых процессов одной командой

---

## 🚀 Как использовать (Для пользователей)

1.  Скачайте актуальный бинарник из [Releases](https://github.com/Why4ck/OBXOD/releases)
2.  Запустите `Why4ck_OBXOD.exe` от имени администратора
3.  Выберите нужный пункт меню:
    * `1` — Запуск обхода
    * `2` — Остановить все процессы
    * `3` — Проверить наличие warp и zapret
    * `4` — Перезапуск ТОЛЬКО Zapret
    * `5` — Перезапуск ТОЛЬКО WARP (НЕ ДЛЯ РФ!!!)
    * `6` — Закрыть программу (убьет процессы и закроет программу)
    * `7` — Документация

---



## 📂 Структура проекта

* `main.py` — Точка входа, логика меню и обработки команд
* `launcher.py` — Управление процессами (subprocess), запуск .bat файлов и warp-cli
* `zp.py` — Логика определения пути zapret
* `panel.py` — Утилиты для работы с логами и текстом
* `zapret/` — Папка с бинарниками и скриптами zapret

---

## Telegram
https://t.me/mcodeg - канал
https://t.me/why4ck - разработчик
```

---

## 🛠️ Разработка и сборка

Если вы хотите внести изменения в код или собрать проект самостоятельно:

### Требования
* Python 3.13+
* Установленный [Nuitka]

### Установка зависимостей
```bash
pip install -r requirements.txt
```
ИЛИ
```bash
pip install rich colorama
```

### Сборка через Nuitka
Для создания быстрого `.exe` файла используйте следующую команду:

```bash
python -m nuitka \
    --onefile \
    --standalone \
    --windows-uac-admin \
    --include-data-dir=zapret=zapret \
    --windows-icon-from-ico=your_icon.ico \
    --output-filename=Why4ck_OBXOD \
    main.py
```
