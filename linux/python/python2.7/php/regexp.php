<?php
// 
//  正则表达式
//  Regexp and PregFunction 
//
//  *正则语法
$str='/http\:\/\/www.(.*?)(org|com|net)/i'; // 筛选常见网址的
//  regexp是个字符串，由常规字符和特殊字符，与一些规则组成；
//  regexp是个筛子，函数通过它来筛选符合条件的字符；
//  两套函数，用Perl的函数；
//  分割、匹配、替换、查找；strFunc pregFunc;
//  regexp=定界符+原子+元字符+模式修正符；
//
//  pattern/model/module/模式moshi、模型moxing、模块mokuai模板muban；
//
//  preg_match_all($reg, $str, $arr);
//
//  定界符 : / /;
//  原子   : 最小的匹配单位，一个筛选条件；
//  元字符 : 对原子修饰扩展限定的，对每个筛选条件修正；
//  修正符 : 对筛子模式修正的，对所有筛选条件修正；
//
//  原子：
//  =打印字符+非打印字符；
//  1.常规字符最为原子：0-9，A-Z, a-z, _;
//  2.特殊字符和转义之后的元字符；\" \' \* \+ \? \.
//  3.一些非打印字符；\f \n \r \t \v \cx
//  4.通用字符类型作为原子；\d \D, w W, s S;数字和非数字,常规字符,空白(回车tabspace)；
//  5.自定义原子表 作为原子；[自定义][13579][^A-Za-z]^除了；
//  6.代表所有字符. ;
//
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

//  元字符：
//  *       ：匹配 >=0 次其前的原子；
//  +       ：匹配 > 1 次其前的原子；
//  ?       : 0 or 1；
//  |       : 或or ；
//  {n}     : 前面的原子恰好出现n次；
//  {n,}    : >=n;
//  {n,m}   : >=n,<=m;
//  ^或\A   : 匹配字符的头；或多行换行之后的头；/^abc/
//  $或\Z   : 尾；/abc$/
//  \b      : 匹配单词的边界；this is island.
//  \B      : 边界以外的部分；
//  ()      : 重要！大原子；/mysql*/, /(mysql)*/;
//
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
/
//  ()小括号；
//  1.优先级；
//  2.大原子；
//  3.子模式,筛中筛,小筛子；(?:)取消子模式；
//  /http\:\/\/www\.(.*)\.(com|net|org)/
  ["http://www.aaa.net", "net"] //大筛子和小筛子匹配到的结果；
//  4.反向引用
//  \1,\2代表第2个小筛子；
// 2014-08/20
'/\d{4}(-|\/)\d{2}\1\d{2}/';
//
//  修正符：
'/go*gle/ieU';
//  i       不区分大小写；
//  m       表达多行，默认都是一行；/^abc/, /abc$/
//  s       (.)可以匹配换行符；
//  x       忽略原子间的空白；/web server/x = /webserver/
//  U       贪婪,只在最后一个“句号”停下；不用，个语言间不通用w；
//          用.*?  .+?替代U；
//  e       exec，替换时，执行里面的函数；配合preg_replace();
//
$str="this is test 
abchello world 
meizi."

$str="this <b>is</b> a test <b>web</b> server.";
'/\<b\>(.*)\<\/b\>/iU';
//
//  url
$str="
        http://www.aaa.com/php/demo.inc.php?name=admin&p=123网站    
";
$reg='/(https?|ftp)\:\/\/www\.(.*?)(com|net)/([\/ \w \- \. \? \= \& \%]*)?/s';

//  email
$str="
    mei-zi@aaa.com   
    mei+zi@aaa.com.cn   
    mei.zi@aaa-bbb.com.cn   
";
$reg='/\w+([+-.]\w+)*@\w+([-.]\w+)*\.\w+/i';

$str="";
$reg='';
if(preg_match_all($reg, $str, $arr)){
    echo echo "<pre>";
        print_r($arr);
    echo "</pre>";
}else{
    echo "fail.";
}
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


//  ***分割匹配查找替换
//  字符串处理函数strFunc | 正则表达式函数pregFunc
//
//  ***@match匹配/查找
//
//    AAA.search function
//  strstr()/strpos()/substr()
//  preg_match()/preg_grep()
//
//strstr()/stristr(); return: str/false;
$str1="this is a test.";
var_dump(strstr($str1, "te", true));    // this is a /
var_dump(strstr($str1, "te")); //false  // test.
strstr($str, "test", true) //test... |...test
//
//strpos()/strrpos()/stripos(); return: number/false;
var_dump(strpos($str1, "is"));  // return: 2;
var_dump(strpos($str1, "t"));   // return: 0=false;
var_dump(strpos($str1, "t", 6));   // return: 10;
strpos($str, "t") //返回位置，0123;strrpos()从后查
//
//substr();
var_dump(substr($str1, 2, 7));   // pos,len; return: is is a;
//

function getFileName($url){
    $loc=strrpos($url, "/")+1;
    return substr($url, $loc);
}
echo getFileName($url);
function getFileName($url){
    $k1=strrpos($url, "/")+1;
    $k2=strpos($url, "?");
    return substr($url,$k1,($k2-$k1));
}

echo getFileName("http://www.aa.com/aa/demo.php");
echo getFileName("../images/logo.gif");

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

preg_match('/^\S+$/', $_POST['username']); //用户名不能为空；
preg_match($reg, $_POST['url'], $arr);
preg_match_all($reg, $_POST['url'], $arr, PREG_SET_ORDER);
//整模式与子模式 不同排序；
//
//preg_grep() 匹配数组；
$arr=["abcd1", "hel lo2", "world", "ni hao"];
$narr=preg_grep('/\d/', $arr);  //["abcd1", "hello2"];
print_r($narr);
//
//  ***分割/连接
//  BBB.@explode function
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

print_r(explode(" ", $str, 3));
print_r(preg_split('/[,.!? ]/', $str, -1, AA)); //按标点符号空格
$str='lamp';
$arr=preg_split('//', $str, -1, PREG_SPLIT_NO_EMPTY);
echo implode("-", $arr); //l-a-m-p
list($a, $b)=explode("_", "mei_zi");

//  ***@replace替换 重点
//   str_replace() 
//  preg_replace()
$nstr=str_replace("php", "java", $str, $num);//替换了几次；
$nstr=str_replace(["this", "is"], "**", $str, $num);//替换了几次；
$nstr=str_replace(["this", "is"], ["that", "are"], $str, $num);//替换了几次；
// 1.删标签；替换成 空；
$htmlTag='/\< [\/!]*? [^\<\>]*? \>/is';
$nstr=preg_replace($htmlTag, "", $str, 4); //是设置次数，不是显示
// 2.加链接；替换成 子模式；
$url='/(https?|ftp?):\/\/ (www|bbs|ftp)\.(.*?)\.(net|com|org|cn)([\/\w-\.\?\=\&\%]*)?/';
$nstr=preg_replace($url, '<a href="\1://\2.\3.\4">$1://$2.$3.$4</a>', $str);
// 3.e替换时执行里面的函数；
$nstr=preg_replace($url, strtoupper('\1://\2.\3.\4'), $str);//执行顺序：先执行里面的函数；
$url='/(https?|ftp?):\/\/ (www|bbs|ftp)\.(.*?)\.(net|com|org|cn)([\/\w-\.\?\=\&\%]*)?/e';//e
$nstr=preg_replace($url, 'strtoupper("\1://\2.\3.\4")', $str);
$nstr=preg_replace($url, '"<a href=\'$1://$2.$3.$4\'>".strtoupper("\1://\2.\3.\4")."</a>"', $str);
// 4.一次多个替换 用数组加载多个筛子，同时筛；
$str="如果http://www.baidu.com的网址<b>替换</b>正则<font color='red'>表达</font>式http://www.aaa.net使用preg_replace().";
$arr=[
    "如果http://www.baidu.com的网址<b>替换</b>正则<font color='red'>表达</font>式http://www.aaa.net使用preg_replace().",
    "如果http://www.baidu.com的网址<b>替换</b>正则<font color='red'>表达</font>式http://www.aaa.net使用preg_replace().",
    "如果http://www.baidu.com的网址<b>替换</b>正则<font color='red'>表达</font>式http://www.aaa.net使用preg_replace()."
];
$reg=[
    '/\< [\/!]*? [^\<\>]*? \>/is',      //replace html label;  //add link;
    '/(https?|ftp?):\/\/ (www|bbs|ftp)\.(.*?)\.(net|com|org|cn)([\/\w-\.\?\=\&\%]*)?/e',
    '/\d/'
];
$rep=[
    '',
    '"<a href=\'$1://$2.$3.$4\'>".strtoupper("\1://\2.\3.\4")."</a>"',
    '**'
];
$nstr=preg_replace($reg, $rep, $str);
$nstr=preg_replace($reg, $rep, $arr);

//  ***其他
//  preg_replace_callback();
$text="今天是2014-08-21，明年今天是2015-08-21."
echo $text.'<br>';
$reg="/(\d{4})(-\d{2}-\d{2})/";
function myfun($m){
    return ($m[1]+1).$m[2];
}
echo preg_replace_callback($reg, "myfun", $text);

//
//  preg_quote();
//  自动加转义线；
$text="this *is* a test";
$reg='/\*is\*/';
$reg='/'.preg_quote('*is*').'/';
echo preg_replace($reg, "##", $text);

$htmlTag='/\< [\/!]*? [^\<\>]*? \>/is';
$htmlTag='/'.preg_quote('< [/!]*? [^<>]*? >').'/is';
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
echo preg_quote($str);/
//
//
//
//
