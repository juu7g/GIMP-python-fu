rem python-fuのファイルをバッチで実行する
@echo off
chcp 65001

setlocal
setlocal enabledelayedexpansion

rem shori：起動方法(1：通常起動、2：コンソール起動)
set shori=2
rem 通常起動用exeの指定
set gimp1="C:\Program Files\GIMP 2\bin\gimp-2.10.exe"
rem コンソール起動用exeの指定
set gimp2="C:\Program Files\GIMP 2\bin\gimp-console-2.10.exe"
rem バッチの存在フォルダ：%~dp0 末尾に\が付く
rem 本ファイルと同じフォルダにあるPythonスクリプトファイルの指定

set scriptpath=%~dp0fu_collage4bat.py
set scripttemp=%~dp0fu_collage4bat.tmp

for /f "delims=" %%a in (%scriptpath%) do (set script=!script!%%a^


)

set script=!script:image_file_name1=%1!
set script=!script:image_file_name2=%2!
set script=!script:image_file_name3=%3!
set script=!script:image_file_name4=%4!

if %shori%==2 set script=!script:123456=False!

echo !script! > !scripttemp!

if %shori%==1 (
!gimp1! -n -c -d -s -f --batch-interpreter=python-fu-eval -b - -b "pdb.gimp_quit(1)" < !scripttemp!
goto :end
)
if %shori%==2 (
!gimp2! -i -n -c -d -s -f --batch-interpreter=python-fu-eval -b - -b "pdb.gimp_quit(1)" < !scripttemp!
goto :end
)
:end
endlocal
pause
exit