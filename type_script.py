#!/usr/bin/env python3
import time
import pyautogui

def type_string(text, delay=0.005):
    """
    Types a string character by character with a delay between each keystroke.
    
    Args:
        text: The string to type
        delay: Delay in seconds between keystrokes (default: 0.005 seconds)
    """
    time.sleep(5)  # Initial 5-second delay to switch to target window before typing starts
    
    for char in text:
        pyautogui.typewrite(char, interval=delay)

if __name__ == "__main__":
    # Read text from input.txt file and type it out
    with open("input.txt", "r") as f:
        text_to_type = f.read().strip()
    
    # Type the text with 500ms delay between each character
    type_string(text_to_type)
