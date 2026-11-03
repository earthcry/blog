<?php
//HJKL
//smarty(程序员)
//1.安装；
//2.变量的分配和加载模板；
//3.以插件形式扩展smart；
//4.缓存控制技术；
//smarty(美工模板设计篇)
//1.编写smarty模板的基本语法；
//2.变量；
//3.变量修改器和组合修改器；
//4.自定义函数；
//5.smarty内置函数；
//6.模板继承机制；
//
require "InitTEO.inc.php";

$title="title from db.";
$content="content from db.";

$smarty->assign("title",$title);
$smarty->assign("content",$content);
$smarty->assign(array("aaa"=>"111","ptime"=>date("Y/m/d H:i:s",(time()+8*60*60))));

function myfun(){
    return date("Y/m/d");
}
$smarty->registerPlugin("function","myfun2","test");
function test($args){
    //$args=array(size=>"7",coler=>"red",num=>"5",content=>"111111111");
    $str="";
    for($i=0;$i<$args[num];$i++){
        $str.=$args["content"].'<br>';
    }
    return $str;
}
$smarty->assign("contacts",array("010-34098908","aaa@bbb.com",array("qq34245","13634546565")));
$smarty->assign("contacts2",array("fax"=>"010-345435","phone"=>array("ph1"=>"4634534","ph2"=>"97899")));
class Person {
    public $name="zhangsan";

    function say(){
        return $this->name."11111111";
    }

    function one(){
        $this->name="wwwwwwww";
        return $this;
    }
}
$smarty->assign("p",new Person());
$smarty->display("default/index.html");
