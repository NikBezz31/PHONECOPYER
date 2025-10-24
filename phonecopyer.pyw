import time
import requests
import sys

try:
    import pyperclip
except ImportError:
    sys.exit("Установи pyperclip: pip install pyperclip")

URL_BASE = "https://trigger.macrodroid.com/ЗАМЕНИТЬ НА СВОЙ ID КОТОРЫЙ В MD/copyerpc?clipboard="

# при запуске просто запоминаем текущее содержимое, но не отправляем
last_text = pyperclip.paste()

print("Скрипт запущен. Скопируй что-нибудь — он отправит GET с этим текстом (без изменений).\n")

while True:
    try:
        text = pyperclip.paste()
        if text != last_text and text != "":
            # собираем URL без дополнительных замен/кодирования
            url = URL_BASE + text
            try:
                r = requests.get(url, timeout=5)
                print(
                    f"[OK] {time.strftime('%H:%M:%S')} отправил {len(text)} символов.\n"
                    f"     URL: {url}\n"
                    f"     HTTP статус: {r.status_code}\n"
                )
            except Exception as e:
                print(f"[ERR] Ошибка отправки GET: {e}\n     URL: {url}")
            last_text = text
    except Exception as e:
        print(f"[ERR] Ошибка чтения буфера: {e}")
    time.sleep(0.5)
