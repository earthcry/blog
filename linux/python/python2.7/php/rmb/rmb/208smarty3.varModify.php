<?php
//HJKL
//变量调节器；变量修改器；
//作用：
//      1.php变量，在模板中预处理，在输出前；
//      2.处理方式是使用函数；
//      3.smarty3可以直接调用php函数;
//      4.可以php端预处理；
//使用场合：
//      1.标题过长时；
//      2.时间显示；模板可以自由使用格式；
//      
//变量修改器的语法：
//      <{$str}>;
//      <{$str|funName}>;
//      <{$str|funName:arg2:arg3:...}>;
//变量修改器有哪些可用？
//      1.自定义变量修改器；
//      2.smarty自带的变量修改器；
//如何自定义？
//      $smary->registerPlugin("modifier","tplfun","phpfun");
//组合修改器
//      同一变量多个修改器
//      test(substr($var))
//      <{$var|fun1|fun2}>
//
//
//
include "InitTEO.inc.php";

$smarty->assign("var","this is2 a3 string4.");
$smarty->assign("nudate",time());
$smarty->assign("var1","自我不是现成的个体，而是借由行为抉择而不断塑造的个体。");

$smarty->registerPlugin("modifier","myfun","test");
$smarty->registerPlugin("modifier","substr","substr");
function test($var,$color="#000000",$size="3"){
   return '<font color="'.$color.'" size="'.$size.'">'.strtoupper($var).'</font>'; 
}


$smarty->registerPlugin("modifier","preplace","demo");
function demo($var,$p,$r){
    return preg_replace($p,$r,$var);
}

$smarty->display("default/index.html");
