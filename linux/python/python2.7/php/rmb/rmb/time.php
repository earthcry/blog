<?php
//
//  time() & date()
//
date_default_timezone_set("prc")date_default_timezone_set("Etc/GMT-8"); // Asia/shanghai; prc; 
echo date("Y-m-d H:i:s",time());
;
//
//mktime()
echo date("Y-m-d H:i:s", time()).'<br>';
$y=1981;
$m=11;
$d=5;
$t=mktime(0,0,0,$m,$d,$y);
$curtime=time();
echo ($curtime-$t)/60/60/24/30/12;echo '<br>';
echo date("Y-m-d H:i:s",$t).'<br><br>';

//
// strtime()
//
$a="2014-11-12 11:20:22";
$b="2015-3-2";
echo strtotime($a).'<br>';
echo floor((strtotime($b)-strtotime($a))/60/60/24);echo '<br>';
//
//microtime()
//
echo microtime().'<br>';    // 0.****** **********
echo microtime(true).'<br>';// *********.****
//
//script excute time.
$start=microtime(true);
for($i=0;$i<10000;$i++){}
$end=microtime(true);
echo $end-$start;echo '<br><br>';
















