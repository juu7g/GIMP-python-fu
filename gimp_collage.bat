@echo off

if "%4"=="" (
echo 4�̉摜���h���b�O���Ă�������
echo �I�����܂�
pause
exit
)

@echo �J�����g�t�H���_�F%CD%
@echo �o�b�`�̃t�H���_�F%~dp0

start %~dp0gimp_fu_collage.bat %1 %2 %3 %4