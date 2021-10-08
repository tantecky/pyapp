@echo off
call run_install.bat
:RUN
python pyapp
pause
goto :RUN