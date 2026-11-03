<?PHP
//
//  data structure
//  mode : weibo dir concept keyword
//
//  math mode -> suanfa -> program 
//  logic structure,storage structure,
//
//  00 08 22 10 35 68
//
//  MemCache
//
//  use memcache for cache sql and session.
//
//  harddisk    file
//  harddisk    mysql     <-  sql     <-
//  ram         memcache
//  
//  php---mysql------harddisk      mysql     db,table 
//  php---memcache---memory        memcache  var
//
//  key/value in memory
//  key / value / length / time
//  name  zhang3   6       1000
//  user  feng     4       0
//
//  apache------cpu
//  memcache----ram
//  mysql-------hd
//
//  memcache is better for session.
//
//  setup : download for windows, copy, 
//  >memcached.exe -d install;
//  >memcached.exe -d uninstall;
//  >memcached.exe -d start;//restart
//  >memcached.exe -d stop;//shutdown
//  >memcached.exe -h           // help;
//  >netstat -a;                // look port 1121
//  >telnet 127.0.0.1 11211
//  >quit
//
//  often line cmd : // win cmd no ";" 
//
//  stats :
//  stats cachedump 1 0://bianli
//  add   :add name flag time length;
//         add one 1 0 10
//         1234567890
//  set   : update ;
//  get   : get one;
//  delete: delete one;
//  flush_all:
//
//










