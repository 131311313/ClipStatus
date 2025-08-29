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
Source: "dist\ClipStatus.exe"; DestDir: "{userappdata}\clipstatus"; Flags: ignoreversion
Source: "config.json"; DestDir: "{userappdata}\clipstatus"; Flags: ignoreversion
Source: "icon.png"; DestDir: "{userappdata}\clipstatus"; Flags: ignoreversion
Source: "dark_icon.png"; DestDir: "{userappdata}\clipstatus"; Flags: ignoreversion
Source: "default_icon.png"; DestDir: "{userappdata}\clipstatus"; Flags: ignoreversion

[Icons]
; スタートアップフォルダにショートカットを作成
Name: "{userstartup}\ClipStatus"; Filename: "{userappdata}\clipstatus\ClipStatus.exe"; IconFilename: "{userappdata}\clipstatus\icon.png"; WorkingDir: "{userappdata}\clipstatus"

; スタートメニューにショートカットを作成
Name: "{userprograms}\ClipStatus"; Filename: "{userappdata}\clipstatus\ClipStatus.exe"; IconFilename: "{userappdata}\clipstatus\icon.png"; WorkingDir: "{userappdata}\clipstatus"

; デスクトップにショートカットを作成
Name: "{userdesktop}\ClipStatus"; Filename: "{userappdata}\clipstatus\ClipStatus.exe"; IconFilename: "{userappdata}\clipstatus\icon.png"; WorkingDir: "{userappdata}\clipstatus"

[Run]
Filename: "{userappdata}\clipstatus\ClipStatus.exe"; Description: "Start ClipStatus"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{userappdata}\clipstatus\*"
