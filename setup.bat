@echo off

setlocal enabledelayedexpansion

echo.
echo "=================> Installing Python..."

echo "Launching Python installer..."
start /wait %~dp0\.setup\python-3.13.2-amd64.exe
echo "Python installer terminated."



echo.
echo.
echo.
echo "=================> Installing Visual Studio Code..."

echo "Launching VSCode installer..."
start /wait %~dp0\.setup\VSCodeUserSetup-x64-1.98.2.exe
echo "VSCode installer terminated."



echo.
echo.
echo.
echo "=================> Setting environment variables..."

set var=PYTHONPATH
set val=!%var%!
set add=%~dp0
if defined !val! (
    echo !val! | findstr /C:"%add%" >nul
    if !errorlevel! neq 0 (
        setx %var% %add%;%val%
    )
) else (
    setx %var% %add%
)

set pypath1=%USERPROFILE%\AppData\Local\Programs\Python\Python313
set pypath2=%USERPROFILE%\AppData\Local\Programs\Python\Python313\Scripts
set pypath3=%USERPROFILE%\AppData\Local\Programs\Python\Launcher

for /F "tokens=*" %%A in ('reg query HKEY_CURRENT_USER\Environment /v Path 2^>nul ^| find "Path"') do (
    for /F "tokens=2*" %%B in ("%%A") do (
        set pathval=%pathval%%%C
    )
)

echo %pathval% | findstr /C:"%pypath3%;" >nul
if !errorlevel! neq 0 (
    set pathval=%pypath3%;%pathval%
)

echo %pathval% | findstr /C:"%pypath2%;" >nul
if !errorlevel! neq 0 (
    set pathval=%pypath2%;%pathval%
)

echo %pathval% | findstr /C:"%pypath1%;" >nul
if !errorlevel! neq 0 (
    set pathval=%pypath1%;%pathval%
)

setx Path "%pathval%"


echo.
echo.
echo.
echo "=================> Installing pip..."

curl https://bootstrap.pypa.io/get-pip.py -o .\.setup\get-pip.py
python .\.setup\get-pip.py


echo.
echo.
echo.
echo "=================> Installing requirements..."

pip install -r "%~dp0\requirements.txt"

echo.
echo.
echo.
echo "Setup complete!"
echo.
pause