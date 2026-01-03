@echo off
TITLE LOGIC PROTOCOL V3 - UNIFIED
COLOR 0A

:: Force the script to look exactly where it is saved
cd /d "%~dp0"

echo [ LOGIC ] Starting Backend...
:: Using 'start' to keep the engine window separate
start "Logic Brain" cmd /k "python app.py"

timeout /t 3 /nobreak > nul

echo [ LOGIC ] Launching Frontend from local folder...
:: This looks for index.html in the SAME folder as this .bat
start "" "index.html"

echo --------------------------------------------------
echo [ SYSTEM ONLINE ]
echo --------------------------------------------------
pause