<?php
include "mytpl.class.php";

$tpl=new MyTpl("./templates/","./compile/");

$title="this is a title from db.";
$content="this is a content from db.";

$tpl->assign("title",$title);
$tpl->assign("content",$content);
$tpl->display("tpl.html");
