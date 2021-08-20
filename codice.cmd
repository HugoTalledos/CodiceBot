@echo off

SET  action=%1
SET  message=%2
SET  script=python ./init.py %action% %message%
cd %ProgramFiles%\CodiceBot
call %script%