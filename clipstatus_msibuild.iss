[Setup]
AppName=ClipStatus
AppVersion=1.0.5
DefaultDirName={userappdata}\ClipStatus
DefaultGroupName=ClipStatus
OutputDir=userdocs:Inno Setup Examples Output
OutputBaseFilename=clipstatus_setup
Compression=lzma
SolidCompression=yes
SetupIconFile=C:\Users\<USERNAME>\Downloads\clipstatus\icon.ico
PrivilegesRequired=none

[Files]
Source: "C:\Users\<USERNAME>\Downloads\clipstatus\clipstatus.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\<USERNAME>Downloads\clipstatus\config.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\<USERNAME>\Downloads\clipstatus\icon.png"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ClipStatus"; Filename: "{app}\clipstatus.exe"
Name: "{userdesktop}\ClipStatus"; Filename: "{app}\clipstatus.exe"

[Run]
Filename: "{app}\clipstatus.exe"; Description: "Launch ClipStatus"; Flags: nowait postinstall skipifsilent

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueName: "ClipStatus"; ValueType: string; ValueData: """{app}\clipstatus.exe"""
