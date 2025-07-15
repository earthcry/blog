#!/bin/sh
#cp .ssh
#cp /var/cache/apt/archives
#cp -pR /home/nu/kuaipan/* /home/nu/nucore
#cp .goldendict/history
tar -zcvpf /home/nudb/nubak/kuaipan-`date '+%Y-%m-%d'`.tar.gz -C /home/nu/kuaipan .
kuaipan4uk
