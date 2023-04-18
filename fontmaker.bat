@echo off
@cls
:start
python C:\admin\fontmaker\b.py
timeout/t 90
cls
timeout/t 9999
goto start