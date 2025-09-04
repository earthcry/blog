<?php
//MySQL扩展库mysql,mysqli,pdo;
//1.connect db,2.select db,3.exec sql,4.do error,5.close link.;
$link=mysql_connect("localhost","root","testmk");

if(!link){
    echo "Not connect";
    exit;
}

mysql_select_db("testdb");
