<?php
try {
    $pdo=new PDO("mysql:host=localhost;dbname=testdb", "root", "123456");
}catch(PDOException $e){
    echo $e->getMessage();
}

$sql="insert into users(name, age, sex) values(:name, :age, :sex)";
$stmt=$pdo->prepare($sql);

$p1=$stmt->execute(array(":name"=>"dd1", ":age"=>22, ":sex"=>"nan"));
var_dump($p1);
$p2=$stmt->execute(array(":name"=>"dd2", ":age"=>23, ":sex"=>"nv"));
var_dump($p2);
$stmt->execute(array(":name"=>"dd3", ":age"=>21, ":sex"=>"nan"));
$stmt->execute(array(":name"=>"dd4", ":age"=>20, ":sex"=>"nv"));

/*
$sql="delete from users where id = :id";
$stmt=$pdo->prepare($sql);

$stmt->execute(array(":id"=>26));
$stmt->execute(array(":id"=>25));
 */

$sql="update users set name='ddd' where id=:id";
$stmt=$pdo->prepare($sql);
$stmt->execute(array(":id"=>22));
$stmt->execute(array(":id"=>21))
