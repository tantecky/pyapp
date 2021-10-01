# pyapp ![tests](https://github.com/tantecky/pyapp/actions/workflows/tests.yml/badge.svg)

An example app in Python. It is using several tools for formatting/linting (`isort`, `black`, `flake8`, `mypy`). Unit testing is done through `pytest` with `coverage`. For CI [GitHub Actions](https://docs.github.com/en/actions) is employed.

## How to prepare dev environment on Windows

- Install [Python 3.8+](https://www.python.org/ftp/python/3.8.10/python-3.8) (e.g. to: `C:/Python38`). Do NOT use `python.exe` from [Anaconda](https://www.anaconda.com/products/individual).

- Clone this repo (`git clone https://github.com/tantecky/pyapp.git`).

- Run PowerShell commands in the repo directory:

```powershell
C:/Python38/python.exe -m venv venv
venv/Scripts/Activate.ps1
python.exe -m pip install --upgrade pip
python.exe -m pip install -r requirements.txt
python.exe -m pip install -r requirements-dev.txt
```

- Open `workspace.code-workspace` in [VS Code](https://code.visualstudio.com/).

- If you modify `requirements.txt` or `requirements-dev.txt` run:
  - `python.exe -m pip install -r requirements.txt`
  - `python.exe -m pip install -r requirements-dev.txt`
  - `tox --recreate`

## Unit testing

- Run `tox` in the repo directory.
