@echo off
setlocal
where python >nul 2>&1
if %ERRORLEVEL% equ 0 (
    python "%~dp0.conscience\scripts\conscience.py" %*
    exit /b %ERRORLEVEL%
)
where py >nul 2>&1
if %ERRORLEVEL% equ 0 (
    py "%~dp0.conscience\scripts\conscience.py" %*
    exit /b %ERRORLEVEL%
)
if exist "%LOCALAPPDATA%\Python\bin\python.exe" (
    "%LOCALAPPDATA%\Python\bin\python.exe" "%~dp0.conscience\scripts\conscience.py" %*
    exit /b %ERRORLEVEL%
)
echo [!] Python executable not found in PATH.
exit /b 1
