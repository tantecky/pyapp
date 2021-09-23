# pyapp

An example app in Python

## How to prepare dev environment on Windows

```bat
python.exe -m venv venv
call venv/Scripts/activate.bat
python.exe -m pip install --upgrade pip
python.exe -m pip install -r requirements.txt
python.exe -m pip install -r requirements-dev.txt
```

Open `workspace.code-workspace` in [VS Code](https://code.visualstudio.com/)

## Unit testing

Run `tox` in the root diretory.
