@echo off

setlocal

set rootDir=%~dp0
set packDir=%rootDir%.packaged\

set packName=PyLab.zip

:: Ensure .package directory exists and clean.
if not exist "%packDir%" (
    mkdir "%packDir%"
) else (
    rmdir "%packDir%" /S /Q
)

:: Copy the files we want to package
echo Staging files to "%packDir%"...
set exclude_dirs=build_Windows __pycache__ >nul 2>&1
robocopy "%rootDir%.vscode" "%packDir%.vscode" /E /XD %exclude_dirs% >nul 2>&1
robocopy "%rootDir%game" "%packDir%game" /E /XD %exclude_dirs% >nul 2>&1
robocopy "%rootDir%images" "%packDir%images" /E /XD %exclude_dirs% >nul 2>&1
robocopy "%rootDir%lessons" "%packDir%lessons" /E /XD %exclude_dirs% >nul 2>&1
robocopy "%rootDir%tinyengine" "%packDir%tinyengine" /E /XD %exclude_dirs% >nul 2>&1
copy "%rootDir%requirements.txt" "%packDir%requirements.txt" /Y >nul 2>&1
copy "%rootDir%setup.bat" "%packDir%setup.bat" /Y >nul 2>&1
copy "%rootDir%update.bat" "%packDir%update.bat" /Y >nul 2>&1

:: Zip the package contents
echo Packaging files to "%rootDir%%packName%"... 
7z a -tzip "%rootDir%%packName%" "%packDir%*" >nul 2>&1

:: Remove the packaging directory
echo Cleaning up staging directory...
rmdir "%packDir%" /S /Q

echo Packaging complete!

endlocal
pause
