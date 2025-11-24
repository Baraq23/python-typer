# Typer

A simple Python automation tool that reads text from a file and types it into any focused window with a 500ms delay between each keystroke.

## Features

- Reads text from `input.txt` file
- Types text to the currently focused window character by character
- Configurable 500ms delay between each keystroke
- 5-second initial delay before typing begins (time to switch to target window)
- Easy automation with Makefile commands
- Works with X11 display systems

## Requirements

- Python 3
- X11 display (Linux with GUI)
- System dependencies: `python3-tk` and `python3-dev`

## Installation

1. Install system dependencies:
```bash
sudo apt-get install python3-tk python3-dev
```

2. Install project dependencies using Makefile:
```bash
make install
```

**Or manually:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Create or edit `input.txt` with the text you want to type
2. Run the script using Makefile:
```bash
make run
```

**Or manually:**
```bash
source venv/bin/activate
python3 type_script.py
```

3. Quickly click on the window/field where you want text typed (you have 5 seconds)

## Makefile Commands

- `make install` - Install dependencies and set up virtual environment
- `make run` - Run the typing script (automatically handles X11 permissions)
- `make clean` - Remove virtual environment
- `make venv` - Create virtual environment only
- `make help` - Show available commands

## Troubleshooting

If `pyautogui` module is not found when using `sudo`, use the venv's Python:
```bash
venv/bin/python3 type_script.py
```

If permission errors occur with keyboard/mouse input, ensure your user is in the correct groups:
```bash
sudo usermod -a -G input $USER
```
Then log out and back in.
