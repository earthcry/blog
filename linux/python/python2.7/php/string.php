<?php
/*
 *  string/字符串
 *
 */
// 字符串 
// 分割匹配、查找替换；
// 分割,连接,比较,匹配,查找,替换；
//  规范、变换、比较；
//  规范化：去空和填补及大小特殊字符 函数
//
// 字符串是一种特殊数组；
// 既可看成是一个元素的常规数组；长度；
// 又可看成是多元素相连的索引数组；存取；
//
// *汉语字符串函数mb_substr();
//
// 字符串函数：
//
//
// 象数组一样访问str；
$str="hello";
echo $str[0].$str[1];
echo $str{0}.$str{1};

$s='';
for($i=0;$i<strlen($str);$i++){
    if($i%2==0)
        $s.=$str{$i};
}
echo $s;
echo strlen("中国"); //6;utf-8;

// 类型转换；
echo strlen('hello'); //5
echo strlen(10000);   //整转串后，再算，5；类型转换；

// 字符串 在内存 是连续存贮
$str="hello";
$str[2]="world";
var_dump($str); //hwllo

// @mb_汉语字符串函数
$str="hello world";
$strh="妹子你好";
echo substr($str, 0, 7);
echo mb_substr($str, 0, 7, "utf-8"); //mb_*;

//双引号识别解析数组对象
$arr=["one"=>100, "two"=>200];
class Demo{
    var $three=100;
}
$p=new Demo;
echo "aaaaaaaa{$arr[one]}aaaaaaaaaaaaaa<br>"; //100
echo "aaaaaaaa{$p->three}aaaaaaaaaaaaaa<br>"; //100


// *字符串输出函数
// echo print
//
// *格式化输出printf();
// sprintf();返回；
$int=100;
printf($int);
printf("%d, %c",$int,$int); //100, d;

// ***字符串函数***

//  规范、变换、比较；
//  分割、匹配、查找、替换；
//  
// *规范化：去空和填补及大小特殊字符 函数
/// echo die("bye")/exit();
// printf
//
//trim()/rtrim()/ltrim()
//trim($str, "delchar")
//trim($str),delspace;
trim($str, "0..9 io");
strlen(trim($str));
//str_pad(), add;
//str_pad_left
//str_pad_right
//str_pad_both

    // trim() : 
    // 字符串正规化函数；//了解特性
    // 删除杂项；
$str="   hellMo wMorld    ";
trim($str); //去两边、缩减中间空格；
trim($str, " a..z"); //从首尾算起，去掉指定字符组成的前连续字符或后

//  str_pad();
//  字符串填补函数；
str_pad($str, 10); //默认 右边，空格填充；
str_pad($str, 10, "#", STR_PDA_LEFT);

// *字符串大小写：
// strtolower();
// strtoupper();
// ucfirst();  第一个字符大写；
// ucwords();  每个词第一个大写；
//  
// *特殊意义字符---html标签 关联的 字符串格式化函数；
echo stripslashes(addslashes($title)); // 删除/添加 反斜线\
echo htmlspecialchars($title);//标签转普通字符
echo strip_tags($title, "<b><u>")  //删除标签, 只留指定的；
$str="this is a test\n";
$str.="this is a demo\n";
$str.="this is a hello\n";
echo nl2br($str);   // \n --> br
//
// *字符@变换函数；
// strrev();    前后倒置，按序列反转；
// number_format();
// md5();
//
// strlen();
$str="aaaaa";
echo count($str);
echo '<br>';
echo count("");
echo '<br>';

$str='1234567890.12345';
echo number_format($str); // 1,234,567,890千分；
echo number_format($str, 2); // 1,234,567,890.12千分；
$str='123456';
echo md5($str);
echo md5(md5($str)."lamp");
//
// *@比较函数；
// strcmp($str1,$str2); 按二进制值比较；
// strcasecmp($str1,$str2); 按二进制值比较；不区分大小写
// strnatcmp();按自然排序算法比较；
// strnatcasecmp();
$arr=["file11", "file2", "file1", "file22"];
usort($arr, "strnatcmp");
print_r($arr);


//字符串@分割、匹配、查找、替换；


//get every element by use key, 
//the key change order in(big,small).
//
//rev str:
$str="12345";
echo strrev($str).'<br>';
function revmy($str){           
    $len=strlen($str);          //such the function run once only.
    $newstr="";
    for($j=$len; $j>0; $j--){
        $newstr.=$str{$j-1};
    }
    return $newstr;
}
echo revmy($str);
echo '<br>';

//
//  number RMB eg. 12,345,678
//
$str="5967890123214352428349750294233752027439083";
//echo number_format($str);
echo rand(12345678,87654321);//8wei
echo '<br>';
echo numfmt3($str);
echo '<br>';
echo numfmt2($str);
function numfmt3($str){     //$k% --- $len%;
$len=strlen($str);
$newstr="";
for($k=0;$k<$len;$k++){
    if($k%3==$len%3 && $k!=0){
        $newstr.=',';
    }
    $newstr.=$str{$k};
}
return $newstr;
}
function numfmt2($str){          // var start out.
    $len=strlen($str);
    $newstr="";
    $start=0;
    echo $len%3;echo '<br>';
    if($len%3==2){
        $newstr=$str{0}.$str{1}.',';
        $start=2;
    }
    if($len%3==1){
        $newstr=$str{0}.',';
        $start=1;
    }
        $j=1;
    for($i=$start; $i<$len; $i++){
        $newstr.=$str{$i};
        if($j==3){
            $newstr.=',';
            $j=0;
        }
        $j++;
    }
    return $newstr;
}
function numfmt1($str){
    $len=strlen($str);
    $newstr="";
        $i=1;
    for($j=$len; $j>0; $j--){
        if($i%3==0){
            $newstr.=$str{$j-1};    //key change with $j;
            $newstr.=",";
        }else{
            $newstr.=$str{$j-1};    //key change with $j;
        }
        $i++;
    }
    $len=strlen($newstr);
    $newstr2="";
    for($j=$len;$j>0;$j--){
        $newstr2.=$newstr{$j-1};
    }
    return $newstr2;
}

//
//  get extname
//
/*
name.txt
page.class.php
c:\wamp\www/log.gif
http://dslfjlsd.inc.php
http://sdlkfjldfl.php?dfjlsdk
*/
$url="http://dsfsdfsdf.inc.php?sdafsdf";
echo extname2($url);

function extname2($url){
    $extname="";
    //strpos();                     // first position is 0, will be  false.
    //$name=strstr($url,"?",true);    // pre ? next
    if(strstr($url,"?")){
        list($file)=explode("?", $url);
    }else{
        $file=$url;
    }
    $key=strrpos($file, "/");
    $filename=substr($file,$key+1);

    $arr=explode(".", $filename);
    $extname=array_pop($arr);

    return $extname;
}


function extname($url){
    $name="";
    $len=strlen($url);
    $m=0;
    $n=$len;
    for($i=$len;$i>0;$i--){
        if($url{$i-1}=="?"){
            $n=$i-1;
        }
        if($url{$i-1}=="."){
            $m=$i-1;
            break;
        }
    }
    for($i=$m+1;$i<$n;$i++){
        $name.=$url{$i};
    }
    return $name;
}
/*
concept

write a function than count path of two files.

*/
function path($a, $b){
    $path="";
    $a=dirname($a);     // /a/b/1c/d
    $b=dirname($b);     // /a/b/12/34/56/c

    $a=trim($a, "/");
    $b=trim($b, "/");
    $a=explode("/",$a);     // array(a, b, c, d)           // str---array
    $b=explode("/",$b);     // array(a, b, 12, 34, 56, c)  // not get !same, must by order,for

    $maxlen=max(count($a), count($b));
    for($i=0; $i<$maxlen; $i++){
        if($a{$i}==$b{$i}){
            unset($a{$i});
            unset($b{$i});  //pointer pnt
        }else{
            break;
        }
    }
    $path=str_repeat("../",count($b)).implode("/", $a); // ../../c/d

    return $path;
}
$a="/a/b/c/d/e.php";
$b="/a/b/12/34/56/c/c.php";
// ../../c/d
echo path($a,$b);

