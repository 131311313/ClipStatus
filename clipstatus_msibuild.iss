[Setup]
AppName=ClipStatus
AppVersion=1.0
DefaultDirName={userappdata}\clipstatus
DisableProgramGroupPage=yes
OutputBaseFilename=clipstatus_installer
Compression=lzma
SolidCompression=yes
PrivilegesRequired=none

[Files]
Source: "C:\Users\z\Downloads\Compressed\ClipStatus-main\ClipStatus-main\clipstatus.exe"; DestDir: "{userappdata}\clipstatus"; Flags: ignoreversion
Source: "C:\Users\x\Downloads\Compressed\ClipStatus-main\ClipStatus-main\config.json"; DestDir: "{userappdata}\clipstatus"; Flags: ignoreversion
Source: "C:\Users\a\Downloads\Compressed\ClipStatus-main\ClipStatus-main\icon.png"; DestDir: "{userappdata}\clipstatus"; Flags: ignoreversion

[Icons]
; スタートアップフォルダにショートカットを作成
Name: "{userstartup}\ClipStatus"; Filename: "{userappdata}\clipstatus\clipstatus.exe"; IconFilename: "{userappdata}\clipstatus\icon.png"; WorkingDir: "{userappdata}\clipstatus"

; スタートメニューにショートカットを作成
Name: "{userprograms}\ClipStatus"; Filename: "{userappdata}\clipstatus\clipstatus.exe"; IconFilename: "{userappdata}\clipstatus\icon.png"; WorkingDir: "{userappdata}\clipstatus"

; デスクトップにショートカットを作成
Name: "{userdesktop}\ClipStatus"; Filename: "{userappdata}\clipstatus\clipstatus.exe"; IconFilename: "{userappdata}\clipstatus\icon.png"; WorkingDir: "{userappdata}\clipstatus"

[Run]
Filename: "{userappdata}\clipstatus\clipstatus.exe"; Description: "Start ClipStatus"; Flags: runhidden

[UninstallDelete]
Type: files; Name: "{userappdata}\clipstatus\*"
