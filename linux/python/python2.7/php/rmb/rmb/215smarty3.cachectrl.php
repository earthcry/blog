<?php
//HJKL
//
//smarty3的缓存控制
//$smarty->cacheing=true;
//$smarty->setCacheDir('');
//$smarty->cache_lifetime=60*60*24*7;
//
//$smarty->display("demo.tpl",$_SERVER["REQUEST_URI"]);
//
//if(!$smarty->isCached("demo.tpl", $_SERVER["REQUEST_URI"])){
//      cache content;
//      <{nocache}>cache content;<{/nocache}>
//      cache content;
//      cache content;
//}
//
//      uncache content;
//      uncache content;
//      uncache content;
//      uncache content;



include "InitTEO.inc.php";
$smarty->display("default/index.html");




