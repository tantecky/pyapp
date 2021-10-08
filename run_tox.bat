@echo off
call run_install.bat
:RUN
tox
pause
goto :RUN