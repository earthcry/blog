

# Python

### python env build

python --version
sudo apt install python3 python3-pip python3-dev python3-venv
python -m pip install --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple


python3 -m venv myvenv/.venv
cd myvenv
source .venv/bin/activate
deactivate

venv       更簡單
virtualenv 更靈活
pipenv     更智能


(myenv) pip install
(myenv) pip list
(myenv) pip freeze > requirements.txt
(myenv) deactivate
rm -rf myenv


my_project/
  .venv/
  app.py
  requirements.txt

pipenv --rm  # 定期清理不用環境

anaconda, pip
pycharm, vim,

# .py
#!

