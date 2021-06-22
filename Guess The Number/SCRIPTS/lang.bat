@echo off
FOR /F "tokens=3" %%a IN ('reg query "HKCU\Control Panel\Desktop" /v PreferredUILanguages ^| find "PreferredUILanguages"') DO set UILanguage=%%a
echo User Display Language: %UILanguage%
if %UILanguage%==pl-PL goto pl
if NOT %UILanguage%==pl-PL goto eng

:pl
start PL
exit

:eng
start ENG
exit