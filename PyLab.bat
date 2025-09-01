@echo off
setlocal

set vscode="%LocalAppData%\Programs\Microsoft VS Code\Code.exe"

echo Welcome to PyLab!
echo ===================================================================
goto bootchoice
:choice
echo -------------------------------------------------------------------
:bootchoice
echo.
echo What would you like to do?
echo 1. Open lessons
echo 2. Create a new game
echo 3. Open an existing game
echo 4. Share a game
echo 5. Nothing
echo.




set /p choice=Please enter your choice: 
echo.

if "%choice%"=="1" (
    goto lessons
) else if "%choice%"=="2" (
    goto projcreate
) else if "%choice%"=="3" (
    goto projopen
) else if "%choice%"=="4" (
    goto projshare
) else if "%choice%"=="5" (
    echo Exiting...
    goto finish
) else (
    echo Invalid choice. Please try again.
    echo.
    goto choice
)




:lessons
echo Starting lessons...
%vscode% ".\lessons"
goto choice




:projcreate
echo Creating a new game...
set /p projname=Enter game name: 
echo.
if "%projname%" equ "" (
    echo Game name cannot be empty.
    echo.
    goto choice
)
:: Create the project directory
set projdir=%~dp0games\%projname%
mkdir "%projdir%"
:: Copy the template files
robocopy "%~dp0.templates\tinygame" "%projdir%" /E >nul 2>&1
:: Substitute the game title
set sprojname=%projname: =%
powershell -Command "(Get-Content '%projdir%/main.py') -replace '_T_GAME_TITLE_T_', '%projname%' | Set-Content '%projdir%/main.py'"
:: Conclude and open the game in VSCode
echo Game project "%projname%" created successfully.
goto projboot




:projopen
echo Opening an existing game...
:: List projects in the games directories and ask the user to pick one
echo Available games:
echo.
cd "%~dp0games"
dir /B /AD
cd "%~dp0"
echo.
set /p projname=Enter game name: 
if "%projname%" equ "" (
    echo Game name cannot be empty.
    echo.
    goto choice
)
echo.
:: Pick the first directory name under the games directory that starts with the input string
for /f "delims=" %%i in ('dir /B /AD "%~dp0games\%projname%*"') do (
    set projdir=%~dp0games\%%i
    set projname=%%i
    goto selected
)
echo.
echo Game project %projname% not found.
echo.
goto choice

:selected
goto projboot




:projboot
echo Opening game project "%projname%" in VSCode...
%vscode% "%projdir%"
echo.
goto choice




:projshare
echo Sharing a game...
:: List projects in the games directories and ask the user to pick one
echo Available games:
echo.
cd "%~dp0games"
dir /B /AD
cd "%~dp0"
echo.
set /p projname=Enter project name: 
echo.
:: Pick the first directory name under the games directory that starts with the input string
for /f "delims=" %%i in ('dir /B /AD "%~dp0games\%projname%*"') do (
    set projdir=%~dp0games\%%i
    set projname=%%i
    goto found
)
echo.
echo Game project %projname% not found.
echo.
goto choice

:found
echo Packaging game project "%projname%"...
:: Create staging directory
pushd "%projdir%"
set stagingdir=%projdir%\.staging
if not exist "%stagingdir%" (
    mkdir "%stagingdir%"
)
popd
:: Create share directory
set sharedir=%~dp0.share
if not exist "%sharedir%" (
    mkdir "%sharedir%"
)
:: Generate executable binaries
pushd "%stagingdir%"
pyinstaller --noconfirm --onedir --console --name "%projname%" --add-data "%projdir%\res;res/" --collect-all "pylab"  "%projdir%\main.py" >nul 2>&1
popd
:: Package binaries
echo Making shareable game bundle...
set archive=%sharedir%\%projname%.zip
if exist "%archive%" (
    del "%archive%"
)
7z a -tzip "%archive%" "%stagingdir%\dist\%projname%\*" >nul 2>&1
explorer "%sharedir%"
echo.
goto choice

:finish

endlocal

pause