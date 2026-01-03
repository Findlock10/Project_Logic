@echo off
TITLE LOGIC PROTOCOL V5 - 127.0.0.1 FOCUS
COLOR 0A

:: 1. Force directory to the Logic folder
cd /d "%~dp0"

echo [ LOGIC ] Resetting Port 3001...
:: This clears any "ghost" processes still hanging on the port
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3001') do taskkill /f /pid %%a >nul 2>&1

echo [ LOGIC ] Starting Backend Engine (app.py)...
:: We use 'start' to keep the engine visible so we can see it working
start "Logic Brain" cmd /k "python app.py"

echo [ LOGIC ] Waiting 5 seconds for Engine to warm up...
timeout /t 5 /nobreak > nul

echo [ LOGIC ] Launching Interface at 127.0.0.1...
:: Using the exact IP as requested
start "" "http://127.0.0.1:3001"

echo --------------------------------------------------
echo [ SYSTEM ONLINE ]
echo --------------------------------------------------
pause