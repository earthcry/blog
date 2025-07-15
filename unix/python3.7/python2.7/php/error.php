<?php
//
//  error
//
//  1.错误报告；
//  错误报告级别；
//error_reporting(E_ALL & E_NOTICE);
//
//
//  2.错误日志
//  3.异常处理
//      1.try{}catch(){}执行顺序是怎样的？
//      2.人为抛出异常；
//      3.错误系统抛出异常；步骤？
//  4.自定义异常；
//      给出解决方法，而不是只提示信息；
//  5.捕获多个异常；
// 
// 人工抛出异常；
echo '早上起床<br>';
$bj=false;
try{
echo '开车上班<br>';
if($bj){
    throw new Exception('车子爆胎<br>');
}
echo '路况很好<br>';
}catch(Exception $e){
echo $e->getMessage().'<br>';
echo '换上备胎，继续开车上班<br>';
}
echo '到公司开始工作<br>';

//错误系统抛出异常；
set_error_handler('myerrfunc');                //注册函数；
function myerrfunc($type,$mess,$file,$line){   //自定义函数；

}

echo '早上起床<br>';
$bj=false;
try{
echo '开车上班<br>';
if($bj){
    throw new Exception('车子爆胎<br>');
}
echo '路况很好<br>';
}catch(Exception $e){
echo $e->getMessage().'<br>';
echo '换上备胎，继续开车上班<br>';
}
echo '到公司开始工作<br>';


// 自定义异常类
class MyBtException extends Exception {
    function __construct($msg){
        parent::__construct($msg);
    }
    function changBt(){
        echo '换上备胎<br>';
    }
}

echo '早上起床<br>';
try{
echo '开车上班<br>';
throw new MyBtException('车子爆胎<br>');
echo '路况很好<br>';
}catch(MyBtException $e){
echo $e->getMessage().'<br>';
$e->changBt().'<br>';
}
echo '到公司开始工作<br>';


// 捕捉多个异常
class WcException extends Exception {
    function pubwc(){
        echo '去公厕<br>';
    }
}
class EatException extends Exception {
    function buy(){
        echo '买早餐<br>';
    }
}
class DrvException extends Exception {
    function chang(){
        echo '换备胎<br>';
    }
}
class RoadException extends Exception {
    function path(){
        echo '走小路<br>';
    }
}

class goWork {
    function wc($ts){
        if($ts){
            throw new WcException('停水了<br>');
        }
        echo '哈哈，事儿办得挺成功。<br>';
    }
    function eat($time){
        if($time){
            throw new EatException('起晚了<br>');
        }
        echo '吃得很好。<br>';
    }
    function drv($dz){
        if($dz){
            throw new DrvException('爆胎了<br>');
        }
        echo '一路顺风。<br>';
    }
    function road($xx){
        if($xx){
            throw new RoadException('下雪了<br>');
        }
        echo '路况很好。<br>';
    }
}

try{
    $go= new goWork;
    $go->wc();
    $go->eat();
    $go->drv();
    $go->road();
}catch(WcException $e){
    echo $e->getMessage().'<br>';
    $e->pubwc();
}catch(EatException $e){
    echo $e->getMessage().'<br>';
    $e->buy();
}catch(DrvException $e){
    echo $e->getMessage().'<br>';
    $e->chang();
}catch(RoadException $e){
    echo $e->getMessage().'<br>';
    $e->path();
}













