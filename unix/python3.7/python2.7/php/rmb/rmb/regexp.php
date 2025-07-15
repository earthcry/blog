<?php
//
//  Regexp and PregFunction 
//           
//  regular expression 正则表达式 
//  Regexp is a pattern string. pattern: /原子&元字符/修正符     
//  $str="/http\:\/\/www(.*?)(com|net|org)/i";
//  分割、匹配、替换、查找；strFunc pregFunc;
//  PCRE is function library of regexp.
//
//  pattern/model/module/模式moshi、模型moxing、模块mokuai模板muban；
//  
//  定界符：常用//；
//  原子：匹配内容；
//  元字符：修饰原子；代表原子出现的次数；
//  模式修正符：修饰表达式；
//
//  preg_match_all($reg, $str, $arr);
//  1.定界符//;
//  2.原子：normal / (\d,\s,\w)[custom] / .
//      一、打印字符word+special和非打印字符space；
//      二、如是有意义字符与非转换和非字，要转义；\
//      三、子 范围定界，子 范围de系列de原子；
//          空白：空格、tab、回车、\n \r \t \f;
//          \d \D digit数字；[0-9] [^0-9] 除0-9；
//          \s \S  space空白；非打印字符；
//          \w \W  word字(0-9,A-Z,a-z,_)；//除此之外都加\; 
//      四、自定义原子表[],[13579][a-z3-9][^abc]
//      五、.   //回车除外；
//   3.元字符：出现次数 {} *
//          * + ?   w{3} k{2,5}=2,3,4,5  {2,} >=2;  *{0,} +{1,} ?{0,1}
//          ^ $     /^.....$/
//          |       (a | b)=a,b,|
//          \b \B   this is a island.  /is\b/ --> is in this.
//          
//     ()   一、大原子；reg*---reggg； (reg)*-->regregreg;
//          二、优先级；oracle|mysql   orac(le|my)sql
//          三、子模式；$arr;   /http\:\/\/www\..*?\.com/  --- http://www.***.com;
//                              /(http|https):\/\/(www|mail)\.(.*?)\.(com|net|org)/
//                              "http://www.***.com", "http", "www", "com";
//          四、取消子模式；(?:  )   (?:http|https)
//          五、反向引用；\1 \2   2014-01-24 '/\d{4}(-|\/)\d{2}\1\d{2}/' 
//              0=>,1=>,2=>       2014/01/24 "                 \\1     "           
//      优先级：
//      \
//      ()(?: )[]
//      * + ? {}
//      ^ $ \b
//      |
//   4.模式修正符：
//     /abc/i
//     m/s  默认视为一行；^ $; s可以匹配换行符；
//     x    忽略表达式中的空白；
//     A/Z ^$
//     e
//     U/?    /***/U  .*?   .+?
// 二、这则表达式的处理函数；
//      a.search
//      preg_match/preg_match_all
//      preg_grep()
//
//      strstr()/stristr()  strstr($str1, $str2[, true])
//      strpos()/strrpos()
//      substr()
//
//      b.replace
//      str_replace()/str_ireplace();//系统提供
//      1.str_replace(string, string, string);
//      2.str_replace(array, string, string);
//      3.str_replace(array, array, string);
//
//      preg_replace();//正则
//      1.同上1.；
//      2.子模式，第二个参数；
//      3.在第二个参数调用函数时，要用e修正符；
//      4.前两个参数都用数组；
//
//      分割：
//      explode();      按某个字符分割；
//      preg_split();   按模式分割；
//
//      imexplode()jion;
//
//      preg_grep();
//      preg_quote();

// 分割、匹配、查找、替换
$str="aaaaaaaaa3aa5aaaaaa77777aaaaaaaaaaaaaaa";
$reg='/\./';
$reg='/\d/';    //'' maybe see \;
$reg='/\a/';    // error; words not ad \
echo $str.'<br>';
if(preg_match_all($reg, $str, $arr)){
    print_r($arr);
}else{
    echo "Failed.";
}
echo preg_replace($reg, "#", $str).'<br>';
print_r(preg_split($reg, $str));echo '<br>'; //explode()

//get domain name from url;
//
$str="http://aaa.dict.youdao.cn.hk/action?ddd";
//$str="dd52_435@kkk.dict.youdao.com";
//|(net)
$reg='/http:\/\/(.*[^(com)|(gov)|(org)|(cn)|(co)]\.)*(.+\..[^\/]+)/i';
//$reg='/[^\d_]\w+@([0-9a-z\.*]+)\.([a-z]+)/i';
echo $str.'<br>';
if(preg_match($reg, $str, $arr)){
    echo "<pre>";
        print_r(print_r($arr));
    echo "</pre>";
}else{
    echo "Failed.";
//
// //  AAA.search function
//  strstr()/strpos()/substr()
//  preg_match()/preg_grep()
//
//strstr()/stristr(); return: str/false;
$str1="this is a test.";
var_dump(strstr($str1, "te", true));    // this is a /
var_dump(strstr($str1, "te")); //false  // test.
//
//strpos()/strrpos()/stripos(); return: number/false;
var_dump(strpos($str1, "is"));  // return: 2;
var_dump(strpos($str1, "t"));   // return: 0=false;
var_dump(strpos($str1, "t", 6));   // return: 10;
//
//substr();
var_dump(substr($str1, 2, 7));   // pos,len; return: is is a;
//
//
$url="http://www.baidu.com/demo.php?aaa=ddd&bbb=ccc";
echo getFileName($url);
function getFileName($url){
    $k1=strrpos($url, "/")+1;
    $k2=strpos($url, "?");
    return substr($url,$k1,($k2-$k1));
}
//preg_match()/preg_match_all();
//preg_match('/***/', $str, $arr);
//
//preg_grep();
$arr=array("abcd1", "hello2", "world", "ni hao");
//$content=preg_grep('/\d/', $arr);   //echo abcd1,hello2
$content=preg_grep('/\s/', $arr);   //echo abcd1,hello2
echo "<pre>";
    print_r($content);
echo "</pre>";
//
//  BBB.explode function
//
//explode()/implode()---join()
//preg_split()
//
//explode(); return: array|all;
$str="this is a test";
$content=explode(" ", $str, 3); //3 members;
echo "<pre>";
    print_r($content);
echo "</pre>";

$str1="this is a test.
    hello world,
    ni hao.";
$content=preg_split('/[,.?!]/', $str1, 3);
echo "<pre>";
    print_r($content);
echo "</pre>";
$str2="lamp";
$arr=preg_split('//', $str2, -1, PREG_SPLIT_NO_EMPTY);
print_r($arr);echo '<br>';
echo implode("---", $arr);
list($a,$b,$c,$d)=explode(" ",$str1);
//
//  CCC.replace
//
    //  str_replace()
    // preg_replace()
//
//str_replace()
$num=0;
$str="http://www.lampbrother.net/php/demo.php";

$newstr=str_replace("php", "java", $str, $num);
echo $str.'<br>';
echo $newstr.'<br>';
echo $num.'<br>';

// 替换 正常、峰哥、妹子
$num=0;
$str="这是一句正常的峰哥句子，妹子但里面有一些不能显示的文字";
$newstr=str_replace(array("正常", "峰哥", "妹子"), array("很正常", "帅气", "漂亮"), $str, $num);
echo $str.'<br>';
echo $newstr.'<br>';
echo $num.'<br>';

// replace html label.
$str="如果没有一些特殊的<b>替换</b>需求（<u>比如正则表达式</u>），你应该使用该函数替换 <font color='red'>ereg_replace()</font> 和 preg_replace()。";
$html='/<[\/|!]*?[^<>]*?>/is';
$newstr=preg_replace($html, "", $str, 4);
echo $str.'<br>';
echo $newstr.'<br><br>';

// add link in url.
// strtoupper()
$str="如果没有5一些http://www.baidu.com特殊的替换9需求（比如正则8表达式），你应http://www.lampbrother.net该使用该http://bbs.brophp.org函数7替换 <font color='red'>ereg_replace()</font> 和 preg_replace()。";
$url='/(https?|ftps?):\/\/(www|mail|bbs|ftp)\.(.*?)\.(com|net|org|cn)([\w\.\/\*\?\&\%]*)?/e';
$newstr=preg_replace($url, '"<a href=\'\1://\2.\3.\4\'>".strtoupper("$1://$2.$3.$4")."</a>"', $str);
echo $str.'<br>';
echo $newstr.'<br><br>';


// add link in url.
// strtoupper()
// replace html label
// replace digit
$str=array(
    "如果没有5一些http://www.baidu.com特殊的替换9需求（比如正则8表达式），你应http://www.lampbrother.net该使用该http://bbs.brophp.org函数7替换 <font color='red'>ereg_replace()</font> 和 preg_replace()。",
    "如果没有5一些http://www.baidu.com特殊的替换9需求（比如正则8表达式），你应http://www.lampbrother.net该使用该http://bbs.brophp.org函数7替换 <font color='red'>ereg_replace()</font> 和 preg_replace()。",
    "如果没有5一些http://www.baidu.com特殊的替换9需求（比如正则8表达式），你应http://www.lampbrother.net该使用该http://bbs.brophp.org函数7替换 <font color='red'>ereg_replace()</font> 和 preg_replace()。"
);
$reg=array(
    '/<[\/|!]*?[^<>]*?>/is',
    '/(https?|ftps?):\/\/(www|mail|bbs|ftp)\.(.*?)\.(com|net|org|cn)([\w\.\/\*\?\&\%]*)?/e',
    '/\d/'
);
$rep=array(
    '',
    '"<a href=\'\1://\2.\3.\4\'>".strtoupper("$1://$2.$3.$4")."</a>"',
    '**'
);
$newstr=preg_replace($reg, $rep, $str);
echo "<pre>";
    print_r($str);
    print_r($newstr);
echo "</pre>";

//
//  DDD.other function
//
//  preg_replace_callback
$text="今天是2014-02-14， 明年2015-02-14你和谁在一起？";
echo $text.'<br>';
$reg='/(\d{4})(-\d{2}-\d{2})/';
function myfun($m){
    return ($m[1]+1).$m[2]; 
}
echo preg_replace_callback($reg, "myfun", $text);
echo '<br><br>';
//
//
//
//
$pattern="/\d{4}(\W)\d{2}\\1\d{2}\s+\d{2}(\W)\d{2}\\2\d{2}\s+(?:am|pm)/";
$string="today is 2010-09-15 15:35:39 pm...";

$pattern="/abc$/im";
$string="sddfjdlkajf\nabcdfssldfjabc\nasldkjf";

$pattern="/a.c/is";
$string="aaaaaaaaaaaaa\ncaaaaaaaaaa";

$pattern="/this\s?is test/isx";
$string="aaaaaaaaaaaaa\ncaaaathis istestaaaaaa";

//border: solid 1px gray;
//border-width: 0 0 1px 1px;


$pattern="/\<b\>(.*?)\<\/b\>/i";
$string="<b>hello</b>aaa<b>php</b>aaaaaaaxcaaaathis istesta<b>lamp</b>aaaaa";
if(preg_match_all($pattern, $string, $arr)){
    echo "正则表达式:<b> {$pattern} </b>和字符串:<b> {$string} </b>匹配成功<br>";
     echo "<pre>";
         print_r($arr);
    echo "</pre>";
}else{
    echo "<font color='red'>正则表达式<b>{$pattern}</b>和字符串<b>{$string}</b>匹配失败</font>";
}

$str="这是一个正则http://www.baidu.com表达式的匹配函数
这是一个正则http://www.baidu1.com表达式的匹配函数
这是一个正则https://www.baidu2.org表达式的匹配函数
这是一个正则http://mail.baidu3.com表达式的匹配函数
这是一个正则https://news.baidu4.net表达式的匹配函数
这是一个正则ftps://www.baidu5.cn表达式的匹配函数
这是一个正则ftp://www.baidu6.com表达式的匹配函数
这是一个正则http://www.baidu7.com表达式的匹配函数
";
$url="/(https?|ftps?):\/\/((www|mail|news)\.([^\.\/]+)\.(com|net|org))/i";
if(preg_match_all($url, $str, $arr)){
    echo "<pre>";
        print_r($arr);
    echo "</pre>";
}else{
    echo "no url";
}
echo $str.'<br>';

foreach($arr[0] as $url){
    $str=str_replace($url, '<a href="'.$url.'">'.$url.'</a>', $str);
}
echo $str.'<br>';
echo strstr("this is a test hello", "test").'<br>';
echo strstr("this is a dtest hello", 100).'<br>';
if(stristr("this is test", "Test")){}

echo getFile('http://www.baidu.com/index.php').'<br>';
echo getFile('/url/www/index.jsp').'<br>';
echo getFile('../../images/bgcolor.gif').'<br>';
echo getFile('c:/hello/demo.rar').'<br>';
function getFile($url){
    $pos=strrpos($url, "/")+1;
    $filename=substr($url, $pos);
    return $filename;
}
$str="http:www.baidu.com/baidu/index.php";
$search="baidu";
$replace="google";
$newstr=str_replace($search, $replace, $str, $count);
echo $newstr.'<br>';
echo $count.'<br>';

$str="这则表达php式的处理函数php这则表达式的处理函数这则linux表达式的mysql处理函数这则表达式的处理函数Mysql这则表达式的处理函apache数这则表达式的处lamp理函数这则表达式的处理函数这则表达式的处理函数这则表达式的处理函数这则表达式的处理函数这则表达式的处理函数这则表达式的处理函数这则表达式的处理函数";
$count=0;
$search=array("lamp", "apache", "linux", "mysql", "php");
$replace=array("j2ee", "tomcat", "windows", "oracle", "jsp");
$newstr=str_ireplace($search, $replace, $str, $count);
echo $newstr.'<br>';
echo $count.'<br>';
 $str=" 字符串中php的替换函数，系统提供的 字符串中的替换函数，系统提供的 字符串中的替换函数，系统提供的 字符串中的替换函数，系统提供的 字lamp符串中的替换函数，[b]系统php提供的 字符串中[/b]的替换函数，系统提供php的 字符串中的替换函数，系统提供的 字符串中的替换函数，系统提供的 字符<b>apache</b>串中的替换函数，系统提供的 [u]mysql字符串中的替换函[/u]数，系统Apache提供的 字符串中的MySQL替换函数，系php统提供的 [i]字符串中的替换函数[/i]，系统提供的[size=7] 字符串中的php替换[/size]函数，系统提供的[color=Magenta] 字linux符串中的替[/color]换mysql函数，系统提供的php 字符串中的替换函数，系统提供的 字符串中的替换函数，系统php提供的 字符串中的替换函数，系统提供的 字[align=center]符串[b]系统php提供的 字符串中[/b]中的替换函数[/align]，系[b]系统php提供的 字符串中[/b]统提php供的 字符串中的替换函数，系统提供的";
echo $str.'<br>'.'<br>';
//echo preg_replace("/\w/",'' , $str, 6).'<br>';
//echo preg_replace("/(\w)/ie",'strtoupper("\1")' , $str, 20).'<br>';
//echo preg_replace("/([a-z]+)/ei",'"<font color=\"red\">"'.'.strtoupper("\1").'.'"<font>"' , $str).'<br>';
//
$ubbcodes=array(
    '/\[b\](.*?)\[\/b\]/i',
    '/\[u\](.*?)\[\/u\]/i',
    '/\[i\](.*?)\[\/i\]/i',
    '/\[color=(.*?)\](.*?)\[\/color\]/i',
    '/\[size=(.*?)\](.*?)\[\/size\]/i',
    '/\[align=(.*?)\](.*?)\[\/align\]/i'
);
$htmls=array(
    '<b>\1</b>',
    '<u>\1</u>',
    '<i>\1</i>',
    '<font color="\1">\2</font>',
    '<font size="\1">\2</font>',
    '<p align="\1">\2</p>'
);
echo preg_replace($ubbcodes, $htmls, $str);

 $str=" 字符串中php的替换函数，系统提供的 字符串中的替换函数，系统提供的 字符串中的替换函数，系统提供的 字符串中的替换函数，系统提供的 字lamp符串中的替换函数，[b]系统php提供的 字符串中[/b]的替换函数，系统提供php的 字符串中的替换函数，系统提供的 字符串中的替换函数，系统提供的 字符<b>apache</b>串中的替换函数，系统提供的 [u]mysql字符串中的替换函[/u]数，系统Apache提供的 字符串中的MySQL替换函数，系php统提供的 [i]字符串中的替换函数[/i]，系统提供的[size=7] 字符串中的php替换[/size]函数，系统提供的[color=Magenta] 字linux符串中的替[/color]换mysql函数，系统提供的php 字符串中的替换函数，系统提供的 字符串中的替换函数，系统php提供的 字符串中的替换函数，系统提供的 字[align=center]符串[b]系统php提供的 字符串中[/b]中的替换函数[/align]，系[b]系统php提供的 字符串中[/b]统提php供的 字符串中的替换函数，系统提供的";

$string="192.168.1.128";
$arr=explode(".", $string);         //按特殊字符分割；
print_r($arr);echo '<br>';

$arrs=preg_split('/[，.?!]/', $str);//按模式分割；
print_r($arrs);echo '<br>';
echo count($arrs);
echo implode("====", $arrs);
 */

$arr=array("zhang san", "lisi", "wang5", "zhao6", "hello", "ni hao");
//print_r(preg_grep('/\s/', $arr));
print_r(preg_grep('/^\S+$/', $arr));echo '<br>';

$str="ab+cd*ef}g";
echo preg_quote($str);
