@echo off
echo Forcibly terminating python.exe...
taskkill /F /IM python.exe

echo Forcibly terminating pythonw.exe...
taskkill /F /IM pythonw.exe

echo Termination complete.
pause
