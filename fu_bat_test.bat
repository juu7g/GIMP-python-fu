rem python-fu�̃t�@�C�����o�b�`�Ŏ��s����

setlocal
rem shori�F�N�����@(1�F�ʏ�N���A2�F�R���\�[���N��)
set shori=1
rem �ʏ�N���pexe�̎w��
set gimp1="C:\Program Files\GIMP 2\bin\gimp-2.10.exe"
rem �R���\�[���N���pexe�̎w��
set gimp2="C:\Program Files\GIMP 2\bin\gimp-console-2.10.exe"
rem �o�b�`�̑��݃t�H���_�F%~dp0 ������\���t��
rem �{�t�@�C���Ɠ����t�H���_�ɂ���Python�X�N���v�g�t�@�C���̎w��
set scriptpath="%~dp0fu_simple_test.py"

rem �ʏ�N��
if %shori%==1 (
%gimp1% -n -c -d -s -f --batch-interpreter=python-fu-eval -b - -b "pdb.gimp_quit(1)" < %scriptpath%
goto :end
)

rem �R���\�[���N��
if %shori%==2 (
%gimp2% -i -n -c -d -s -f --batch-interpreter=python-fu-eval -b - -b "pdb.gimp_quit(1)" < %scriptpath%
goto :end
)

:end
endlocal
pause
exit