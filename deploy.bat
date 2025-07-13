@echo off

setlocal

set rootDir=%~dp0
set packDir=%rootDir%.packaged\
set deployDir=C:\Users\choco.EUCLID\Sync\Shared\Ghys\
set packName=PyLab.zip

set /p input_package="Would you like to re-package prior to deploying? (y/n)"
if /i "%input_package%"=="y" (
    call .\package.bat
)

:: Copy to deployment location
echo Deploying to "%deployDir%"...
copy "%rootDir%%packName%" "%deployDir%%packName%"

echo Deployment complete!

endlocal
pause