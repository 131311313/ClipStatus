[Setup]
AppName=ClipStatus
AppVersion=1.0.2
DefaultDirName={pf}\ClipStatus
DefaultGroupName=ClipStatus
OutputDir=userdocs:Inno Setup Examples Output
OutputBaseFilename=clipstatus_setup
Compression=lzma
SolidCompression=yes
SetupIconFile=C:\Users\PC_User\Downloads\clipstatus\icon.ico

[Files]
; ClipStatus EXE ファイルをインストール
; Install ClipStatus EXE file
Source: "C:\Users\<USERNAME>\Downloads\clipstatus\clipstatus.exe"; DestDir: "{app}"; Flags: ignoreversion

; config.json ファイルをインストール
; Install config.json file
Source: "C:\Users\<USERNAME>\Downloads\clipstatus\config.json"; DestDir: "{app}"; Flags: ignoreversion

Source: "C:\Users\<USERNAME>\Downloads\clipstatus\icon.png"; DestDir: "{app}"; Flags: ignoreversion


[Icons]
; スタートメニューにショートカットを作成
; Create shortcut in Start Menu
Name: "{group}\ClipStatus"; Filename: "{app}\clipstatus.exe"

; デスクトップにもショートカットを作成
; Create shortcut on Desktop
Name: "{userdesktop}\ClipStatus"; Filename: "{app}\clipstatus.exe"

[Run]
; インストール後にアプリケーションを実行
; Run the application after installation
Filename: "{app}\clipstatus.exe"; Description: "Launch ClipStatus"; Flags: nowait postinstall skipifsilent

[Registry]
; スタートアップに clipstatus.exe を登録
; Register clipstatus.exe in Windows Startup
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueName: "ClipStatus"; ValueType: string; ValueData: """{app}\clipstatus.exe"""

