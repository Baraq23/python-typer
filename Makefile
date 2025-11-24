.PHONY: help install venv run clean

help:
	@echo "Typer - Usage:"
	@echo "  make install    - Install dependencies and set up virtual environment"
	@echo "  make run        - Run the typing script"
	@echo "  make clean      - Remove virtual environment"
	@echo "  make venv       - Create virtual environment only"

venv:
	python3 -m venv venv

install: venv
	. venv/bin/activate && pip install -r requirements.txt
	@echo "Installation complete. Run 'make run' to start."

run:
	@xhost +local: 2>/dev/null || true
	. venv/bin/activate && python3 type_script.py

clean:
	rm -rf venv
	@echo "Virtual environment removed."
