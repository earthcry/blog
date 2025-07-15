<?php
/*
//
//  php base syn 
//  
//
//  
//  web2.0 1.mbl link; 2.ew; 3.object net; 4.cloud 
//  biaozhun;
//  script:
//  c++ ------------------bnr---cpu---display;
//  html--------browser---bnr---cpu---display;
//  script--ts-srv--brs---bnr---cpu---display;
//
//
//  1.php cmd fengefu ";"; // 指令、命令分隔符。
//      execute   功能执行语句；必加；执行一个功能；
//      structure 代码结构语句；不加
//  2.note ; 注释；
//      // sing line note; 
//      #  cmd line note;
//      /* ... */ multilines note;
//      /** ... */ file note;
//  3.blank:
//      空格、Tab、换行；------无关紧要；----可增加可读性；
//  4.variable
//      varname, varadd, varspace;
//      var <-- data;
//      var_dump();isset();empty();unset;
//
//      $a=&$b;别名；指针；地址；
//      &var, no data and no 常量
//      unset($b);$a还在；
//
//  5.弱类型，类型是由存的值决定的。
//      bool false;
//      int   0   ;
//      float 0.0 ;
//      string "","0";
//      array();
//      null;
//      all arthor are true;
//  6.int float/double
//      ord(a);//97;
//      进制；边界；
//      int : 0 0000000 00000000 00000000 01101000;64+32+8=104;h;
//      第一个0为+-符号位，最大为2的31次方2^31；
//      float:64;
//      进制：time,60; linux权限0755,8; color,#fff000,16;
//  7.string
//      "": parse var and use "\";转义符；'' not can;
//      \n换行；\r回车；\t Tab;
/*      $str=<<<customstr

customstr;
    8.data type
        a.force to trans;settype();
            $d=(string)$int;//not change $int type.
            //int/bool/fload/double/real/string/array/object;
            intval();floatval();strval();
        b.self to  trans;all to numb;
        c.if function
            is_bool()/is_int()/is_string()/is_array()/is_objece
            /is_resource()/is_null/is_scalar()/
            /is_numberic()/if num or numstr
            /is_callable()/if real function name;
            empty()/is_null;
    9.constant 
        define("ROOT", "localhost");
        defined;cst;
        get_defined_constants();get all constant;
        M_PI;
        magic constant;
    10.割舍
        var_dump()/false--echo--blank(null);true--echo--1;
    11.位运算符
        & | 
        位运算符不会短路；
        位运算 通常 当做 不短路的 逻辑运算符；
    12.其他运算符
        @ 临时屏蔽 error msg;
        `` 系统命令 `ls -hl`

2----10-------2^1
3----11--------------=2+1=2^1+2^0
4----100------2^2
5----101-------------=4+1=2^2+2^0
6----110
7----111
8----1000-----2^3

hello world
h e l o
ord(h);//104
104=64+32+8=2^6+2^5+2^3
0 0000000 00000000 00000000 01101000 = 104

12 & 13 =
12 = 8 + 4;
13 = 8 + 4 + 1;
00000000 00000000 00000000 00001100
00000000 00000000 00000000 00001101 &
--------------------------------------------
00000000 00000000 00000000 00001100
8+4=12;
var_dump(12 & 13);//12
var_dump('A' & 'a');
65 = 64 + 1      = 01000001
97 = 64 + 32 + 1 = 01100001 &
----------------------------------
                   01000001

var_dump('A' & 97);
var_dump(0 & 97);



*/
//
//  
//

echo ord("h");  echo '<br>';
echo 077;       echo '<br>';
echo 0xff;      echo '<br>';

$a=300000000000000000000; //3.0E+17;
var_dump($a);

$str='this is a \'demo\'.';     echo $str;      echo '<br>';
$str="this is a \"demo\".";     echo $str;      echo '<br>';
$str=<<<customstr
dsfjsdofj
sdofiosd
    kldjfl
dsfj
    dsjofj
customstr;

// the good
$a=0;$b=0;
if($a=3 && $b=3){
    $a++;
    $b++;
}
var_dump($a);
echo $a.",".$b;

true + false = 1;
var_dump(true & false);//int 0
$a=10;
if($a>5 & $a<100){echo "aaa";}

$a=3;$b=5;
if($a>5 & $b++ < 100){}//&&/位运算不 短路
echo $b;










PHP基本语法：

1.变量@var
2.常量@constant
3.数据类型@dataType，类型转换@typeChange
4.运算符@operators，表达式

指令分隔符：分号；
功能语句；结构语句
多行注释，文档注释；
空白调整；

1.@var
* 变量常量
 *
*变量的表达、赋值声明、作用范围、存储的数据类型及其转换、判断测试;
*变量是在代码中临时指代存储数据的容器，指代存储的数据叫值，指代； 
*变量，是为了方便多次引用/编辑同一个数据，而引入的； 

*$string; 
*变量常量名称区分大小写； 
*PHP中直接赋值使用，类型由上下文决定； 
* 
*变量的使用范围： 
*从声明处到文件尾，也包括include/require引入的文件，
*如果使用cookie/session,还可以在多个页面中使用； 
* 
*变量的存在、释放、为空、类型：isset();unset();empty()？1;var_dump(); 
 */

    // 可变变量；$$var
	$one="#########";
    $two="one";

    echo $$two."<br>";

    // 引用变量，别名;引用赋值；&$var;关联变化；
    // & 取地址符号；只有变量才有地址；数字没地址；
    $one=10;    //two为one的别名;
	$two=&$one; //引用变量two存了one的地址，规定存地址的var的值为。。。
	$two="hello";

	echo $one."<br>";  // hello
	echo $two."<br>";  // hello
    unset($one);       // 释放变量名；
	echo $two."<br>";  // hello

/* 2.@constant
 * 常量的声明与使用
 *      1. 常量是一个简单值的标识符
 *      2. 常量定义后不能再改变他的值，也不能使用unset()取消
 *      3.常量可以不用理会变量范围的规则而在任何地方都可以定义和访问
 *      4.常量使用define("常量名"， 值);
 *      6.常量名称习惯都使用大写
 *      7.常量的值只能用标量类型（int, float, bool, string）
 *      8.常量一定要在声明时就给值
 *      9.defined("常量");//查看常量存在；变量是isset();
*常量的表达、定义、特性、作用范围、预定义常量和魔术常量; * 
 *  固定常量、预定义常量和魔术常量get_defined_constants()all;
 */

	define("CON_INT", 100);          	//声明一个名为CON_INT的常量，值为整型100
	echo CON_INT;                  		//使用常量，输出整数值100

	define("FLO", 99.99);             	//声明一个名为FLO的常量，值为浮点数99.99
	echo FLO;                      		//使用常量，输出浮点数值99.99
	
	define("BOO", true);             	//声明一个名为BOO的常量，值为布尔型true
	echo BOO;                     		//使用常量，输出整数1

	//声明一个名为CONSTANT的常量，值为字符串hello, world.
	define("CONSTANT", "Hello world.");ctt 
	echo CONSTANT;              		//输出字符串 "Hello world."
	echo Constant;                  	//输出字符串"Constant" 和问题通知
    
	//声明一字符串常量GREETING, 使用第三个参数传入true值，常数将会定义成不区分大小写
	define("GREETING", "Hello you.", true);
	echo GREETING;              		//输出字符串 "Hello you."
	echo Greeting;                 		//输出字符串 "Hello you.""
     
	//使用defined()函数，检查常量CONSTANT是否存在，如果存在则输出常量的值
	if (defined('CONSTANT')) {
   		 echo CONSTANT;
	}

//固定魔术预定义常量
echo M_PI;
echo __FILE__."<br>";
echo __LINE__."<br>";
echo PHP_VERSION."<br>";
echo PHP_OS."<br>";

    //常量变量的范围、特性
    define("HOME", "http://www.aaa.com");
    $a='hello';
    $a=200;

	function demo(){
        echo $a.'aaa'.'<br>';          // aaa
		global $a;
		echo $a.'<br>';                // 200
		echo HOME.'<br>'.'<br>';       // http://www.aaa.com
	}
    demo().'<br>';

	define("HOME", "2222222222222");
    if(defined("HOME")){
	    echo HOME.'<br>';               // http://www.aaa.com
    }



// 3.@dataType
// 数据类型：var_dump()
//     四种标量：布尔、整型、浮点、字符串；bool, int, float/double, string;
//     两种复合：数组、对象；array(), object;
//     两种特殊：资源、空；resource, NULL;
//
//
	$int=10;   //十进制声明
    $int=-5; 
	$int=045;  //以0开头的表示以8进制声明一个变量
	$int=0xff; //以0x或0X开头的表示以16进制声明一个变量 0-9 a-f 0X A-F
    echo PHP_INT_MAX.'<br>'  
	//整数的最大值 4字节   32位系统为2的32次方， 214483647

	$float=3.14E5;
	$float=3.15e+5;
	$float=5.14E-2;  //E可以大写也可以小写

	//以下都是false的情况
	var_dump((bool) " ");echo '<br>';     //true  有空格的为真；
if(false){echo "dddd".'<br>';}
if(0){echo "d".'<br>';}
if("0"){echo "x".'<br>';}
if(""){echo "dd".'<br>';}
if(array()){echo "ddddd".'<br>';}
if(null){echo "ddd".'<br>';}
false==0,null==0;
其他值被认为为真,包括任何资源类型；
    echo true;  //1;
    echo false; //空；

	//字符串的声明有多种方法
	//1. 单引号和双引号都可以声明字符串
	//2. 声明的字符串没有长度限制
	//3. 在双引号的字符串中，即可以直接解析变量，又可以直接使用转义字符
	//4. 在单引号的字符串中，不可以解析变量，也不可以使用转义字符(可以以转义单引号本身，也可以转义转义字符"\")
	//5. 在双引号中不能再使用双引号， 在单引号中不能使用单引号
	//6. 最好使用单引号,只有双引号可以套单引号；
    //7. 可以使用转义字符\;

	//定界符号声明字符串， 大量字符串
	//hello是自定义的一个字符串，他后面不能有任何字符，空格也不可以
	//也要以这个字符串结束，但结束前也不能有任何字符
    $int=100;
    $str="aa{$int}aaa\naaa$int,aaa\raaa\taaa${int}aaa\$intaa\"aaaaa<br>";
    $str2='aa{$int}aaa\naaa$int,aaa\raaa\taaa${int}aaa\$intaa\"aa\'aaa<br>';
	$str1=<<<eot
		dsafiw" rkd{$int}jrekjf\nds"hfkefhdsfdsaf
		dsafjue'wkjfds"au${int}fed'sa\rfdsafdsfsd<br>
eot;
    $str11=<<<'st'
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa;
st;
    echo $str;
    echo $str1;
    echo $str2;

    /* @typeChange
     * 数据类型之间相互转换
 * 	一种是强制转换：
 *		改变原变量的类型:
 * 		setType(变量， 类型); 
 * 		    //类型int, integer, float, double,real, 
 * 		    //bool, boolena, string, array, object
 *
 *		不改变原变量的类型，在赋值前使用(类型)的形式:
 *		$a=(int)"123abc";
 *		
 *		$变量=intval(变量或值);
 *		$变量=floatval(变量或值);
 *		$变量=stringval(变量或值);
 *
 *		注意： 整型在内存中占4个字节，  2.147e9
 *			浮点型在内存中点8个字节
 *
 * 		字符串
 *
 * 	一种自动转换 ： 最常用的方式，因为这种我们开发时不用去管理类型，变量会根据运行环境自动转换 
 * 	   算术运算：其他类型自动转换数字；
 *
 * 与变量和类型有关的一些常用函数
 *    isset(); 值如果是null，也表示空
 *    empty();  //判断一个变量是否为空， “”  null
 *    unset();
 *
 *    setType();  
 *
 *    getType();  //var_dump();
 *
 *    变量类型测试函数
 *    is_bool();
 *    is_int() is_integer() is_long()
 *    is_string();
 *    is_float(), is_double() is_real()
 *    is_array()//if(is_array($a))
 *    is_object()
 *    is_resource()
 *    is_null();
 *
 *    is_scalar()
 *    is_numberic()
 *    is_callable()
 */


  //自动转换；
  $a=10;
  $b="100abc";
  $c=true;
  $d=12.34;

  $sum=$a+$c+$b+$d;
  var_dump($sum);


  	$foo = "5bar";                  	//string
	$bar = true;                      	//boolean
	settype($foo, "integer");           //$foo 现在是 5 (integer)
	settype($bar, "string");            //$bar 现在是 "1" (string；

    $str = "123.45abc";               		//声明一个字符串
	$int = intval($str);                	//获取变量$str的整型值123
	$flo = floatval($str);              	//获取变量$str的浮点值123.45
	$str = strval(123.45);              	//获取变量$flo的字符串值"123.45

    $foo = 10;             		// $foo 是一个整型
	$bar = (boolean)$foo;   	// $bar 是一个布尔

    echo 1+1+"4+5+6"+1+1;       //8,在js中为24+5+611;
    echo 1+1+"4e+5+6"+1+1;       //400004;

// 整形、浮点、字符串、布尔、数组、对象、资源；
	$var=10;

	echo '<pre>';
	var_dump($var);
	echo '</pre>';

	echo "-----------------------<br>";
	$var=34.5;

	echo '<pre>';
	var_dump($var);
	echo '</pre>';

	echo "-----------------------<br>";
	$var="abc";

	echo '<pre>';
	var_dump($var);
	echo '</pre>';

	echo "-----------------------<br>";
	$var=true;

	echo '<pre>';
	var_dump($var);
	echo '</pre>';

	echo "-----------------------<br>";

	$var=array(1,2,3);

	echo '<pre>';
	var_dump($var);
	echo '</pre>';

	echo "-----------------------<br>";

	$var=new mysqli("localhost", "root", "123456", "test");

	echo '<pre>';
	var_dump($var);
	echo '</pre>';

	echo "-----------------------<br>";

	$var=fopen("test2.php", "r");

	echo '<pre>';
	var_dump($var);
	echo '</pre>';

	echo "-----------------------<br>";

	$var=null;

	echo '<pre>';
	var_dump($var);
	echo '</pre>';

	echo "-----------------------<br>";



/* 运算符号（PHP）操作符号@operators 
 *  
 *
 *    true ? 1 : 0  
 *
 *
 *    按运算符号的功能分为：
 *
 *    一、算术运算符    +   -  *  /  %  ++  --
 *    二、字符串运算符  .  可以叫连接运算符号 
 *    三、赋值运算符    =   += -= *= /= %=  .= 
 *    四、比较运算符    >  <  >= <= == ===  != 或<> !== 
 *    五、逻辑运算符    && 或and  ||或 or  ! 或not   
 *    六、位运算符      &   ｜ ^ ~   <<  >> >>>
 *    七、其他运算符   ? :  ``  @  => -> ::  & $
 *   
 *    %取模运算/求余；有两个目的： 整除运算， 控制范围； 不要用小数，也不要用负用
 *    %会把两边的数转为整数后再进行整除。b/a;要先排除a不为0的情况；
 *    ++$a, 前加，$a的值加1，然后返回$a;
 *    $a--, 后加，返回$a的值，然后加1；
 *    === ;var_dump("007"===7);
 *    !== ,var_dump(7!==7.00);
 *    && ;短路特性，第一个条件不成立，第二个就不计算了；$link=... or die("error");
 *    || ;短路特性，第一个条件成立，第二个就不计算了；
 */
    echo 13%-2;  //1;
    echo -13%-2;  //-1;
    echo 12.3%2.8   //1;
    //ddddddddddddddddddddddddd
	$year=2010;

	if(($year%4==0 && $year%100!=0) || $yaer%400==0){
		echo "11111111111111";
	}else{
		echo "0000000000000";
	//dddddddddddddddddddddddddddddd
	$num = rand()%10;     	//让一个随机数不超过10
	echo $num.'<br>';           	//输出不会超过10的一个
	echo rand().'<br>';           	
    // ++是变量自增，dddddddddddddddddd
    // $a++;先用再加；
    // ++$a;先加再用;
    // bool 不参加++;
    // string ++ 是升降序abcd
  
  $a=10;
  $b= $a++;          //b=10,  a=11
  $c= --$b;          //c=9 ,   b=9
  // 9 +   11     
  $d=$c++ + ++$c;       //d=20,  c=11
  $e=$d-- - --$d;       //d=18, e=2 ;20先拿出来用；
  // 20   -  18
  echo $e;  
  //ddddddddddddddddddddddddddddddddddd
	$i = 'a';							//声明一个变量$a, 值是字母'a'
    echo 'a'+1;echo '<br>';             ???
	for($n = 0; $n < 26; $n++) {		//使用for循环52次
		echo $i++ . "\n";				//$i通过++进行递增
	}

  //dddd追加赋值dddddddddd

  	$str='<table>';
	$str.='<tr>';   $str=$str.'<tr>';
	$str.='<td>';
	$str.='</td>';
	$str.='</tr>';
	$str.='</table>';

    echo $str;

    //ddddddddddddddddd
    $page=isset($_GET["page"])?$_GET["page"]:1;

    echo $page;

    //dddddddddddddddddddddddddddddddddddddddddddddddd

        //使用反引号（``）执行服务器操作系统的命令，并将结果赋给变量$output
	$output = `dir`;   

    //输出操作系统命令返回的结果
	echo "<pre>".$output."</pre>";  

    //ddddddddddddddddddddddddddddddddddddddddddddddddddddd
        //当打开一个不存在的文件时会产生警告，使用@将其忽略掉
	$my_file = @file ('non_existent_file');
    
    //除数为0会产生警告，使用@将其忽略掉
	@$num = 100/0;

	echo " ";        //输出空
	//使用头发送函数前面不能有任何输出，空格、空行都不行，否则会产生警告，使用@将其忽略掉
	@header("Location: http://www.brophp.com/");

    // 运算符优先级, 短路，
    $a=0;
    $b=0;
    if($a=3 || $b=3){
        $a++;
        $b++;
    }
    var_dump($a);
    echo $a.",".$b;     //1,1

    // 位运算, 按位运算；
    // 位运算<数运算<字符运算，声象运算；

    //          h  
    //         104
    // 0 0000000 00000000 00000000 00000000 = 0 2^31 2^30 ... 2^3 2^2 2^1 2^0
    // 104= 64+32+8;
    // 0 0000000 00000000 00000000 01101000 = 104   //用计算器算；
    //
    // & ; num & num; bool & bool; &>&&;位运算符不短路；要两个都为1；
    // | ; 有一个或两个为1，值为1；
    // ^ ; 不同为真，
    // ~ ; 按位非，取反；
    // <<;
    // >>;
    // 12 & 13 = 12;
    // 12 = 8 + 4
    // 13 = 8 + 4 + 1
    // 00000000 00000000 00000000 00001100
    // 00000000 00000000 00000000 00001101  &
    // -------------------------------------------
    // 00000000 00000000 00000000 00001100
    //
    var_dump(12 & 13); //12
    var_dump('A' & 'a'); //A
    $a=10;
    var_dump($a>5 & $a<100); //1;

    // ? : ;
    // ``  ;$a=`ls --al`;





















