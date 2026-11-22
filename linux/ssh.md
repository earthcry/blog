

# SSH

Secure Shell
安全外壳协议

用途：
- login
- transfer, sftp scp
- port transmit 22


## 生成密钥对,配置后可免密登录

### Key Client
```
$ ssh-keygen -t rsa
$ cd ~/.ssh
$ ls
```
```
 id_rsa id_rsa.pub known_hosts
```
```
$ssh-copy-id user@ip
```
Not root Only user can be ssh access

One Client links to more Servers.
```
$ touch config
$ vim config
```
```
Host rpi
  HostName 192.1698.1.1
  Port 22
  User nu
  IdentityFile ~/.ssh/rd_rsa

Host github	
  HostName http://xxx.io
  Port 22
  User nu
  IdentityFile ~/.ssh/rd_rsa
```

### Key Server

```
#cd ~/.ssh
#ls
```
```
id_rsa.pub authorized_keys
```
```
#cp rd_rsa.pub to authorized_keys
```





