<?php
//
//      Error && Exception
//
// Error Reporting Grade.
// php.ini: error_reporting = E_ALL & ~E_NOTICE
error_reporting(E_ALL & ~E_NOTICE);
//
//
// fangshi of error reporting.
$msg="";
set_error_handler("regErrFun");  //register custom php function.
function regErrFun($error_type, $error_message, $error_file, $error_line){
    global $msg;
    $msg="错误级别：{$error_type}<br>
        错误消息：{$error_message}<br>
        所在文件：{$error_file}<br>
        所在__行：{$error_line}<br><br>";
}

getType($a);
echo "1111111111111<br>";
getType();
echo "2222222222222<br>";
echo $msg;
//
//
//  Record error log
//  php.ini:display_errors=off
//  1.php.ini:log_errors=on //apache / wamp
//  2.php.ini:error_log=syslog
//  3.php.ini:error_log="c:/wamp/logs/php_error.log"

//
//  Exception Handle
//
//  try --> $e --> catch
//
try{
    echo "week,get up.<br>";
    echo "go to work by driver.<br>";
    throw new Exception("car circle bad.(disp in msg.)<br>"); //抛出异常；
    echo "no execute if exception.<br>";
}catch(Exception $e){       //Exception $e=new Exception('');
    echo $e->getMessage().'<br>';
    echo "change a readied circle,continue to drive.<br>";
}
echo "start work.<br><br>";

//
//  Exception && Error Handle
set_error_handler("regErrFun2");  //register custom php function.
function regErrFun2($type, $msg, $file, $line){
    if($type==E_WARNING){
        throw new Exception("Exception: {$msg},{$file},{$line}");
    }
}

function drive($drv){
    echo $drv.'<br>';
}
echo "week,get up.<br>";
try{
    echo "go to work by driver.<br>";
    drive();
    echo "no execute if exception.<br>";
}catch(Exception $e){       //Exception $e=new Exception('');
    echo $e->getMessage().'<br>';
    echo "change a readied circle,continue to drive.<br>";
}
echo "start work.<br><br>";

//
//  Custom Exception Class
//
class BtExcpt extends Exception {
    function __construct($msg){
        parent::__construct($msg);
    }
    function handleBt(){
        echo "Change a readed driver circle.<br>";
    }
}

echo "Get up at morning.<br>";
try{
    echo "drive to work.<br>";
    throw new BtExcpt("driver circle bad.<br>");
    echo "Not display at exception.<br>";
}catch(BtExcpt $e){
    echo $e->getMessage().'<br>';
    $e->handleBt().'<br>';
}
echo "Start work.<br><br>";

//
//  Custom Exception Class for More
//
class GowcExcpt extends Exception {
    function repaireWC(){
        echo "WC is repaired good.<br>";
    }
}
class DrvExcpt extends Exception {
    function replaceNew(){
        echo "Circle is replaced good.<br>";
    }
}
class GoWork {
    var $bj=false;
    function getup(){
        echo "Get up at morning.<br>";
    }
    function gowc($bj){
        if($bj){throw new GowcExcpt("WC is bad.<br>");}
        echo "Eat morning food.<br>";
    }
    function drv($bj){
        if($bj){throw new DrvExcpt("Circle is bad.<br>");}
        echo "Drive to work.<br>";
    }
    function work(){
        echo "Start to work.<br>";
    }
}

    $gw=new GoWork;
    $gw->getup();
try{
    $gw->gowc(false);
    $gw->drv(true);
}catch(GowcExcpt $e){
    echo $e->getMessage();
    $e->repaireWC();
}catch(DrvExcpt $e){
    echo $e->getMessage();
    $e->replaceNew();
    //try{}catch(){}
}catch(Exception $e){
    echo $e->getMessage();
}
    $gw->work();


















