@echo off
echo Installing Python packages from requirements.txt...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo All packages installed successfully.
) else (
    echo.
    echo There was an error installing the packages.
)

pause
