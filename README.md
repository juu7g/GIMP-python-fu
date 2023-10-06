# GIMP-python-fu
GIMP Python-Fu script collection

## �T�v Description
GIMP �� Python-Fu  �X�N���v�g���g�����c�[��

## ���� Features

- 4�̉摜���R���[�W������GIMP �̃X�N���v�g�ƋN������o�b�`  
	- �X�N���v�g�t�@�C���F`fu_collage4bat.py`
	- �N���p�o�b�`�@�@�@�F`gimp_collage.bat`
	- GIMP�N���p�o�b�` �F`gimp_fu_collage.bat`
- 4�̉摜���R���[�W������GIMP �̃X�N���v�g�ƋN������v���O����  
	- �X�N���v�g�t�@�C���F`fu_collage.py`
	- �v���O�����@�@�@�@�F`collage_by_GIMP.py`
	- �ݒ�t�@�C���@�@�@�F`settings_collage.py`

## �ˑ��֌W Requirement

- ����
	- GIMP 2.10.18
	- Windows 64bit OS
- �v���O����
	- Python 3.8.5
	- Pillow 10.0.0

## �g���� Usage

- 4�̉摜���R���[�W������GIMP �̃X�N���v�g�ƋN������o�b�`  
	- �N�����@  
		1. �G�N�X�v���[���ȂǂŃR���[�W���������S�̉摜��I���iCtrl �������Ȃ���N���b�N�j
		2. `gimp_collage.bat` ��4�̉摜���h���b�N�A���h�h���b�v
		3. �S�̉摜������t�H���_�� `GIMPyymmddhhmm.jpg` �摜���쐬
	- �ݒ���@  
		`fu_collage4bat.py` ���C��
		- �쐬�����摜�̕��F`_width = 800` ��800��ύX(px)
		- �S�̐}�`�̋��E���̕��F`border_width = 10` ��10��ύX(px)
		- ���E���̐F�F`_color = gimpcolor.RGB(211, 211, 2111)` �̐�����ύX

- 4�̉摜���R���[�W������GIMP �̃X�N���v�g�ƋN������v���O����  
	- �N�����@
		- RPA_GIMP_collage.exe �����s���܂�
		- �܂��� RPA_GIMP_collage.exe �̃A�C�R���ɃR���[�W���������摜���h���b�O�A���h�h���b�v���܂�

	- ������@  
		- �h���b�O���h���b�v�ł̑���
			- �A�v����ʏ��4�̘g�ɂɃR���[�W���������摜���h���b�O���h���b�v  
		- �����摜�̕����w��
			- �e�L�X�g�{�b�N�X�ɐ����摜�̕�����͂�Enter�������܂�
				- ��ʂ��w�肵�����ɕς��܂�
		- ���E���̕����w��
			- �e�L�X�g�{�b�N�X�ɋ��E���̕�����͂�Enter�������܂�
				- ��ʂ��w�肵�����ɕς��܂�
		- �F�̑I��
			- �F�I���{�^���őI��  
				- �F�I���{�^���������ƐF�I���_�C�A���O���\������܂�
				- ��]�̐F��I������ OK �{�^���������܂�
			- �F�I���R���{�{�b�N�X�őI��
				- �R���{�{�b�N�X�́��������ƐF���̑I�������o��̂őI�����܂�
				- �R���{�{�b�N�X�ɐF���̈ꕔ�����ā��L�[�������Ɠ��͂������������F�����o�͂��܂�  
		- �摜�̐���
			- �쐬�{�^���������܂�

	  - ��ʂ̐���  
		- �쐬�{�^���@�@�@�@�@�F�R���[�W�������摜���쐬���܂�
		- �F�I���{�^���@�@�@�@�F���E���̐F���w�肵�܂�
		- �F�I���R���{�{�b�N�X�F���E���̐F��F���Ŏw�肵�܂�
		- �����摜�̕��@�@�@�@�F�����摜�̕��� px �Ŏw�肵�܂�
		- ���E���̕��@�@�@�@�@�F���E���̕��� px �Ŏw�肵�܂�
		- �S�̎l�p�@�@�@�@�@�F�R���[�W������摜��\�����܂�

	- �ݒ���@  
		`settings_collage.py` ���C��  
		- GIMP �� exe �̃p�X�@�@�@�@�@�F`gimp1 = r"C:\Program Files\GIMP 2\bin\gimp-2.10.exe"`
		- GIMP �̃R���\�[�� exe �̃p�X�F`gimp2 = r"C:\Program Files\GIMP 2\bin\gimp-console-2.10.exe"`
		- GIMP �̃X�N���v�g�̃p�X�@�@ �F`scriptpath = r'scripts\fu_collage.py'`  
			�A�v�����g�p����ꍇ�A�X�N���v�g�̃p�X�͂��̂܂܎g�p���Ă��������B  
			�\�[�X�𗘗p����ꍇ�A�X�N���v�g�̃p�X�̓\�[�X��u�����t�H���_�̐e�t�H���_����̑��΃p�X���w�肵�Ă��������B 

## ��������  

- �������ŃA�X�y�N�g�䂪 4:3 �̉摜���Ώ�  

## �v���O�����̐����T�C�g Program description site

- [�R���[�W��������Python-Fu�X�N���v�g�Ńo�b�`�����yGIMP�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/blog/gimp/collage/fu-bat)  
- [�R���[�W��������Python-Fu�X�N���v�g��Python��GUI��t���āyGIMP�APython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/blog/gimp/collage/fu-python)  
  
## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE�t�@�C�����m�F���Ă��������B  
This software is released under the MIT License, see LICENSE file.

