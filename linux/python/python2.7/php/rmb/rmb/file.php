<?php
// 1.filetype();
// file_exists();is_file();is_dir();
// is_array();is_int();	is_string();is_null;is_bool();
// is_uploaded_file;is_link -- 是否为一个符号连接
//
// 2.property:
// is_readable();is_writable();is_executable
// filectime();filemtime();fileatime();filesize();
// date_default_timezone_set("prc");
// $size=round($size/pow(2, 40),2),TB;
// stat(demo.txt);
//
// 3.path:
// .  current dir;
// .. up grade dir;
//  / window or linux
//  / root dir/sysroot or webroot
// dir:basename(url), dirname(), pathinfo();
// 
// 4.file operate:           handle
// touch()/unlink()/rename()/copy();
//
// 5.permission
//   ls-l or ll; _rwxrwxrwx 777 文件拥有者/拥有者所在组/其他用户
//   _文件类型 d目录 l b
//   r w x 4 2 1 777 4+2+1
//
//   chmod u=rwx,g=rw,o=x
//   chmod 777 demo.php
//   chown mysql demo.php
//   chgrp apache demo.php
//   filegroup
//   fileowner
//
//  6.file read and write
//      path/url=dir+filename
//      file_get_contents()
//      file_put_contents(url,str)
//      readfile();echo direct;download;
//      $lines=file("test.txt");echo count($lines);
//      fopen(url,r+)/fclose();
//          r,r+;w,w+,a,a+;b/binary;t/txt;rb,wb,rt,wt/window.linux;
//          fwrite(filename, str);
//          fread();    //a length of number;
//          fgetc();    //read one char;
//          fgets();    //read one line;
//              feof($file);if read to error or read to end, then return true.
//
//  7.file seek
//      ftell($file);
//      fseek($file, 10);
//      fread();
//      rewind();
//  
//  8.file lock
//
//  9.dir handle
//
//  10.file upload and download
//
$url1="./aaa/bbb/index.php";
$url2="../www/yyy/login.rar";
$url3="c:/appserv/www/demo.html";
$url4="http://localhost/yyy/www.gif";

echo basename($url1).'<br>';
echo dirname($url1).'<br>';
echo dirname(dirname($url1)).'<br>';
echo "<pre>";
    print_r(pathinfo($url3));
echo "</pre>";

touch("./apache.php");
unlink("c:/appserv/www/apache.php");
rename("./test.txt", "c:/test2.txt");
copy("c:/test2.txt", "./test3.txt");

chmod("/aaa/index.php", "755");

$str=file_get_contents("http://www.wowody.net/Meiju/");
preg_match_all('/\<img\s+.*?\>/i', $str, $images);
$imgs="";
foreach($images[0] as $img){
    $imgs.=$img.'<br>';
    echo $img.'<br>';
}

if(isset($_POST[sub])){
    setConfig($_POST);
}
function setConfig($post){
    //read file
    $str=file_get_contents("config.inc.php");
    //mod file
    $zz=array();
    $rep=array();
    foreach($post as $key=>$val){
        $zz[]="/define\(\"{$key}\",\s*.*?\);/i";
        $rep[]="define(\"{$key}\",\"{$val}\");";
    }
    echo "<pre>";
        print_r($zz);
        print_r($rep);
    echo "</pre>";
    $str=preg_replace($zz, $rep, $str);
    //write file
    file_put_contents("config.inc.php", $str);
}


<form action="test2.php" method="post">
    <p>host:<input type="text" name="DB_HOST"></p>
    <p>user:<input type="text" name="DB_USER"></p>
    <p>pass:<input type="text" name="DB_PWD"></p>
    <p>dbname:<input type="text" name="DB_NAME"></p>
    <p>tabPREFIX:<input type="text" name="TAB_PREFIX"></p>
    <p><input type="submit" name="sub" value="mod"></p>
</form>

$str="";
$lines=file("lampcms.sql");
foreach($lines as $line){
    $line=trim($line);
    if($line!=""){
        if(!($line{0}=="#" || $line{0}.$line{1}=="--")){
            $str.=$line;
        }
    }
}
$str=rtrim($str, ";");
$arr=explode(";", $str);
echo "<pre>";
    print_r($arr);
echo "</pre>";

$file=fopen("./test.txt", "w");
for($i=0;$i<100;$i++){
    fwrite($file, "www.google.com{$i}\n");
}

fclose($file);

//$file=fopen("./test.txt", "r");
//echo fread($file, filesize("./test.txt"));
$file=fopen("http://www.huxiu.com", "r");
$str="";
while(!feof($file)){
    $str.=fread($file, 1024);
}
echo $str;

fclose($file);

$file=fopen("./test.txt", "r");
echo ftell($file).'<br>';
echo fread($file, 10).'<br>';
echo ftell($file).'<br>';
echo fread($file, 10).'<br>';
echo ftell($file).'<br>';
fseek($file, 100, SEEK_CUR);
echo fread($file, 10).'<br>';
echo ftell($file).'<br>';

fseek($file, -20, SEEK_END);
echo fread($file, 20).'<br>';
echo ftell($file).'<br>';
rewind($file);
echo ftell($file).'<br>';

fclose($file);


date_default_timezone_set("prc");
$dt=date("Y-m-d H:i:s", time());
$mess="data.txt";
if(isset($_POST[sub])){
   $strmess=$_POST["username"].'<l>'.$_POST["title"].'<l>'.$_POST["body"].'<l>'.$dt.'<n>';  
   write($mess, $strmess); 
   if(file_exists($mess)){
        $con=read($mess);
        $con=rtrim($con, "<n>");
        $arr=explode("<n>", $con);
            foreach($arr as $line){
                $cols=explode("<l>", $line);  //list($name, $title);
                echo $cols[0].' : '.$cols[1].'||'.$cols[2].'||'.$cols[3].'<br>';
            }
   }
}

function read($filename){
    $file=fopen($filename, "r");
    if(flock($file, LOCK_SH)){
        $con=fread($file, filesize($filename));
        flock($file, LOCK_UN);
    }
    fclose($file);
    return $con;
}
function write($filename, $mess){
    $file=fopen($filename, "a");
    if(flock($file, LOCK_EX)){
        fwrite($file, $mess);
        flock($file, LOCK_UN);
    }
    fclose($file);
    
}
//   tiny to file;design same long;
//   small to xml;
//   big to database;

<form action="test2.php" method="post">
    username:<input type="text" name="username"><br>
    title:<input type="text" name="title"><br>
    body:<input type="text" name="body"><br>
    <input type="submit" name="sub" value="msg"><br>
</form>
*  
****************************************************************
*  file operate: touch/unlink/rename/copy/read (sys inside) 
*  dir  operate: mkdir/del   /cute  /copy/size/traverse(custom)
* 
*   opendir()
*   readdir()
*   closedir()
*   rewinddir()
*
date_default_timezone_set("prc");
$dt=date("Y-m-d H:i:s", time());
$dirname="phpMyAdmin";
echo chdw(dirsize($dirname)).'<br>';
$dir=opendir($dirname);
//readdir($dir);
//readdir($dir);
while($filename=readdir($dir)){
    $file=$dirname.'/'.$filename;   //dir of no upgrade dir is not a real dir.
    if($filename!="." && $filename!=".."){
        if(is_dir($file)){
            $dt=date("Y-m-d H:i:s", filectime($file));
            echo "<font color='red'>{$filename}--".$dt."---".filetype($file)."---".chdw(dirsize($file))."----</font>".'<br>';
        }else{
            $dt=date("Y-m-d H:i:s", filectime($file));
            echo "<font color='green'>{$filename}--".$dt."---".filetype($file)."--".chdw(filesize($file))."-----</font>".'<br>';
        }
    }
}
function chdw($size){
    $dw="Bytes";
    if($size > pow(2, 30)){
        $size=round($size/pow(2, 30), 2);
        $dw="GB";
    }elseif($size > pow(2, 20)){
        $size=round($size/pow(2, 20), 2);
        $dw="MB";
    }elseif($size > pow(2, 10)){
        $size=round($size/pow(2, 10), 2);
        $dw="KB";
    }else{
        $dw="Bytes";
    }
    return $size.$dw;
}

function dirsize($dirname){
    $dirsize=0;
    $dirRSC=opendir($dirname);
    while($filename=readdir($dirRSC)){
        $file=$dirname.'/'.$filename;
        if($filename!="." && $filename!=".."){
            if(is_dir($file)){
                $dirsize+=dirsize($file);
            }else{
                $dirsize+=filesize($file);
            } 
        }
    }
    closedir($dirRSC);
    return $dirsize;
}
closedir($dir);


$dirname="phpMyAdmin";
//mkdir("uploads", "755");
//rmdir("uploads");
//copydir("c:/aaa", "./bbb/ddd");
function copydir($dirsrc, $dirdst){
    if(is_file($dirdst)){
        echo $dirdst.' is not a dir.';
        exit;
    }
    if(!file_exists($dirdst)){
        mkdir($dirdst);
    }
    $dirrsc=opendir($dirsrc);
    while($filename=readdir($dirrsc)){
        if($filename!="." && $filename!=".."){
            $file1=$dirsrc."/".$filename;
            $file2=$dirdst."/".$filename;
            if(is_dir($file1)){
                copydir($file1, $file2);
            }else{
                copy($file1, $file2);
            }
        }
    }
    closedir($dirrsc);
}

function getbasename($path){
    if(is_int(strrpos($path, "/"))){
        $pos=strrpos($path, "/")+1;
        $basename=substr($path, $pos);
        return $basename;
    }else{
        return $path;
    }
}

function deldir($dirname){
    if(file_exists($dirname)){
        $dirRSC=opendir($dirname);
        while($filename=readdir($dirRSC)){
            if($filename!="." && $filename!=".."){
                $file=$dirname."/".$filename;
                if(is_dir($file)){
                    deldir($file);
                }else{
                    unlink($file);
                    echo "<font color='green'>del file {$file} success.</font><br>";
                }
            }
        }
        closedir($dirRSC);
    }
    rmdir($dirname);
    echo "<font color='#ff0000'>del dir {$dirname} success.</font><br>";
}
*********************download*************************************
 */
	header("Content-Type:image/gif");
	header('Content-Disposition: attachment; filename="logo3333.gif"');
	header('Content-Length:'.filesize("logo.gif"));
	readfile("logo.gif");
?>
<br>
<a href="down.php">logo.gif</a>
