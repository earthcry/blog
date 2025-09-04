<?php
/*

Use two language dec a same conception. computer language and human language.
computer first.

function_exists(funcname);
fun in var , before finish unset(var)
static var , for same func share times;
number / mixed /callback
$var()
callback function, extend function by call another function.
callback function, give a interface that function call function from outside.
and the called function can be custom.
require error out;
include error ignore;
include_once();
$var=function(){};<---
$var();
neibu function closure function

 */
//pass fuben
function aaa($a){
    $a=3;
    return $a;
}
$a=2;
$b=aaa($a);
echo $a;echo '<br>';
echo $b;echo '<br>';
//返回值函数
function tablestr($name, $m, $n){
     $str = "";
     $str.= '<table border="1" width="800" align="center">';
     $str.= '<caption><h1>'.$name.'</h1></caption>';
     for($i=0; $i<$m; $i++){
        $bg=($i%2==0) ? "#cccccc" : "";
        $str.= '<tr bgcolor="'.$bg.'">';
        for($j=0; $j<$n; $j++){
            $str.= '<td>'.$i.','.$j.'</td>';
        }
        $str.= '</tr>';
     }
     $str.= '</table>';
     return $str;
}

//引用变量函数
$b=20;
function demo(&$a){     //函数的引用变量，实质是 传址，不是传值；
    $a=100;             //目的让内外变量一起变化；
}
demo($b);

//默认变量函数，即可选变量函数
function demo2($a=1, $b=3){ echo $a*$b;}
demo2(3);
function demo3($a, $b=5){}
//function demo5($a, [$b]){}

//可变 参数个数 函数
//实参 > 形参
function demo6($a, $b=2){   //function demo6(){ 
    $arr=func_get_args();   //当变量够多时，可用参数数组函数；
    var_dump($arr);         //func_num_args();
}                           //func_get_arg($i)
demo6(1);echo '<br>';
demo6(1, 2, 3, 4, 5, 6);echo '<br>';

$arr = array(1,4,9,3,8,5,2);

function mycom($a, $b){
    if($a>$b){
        return 1;
    }else if($a<$b){
        return -1;
    }else{
        return 0;
    }
}
print_r($arr);
usort($arr, "mycom");
echo '<br>';
print_r($arr);
echo '<br>';

//callback function
function demo7($num, $n){
    for($i=0; $i<$num; $i++){
        if($i%$n==0){continue;}
        echo $i.'<br>';
    }
}
//demo7(100, 5);echo '<br>';

function demo8($num, $n){
    for($i=0; $i<$num; $i++){
        if($n($i)){continue;}
        echo $i.'<br>';
    }
}
function test($i){
    if($i%3==0){return true;}
}
demo8(100, "test");echo '<br>';

function fun($one="1", $two="2", $three="3"){
    echo "$one-------$two-----------$three--------";
}//参数个数变长时，不能直接调用函数；
call_user_func_array("fun", array("111", "222"));
function demo9($num, $n){
    for($i=0; $i<$num; $i++){
        if(call_user_func_array($n, array($i)))){continue;}
        echo $i.'<br>';
    }
}

class Filter {
    function one($i){
        if($i%3==0){
            return true;
        }else{
            return false;
        }
    }
    static function two(){
        if(pre_match('/3/', $i)){
            return true;
        }else{
            return false;
        }
    }
}
//demo9(100, "test");
demo9(100, array(new Filter(), "one"));
demo9(100, array("Filter", "two"));

function demo10(){
    $a=10;
    $b=20;

    $one=function($str) use (&$a, &$b){
        echo $str.'<br>';
        echo $b.'<br>';
        $a++;
        echo $a.'<br>';
    }
    return $one;
}
$var=demo10();
$var("hello world");

function demo11($fun){
    echo $fun();
}
demo11(function(){return "";});














