@echo off
start "" pythonw.exe "C:\Program Files (x86)\clipstatus\ClipStatus.pyw"
if errorlevel 1 (
    echo Error occurred while starting the script.
    pause
) else (
    exit
)
