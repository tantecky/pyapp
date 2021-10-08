# pyapp ![tests](https://github.com/tantecky/pyapp/actions/workflows/tests.yml/badge.svg)

An example GUI app in Python. It is using several tools for formatting/linting (`isort`, `black`, `flake8`, `mypy`). Unit testing is done through `pytest` with `coverage`. For CI [GitHub Actions](https://docs.github.com/en/actions) is employed.

## How to prepare dev environment on Windows

- Install [Python 3.8+](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe) (e.g. to: `C:/Python38`). Do NOT use `python.exe` from [Anaconda](https://www.anaconda.com/products/individual).

- Create virtualenv in the repo directory:

```powershell
C:/Python38/python.exe -m venv venv
```

- Run `run_install.bat`

- Open `workspace.code-workspace` in [VS Code](https://code.visualstudio.com/).

- Run `run_dev.bat` to start the program in console for easier debugging. You can press ENTER for re-run.

- If you add a new dependecy run:
  - `run_tox_recreate.bat`

### Unit testing/linting

- Run `run_tox.bat` You can press ENTER for re-run.

## Usage

- Run `pyapp.exe` to start the program without console window

## Screenshots

<img align="left" width="357" src="screenshots/1.png"/>
