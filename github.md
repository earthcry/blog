Github
# Blog

Source of earthcry.github.io.git

## Usage of githunb

## Two device modify at same time.

Order:

1. before edit, pull.
2. after edit, 
  1. first to stash, 
  2. and then pull
  3. stash apply
  4. fix
  5. add and commit
I

If commit first and then pull, to reset:
git status
git reflog
git reset --mixed HEAD^
git stash
git pull
git apply
edit fix
add , commit


## Two device push/pull to github

1. second device:
   1. cp .ssh/id_rsa ~/.ssh
   2. git clone git@github.com:earthcry/blog.git
   3. git config email && name
   4. 
   
2. 撤销提交
  - git reflog # find record number before the willback commit.
  - git rebase -i 6811234
  - rewrite the numble bad commit from "pick" to "drop"
  - git push origin HEAD --force
  - if find pubrom
  - git reset --hard 14dfdf5
  - git push origin HEAD --force
  



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

git remote -v
git branch -a
git status
git stash -l
git reflog


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


git@github.com:earthcry/blog.git


### 原生SSH协议裸仓库搭建
‌服务器初始化‌：在Linux环境下安装Git（CentOS使用yum install git，Ubuntu使用apt install git）。‌‌‌‌1
‌创建专用用户‌：
执行命令adduser git创建系统用户。
修改/home/git/.ssh/authorized_keys文件，添加开发者SSH公钥。‌‌1‌‌2
‌初始化裸仓库‌：
sudo su - git切换用户。
git init --bare project.git创建裸仓库。‌‌1‌‌3
‌权限管理‌：
使用chown -R git:git project.git确保所有权。
禁用git用户shell登录（修改/etc/passwd中git用户的shell为/usr/bin/git-shell）。‌‌

git clone user@ip:path
git remote add origin youruser@your-server-ip:~/gitrepos/myproject.git
git push -u origin main


https://github.com/kiwibrowser/src.next/releases/tag/14310011181
https://github.com/TeamAmaze/AmazeFileManager/releases/download/v3.10/app-fdroid-release.apk


Material Files

sudo -u git mkdir -p /home/git/myproject.git
sudo -u git git init --bare /home/git/myproject.git

termux开启的sshd服务用的是8022端口，执行echo "sshd" >> ~/.bashrc可让termux自动启动ssh。

ssh admin@10.041.199.36 -p 8022
git clone ssh://u0_a75@192.168.101.175:2222/~/project1.git

在Linux系统中搭建内网DNS服务主要可通过BIND或dnsmasq两种方案实现

ps -ef
pkill sshd 


压缩为.tar.gz‌：tar -czvf archive.tar.gz dir/


.gitignore

### stash

git stash list
git stash show -p

git stash 
git stash push -m "包括暂存区和工作区"

git stash -u：额外保存未追踪文件（Untracked files)。‌‌3‌‌5
git stash -a：保存所有文件（包括被.gitignore忽略的文件）。‌‌

3. 恢复修改‌。

git stash pop：应用最新记录并删除该存储项（栈结构后进先出）。‌‌3‌‌7
git stash apply stash@{n}：指定恢复任意存储项但不删除。‌‌2‌‌6
git stash branch 新分支名：基于存储时的提交创建新分支并自动应用存储。‌‌5
‌清理存储记录‌。

git stash drop stash@{n}：删除指定存储项。
git stash clear：清空所有


git clone git@github.com:earthcry/blog.git
                    .com:8022/


### GIT 教程： 分布式网络，版本控制系统。

From: liaoxuefeng.com

学习方式：
1. 阅读原文，摘抄要点。
2. 阅读原文，理清主线逻辑，消化要点。
3. 阅读原文，操作细节，练习命令。

在早上头脑清醒时，查找笔记要点，理解并自己如语言描述。
之后学习新东西，做要点笔记。
下午，做实践，
晚上，整理笔记markdown，


1 Git 是什么？解决什么问题？

对文本的多次修改，能任意回退还原的工具，特别是対大型文本，众多文本，多人修改的情況。

实例：
A：readme.txt，readme1.txt，readme2.txt，readme3.txt，readme4.txt，readme5.txt。dog3.md 

多次修改，多个文件，不方便查看，查找和后续修改。

B：
版本	文件名	用户	说明	日期
1	service.doc	张三	删除了软件服务条款5	7/12 10:38
2	service.doc	张三	增加了License人数限制	7/12 18:09
3	service.doc	李四	财务部门调整了合同金额	7/13 9:51
4	service.doc	张三	延长了免费升级周期	7/14 15:17

一个文件，一个时间线，一个表格。就表达了所有的修改。


2. 出生历史

SVN，集中式版本管理
GIT，分布式版本管理。Linux代码管理


3. 安装配置git

- [ ] Git网络终端，自报家门。
git config --global user.name, email, 


- [ ] Repository

4. 创建版本库

什么是版本库？
版本库可以简单的理解成一个目录，目录内的所有文件都可以被git管理起来，每个文件的修改删除，git都可以追踪，在任意时刻都可以回退还原。


用git的初始化一个目录，版本库就建好了。
mkdir learngit 
git init ~/learngit 
ls learngit 


- [ ] 只能追踪管理有编码的纯文本文件
只能跟踪纯文本文件的改动，无法跟踪二进制文件图片视频word文档。文本统一使用UTF-8编码。

把文件添加到版本库

- [ ] 为什么Git添加文件需要add，commit一共两步呢？因为可以多次add，一次commit。


5 时光穿梭，版本回退

- [ ] git status, git diff

- [ ] Git会把每次提交的新修改新版本，自动串成一条时间线一个分支。

- [ ] 在版本提交时间线上， Git版本移动非常快，只是移动指针。

- [ ] reflog 显示整个时间线的id和commit的注解

- [ ] 仓库  ---整个目录        /home/learngit，
- [ ] 工作区---原始文件储存区  /home/learngit，.git exclude.
- [ ] 版本库---改动储存区      /home/learngit/.git/
- [ ] 暂存区---改动暂存储存区  /home/learngit/.git/stage or index 
- [ ] 分支  ---改动分支储存区  /home/learngit/.git/master 

- head指针，分支指针指向分支时间线.

- [ ] Git跟踪管理的是修改而不是文件。

- [ ] git只提交暂存区的内容，没有添加的工作区的内容不会被提交。

- [ ] git diff HEAD -- readme.txt 查看工作区与版本库的区别

- [ ] 显示工作区文件与本地仓库最后一次提交版本之间的差异。若工作区有未提交的改动，git diff HEAD 会对比这些改动与本地仓库最新版本；若暂存区（已添加未提交的改动）有文件，则会同时显示工作区和暂存区的差异。 ‌12

常见用法
‌基本用法‌：直接运行 git diff HEAD，显示所有未提交的改动（包括工作区和暂存区）。
‌仅显示工作区改动‌：运行 git diff --cached 或 git diff --staged，仅对比工作区与暂存区的共同文件。 ‌23
‌查看历史版本差异‌：使用 git diff HEAD\~1（查看上一个版本）、git diff HEAD\~2（查看上两个版本）等命令，比较不同历史版本。 ‌1


- [ ] 版本退回，时间穿梭功能，
- git log --pretty=oneline， git reflog, 
-  Head表示当前版本，也是最新的提交，
- 上一个版本是 Head^，上上个版本是Head^^，Head\~100.
- $ git reset --hard HEAD^ 退回上一版本。
HEAD is now at e475afc add distributed
    - hard: 退回到上次已提交状态 pull not fetch
    - mixed: 退回到上次已添加，但未提交状态,
    - soft: 退回到上次未提交状态

- [ ] 反悔回退
- 只要上面的窗口没有关闭,并且还记得上次的id
- $ git reset --hard 1094a

- [ ] $ git reset HEAD readme.txt 从暂存区撤回到工作区

- [ ] $ git checkout -- readme.txt 在工作区撤销修改

- [ ] git checkout -- file命令中的--很重要，没有--，就变成了“切换到另一个分支”的命令，有横线就表示撤销未添加的修改.

git 三个区域的回退

Git 的三个核心区域（工作区、暂存区、本地仓库）回退操作如下：

工作区回退

使用 git checkout -- <file> 命令可撤销当前工作区未提交的修改，恢复为最近一次提交的状态。 ‌‌12

暂存区回退

通过 git reset HEAD <file> 可将已添加到暂存区的文件移回工作区，保留修改内容。 ‌‌12

本地仓库回退

采用 git reset 命令结合不同模式操作：

‌--soft‌：仅移动 HEAD 指针，保留暂存区和工作区内容 ‌‌34

‌--mixed‌：保留工作区内容，移除暂存区相关文件 ‌‌34

‌--hard‌：彻底丢弃工作区和暂存区修改，无法恢复（除非使用 reflog） ‌‌13

‌示例‌：

回退到最近一次提交（保留修改）
git reset --soft HEAD\~1

由于 HEAD 从 4 移动到了 3，而且在 reset 的过程中工作目录和暂存区的内容没有被清理掉，所以 4 中的改动在 reset 后就也成了工作目录新增的「工作目录和 HEAD 的差异」。这就是上面一段中所说的「重置 HEAD 所带来的差异」。

首先，Git必须知道当前版本是哪个版本，在Git中，用HEAD表示当前版本，上一个版本就是HEAD^，上上一个版本就是HEAD^^，以此类推，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100。
回退到上一版本：
git reset --hard HEAD^ 
回退到指定版本号（以1a2b3c为例）的版本：
git reset --hard 1a2b3c 
--hard 会清空工作目录和暂存区的改动,
--soft则会保留工作目录的内容，并把因为保留工作目录内容所带来的新的文件差异放进暂存区。
--mixed 参数。git reset 如果不加参数，那么默认使用 --mixed 参数。此时表示要：保留工作目录，并清空暂存区。
六、特别提示
HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令
git reset --hard commit_id
穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。
要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

作者：IOS转行ing
链接：https://juejin.cn/post/7469447752741715983
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


- [ ] git rm file 


6 远程仓库

- $ ssh-keygen -t rsa -C "youremail@example.com"
- ssh -T git@github.com 
- $ git remote add origin git@github.com:michaelliao/learngit.git
- git push -u origin master 参数关联两个分支
- $ git remote rm origin
- git clone git@github.com:michaelliao/gitskills.git
- 



7 分支

- 既是每次提交的版本串联成的的时间线。
- 分枝指针，  Master分支指针，dev分支指针,
-  Head指针指向当前分支，分枝指针指向提交。
- $ git branch dev
- $ git checkout dev  #checkout 结帐，检验，校验

Switched to branch 'dev'
- $ git checkout master
Switched to branch 'master'
- $ git merge dev 合并单位分支到当前分支
Updating d46f35e..b17d20e
Fast-forward
 readme.txt | 1 +
 1 file changed, 1 insertion(+)
- git merge命令用于合并指定分支到当前分支。
- $ git branch -d dev
Deleted branch dev (was b17d20e).
- $ git switch -c dev
- git log --graph --pretty=oneline --abbrev-commit
- 通常，合并分支时，如果可能，Git会用Fast forward模式，但这种模式下，删除分支后，会丢掉分支信息。
- 如果要强制禁用Fast forward模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。
- $ git merge --no-ff -m "merge with no-ff" dev
Merge made by the 'recursive' strategy.
 readme.txt | 1 +
 1 file changed, 1 insertion(+)
 - git stash
 - $ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 6 commits.
  (use "git push" to publish your local commits)

- $ git checkout -b issue-101
Switched to a new branch 'issue-101'

- $ git switch master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 6 commits.
  (use "git push" to publish your local commits)

- $ git merge --no-ff -m "merged bug fix 101" issue-101
Merge made by the 'recursive' strategy.
 readme.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
- git stash apply
- $ git branch
* dev
  master
$ git cherry-pick 4c805e2
[master 1d4b803] fix bug 101
 1 file changed, 1 insertion(+), 1 deletion(-)
- $ git switch -c feature-vulcan
Switched to a new branch 'feature-vulcan'
- git branch -D <name>
- $ git push origin dev
- 当你的小伙伴从远程库clone时，默认情况下，你的小伙伴只能看到本地的master分支
- $ git checkout -b dev origin/dev
- $ cat env.txt
env

$ git add env.txt

$ git commit -m "add new env"
[dev 7bd91f1] add new env
 1 file changed, 1 insertion(+)
 create mode 100644 env.txt

$ git push origin dev
To github.com:michaelliao/learngit.git
 ! [rejected]        dev -> dev (non-fast-forward)
error: failed to push some refs to 'git@github.com:michaelliao/learngit.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
- $ git branch --set-upstream-to=origin/dev dev
Branch 'dev' set up to track remote branch 'dev' from 'origin'.关联两个分支

- rebase操作可以把本地未push的分叉提交历史整理成直线；
- rebase的目的是使得我们在查看历史提交的变化时更容易，因为分叉的提交需要三方对比。
- .gitignore
- GitHub/gitignore
- # Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build
- 
https://michaelliao.github.io/gitignore-online-generator/

- 
# 排除所有.开头的隐藏文件:
.*
# 排除所有.class文件:
*.class

# 不排除.gitignore和App.class:
!.gitignore
!App.class

alins
- 
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"


步，创建证书登录：

收集所有需要登录的用户的公钥，就是他们自己的id_rsa.pub文件，把所有公钥导入到/home/git/.ssh/authorized_keys文件里，一行一个。

$ sudo chown -R git:git sample.git


git:x:1001:1001:,,,:/home/git:/bin/bash
git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell

SourceTree


