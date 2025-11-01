@echo off
setlocal enabledelayedexpansion
mode con: cols=70 lines=25
title DVD Logo

:: dvd logo by las-r on github

:: constants
set hexm=0123456789ABCDEF
set /a maxX=67
set /a maxY=23

:: init pos and dir
set /a x=1, y=1
set /a dx=1, dy=1

:: main loop
:loop
cls

:: xy offset
for /l %%i in (1,1,!y!) do echo.
for /l %%i in (1,1,!x!) do set /p="." <nul

:: dvd text
echo DVD

:: movement
set /a x+=dx, y+=dy

:: bounce
if !x! lss 0 set /a x=0, dx*=-1 & call :randcolor
if !x! gtr %maxX% set /a x=%maxX%, dx*=-1 & call :randcolor
if !y! lss 0 set /a y=0, dy*=-1 & call :randcolor
if !y! gtr %maxY% set /a y=%maxY%, dy*=-1 & call :randcolor

:: wait
ping -n 1 -w 50 127.0.0.1 >nul

:: loop
goto loop

:: random color subr
:randcolor
set /a c=%RANDOM% %% 16
set "ch=!hexm:~%c%,1!"
color 0!ch!
exit /b
