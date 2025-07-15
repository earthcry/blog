

ubnt

@mac/ip
b8:ac:6f:72:52:47 pc
ac:22:0b:48:0a:26 nexus
34:e2:fd:09:2e:af apple

@bridge, @br0, 1wan+2lan -> 1wan+1lan
# 1.del eth2 ip;
configure
delete interfaces ethernet eth2 address 192.168.2.1/24
commit

# 2.set br0, ip, eth2 >> br0
set interfaces bridge br0
set interfaces bridge br0 address 192.168.2.1/24
set interfaces ethernet eth2 bridge-group bridge br0
commit
save
exit

# 3.pc - eth2, del eth1 ip, eth1 >> br0
delete interfaces ethernet eth1 address  192.168.1.1/24
commit
set interfaces ethernet eth1 bridge-group bridge br0

# 4.del old dns, set new dns;
delete service dns forward listen-on eth1 ?
delete service dns forward listen-on eth2 ?
set service dns forward listen-on br0 ?
delete service dhcp-server shared-network-name LAN1
? set service dhcp-server shared-network-name LAN2
commit
save
exit

@offload @hardware speed @hdnat @TCP/IP减负引擎
# TOE(TCP/IP Offload Engine)网卡与一般网卡的区别:
# TCP减负引擎 网卡的工作原理与普通网卡不同。普通网卡处理每个数据包都要触发一次中断，TCP减负引擎网卡则让每个应用程序完成一次完整的数据处理进程后才触发一次中断，显著减轻服务器对中断的响应负担。
# IP offload, hw offload, hardware speed, IPv4, IPv6;
# erl3/erpoe5/er8/erp8

configure
set system offload ipv4 forwarding enable
set system offload ipv4 vlan enable
set system offload ipv4 pppoe enable
commit
save
exit
reboot

# erx/erxsfp
set system offload hwnat enable

# if sucess
show ubnt offload


@pppoe-server

configure
set service pppoe-server interface eth2

set service pppoe-server client-ip-pool start 10.180.76.101
set service pppoe-server client-ip-pool stop 10.180.76.200

set service pppoe-server dns-servers server-1 180.76.76.76
set service pppoe-server dns-servers server-2 114.114.114.114

set service pppoe-server authentication mode local

set service pppoe-server authentication local-users username user1 password p1
set service pppoe-server authentication local-users username user2 password p2
set service pppoe-server authentication local-users username user3 password p3

commit
save
# save to /config/config.boot

show pppoe-server

clear pppoe-server user user1

dm2315a@golf.gd test
dm2316a@golf.gd 1234 
dm2316b@golf.gd 1234 
dm2207@golf.gd 1234
075500762443@163.gd TDLYODYR

# dpi open, offload is off.
# <100m, not need offload.


@ssh
ssh ubnt@192.168.1.1


@ip,set ip of ubuntu/linux
# /etc/network/interface
# /etc/NetworkManager/NetworkManager.conf managed true;
# 1.dhcp ip
auto eth0
iface eth0 inet dhcp
sudo /etc/init.d/networking restart
or
$>sudo dhclient eth0
# 2.static ip
auto eth0
iface eth0 inet static
address 192.168.2.100
netmask 255.255.255.0
gateway 192.168.2.1
#network 192.168.2.0
#broadcast 192.168.2.255
sudo /etc/init.d/networking restart ?
stop: Job failed while stopping
start: Job is already running: networking
tail -f /var/log/upstart/networking.log

ifdown eth0 && ifup eth0 

# 3.set xuni ip
# 4.see hostname, set hostname
sudo /bin/hostname
sudo /bin/hostname newname xxx
# 5.set dns
method 1:
vi /etc/network/interfaces
dns-nameservers 8.8.8.8
method 2:
sudo vi /etc/resolvconf/resolv.conf.d/base
nameserver 202.96.134.133
nameserver 202.96.134.33
sudo etc/init.d/resolvconf restart
# list DNS
nmcli dev list iface eth0 | grep DNS   
# 6.pppoe


