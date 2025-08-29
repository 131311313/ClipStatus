@echo off
echo Building ClipStatus installer...

echo Step 1: Creating executable with PyInstaller...
pyinstaller --onefile --windowed --icon=icon.ico --name=ClipStatus ClipStatus.pyw

echo Step 2: Building installer with Inno Setup...
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" clipstatus_msibuild.iss

echo Build complete!
echo - Executable: dist\ClipStatus.exe
echo - Installer: Output\clipstatus_installer.exe

pause
