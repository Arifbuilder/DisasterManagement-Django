@echo off
echo =======================================================
echo     Disaster Management App - Setup and Run Script
echo =======================================================

echo.
echo [1] Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python.
    pause
    exit /b
)

echo.
echo [2] Checking/Creating Virtual Environment (venv)...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists.
)

echo.
echo [3] Activating Virtual Environment and Installing Dependencies...
call venv\Scripts\activate
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo No requirements.txt found! Skipping dependency installation.
)

echo.
echo [4] Applying Database Migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo [5] Starting the Django Development Server...
echo The server will be available at http://127.0.0.1:8000/
start http://127.0.0.1:8000/
python manage.py runserver

pause
