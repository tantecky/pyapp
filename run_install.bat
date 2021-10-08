@echo off
call venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
python.exe -m pip install pyside6
python.exe setup.py develop
python.exe -m pip install -e .[dev]