@echo off
:: 管理者権限で実行されていない場合、管理者権限で再実行する
set "params=%*"
if not "%1"=="am_admin" (
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0 am_admin %params%' -Verb RunAs"
    exit /b
)

:: C:\Program Files (x86)\clipstatus フォルダを作成 (既存の場合は削除して再作成)
echo Creating or recreating C:\Program Files (x86)\clipstatus...
rmdir /s /q "C:\Program Files (x86)\clipstatus"
mkdir "C:\Program Files (x86)\clipstatus"



:: 必要なファイルをコピー
echo Copying files to C:\Program Files (x86)\clipstatus...
copy "%~dp0startup.bat" "C:\Program Files (x86)\clipstatus\startup.bat"
copy "%~dp0killpython.bat" "C:\Program Files (x86)\clipstatus\killpython.bat"
copy "%~dp0ClipStatus.pyw" "C:\Program Files (x86)\clipstatus\ClipStatus.pyw"
copy "%~dp0config.json" "C:\Program Files (x86)\clipstatus\config.json"
copy "%~dp0requirements.txt" "C:\Program Files (x86)\clipstatus\requirements.txt"
:: requirements.txt を使って依存関係をインストール
echo Installing required packages...
pip install -r "C:\Program Files (x86)\clipstatus\requirements.txt"



:: スタートアップフォルダのパスを取得
set "startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

:: Startup.bat のショートカットを作成
echo Creating shortcut for startup.bat in Startup folder...
powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut('%startup_folder%\ClipStatusStartup.lnk');$s.TargetPath='C:\Program Files (x86)\clipstatus\startup.bat';$s.Save()"

:: 完了メッセージ
echo Setup complete! ClipStatus will now start automatically on system boot.
pause
