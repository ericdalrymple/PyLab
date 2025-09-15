@echo off

setlocal

set iconpath=%~dp0..\icons\pylab.ico
set lnkname=PyLab.lnk
set lnkpath1=%~dp0..
set lnkpath2=%userprofile%\Start Menu\Programs\PyLab
set target=%~dp0\PyLab.bat

:: Create a link in the PyLab directory
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%lnkpath1%\%lnkname%');$s.TargetPath='%target%';$s.IconLocation='%iconpath%';$s.Save()"  >nul 2>&1

:: Create a link for the Start Menu
mkdir "%lnkpath2%"
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%lnkpath2%\%lnkname%');$s.TargetPath='%target%';$s.IconLocation='%iconpath%';$s.Save()"  >nul 2>&1

endlocal