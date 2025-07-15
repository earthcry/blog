<?php
//  
//  PDO
//
//
//  PDO prepare fetch
//
//1.PDO类，connect/query;
//2.PDOSatement类,准备语句、结果集；
//3.PDOException;
//4.很多常量；
//
//创建PDO对象：
//数据源dsn（data source name）
//主机地址、数据库名、数据库驱动
//$mysqli=new mysqli("localhost", "root", "12345", "testdb");
//connect by create a PDO object in trycatch.
//$dsn/dsn.ini->uri:dsn.ini;
//php.ini->pdo.dsn.meizi="mysql:host=localhost;dbname=xsphp";
try{
    $dsn="drv:dburl";
    $dsn="mysql:host=localhost,dbname=xsphp";
    $user="root";$pass="123456";
    $drv_opts=array(PDO::ATTR_AUTOCOMMIT=>0,PDO::ATTR_PERSISTENT=>true);

    $pdo=new PDO($dsn,$user,$pass,$drv_opts);
}catch(PDOException $e){
    echo "Connect Error:".$e->getMessage();
    exit; 
}

echo $pdo->getAttribute(PDO::ATTR_PERSISTENT).'<br>';
echo $pdo->getAttribute(PDO::ATTR_AUTOCOMMIT).'<br>';
echo $pdo->getAttribute(PDO::ATTR_CLIENT_VERSION).'<br>';
echo $pdo->getAttribute(PDO::ATTR_SERVER_INFO).'<br>';
echo $pdo->getAttribute(PDO::ATTR_SERVER_VERSION).'<br>';
echo $pdo->getAttribute(PDO::ATTR_DRIVER_NAME).'<br>';

$pdo=null;
