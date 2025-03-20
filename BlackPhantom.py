import os
import sys 
import requests
from socks import SOCKS5, ProxyError
from socket import timeout
from pyfiglet import Figlet
import subprocess
from termcolor import colored

def banner():
    try:
        # إعداد الخط المتعرج الكبير مع ألوان داكنة
        custom_fig = Figlet(font='big', width=100)
        ascii_art = custom_fig.renderText('BlackPhantom')
        
        # تلوين النص (أحمر داكن)
        dark_red = "\033[38;5;124m"  # رمز لون أحمر داكن
        bold = "\033[1m"  # نص سميك
        reset = "\033[0m"
        
        print(f"{bold}{dark_red}")
        print(ascii_art)
        print(reset)
    
    except:
        # النسخة الإحتياطية الأكثر تفصيلاً
        print("\033[1;38;5;124m")  # أحمر داكن مع تأثير سميك
        print(r'''
  ██████╗ ██╗      █████╗  ██████╗██╗  ██╗██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 ██╔════╝ ██║     ██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 ██║  ███╗██║     ███████║██║     █████╔╝ ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 ██║   ██║██║     ██╔══██║██║     ██╔═██╗ ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 ╚██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
        ''')
        print("\033[0m")

if __name__ == "__main__":
    banner()

def check_root():
    if os.getuid() != 0:
        print("\033[91mError: not root!\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    check_root()

def check_tor():
    try:
        session = requests.Session()
        session.proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
        
        response = session.get("https://check.torproject.org/", timeout=10)
        
        if "Congratulations. This browser is configured to use Tor" in response.text:
            print("\033[92m[*] Tor connection active\033[0m")
            return True
        else:
            print("\033[91m[-] Not using Tor\033[0m")
            return False
            
    except (ProxyError, timeout, requests.exceptions.ConnectionError):
        print("\033[91m[-] Tor connection failed! Check if Tor is running\033[0m")
        return False
    except Exception as e:
        print("\033[91m[-] Error:", str(e), "\033[0m")
        return False

if __name__ == "__main__":
    if not check_tor():
        sys.exit(1)
    else:
        print("\033[94m[+] Proceeding with Tor anonymity...\033[0m")
