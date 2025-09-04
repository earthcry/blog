<?php
//HJKL
//
//
//
//
$cachefile="./cache/demo_".$_GET['page'].".html";
$cachetime=20;
if(!file_exists($cachefile) || (filemtime($cachefile)+$cachetime) < time()){
ob_start();




include "InitTEO.inc.php";
$smarty->display("default/index.html");




$html=ob_get_contents();
file_put_contents($cachefile, $html);
ob_flush();
}else{
    echo "######cachefile########";
    include $cachefile;
}
