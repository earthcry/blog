Github
# Blog

Source of earthcry.github.io.git

## Usage of githunb

## Two device push/pull to github

1. second device:
   1. cp .ssh/id_rsa ~/.ssh
   2. git clone git@github.com:earthcry/blog.git
   3. git config email && name
   4. 
   




## By ssh band Local git and remote github 

push authenfitation by ssh after clone
Github do not to be access by password, it can be ssh key.

本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，因此需要进行一些配置

1.生成SSH密钥 
ssh-keygen -t rsa -b 4096 -C "earthcry@mail.com"

2.添加SSH公钥到GitHub
将生成的公钥内容复制并粘贴到GitHub账号的SSH密钥管理页面。通过以下命令验证
ssh -T git@github.com


3. 配置Git环境：确保Git已安装并配置了用户名和电子邮件。
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱地址"
git config -l


## edit and update 

git add .
git commit -m "change info"
git remote -v
git branch -v
git push origin main

Error in the HTTP2 framing layer
Mode of push did change to ssh from http-account


git remote remove origin
git remote add origin git@github.com:earthcry/blog.git
git push -u origin main


