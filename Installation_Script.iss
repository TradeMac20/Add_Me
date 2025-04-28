[Setup]
AppName=ADD IT
AppVersion=1.0
DefaultDirName={pf}\ADD IT
DefaultGroupName=ADD IT
OutputBaseFilename=ADD_IT_Installer
Compression=lzma2
SolidCompression=yes
OutputDir=.
UninstallDisplayIcon={app}\ADD IT.exe
UninstallDisplayName= ADD IT
[Files]
Source: "I:\Codes\Python\add_me\dist\ADD IT\*.*"; DestDir: "{app}"; Flags: recursesubdirs


[Tasks]
Name: "desktopicon"; Description: "Creates a desktop shortcuts"; GroupDescription: "Additional Icons"

[Icons]
Name: "{group}\ADD IT"; Filename: "{app}\ADD IT.exe"
Name: "{commondesktop}\ADD IT"; Filename: "{app}\ADD IT.exe"; Tasks: "desktopicon"
Name: "{group}\Uninstall"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\ADD IT.exe"; Description: "Launch ADD IT application"; Flags: nowait postinstall