@echo off
:: fucking windows
for /f %%i in ('poetry env activate') do set output=%%i
call %output%