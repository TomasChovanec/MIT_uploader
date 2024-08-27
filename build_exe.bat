@echo off
SET PYTHONPATH=%~dp0\venv\Lib;%~dp0\venv\;%~dp0\venv\Scripts\DLLs
SET PYTHONHOME=%~dp0\venv\Scripts\
echo on

call "%~dp0\venv\Scripts\activate.bat"

::delete old builds
del /s /Q "%~dp0\build\
rmdir /s /q "%~dp0"\build\

::build script
"%~dp0\venv\Scripts\python.exe" setup.py build

call "%~dp0\venv\Scripts\deactivate.bat"
pause
