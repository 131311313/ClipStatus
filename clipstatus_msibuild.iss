[Setup]
AppName=ClipStatus
AppVersion=1.0
DefaultDirName={pf}\ClipStatus
DefaultGroupName=ClipStatus
OutputDir=userdocs:Inno Setup Examples Output
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
; ClipStatus EXE ファイルをインストール
Source: "C:\Users\PC_User\Downloads\clipstatus\clipstatus.exe"; DestDir: "{app}"; Flags: ignoreversion

; アイコンファイルをインストール
Source: "C:\Users\PC_User\Downloads\clipstatus\dark_icon.png"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; スタートメニューにショートカットを作成
Name: "{group}\ClipStatus"; Filename: "{app}\clipstatus.exe"
; デスクトップにもショートカットを作成
Name: "{desktop}\ClipStatus"; Filename: "{app}\clipstatus.exe"

[Run]
; インストール後にアプリケーションを実行
Filename: "{app}\clipstatus.exe"; Description: "Launch ClipStatus"; Flags: nowait postinstall skipifsilent

[Registry]
; スタートアップに登録するためのレジストリを追加
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueName: "ClipStatus"; ValueType: string; ValueData: "{app}\clipstatus.exe"
