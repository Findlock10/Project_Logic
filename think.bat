@echo off
echo Starting Logic Enterprise Agent...
:: This starts the Python backend in the background
start /b python app.py
:: This waits 3 seconds to let the server warm up
timeout /t 3 /nobreak > nul
:: This opens your browser to the local address
start http://127.0.0.1:3001
echo System Uplink Active.
pause