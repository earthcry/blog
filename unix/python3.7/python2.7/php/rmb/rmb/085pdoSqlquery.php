<?php
//
//  PDOStatement
//
//  预处理：先编译一个语句，再处理多个结果(参数)；
//  预处理：先编译一个语句with param等待，再pass多个参数值后执行；
//
//  PHP预处理语句作用：
//  提高效率；编译执行分开；
//  提高安全；SQL注入；
//
//
//  Get result : fetch() fetchAll();
//
try {
    $pdo=new PDO("mysql:host=localhost;dbname=testdb", "root", "123456");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}catch(PDOException $e){
    echo "Connect Error: ".getMessage();
}
// 
// PDO two 占位符；
//
// ？    参数    ----索引数组
// :name 参数    ----关联数组
/*
$sql="insert into users(name, age, sex) values(?, ?, ?)";
$sql="update users set name=:name where id=:id";
//已备好语句并编译完成，等待分配数据；
$sql="insert into users(name, age, sex) values(:name, :age, :sex)";
$stmt=$pdo->prepare($sql);    //all sql can run;
//var_dump($stmt);
//
//
//  赋值方法一：
//
//绑定参数；
$stmt->bindParam(1, $name, PDO::PARAM_STR);
$stmt->bindParam(2, $age);  // ?,?,? no order, so must bind.
$stmt->bindParam(3, $sex);

$stmt->bindParam(":name", $name);
$stmt->bindParam(":age", $age);
$stmt->bindParam(":sex", $sex);

// bind once and exec more.

$name="kkdk";
$age="22";
$sex="nv";

if($stmt->execute()){
    echo "success";
    echo $pdo->lastInsertId();
}else{
    echo "failure";
}

$name="mmm";
$age="22";
$sex="nv";

if($stmt->execute()){
    echo "success";
    echo $pdo->lastInsertId();
}else{
    echo "failure";
}
//
//
//      赋值方法二：
//
$stmt->execute(array("wangwu1", 23, "nv"));
$stmt->execute(array("wangwu2", 23, "nv"));
$stmt->execute(array("wangwu3", 23, "nv"));

$stmt->execute(array(":age"=>22, ":name"=>"jjj", ":sex"=>"nan"));
$stmt->execute(array(":age"=>22, ":name"=>"lll", ":sex"=>"nan"));
$stmt->execute(array(":age"=>22, ":name"=>"kkk", ":sex"=>"nan"));
//$stmt->execute($_POST);
 */

//  Get result : fetch() fetchAll();

$sql="select name, age, sex from users where id > :id order by id";
$stmt=$pdo->prepare($sql);
$stmt->execute(array(":id"=>15));

/*
$row=$stmt->fetch(PDO::FETCH_NUM);
print_r($row);echo '<br>';
$row=$stmt->fetch(PDO::FETCH_ASSOC);
print_r($row);echo '<br>';
$row=$stmt->fetch(PDO::FETCH_BOTH);
print_r($row);echo '<br>';

$stmt->setFetchMode(PDO::FETCH_NUM);
while($row=$stmt->fetch()){
    print_r($row);echo '<br>';
}
 */

$stmt->setFetchMode(PDO::FETCH_ASSOC);  
$data=$stmt->fetchAll();

echo '<pre>';
print_r($data);
echo '</pre>';


// fetch()  allfetch()
$sql="select * from users";
$arr=null;
$stmt=$pdo->prepare($sql);
$stmt->execute($arr);

while($row=$stmt->fetch(PDO::FETCH_ASSOC)){;   // while 一维数组；
    print_r($row);echo '<br>';
}

$data=$stmt->fetchAll(PDO::FETCH_ASSOC);       // foreach 二维数组
foreach($data as $row){
    print_r($row);echo "****".'<br>';
}

echo $stmt->rowCount();   echo '<br>';  //total rows or affected rows;
echo $stmt->columnCount();echo '<br>';
echo $pdo->lastInsertId();echo '<br>';


$pdo=null;
//delete from users where id='5' or 1='1';//sql 注入；
