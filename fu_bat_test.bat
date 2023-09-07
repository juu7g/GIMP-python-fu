rem python-fuのファイルをバッチで実行する

setlocal
rem shori：起動方法(1：通常起動、2：コンソール起動)
set shori=1
rem 通常起動用exeの指定
set gimp1="C:\Program Files\GIMP 2\bin\gimp-2.10.exe"
rem コンソール起動用exeの指定
set gimp2="C:\Program Files\GIMP 2\bin\gimp-console-2.10.exe"
rem バッチの存在フォルダ：%~dp0 末尾に\が付く
rem 本ファイルと同じフォルダにあるPythonスクリプトファイルの指定
set scriptpath="%~dp0fu_simple_test.py"

rem 通常起動
if %shori%==1 (
%gimp1% -n -c -d -s -f --batch-interpreter=python-fu-eval -b - -b "pdb.gimp_quit(1)" < %scriptpath%
goto :end
)

rem コンソール起動
if %shori%==2 (
%gimp2% -i -n -c -d -s -f --batch-interpreter=python-fu-eval -b - -b "pdb.gimp_quit(1)" < %scriptpath%
goto :end
)

:end
endlocal
pause
exit