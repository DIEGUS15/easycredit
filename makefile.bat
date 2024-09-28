@echo off

rem run the server
if "%1"=="run" (
    call venv\Scripts\python.exe manage.py runserver
)
rem migrate apps
if "%1"=="migrate" (
    call venv\Scripts\python.exe manage.py migrate
)
rem install dependencys
if "%1"=="install" (
    call venv\Scripts\python.exe -m pip install -r requirements.txt
)
rem create a super user in the project of django
if "%1"=="createsuperuser" (
    call venv\Scripts\python.exe manage.py createsuperuser
)
rem run linter
if "%1"=="lint" (
    call venv\Scripts\python.exe -m flake8 .
)
rem run black formatter
if "%1"=="format" (
    call venv\Scripts\python.exe -m black .
)
if "%1"=="activate" (
    call venv\Scripts\activate
)
if "%1"=="smigrations" (
    call venv\Scripts\python.exe manage.py showmigrations
)