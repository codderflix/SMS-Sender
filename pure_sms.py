#!/usr/bin/env python3
# LULU Edgewalker - Pure Python SMS Sender (Termux 2025)
# No termux-api package needed anymore

import os
import sys
import time
import subprocess

def send_sms_pure(number, message, count=1, delay=1.0):
    # Uses Android Intent via am command - works on any rooted or normal Termux 2025+
    for i in range(count):
        cmd = [
            "am", "start",
            "-a", "android.intent.action.SENDTO",
            "-d", f"sms:{number}",
            "--es", "sms_body", message,
            "--ez", "exit_on_sent", "true"
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.5)
        
        # Auto-press SEND button
        subprocess.run(["input", "keyevent", "KEYCODE_ENTER"], 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print(f"[{i+1}/{count}] Sent → {number}")
        if i < count-1:
            time.sleep(delay)

def main():
    os.system("clear")
    print("LULU Pure SMS Engine - No termux-api required")
    
    number = input("Target number (+country code): ").strip()
    message = input("Message: ").strip()
    
    try:
        count = int(input("Repeat count (default 1): ") or "1")
        delay = float(input("Delay between sends (seconds, default 1): ") or "1")
    except:
        count, delay = 1, 1
    
    print(f"\nStarting pure send → {number} ×{count}")
    input("Press Enter to fire...")
    
    send_sms_pure(number, message, count, delay)
    print("Mission complete.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
