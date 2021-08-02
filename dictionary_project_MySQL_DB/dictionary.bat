@echo off
pip install mysql-connector-python
pip install stdiomask
start "Dictionary" cmd /k "@echo off & python startup.pyc & pause & exit"
TIMEOUT /T 5
pip uninstall -y mysql-connector-python
pip uninstall -y stdiomask