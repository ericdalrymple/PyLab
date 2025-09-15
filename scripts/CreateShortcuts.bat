@echo off

setlocal

set iconpath=%~dp0..\icons\pylab.ico
set lnkname=PyLab.lnk
set lnkpath1=%~dp0..
set lnkpath2=%userprofile%\Start Menu\Programs\PyLab
set lnkpath3=%userprofile%\Desktop
set target=%~dp0\PyLab.bat

echo Creating project shortcut...
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%lnkpath1%\%lnkname%');$s.TargetPath='%target%';$s.IconLocation='%iconpath%';$s.Save()"  >nul 2>&1

echo Creating Start Menu shortcut...
mkdir "%lnkpath2%" >nul 2>&1
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%lnkpath2%\%lnkname%');$s.TargetPath='%target%';$s.IconLocation='%iconpath%';$s.Save()"  >nul 2>&1

echo Creating Desktop shortcut...
mkdir "%lnkpath2%" >nul 2>&1
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%lnkpath3%\%lnkname%');$s.TargetPath='%target%';$s.IconLocation='%iconpath%';$s.Save()"  >nul 2>&1

endlocal