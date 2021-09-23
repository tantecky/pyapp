# pyapp ![tests](https://github.com/tantecky/pyapp/actions/workflows/tests.yml/badge.svg)

## How to prepare dev environment on Windows

Install Python 3.8+ from [Anaconda](https://www.anaconda.com/products/individual), or download it [directly](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe).

```bat
python.exe -m venv venv
call venv/Scripts/activate.bat
python.exe -m pip install --upgrade pip
python.exe -m pip install -r requirements.txt
python.exe -m pip install -r requirements-dev.txt
```

Open `workspace.code-workspace` in [VS Code](https://code.visualstudio.com/)

Run `tox --recreate` if you modify `requirements*.txt`.

## Unit testing

Run `tox` in the root diretory.
