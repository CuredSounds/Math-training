@echo off
echo Starting Lab in a Box...

REM Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python.
    pause
    exit /b
)

REM Check for venv directory
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate venv
call .venv\Scripts\activate.bat

REM Install dependencies
echo Checking dependencies...
pip install -r requirements.txt

REM Run the dashboard
echo Launching Dashboard...
streamlit run src/app/dashboard.py

pause
