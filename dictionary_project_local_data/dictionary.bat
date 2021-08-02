@echo off
pip install cryptography
start "Dictionary" cmd /k "@echo off & python startup.pyc & pause & exit"
TIMEOUT /T 2
pip uninstall -y cryptography
