<?php
//
//      time & date
//
//  日期和时间；
//  
//  时间戳，具体为time(); 方便运算；
//  time(),  把当前日期转化为戳；当前系统时间；
//  mktime();把给定日期转化为戳；mktime($H,$i,$s, $m,$d,$Y);
//  date(),  把戳转化成日期de各种格式；        
//          三个函数通过时间戳来关联；
//  strtotime();英文文本转化为日期；
//  
//  date_default_timezone_set('prc');   the People's Republic of China 
echo date('Y-m-d H:i:s',time()+8*60*60).'<br>';
echo date('Y-m-d H:i:s', -60*60*24*3 +time()+8*60*60).'<br>';
mktime($h,$i,$s, $m,$d,$y);
mktime(0,0,0, $m,$d,$y);
floor()//四舍五入，取整；

date('', mktime());

$str='2014-11-12 11:11:11';
strtotime();    // 文本 转成时间戳；

// microtime() 
microtime()     // 微妙 时间戳；
microtime(true) // 时间戳.微妙；
$start=microtime(true);
for($i=0;$i<100000;$i++){

}
$end=microtime(true);
echo $end-$start;

// 日历算法

//  1.var set, request
date_default_timezone_set("prc");
$y=isset($_GET['year'])?$_GET['year']:date('Y');
$m=isset($_GET['month'])?$_GET['month']:date('m');
$d=isset($_GET['date'])?$_GET['date']:date('d');
//year and month
//week
//date
//date
////for
////pre space
////m
////end space
echo '<table border="1" width="800" align="center">';
echo '<tr><td colspan=7 align="center">'.$y.'年'.$m.'月'.'</td></tr>';
echo '<tr><th>日</th><th>一</th><th>二</th><th>三</th><th>四</th><th>五</th><th>六</th></tr>';
echo '<tr>';
$t=date('t');
$w=date('w', mktime(0,0,0, $m,1,$y));
for($i=0;$i<$w;$i++){
    echo '<td>'.'&nbsp;'.'</td>';
}
for($i=0;$i<$t;$i++){
    echo '<td>'.($i+1).'</td>';
    if(($w+$i+1)%7==0)
        echo '</tr><tr>';
}
$ys=($w+$t)%7;
if($ys>0){
    $n=7-$ys;
    for($i=0;$i<$n;$i++)
        echo '<td>'.'&nbsp;'.'</td>';
}
echo '</tr>';
echo '</table>';
















