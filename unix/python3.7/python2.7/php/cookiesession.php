<?php
/*
 *
http
hyper text transfer protocol

http base tcp/ip.
数据传输过程；
计算机网络；系统互联，七层传输模型；
baike/OSI模型/OSI参考模型/OSI七层模型；
socket网络编程，TCP,UDP；
UDP,不安全，不可靠；
TCP,C/S架构，规模百千级；
HTTP，B/S架构，规模万万级
请求响应后，会及时释放、无状态；
http请求，响应，方式，状态码，URI,MIME等；
请求：
1.请求行；
2.信息头；
3.内容；
响应；
1.响应行;200 ok
2.响应头;header();
3.内容；echo ***;
page中有<img>会再建立连接；
点超链接会触发新HTTP连接；
一个TCP可以建多个HTTP;
多个HTTP可以重叠；
    格式：
消息行;
多个消息头;
一个空行;
消息内容;
常用状态码；
200 ok
302/307 临时重定向；
304 未修改；
404 找不到；
500 内部错误；
google chrome 查看link status

var type:
page:       var;
pages:      get;        少量数据，
website:    session;    临时数据，数量万万级;
global:     file,db;    长久存储，存取耗时;

cookie  健身会员卡；
ie /sets and doc/user/cookies
chrome sets
$username="meizi";
setCookie("username", $username, time()+60*60*24);  // send in header.
setCookie("arr[0]", $aaa, time()+60*60*24);         // send in header.
setCookie("arr[1]", $bbb, time()+0);                // 0 is current session.
echo 'save success.';      //first  access display  // send in body.
echo $_COOKIE['arr[0]'];   //second access display  //cookie values in file-->ie---header---svr--$_COOKIE  
// del cookie
// expire 过期即可
setcookie("username",'',time()-3600);



session

原理，技术无难点；

开启会话session(cookie不用),session_start()前无任何输出；\
other pages session_start also,and readwrite in $_session.

*/
//start session and store user in it in page1.
session_start();
//send session_id to client and server.
//start php.session.
//read and write session in page2.
$_SESSION['username']="aaa";
echo session_name()." = ".session_id().'<br>';
//destroy session in page3.
$username=$_SESSION['username'];

//del session
//del in ram
//unset($_SESSION['username']);
$_SESSION=array();
//del session_id at client.
if(isset($_COOKIE[session_name()])){
   setCookie(session_name(),"",time()-3600, "/");
}
//del session file at server.
session_destroy();
echo 'bye '.$username;

// session sets      php.ini
// session.auto_start //not use, for class init before session.
// session.save_path=
// session.cookie_lifetime=0
//
// session.gc_maxlifetime=15  //destroy/reback.
// session.gc_divisor=10      //access 10 times;
// session.gc_probability=1   //del once;
//
// url pass session id,when client diable cookie.
// window use SID.   
echo '<a href="one.php?<?php echo SID; ?>">page</a>';
//      Linux
// enable-trans-sid           
// session.use_trans_sid
//
$sid=$_GET[session_name()];
if(!empty($sid)){
    session_id($sid);       // set use exits sid;
}
session_start();


// custom session handler
//
// php.ini
// session.save_handler=file
//
// session.save_handler=memcatche
// session.save_path="tcp://localhost:11211;tcp://192.168.1.137:11211"

// session.save_handler=user
// session.php
session_set_save_handler("open","close","read","write","destroy","gc");
function open(){}
function close(){}
function read(){}
function write(){}
function destroy(){}
function gc(){}
//
















