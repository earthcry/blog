<?php
/*
 * 恋人态度
   概念 要具体化的 实物 才有操作意义； 
 *
函数
1.全局、局部、静态变量、
2.默认、引用、可变参数、
3.系统、递归函数、
4.变量、回调、匿名、闭包函数、
5.自定义函数库加载；

0.
函数
是封装已命名的代码块；
是给个变量，可以返回个结果的加工机器，不同的函数具有不同的加工功能；

函数结构：
function name($arg1, $arg2){
    return $arg1+$arg2;
}

参数:实现函数多用性；由外到内传入的变量或数值；形参，实参，赋的值；
    返回值：功能的结果；函数的实质；
    return值：表达式，变量，数组，函数及访问；
函数名不区分大小写；变量、常量区分大小写；
函数调用才执行，且执行后，变量会释放；函数国；局部变量；形参；

1.
全局变量，局部变量（内部变量、外部变量、边界变量形参）；
global var;常量；魔术变量$_POST；函数静态变量；

@static内部静态变量：函数完成不释放；第一次调用声明，二三次无效；
目的：同一个函数多次调用共享。同闭包父变量有什么区别？？？
func1.age=3;
func2.age=5;
func调用:功能、参数、返回值；

2.
引用参数、默认参数、可变参数：
引用参数&param,即要传一个变量var：
目的是改变外边引用的变量；
a.相当于别名；
b.只有在内存中的变量才有地址；

默认值参数；
部分默认值的要从后向前；demo($a,$b,$c=2;$d=3);因为传值从前开始并对应
demo($a[,$b[,$c]]);内内有【】的表明单独可选；

可变参数：
可变数量、顺序；demo($...);
不用形参接受，在函数内部用内置函数来接受；
在demos()内用func_get_args()来接受；
目的：参数数量多时可灵活传参数；
func_get_args();返回所有参数的数组
func_num_args();返回参数总数；
func_get_arg();接收一个数字，返回指定参数；

3.
递归函数：
在函数中调用自己的函数。
递进去，归回来；层层递进，层层归来；梦中梦，故事中的故事，镜中镜；
自己调用自己，被调用的自己再调用自己。。。循环调用；
故要给一个退出条件；一种特殊循环；
应用：遍历目录，无限分类；
.递归函数、系统函数、

4.
变量函数：$var():
名字可变的函数；
echo, print_r();

回调函数：
在函数内部，把复杂的部分，变化的部分，调用一个函数来解决；
call_user_func_array(callback,array())

匿名函数：
匿名函数也叫闭包函数，经常用作回调函数的参数，即被调用的函数；
声明：
$var=function(){}; //一定要加分号；把closure对象赋值给一个变量；
调用：
$var();
//var_dump($var); object(closure);
区别变量函数
function demo(){}
$var="demo";
echo $var();
匿名函数可以作为参数传递；
    demo(function(){
        echo "aaa";
    })

    demo2($a, function(){})

内部函数：
又子函数；
子函数调用的外部变量，只能是父函数外的，而非父函数内的；

闭包函数：

闭包函数是父子函数，实质子函数，父只起到一个包的作用，与外界隔绝；
内部变量对子函数就成了局部外部变量；最终实现被共用；

子函数可以使用父函数中的局部变量，这种行为称为闭包；不是使用副本；
将匿名函数在普通函数中当做参数传入，也可以被返回。（返回整个子函数）
这就实现了一个简单的闭包；

回调函数调用一个可被返回的匿名函数，就叫闭包函数；

目的:可以吧局部变量当全局变量使用；防止闭包全局变量冲突；

闭包特性：
闭包函数返回时，内部变量处于激活状态，函数所在栈区依然保留；没释放。
11.闭包内外层都是函数，父子函数；
22.闭包会return内部函数，父派子；
33.被返回的内部函数即子函数不能再返回，否则就结束了；
44.执行闭包后，闭包内部变量会存在，而子函数的变量不会存在；
55.父函数的变量食物受保护仅供内部使用，且一处处于内存中，
父每次执行回家，都还会用到。
可以用class来实现；

5.
加载自定义函数库：
include "function.inc.php";  //指令式；
include("fucntion.inc.php"); //函数式；
echo/break/exit/print
include 不是简单的复制，include "aaa.txt";
include_once "function.inc.php";
require "function.inc.php";
require_once "function.inc.php"
区别：包含失败，require会崩毁，include会警告；
固定包含用require,条件包含用include



 */
//引用参数，传递变量；
//$b=&$a; 把a的地址赋给b；存地址的就是指针，b是a的指针；b是a的别名；
$b=20;
function demo(&$a){
    $a=100;
}
echo $b."<br>";
demo($b);   //not demo(20); 
echo $b.'<br>';  //100; 函数里变，外就变；目的改变外边的变量；
//把b改成a？不重名，全局变量与局部变量；
//实例 sort(&array);

//可变参数
function demo2(){
    $sum=0;
    for($i=0;$i<func_num_args();$i++){
        $sum+=func_get_arg($i);
    }
    return $sum;
}
echo demo2(1,2,3,4,5,6,7,8,9,0);

//回调函数
//把复杂的部分，变化的部分，调用一个函数来解决；
//按条件过滤数字；
function demo3($num,$n){
    for($i=0;$i<$num;$i++){
        if($i%$n==0)
            continue;
        echo $i.'<br>';
    }
}
demo3(500,5);
//条件部分改成调用函数
function demo4($num,$n){
    for($i=0;$i<$num;$i++){
        //if($n($i))
        if(call_user_func_array($n,array($i))) //可以调用对象和类里的函数
            continue;
        echo $i.'<br>';
    }
}
function test($i){
    if($i%5==0)
        return true;
    else
        return false;
}

class Filter {
    function one($i){
        if($i%3==0){
            return true;
        }else{
            return false;
        }
    }
    static function two($i){
        if(preg_match('/3/', $i)){
            return true;
        }else{
            return false;
        }
    }
}
/*
调用函数
$filter=new Filter();
$filter->one();
Filter::two();

 */
demo4(500,"test");
demo4(500,array(new Filter(),"one"));
demo4(500,array("Filter", "two"));
//usort();

//调用的函数参数个数不定时
function fun($a=1,$=2,$c=3){
    echo "$a====$b====$c<br>";
}
call_user_func_array("fun", array(111,222,3333));

//内部函数
$a=500;
function one(){
    $a=100;
    echo "11111111<br>";
    function two(){
        echo "2222{$a}22222<br>";//500
    }
    function three(){
        echo "3333333333<br>";
    }
    two();
    three();
}
one();

//匿名函数
//声明并调用
function demo45(){
    $one=function($str){
        echo $str;
    };
    $one('hello world');
}
//$one('hello world');  在外部没法直接调用，找不到变量$one;
demo45();

//非闭包函数
function demo5(){
    $a=10;
    $b=20;
    $one=function($str) use(&$a,&$b) {  //无&的话，传入的是副本，就不叫使用。。。
        echo $str.'<br>';
        echo $b.'<br>';
        $a++;
        echo $a.'<br>';
    };
    $one("hello world");                // 内部调用；
    echo "=====".$a."===<br>";
}
demo5();
//闭包函数
//$a 闭包全局变量；
function demo6(){
    $a=10;
    $b=20;
    $one=function($str) use(&$a,&$b) {
        echo $str.'<br>';
        echo $b.'<br>';
        $a++;
        echo $a.'<br>';
    };
    return $one;                        // 内部返回；
}
$var=demo6();   // $var=$one;   return返回值是变量?是函数?；

$var("hellow world");    //11,20;
$var("this is a test");  //12,20;
$var("#########");       //13,20;

function demo7($fun){
    echo $fun();
}
function test(){
    return "##########";
}
demo7("test");
//匿名函数作为参数来用。的闭包函数；
demo8(function(){
    return "##########";
})

//递归函数
x
function digui($n){
    echo $n.'<br>';
    if($n>0)
        digui($n-1);
    else
        echo "------------------";
    echo $n.'<br>';
}
//Realize:feel recursion function.
//递归应用：阶乘、无限分类、遍历目录菜单、
function rcsFun($num){
    echo $num.'_pre'.'<br>';

    if($num>0)
        rcsFun($num-1);
    else
        echo '-------------------------------------<br>';

    echo $num.'_lat'.'<br>';
}

rcsFun(3);

/////////////用 展开代码 的方式来理解递归函数；
echo '------------展开代码--------------<br>';

    echo $num.'_pre'.'<br>';//3


            echo $num.'_pre'.'<br>';//2


                    echo $num.'_pre'.'<br>';//1


                            echo $num.'_pre'.'<br>';//0

                                echo '-------------------------------------<br>';

                            echo $num.'_lat'.'<br>';//0


                    echo $num.'_lat'.'<br>';//1


            echo $num.'_lat'.'<br>';//2


    echo $num.'_lat'.'<br>';//3

//加载自定义函数库
require "function.inc.php";
if($a=="a")
    include "demo.php";
else
    include "demo2.php";
include1();
include2();
include3();

//Realize:func of table with put in row and colume;

function table($row,$col,$name){
    echo '<table border=1 align="center">';
    echo '<caption><h2>'.$name.'</h2></caption>';
    for($i=0;$i<$row;$i++){
        $bg=($i%2==0)? "#cccccc" : "";
        echo '<tr bgcolor="'.$bg.'">';
        for($j=0;$j<$col;$j++){
            echo '<td>'.$i.$j.'</td>';
        }
        echo '</tr>';
   } 
   echo '</table>'; 
}

table(13,19,TEST);

















//        echo '<tr onmouseover="onRow(this)" onmouseout="outRow(this)" bgColor="'.$bg.'">';
?>
<script>
var oriColor=null;
function onRow(obj){
    oriColor=obj.bgColor;
    obj.bgColor='red';
}
function outRow(obj){
    obj.bgColor=oriColor;
}
</script>
