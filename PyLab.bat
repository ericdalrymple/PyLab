@echo off
setlocal

set vscode="%LocalAppData%\Programs\Microsoft VS Code\Code.exe"

echo Welcome to PyLab!
echo.
echo What would you like to do?
echo 1. Create a new game
echo 2. Open an existing game
echo 3. Share a game
echo 4. Nothing
echo.




:choice
set /p choice=Please enter your choice: 

if "%choice%"=="1" (
    echo Creating a new game...
    goto projcreate
) else if "%choice%"=="2" (
    echo Opening an existing game...
    goto projopen
) else if "%choice%"=="3" (
    echo Sharing a game...
    goto projshare
) else if "%choice%"=="4" (
    echo Exiting...
    goto finish
) else (
    echo Invalid choice. Please try again.
    echo.
    goto choice
)




:projcreate
echo Creating a new game...
set /p projname=Enter game name: 
:: Create the project directory
set projdir=%~dp0games\%projname%
mkdir "%projdir%"
:: Copy the template files
robocopy "%~dp0.templates\tinygame" "%projdir%" /E >nul 2>&1
:: Substitute the game title
powershell -Command "(Get-Content '%projdir%/main.py') -replace '\$\$GAME_TITLE\$\$', '%projname%' | Set-Content '%projdir%/main.py'"
:: Conclude and open the game in VSCode
echo Game project %projname% created successfully.
echo Opening game in VSCode...
%vscode% "%projdir%"
goto projboot




:projopen
echo Opening an existing game...
:: List projects in the games directories and ask the user to pick one
echo Available games:
cd "%~dp0games"
dir /B /AD
cd "%~dp0"
set /p projname=Enter game name: 
:: Pick the first directory name under the games directory that starts with the input string
for /f "delims=" %%i in ('dir /B /AD "%~dp0games\%projname%*"') do (
    set projdir=%~dp0games\%%i
    set projname=%%i
    goto selected
)
echo Game project %projname% not found.
goto finish

:selected
echo Opening game project "%projname%"...
goto projboot




:projboot
%vscode% "%projdir%"
goto finish




:projshare
echo Sharing an existing game...
:: List projects in the games directories and ask the user to pick one
echo Available games:
cd "%~dp0games"
dir /B /AD
cd "%~dp0"
set /p projname=Enter project name: 
:: Pick the first directory name under the games directory that starts with the input string
for /f "delims=" %%i in ('dir /B /AD "%~dp0games\%projname%*"') do (
    set projdir=%~dp0games\%%i
    set projname=%%i
    goto found
)
echo Game project %projname% not found.
goto finish

:found
echo Packaging game project "%projname%"...
pushd "%projdir%"
set stagingdir=%projdir%\.staging
if not exist "%stagingdir%" (
    mkdir "%stagingdir%"
)
popd
pushd "%stagingdir%"
pyinstaller --noconfirm --onedir --console --name "%projname%" --add-data "%projdir%\res;res/" --collect-all "tinyengine"  "%projdir%\main.py"
popd
goto finish



:finish

endlocal

pause