<?php
/*
    数组

1.数组概念、作用、分类、声明、特性；    
@2.数组遍历；
@3.全局数组；
@4.常用数组函数分类；       统计排序、键值分合、回调、结构、其他
@5.键值相关函数、           
    数组数量统计函数、      键值的获取，存在，对调，倒序；
    回调处理数组的函数、
@6.排序算法及排序函数、     键值升降自然自定义、键名、键值对应、多数组；
@7.分合数组函数；           切取，切除替换，化合合并，交集差集；
@8.数组与数据结构函数；
@9.其他数组处理函数；
连接，分割匹配查找替换；
1.
变量，使用“组”的概念；组变量；
目的：批量操作变量；操作灵活；用函数来操作；

声明表示：
 */
$a=[3,5,9];  $a[0]=3;
$a=array(3,5,9); 
$a=['one'=>3,'two'=5,8=>9];
$a['two']=5;

/*
数组元素结构：
元素=键key/值value对；
$arr[key]="value";  $a[0]=3;
arr组名，key组内变量名，


索引数组：下标是整数的数组；  按序号定位组内变量；for     ; 序号=下标=键名, 只有值的数组；
关联数组：下标是字符串的数组；按键名确定组内变量；foreach
    十进制整数；浮点割舍；
一维数组：arr[]     =[];
二维数组：arr[][]   =[]; 遍历foreach(arr as value)
多维数组：arr[][][] =[];
 */
$aa=[3, 5, 6, 7];
$bb=['a'=>3, 'b'=>5, 'c'=>6, 'd'=>7];
$cc=[
    [4,6,7,9],
    ['a', 'b', 'c'],
    'aa'=>[5,6,8]
];
/*
print_r();
11.自增下标，自增的是最大下标加1；
22.关联下标 不会影响 索引下标的排列规则；


 */
//其他数据类型 为下标 的自动转换
echo "1111111$arr[two]11111111111"; //111131111;
$arr[2.7]=3;    //$arr[2];
$arr[true]=2;   //$arr[1],[0];true-1,false-0;
$arr[null]=5;   //$arr[],"";
print_r($arr);
//声明
$arr=array(3,"aa",55.5);
$arr=[3,"bb",6=>7];
//函数返回值为数组的元素的访问：
function demo(){
    return ["one", "two", "three"];
}
$arr=demo();
echo $arr[0]; //one;
echo demo()[1];//two;  <------
//数组某些元素的消除，unset(),null;
$arr=['one', 'two', 'three'];
unset($arr[2]); //名为空；索引位也为空；
$arr[1]=null;   //值为空；
$arr=array_values($arr);//重新索引函数；
//猴子选大王，
//任意m只猴子围成圈，从任意位置开始，数出第n只，出局，
//接着出局后的位置，再数出第n只，再出局，直到剩下最后一只；
//先写程序结
//1.化现实问题为虚，生成元素数为m的数组，值为字母吧[a,b,c,d,e,f,g]；
//2.遍历每个猴子，过滤n的倍数；每只猴子序数为n的倍数；
//3.按新索引顺序，再进行同样过滤，直到剩下最后一个；
//  即对新索引数组再过滤；
构框架；
function monkey($m,$n){
    $arr=[];
    $a="a";
    for($i=0;$i<$m;$i++){
        $arr[]=$a;      //$arr[]给索引数组的每个元素赋值；
        $a++;
    }
    var_dump($arr);
    for($i=0;count($arr)>1;$i++){
        if($i%$n==0){
            unset($arr[$i]);
        }else{
            $arr[]=$arr[$i];    //连续索引才能for遍历；
            unset($arr[$i]);
        }
        echo count($arr);
    }
/*
    $i=0;
    while(count($arr)>1){
        if($i%$n==0){
            unset($arr[$i]);
        }else{
            $arr[]=$arr[$i];
            unset($arr[$i]);
        }           
        $i++;
    }
 */
    return $arr;
}
print_r(monkey(30,3));

/*
    二维数组/多维数组

数组中某个元素的 值 又是数组；
*/
$one=["name"=>"one", "age"=>20, "sex"="nan"];
$two=["name"=>"two", "age"=>21, "sex"="nv"];
$three=["name"=>"three", "age"=>22, "sex"="nan"];
$group=[$one, $two, $three];

$group=[
         ["name"=>"one", "age"=>20, "sex"="nan"],
         ["name"=>"two", "age"=>21, "sex"="nv"],
"three"=>["name"=>"three", "age"=>22, "sex"="nan"]
];

echo $group[1][0];
echo $group["two"]["age"];
$group["three"]["age"]=20;

$class=[$group1, $group2, $group3];

@2.
//遍历数组；
//for/foreach/list()each()while
//@foreach($arr as [$key=>] $value){}

$group=[
    "groupname"=>"banwei",
    "price"=>2000,
    ["name"=>"aaa", "age"=>22, "sex"=>"nan"],
    ["name"=>"bbb", "age"=>22, "sex"=>"nv"],
    ["name"=>"ccc", "age"=>22, "sex"=>"nan"]
];
////////////表格图形、表格标签、表格内容数组之间的对应关系；/////////
//表格数目-----表个数-------三维数组；
//表格边界-----<table>----二维数组；
//表格行row----<tr>-------一维数组；
//表格列col----<td>-------元素值
  
echo '<table border="1" width="800" align="center">';
echo '<caption><h1>数组转表格</h1></caption>';
    foreach($group as $row=>$value){
        echo '<tr>';
        if(is_array($value)){
            foreach($value as $col){
                echo '<td>'.$col.'</td>';
            }
        }else{
            echo '<td colspan=3>'.$row.": ".$value.'</td>';
        }
        echo '</tr>';
    }
echo '</table>';
/*
 *  @list()
 *  作用，将数组中的元素转为变量；
 *  1.=右边只能是数组；
 *  2.参数和数组要一一对应；
 *  3.只能将连续索引数组转为变量；
 *  4.参数可空；
 */
list($a, $b, $c)=["a", "b", "c"];
list($a, , $c)=["a", "b", "c"];

$str="峰哥_好帅";
list($name, $pro)=explode("_", $str);

/*
 *  @each()
 *  作用，返回每个元素的详细信息，每次一个；
 *  遍历数据库；
 *  1.传入数组，返回数组；
 *  2.把返回的每个元素分为四个子元素[key,value,0,1];
 *  3.读完最后一个元素后返回false;
 */
$arr=["one"=>"妹子", "峰哥", "第三者"];
var_dump(each($arr));                   // each()返回一个元素的键值，关联索引两套；
while(list($key, $val)=each($arr)){     
    echo $key.'---'.$val.'<br>';
}
reset($arr);

// 数组指针
// reset();prev();next();end();
	$user=array("id"=>1, "name"=>"zhangsan", "age"=>10, "sex"=>"nan");

	while(list($key, $value)=each($user)){
		echo $key."==>".$value."<br>";
	}
	reset($user);
	while(list($key, $value)=each($user)){
		echo $key."==>".$value."<br>";
	}
	reset($user);
	next($user);
	next($user);
	while(list($key, $value)=each($user)){
		echo $key."==>".$value."<br>";
	}
	reset($user);

	echo current($user)."===========>".key($user)."<br>";
	end($user);
	echo current($user)."===========>".key($user)."<br>";
	prev($user);
	echo current($user)."===========>".key($user)."<br>";
 

// @3 超全局数组（预定义变量）superGlobalArray
//
// $_SERVER / $_ENV / $_GET / $_POST / $_REQUEST
// $_FILES / $_COOKIE / $_SESSION / $GLOBALS 包括声明的变量常量
// 全局，即全局组变量；
// 超，多了各自的独特能力，如$_GET；

// @4 数组函数
//
// 要会用手册——如何查需要的函数，百度、手册；
// 用到什么功能，在现查学什么函数；
// 要求PHP数组与字符串函数要熟；
//
// 键值：显示，存在，对调，倒序；
// 统计：个数，重复；
// 回调处理：
// 排序：
// 分合：
// 数据结构：
// 其他：
    //

// * 数组的相关处理函数(上)
/* 
  一 数组键/值操作有关的函数
  	1.  array_values()
 	2.  array_keys()
  	3.  in_array()
 	4. array_key_exists
	5. array_flip -- 交换数组中的键和值
	6. array_reverse --  返回一个单元顺序相反的数组 
   
    二、 统计数组元素的个数和惟一性

    1. count() sizeof();
    2. array_count_values -- 统计数组中所有的值出现的次数
    3. array_unique -- 移除数组中重复的值

    三、使用回调函数处理数组的函数

    	1. array_filter()  用回调函数过滤数组中的单元 
	2. array_walk()   数组中的每个成员应用用户函数

	3. array_map()     将回调函数作用到给定数组的单元上 


 * 拆分、合并、分解、接合的数组函数
 *    1. array_slice()
 *    2.array_splice()
 *    3. array_combine();
 *    4. array_merge();
 *    5. array_intersect();
 *    6. array_diff()
 *
 *
 *
 * 数组与数据结构的函数
 *    1. 使用数据实现堆栈
 *    	 array_push()
 *    	 array_pop()
 *
 *    2. 使用队列
 *    	  array_unshift()
 *    	  array_shift()
 *
 *    	  unset()
 
*/  @5
// ***与@key键值 相关函数***
// 键值的获取，存在，对调，倒序；
//
// array_values()  返回所有值，并重新索引；
// array_keys()     返回所有键名或指定值的键名，
$lamp=["os"=>"linux", "webserver"=>"apache", ["a", "b"], "aa"=>"10", "num"=>10, "db"=>"mysql", "language"=>"php", "hello"=>null];
$lamp1=["os"=>"linux", "webserver"=>"apache", "db"=>"mysql", "language"=>"php"];
print_r($lamp);echo '<br>';
$arr=array_values($lamp);
print_r($lamp);echo '<br>';
print_r($arr);echo '<br>';
list($os, $webserver, $db, $language)=array_values($lamp);

print_r(array_keys($lamp, 10, true));//true, 值的类型也相同的键，完全匹配的；

// in_array()
// search values, return bool.
// array_search()
// search values, return key.
// 搜索数值
//
if(in_array("mysql", $lamp)){}
if(in_array(10, $lamp, true)){}
if(in_array(["a", "b"], $lamp, true)){}
if(in_array(["b", "a"], $lamp, true)){}

if(array_search("mysql", $lamp)){}

// array_key_exists() / isset()
// 判断键名是否存在
if(array_key_exists("os", $lamp)){}
if(isset($lamp['db'])){}
if(isset($lamp['hello'])){} //不能判断空值的键；

// array_flip()
// 键值对调翻转；
// 数组键名唯一，数值可同；相同值，后边会覆盖前边
// 一些特殊值不被允许，值允许整型和字符串；
$arr=array_flip($lamp); 

// array_reverse()
// 数组元素 顺序倒置，倒序, 逆向；
// true, 保留索引数组键名；

// ***@统计数组个数和唯一性的函数***
//
// count()、值的个数
echo count($lamp, 1); //1, 统计第二三层的多维数组元素的个数；
strlen();  //1
// array_count_values()
// 统计每个值 重复的次数；
// array_unique()
// 删除重复的值；留第一次出现的；

// ***使用@callback回调函数 处理数组的函数***
// 过滤，加工原数组，加工多个数组；
// 
// array_filter()
// 用回调函数过滤数组中的元素单元；
// 回调的函数返回值为 真的会被留下；
// 返回数组的索引不变，键名不变；
$arr = [1, 2, 3, -4, 5, 6, 7, 8, 9, -1, -2, -3, 4, -5, -6, -7, -8, false, "", null];
print_r($arr);// nothing
var_dump($arr);
array_filter($arr); //nothing 默认假的过滤掉了
//过滤掉负数；
function myfun($value){
    return $value>0?true:false;
}
var_dump(array_filter($arr, "myfun"));
// 过滤掉2的倍数；
var_dump(array_filter($arr, function($value){
    return !($value%2==0);                      //false,'',null 都是2的倍数；
}));
// 重新索引
var_dump(array_values(array_filter($arr, function($value){
    return !($value%2==0);
})));

// array_walk() 
// 对原数组加工
// 对每个传入的数组元素用子函数进行 引用加工，最后原数组变化；
$arr=["one"=>1, "two"=>2, "three"=>3, "four"=>4, "five"=>5];

array_walk($arr, function(&$value){
    $value=$value*$value;
});
var_dump($arr);

array_walk($arr, function(&$value, $key){
    $value=$key.":".$value;
});
var_dump($arr);

array_walk($arr, function($value, $key, $str){
    echo "{$key}{$str}{$value}<br>";
}, "##########");
print_r($arr);echo '<br>';

// array_map()
// 可加工多个数组, 返回一个数组；
$arr=[1, 2, 3, 4, 5];
$brr=["one", "two", "three"];

$rarr=array_map(function($v){
    return $v*$v*$v;
}, $arr);

// 加工俩数组，返回一个新数组；

$rarr=array_map(function($av, $bv){
    echo "$av---$bv";
    return 1;
}, $arr, $brr); // 用空来补；新数组都为1；

//
$rarr=array_map(null, $arr, $brr); //会合并俩数组；

// @6
// ***@sort排序算法***
//
// 冒泡排序：
// 思想：一路两两比较，选出最大的，后循环之；
$arr=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
// 二分叉法排序
// 
// ***PHP@排序函数***
//
//  键值升降自然自定义、键名、键值对应、多数组；
//
// sort—— 升序排序; 数字字母；去掉原键名； 
// rsort——降序排序,en取反
//
// ksort——按键名排序
// krsort——
//
// asort——保持键值对应关系的排序，适合关联数组；
// arsort
//
// natsort——自然排序算法,a1,a2,a11,a12;大写在前；
// natcasesort——不区分大小写
//
// usort——用自定义比较函数对值排序；
// uasort
// uksort
//
// array_multisort对多个或多维数组排序；
//
$a=['a', '10', 'b', 20];          //'10','a','b',20;
sort($a);

$arr=["a", "aaaaaaaaaa", "aaa"];
//按长度排序
usort($arr, function($a, $b){   // 比较置换
    $alen=strlen($a);
    $blen=strlen($b);
    if($alen>$blen){
        return 1;
    }elseif($alen<$blen){
        return -1;
    }else{
        return 0;
    }
});
// array_multisort(); **重点；
// 多个数组或多维数组；
// 同步排序；
// 多个数组，都 按第一个数组的 新索引序列 排序；
// 应用：模拟data表的按某列排序；
// 对表按列排序；
$table=[
    ["id"=>1, "name"=>"aa", "age"=>10],
    ["id"=>2, "name"=>"ww", "age"=>30],
    ["id"=>3, "name"=>"cc", "age"=>20],
    ["id"=>4, "name"=>"dd", "age"=>40]
];
$ages=[];
foreach($table as $value){
    $ages[]=$value['age'];
}
array_multisort($ages, $table);
echo "<pre>";
    print_r($table);
echo "</pre>";

$ages=[];
$names=[];
foreach($table as $value){
    $ages[]=$value['age'];
    $names[]=$value['name'];
}
array_multisort($ages, $names, SORT_DESC, $table);
echo "<pre>";
    print_r($table);
echo "</pre>";

// @7
// ***@分合数组函数***
// 切取，切除替换，化合合并，交集差集；
//
// array_slice() //切片，部分；
// 分出一段的；
// 参数，索引序数，个数，保留原索引与否；
// 负数为倒序，从1开始；
$arr=["a", "b", "c", "d", "e"];
$narr=array_slice($arr,-3,2,true);
print_r($narr); //array([2]=>c [3]=>d);

// array_splice(&)
// 分出没用替换
array_splice($arr,-3,2,["hello", "world"]);
print_r($arr);["a", "b", "hello", "world", "e"];

// array_combine() //联合化合；
// 按键值配对；
// 个数类型要对应
$a=["os", "webserver", "db", "language"];
$b=["linux", "apache", "mysql", "php"];
$arr=array_combine($a,$b);
print_r($arr);

// array_merge()    //合并；
// 两组前后衔接合；
$a=["a", "b", "c"];
$b=[10, 11, 12]; // [5=>10]
$c=$a + $b;
var_dump($c);   // $c=$a;下标相同相加时，前覆盖后；
$c=array_merge($a, $b);
var_dump($c); 

$a=["a", "one"=>"b", "c"];
$b=[10, "one"=>11, 12]; // 

$c=array_merge($a, $b);
var_dump($c); // 关联数组会覆盖，

// array_intersect() 贯穿，相交
// 相同合；
// 计算交集；
$a=[5, 6, 10, 11, 12, 13, 14];
$b=[5, 6, 12, 15, 14];
print_r(array_intersect($a, $b));
// 取开头相同的交集；
$min=(count($a)>count($b)) ? count($b) : count($a);
$narr=[];
for($i=0; $i<$min; $i++){
    if($a[$i]==$b[$i]){
        $narr[]=$a[$i];
    }else{
        break;
    }
}

// array_diff()
// 不同合；
// 计算差集；
print_r(array_diff($a, $b));
//@8
// ***@struct数组与数据结构 ***
// 
// 栈，子弹夹，后进先出；
$zhan=[];
array_push($zhan, "1");
array_push($zhan, "2", "3");
array_pop($zhan);echo '<br>';
array_pop($zhan);echo '<br>';
// 队列，排队，先进先出；
$duilie=[];
array_unshift($duilie,1);
array_unshift($duilie,2,3);
echo array_pop($duilie);echo '<br>';//先进先出；
array_shift($duilie); //后进先出；

// @9 ***@other其他函数***
//
// array_rand($arr, 3) //随机取,返回下标，值可相同；
// shuffle(&$arr)    //打乱；
// array_sum()       //返回值得和；
// range(0,10,3)     //返回大数组，指定值得范围的, 跳步；
// array_fill(0,9,"*")      //











//
// ***@分合数组函数***
//
// array_slice()
// 分出有用的；
$arr=["a", "b", "c", "d", "e"];
$narr=array_slice($arr,-3,2,true);
print_r($narr); //array([2]=>c [3]=>d);

// array_splice(&)
// 分出没用的
array_splice($arr,-3,2,["hello", "world"]);
print_r($arr);["a", "b", "hello", "world", "e"];

// array_combine()
// 配对合；
// 个数类型要对应
$a=["os", "webserver", "db", "language"];
$b=["linux", "apache", "mysql", "php"];
$arr=array_combine($a,$b);
print_r($arr);

// array_merge()
// 衔接合；
$a=["a", "b", "c"];
$b=[10, 11, 12]; // [5=>10]
$c=$a + $b;
var_dump($c);   // $c=$a;下标相同相加时，前覆盖后；
$c=array_merge($a, $b);
var_dump($c); 

$a=["a", "one"=>"b", "c"];
$b=[10, "one"=>11, 12]; // 

$c=array_merge($a, $b);
var_dump($c); // 关联数组会覆盖，

// array_intersect()
// 相同合；
// 计算交集；
$a=[5, 6, 10, 11, 12, 13, 14];
$b=[5, 6, 12, 15, 14];
print_r(array_intersect($a, $b));
// 取开头相同的交集；
$min=(count($a)>count($b)) ? count($b) : count($a);
$narr=[];
for($i=0; $i<$min; $i++){
    if($a[$i]==$b[$i]){
        $narr[]=$a[$i];
    }else{
        break;
    }
}

// array_diff()
// 不同合；
// 计算差集；
print_r(array_diff($a, $b));

// ***@struct数组与数据结构 ***
// 
// 栈，子弹夹，后进先出；
$zhan=[];
array_push($zhan, "1");
array_push($zhan, "2", "3");
array_pop($zhan);echo '<br>';
array_pop($zhan);echo '<br>';
// 队列，排队，先进先出；
$duilie=[];
array_unshift($duilie,1);
array_unshift($duilie,2,3);
echo array_pop($duilie);echo '<br>';//先进先出；
array_shift($duilie); //后进先出；

// ***@other其他函数***
//
// array_rand($arr, 3) //随机取,返回下标，值可相同；
// shuffle(&$arr)    //打乱；
// array_sum()       //返回值得和；
// range(0,10,3)     //返回大数组，指定值得范围的, 跳步；
// array_fill(0,9,"*")      //
range('a', 'g');









