@echo off

if "%4"=="" (
echo 4つの画像をドラッグしてください
echo 終了します
pause
exit
)

@echo カレントフォルダ：%CD%
@echo バッチのフォルダ：%~dp0

start %~dp0gimp_fu_collage.bat %1 %2 %3 %4