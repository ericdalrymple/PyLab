set rootDir=%~dp0
set packDir=%rootDir%.packaged\

:: Ensure .package directory exists and clean.
if not exist "%packDir%" (
    mkdir "%packDir%"
) else (
    del "%packDir%" /q
)

:: Copy the files we want to package
xcopy "%rootDir%.doc\" "%packDir%.doc\" /E /Y
xcopy "%rootDir%.vscode\" "%packDir%.vscode\" /E /Y
xcopy "%rootDir%images\" "%packDir%images\" /E /Y
xcopy "%rootDir%lessons\" "%packDir%lessons\" /E /Y
xcopy "%rootDir%tinyengine\" "%packDir%tinyengine\" /E /Y
copy "%rootDir%__init__.py" "%packDir%__init__.py" /Y
copy "%rootDir%requirements.txt" "%packDir%requirements.txt" /Y
copy "%rootDir%setup.bat" "%packDir%setup.bat" /Y

:: Zip the package contents
7z a -tzip "%rootDir%PyLab.zip" "%packDir%*"