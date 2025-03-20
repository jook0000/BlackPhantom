#!/usr/bin/env python3
import sys
import subprocess
from termcolor import colored

# List of required libraries
REQUIRED_LIBRARIES = [
    "requests",
    "pyfiglet",
    "termcolor",
    "sys",
    "os",
    "subprocess",
    "termcolor"
]

def check_and_install_libraries():
    missing_libs = []
    
    # Check installed libraries
    for lib in REQUIRED_LIBRARIES:
        try:
            __import__(lib)
        except ImportError:
            missing_libs.append(lib)
    
    # Install missing libraries
    if missing_libs:
        print(colored("[!] Installing required libraries...", "yellow"))
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_libs])
            print(colored("[✓] Installation successful!", "green"))
        except Exception as e:
            print(colored(f"[X] Installation failed: {e}", "red"))
            sys.exit(1)

def run_main_script():
    try:
        # Run main tool
        print(colored("\n[+] Starting the tool...", "cyan"))
        subprocess.check_call([sys.executable, "BlackPhantom.py"])
    except FileNotFoundError:
        print(colored("[X] Main tool file not found!", "red"))
    except Exception as e:
        print(colored(f"[X] Unexpected error: {e}", "red"))

if __name__ == "__main__":
    check_and_install_libraries()
    run_main_script()
