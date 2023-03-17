from colorama import Fore as f
from datetime import datetime
import os; os.system("cls")
import time, base64, string, random, threading
from decimal import Decimal

def random_string(length, numbers=False):
    defualt = string.ascii_lowercase+string.ascii_uppercase
    if numbers:
        defualt+string.digits
    return ''.join(random.sample(defualt,length))

def real_token():
    return base64.b64encode(
        str(round(Decimal(time.time()*1000-1420070400000)*4194304)).
        encode()).decode()[:-5]+f"***.{random_string(length=7)}.{random_string(length=3, numbers=True)}"

def make_token():
    while True:
        log(f"{f.LIGHTBLACK_EX}Captcha Solved !  {f.LIGHTWHITE_EX}| {str(round(random.uniform(2, 10),2))}s")
        time.sleep(random.uniform(0, 1))
        log(f"[{f.LIGHTGREEN_EX}U] {real_token()}")
        time.sleep(0.1)

def log(obj):
    clock=datetime.now().strftime(f"%H:%M:%S")
    print(f'[{f.LIGHTBLACK_EX}{clock}] {obj}'
          .replace("]",f"{f.LIGHTWHITE_EX}]"))

for x in range(60):
    threading.Thread(target=make_token).start()