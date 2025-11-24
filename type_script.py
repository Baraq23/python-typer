#!/usr/bin/env python3
import time
import pyautogui

def type_string(text, delay=0.005):
    """
    Types a string character by character with a delay between each keystroke.
    
    Args:
        text: The string to type
        delay: Delay in seconds between keystrokes (default: 0.5)
    """
    time.sleep(10)  # Initial 10-second delay to switch to target window
    
    for char in text:
        pyautogui.typewrite(char, interval=delay)

if __name__ == "__main__":
    # Read text from input.txt
    with open("input.txt", "r") as f:
        text_to_type = f.read().strip()
    
    type_string(text_to_type)
