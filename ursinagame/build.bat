for %%a in ("%cd%") do set "current_dir=%%~nxa"

echo Building '%current_dir%'...
python -m ursina.build --overwrite > buildlog.txt
echo Build complete!

set /p answer=Do you want to run the game? (y/n):
if /i "%answer%"=="y" (
    python .\build_Windows\src\main.pyc > ".\build_Windows\log.txt" 2>&1
)
