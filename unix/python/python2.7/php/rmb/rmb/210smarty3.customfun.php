<?php
//HJKL
//smarty模板中自定义函数
//常用三类：1.变量修改器；2.标签函数；3.块标签函数;
//
//自定义函数与 smarty类 集成或的方法：
//1.smarty的registerPlugin()方法；
//  $smarty->registerPlugin(function/modifier/block,tplfun,phpfun);
//
//2.开发smarty插件；
//  一、位置：$smarty->addPluginsDir();
//  二、文件命名：modifier.funone.php; function.funtwo.php; block.funthree.php;
//  三、函数命名：smarty_modifier_funone()...;
//  四、参数的规则：
//      smarty_modifier_funone($var, $a="", $b="");
//      smarty_function_funtwo($args, $smarty);
//      smarty_block_funthree($args, $content, $smarty, &repeat);
//
//
//三类函数的用法：
//1.变量修改器：<{$var|myfun:arg2:arg3}>;
//2.标签函数：<{myfun color="red" size="7" num="5"}>;
//3.块标签函数：<{myfun color="red" size="7"}>content</myfun>
//
//
//
include "InitTEO.inc.php";

$smarty->assign("var","abcdef");


$smarty->registerPlugin("modifier","funone","one");
$smarty->registerPlugin("function","funtwo","two");
$smarty->registerPlugin("block","funthree","three");

function one($var,$a="",$b="",$c="1"){
    return strtoupper($var);
}
function two($args,$smarty){
    return '<font color="'.$args[color].'" size="'.$args[size].'">'.$args['content'].'</font>';
}//$smarty object;print table;custom plugin;
function three($args,$content,$smarty){
    return '<font color="'.$args[color].'" size="'.$args[size].'">'.$content.'</font>';

}
/*
 *
 plugin/modifier.funone.php
function smarty_modifier_funone(){
    return strtoupper($var);
}

plugin/function.funtwo.php
function smarty_function_funtwo($args, $smarty){
    return '<font color="'.$args[color].'" size="'.$args[size].'">'.$args[content].'</font>';
}

plugin/block.funthree.php
function smarty_block_funthree($args, $content, $smarty, &$repeat){
    if(!$repeat){   
        return '<font color="'.$args[color].'" size="'.$args[size].'">'.$content.'</font>';
    }
}
 
 *
 */



$smarty->display("default/index.html");
