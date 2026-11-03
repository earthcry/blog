<?php
//HJKL
//
//模板间的继承
//1.在子模板中的第一行用<{extends file="parentTpl"}>
//2.在php中用smarty->display("extends:parent.tpl|child.tpl|cchild.tpl");
//继承后的改变
//1.父模板中定义<{block}>块；
//      <{block name="b1"}>aaaaa<{/block}>
//      <{block name="b2"}>aaaaa<{/block}>
//      <{block name="b3"}>aaaaaa<{$smarty.block.child}>aaaaaaa<{/block}>
//      <{block name="b4"}>newDDDDD<{/block}>
//2.在子模板中重定义块；
//      <{block name="b1" append}>bbbbb<{/block}>
//      <{block name="b2" prepend}>11111<{/block}>
//      <{block name="b3"}>newAAAA<{/block}>
//      <{block name="b4"}>ddddd<{$smarty.block.parent}>ddddd<{/block}>
//
//
//
//
//
include "InitTEO.inc.php";




$smarty->display("default/index.html");
