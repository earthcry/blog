

# Python

### python env build

python --version
build-essential
sudo apt install python3 python3-pip python3-dev python3-venv
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
 https://mirrors.aliyun.com/pypi/simple/ 
 https://pypi.mirrors.ustc.edu.cn/simple/ 

https://mirrors.tuna.tsinghua.edu.cn/python/
https://mirrors.aliyun.com/python/
https://pypi.python.org/simple

curl 或 wget
git

# 配置ssh  如上图
ssh-keygen #按3下回车
cd ~/.ssh

cat id_rsa.pub
#把公钥放到git平台上
# 配置用户名和邮箱
git config --global user.name 'xuehu96'
git config --global user.email 'xuehu96@xxx.com'


@venv
python3 -m venv myvenv/.venv
cd myvenv
source .venv/bin/activate

deactivate

venv       更簡單
virtualenv 更靈活
pipenv     更智能


//python3 -m pip install --upgrade pip
(myenv) pip install --upgrade pip
(myenv) pip install
(myenv) pip list
(myenv) pip freeze > requirements.txt
(myenv) deactivate
rm -rf myenv/.venv


my_project/
  .venv/
  app.py
  requirements.txt

pipenv --rm  # 定期清理不用環境

anaconda, pip
pycharm, vim,

# .py
#!/bin/python3

