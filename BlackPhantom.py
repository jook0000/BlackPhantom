import os
import sys 
import requests
from socks import SOCKS5, ProxyError
from socket import timeout
from pyfiglet import Figlet
import subprocess
from termcolor import colored

# ----- Banner -----
def banner():
    try:
        custom_fig = Figlet(font='big', width=100)
        ascii_art = custom_fig.renderText('BlackPhantom')
        print(colored(ascii_art, 'red', attrs=['bold']))
    except:
        print(colored('''
  ██████╗ ██╗      █████╗  ██████╗██╗  ██╗██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 ██╔════╝ ██║     ██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 ██║  ███╗██║     ███████║██║     █████╔╝ ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 ██║   ██║██║     ██╔══██║██║     ██╔═██╗ ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 ╚██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
        ''', 'red'))

# ----- Root Check -----
def check_root():
    if os.getuid() != 0:
        print(colored("Error: Run as root!", "red"))
        sys.exit(1)

# ----- Tor Check -----
def check_tor():
    try:
        session = requests.Session()
        session.proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
        response = session.get("https://check.torproject.org", timeout=10)
        if "Congratulations" in response.text:
            print(colored("[✓] Tor Active", "green"))
            return True
        else:
            print(colored("[X] Tor Not Detected", "red"))
            return False
    except (ProxyError, timeout, requests.ConnectionError):
        print(colored("[X] Tor Connection Failed", "red"))
        return False

# ----- Main Menu -----
def main_menu():
    print(colored("\n[1] Social Media Attack", "cyan"))
    print(colored("[2] Password List Manager", "yellow"))
    print(colored("[3] Change Tor Identity", "magenta"))
    print(colored("[0] Exit", "red"))
    return input(colored("Select Option: ", "green"))

# ----- Social Media Menu -----
def social_media_menu():
    print(colored("\n[1] Instagram", "magenta"))
    print(colored("[2] Facebook", "blue"))
    print(colored("[3] TikTok", "red"))
    print(colored("[0] Back", "yellow"))
    return input(colored("Select Platform: ", "green"))

# ----- Main Execution -----
if __name__ == "__main__":
    banner()
    check_root()
    
    if not check_tor():
        sys.exit(1)
        
    while True:
        user_choice = main_menu()
        
        if user_choice == "1":
            while True:
                platform = social_media_menu()
                if platform == "1":
                    target = input(colored("Instagram Username: ", "cyan"))
                    print(colored(f"Attacking: @{target}", "magenta"))
                elif platform == "2":
                    target = input(colored("Facebook Profile URL: ", "cyan"))
                    print(colored(f"Attacking: {target}", "blue"))
                elif platform == "3":
                    target = input(colored("TikTok Username: ", "cyan"))
                    print(colored(f"Attacking: @{target}", "red"))
                elif platform == "0":
                    break
                else:
                    print(colored("Invalid Choice!", "red"))
        
        elif user_choice == "3":
            print(colored("\nChanging Tor Identity...", "magenta")) # Placeholder
            
        elif user_choice == "0":
            print(colored("Exiting...", "red"))
            sys.exit(0)
