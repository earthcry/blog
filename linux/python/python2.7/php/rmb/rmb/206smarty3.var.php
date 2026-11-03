<?php
//HJKL
//smarty 中的三种变量；
//一、php中分配的变量；$str;
//      $smarty->assign();
//      动态变量；数据；
//
//二、配置文件中读取的变量；#str#;
//     smarty配置文件的内容：
//     是修改模板版式的、外观，非php的；
//     首页、二级页、三级页；
//
//三、保留变量；$smarty.str;
//      $_GET
//      $_POST
//      $_SESSION
//      $_SERVER
//      $_ENV
//      $_COOKIE
//      <{$smarty}>//数组
//
include "InitTEO.inc.php";
$smarty->display("default/index.html");
