<?php
define("ROOT",str_replace("\\","/",dirname(__FILE__)).'/');
require ROOT."libs/Smarty.class.php";

$smarty=new Smarty();

$smarty->setTemplateDir(ROOT."template");
$smarty->setCompileDir(ROOT."compiled");
$smarty->left_delimiter="<{";
$smarty->right_delimiter="}>";
$smarty->auto_literal=false;
