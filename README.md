# pypip
pypi를 이용해서 자신이 만든 pip 올리기  
일단 pypi 회원가입  
pip install setuptools wheel  
다 하고 나서  
python setup.py sdist bdist_wheel  
pip install twine  
python -m twine upload dist/자신이 원하는 버전 .whl으로 끝나는 파일적기  
pypi 아이디  
pypi 비밀번호  
