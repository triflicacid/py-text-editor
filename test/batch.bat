@echo off
setlocal enableDelayedExpansion

:TimesTableMENU
cls
title TIMES TABLE MENU
color EC
echo.
echo 1 - times table [up to 12]
echo 2 - times table [up to whatever]
echo 3 - exit
set /p CHOICE=Choice:
if %CHOICE%==1 goto TimesTable
if %CHOICE%==3 exit
if %CHOICE%==2 goto NewTimes

:TimesTable
cls
title TIMES TABLE
color CE
echo.
echo.
echo enter the times table you want to see (only go up to 12x).
set /p XTable=Times Table - 
set /A one=%XTable% * 1
set /A two=%XTable% * 2
set /A three=%XTable% * 3
set /A four=%XTable% * 4
set /A five=%XTable% * 5
set /A six=%XTable% * 6
set /A seven=%XTable% * 7
set /A eight=%XTable% * 8
set /A nine=%XTable% * 9
set /A ten=%XTable% * 10
set /A eleven=%XTable% * 11
set /A twelve=%XTable% * 12
echo ________________________________________________
echo 1 = %one%
echo 2 = %two%
echo 3 = %three%
echo 4 = %four%
echo 5 = %five%
echo 6 = %six%
echo 7 = %seven%
echo 8 = %eight%
echo 9 = %nine%
echo 10 = %ten%
echo 11 = %eleven%
echo 12 = %twelve%
pause
goto TimesTableMENU


:NewTimes
cls
echo.
set /p XTableTWO=Times Table starting digit:
goto loop

:loop
set /p num=Number of times multiplied:
set MultNum=1
:SecLoop
set /A result=%XTableTWO% * !MultNum!
echo !result!
if !MultNum!==%num% goto EXTRA
set /A MultNum+=1
goto SecLoop


:EXTRA
echo.
pause
goto TimesTableMENU