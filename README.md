# Typer

A simple Python script that types text from a file character by character with a 500ms delay between each keystroke.

## Features

- Reads text from `input.txt` file
- Types text to the currently focused window
- 500ms delay between each keystroke for slow/deliberate typing
- 5-second initial delay to allow switching to target window

## Requirements

- Python 3
- X11 display (Linux with GUI)
- System dependencies: `python3-tk` and `python3-dev`

## Installation

1. Install system dependencies:
```bash
sudo apt-get install python3-tk python3-dev
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Create or edit `input.txt` with the text you want to type
2. Run the script:
```bash
python3 type_script.py
```
3. Quickly click on the window/field where you want text typed (you have 5 seconds)

## Wayland/Display Permissions

If using Wayland or experiencing display/input permission issues:

1. Ensure X11 access is allowed:
```bash
xhost +local:
```

2. Set DISPLAY variable if needed:
```bash
export DISPLAY=:0
python3 type_script.py
```

3. For Wayland systems, you may need to run the script with proper permissions or switch to X11 session temporarily.

## Troubleshooting

If you get `DisplayConnectionError`, run:
```bash
xhost +local:
python3 type_script.py
```

If `pyautogui` module is not found when using `sudo`, use the venv's Python:
```bash
venv/bin/python3 type_script.py
```

If permission errors occur with keyboard/mouse input, ensure your user is in the correct groups:
```bash
sudo usermod -a -G input $USER
```
Then log out and back in.
