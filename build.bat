@echo off

set progname=norms
set pyinstaller_dir=D:\Programming\Apps\pyinstaller

%pyinstaller_dir%\Makespec.py --onefile --icon=resources/icon.ico --name=%progname% main.py -X -c -w
%pyinstaller_dir%\Build.py %progname%.spec

rd build /s /q
del warn%progname%.txt
del logdict2.6.6.final.0-1.log
del %progname%.spec
copy dist\%progname%.exe %progname%.exe
rd dist /s /q
echo.
pause