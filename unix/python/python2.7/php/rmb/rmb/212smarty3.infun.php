<?php
//HJKL
//
//
//
//
include "InitTEO.inc.php";

$lamp=array('os'=>'linux', 'ws'=>'apache', 'db'=>'mysql', 'sc'=>'php');
$smarty->assign("lamp", $lamp);
$lamp1=array('linux', 'apache', 'mysql', 'php');
$smarty->assign("lamp1", $lamp1);

$link=mysql_connect("localhost", "root", "testmk");
mysql_select_db("testdb");
$sql="select id,name,age,sex from users";
$result=mysql_query($sql);

$i=0;
while($row=mysql_fetch_assoc($result)){
    $data[$i]=$row;
    $i++;
}

$smarty->assign("data",$data);


mysql_free_result($result);
mysql_close();


$smarty->display("default/index.html");
