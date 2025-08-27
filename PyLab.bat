@echo off
setlocal

set vscode="%LocalAppData%\Programs\Microsoft VS Code\Code.exe"

echo Welcome to PyLab!
echo.
echo What would you like to do?
echo 1. Create a new game
echo 2. Open an existing game
echo 3. Nothing



:choice
set /p choice=Please enter your choice: 

if "%choice%"=="1" (
    echo Creating a new game...
    goto projcreate
) else if "%choice%"=="2" (
    echo Opening an existing game...
    goto projopen
) else if "%choice%"=="3" (
    echo Exiting...
    goto finish
) else (
    echo Invalid choice. Please try again.
    echo.
    goto choice
)

set rootDir=%~dp0

:projcreate
echo Creating a new project...
set /p projname=Enter project name: 
:: Create the project directory
mkdir "%projname%"
:: Copy the template files
robocopy "%~dp0.templates\tinygame" "%~dp0%projname%" /E >nul 2>&1
:: Substitute the game title
powershell -Command "(Get-Content '%~dp0%projname%/main.py') -replace '\$\$GAME_TITLE\$\$', '%projname%' | Set-Content '%~dp0%projname%/main.py'"
:: Conclude and open the game in VSCode
echo Project %projname% created successfully.
%vscode% ".\%projname%"
goto finish



:projopen
echo Opening an existing project...
set /p projname=Enter project name: 
cd "%projname%"
echo Project %projname% opened successfully.
goto finish

:finish

endlocal