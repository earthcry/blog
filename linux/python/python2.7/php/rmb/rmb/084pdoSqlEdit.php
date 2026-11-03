<?php
//  
//  PDO
//  query($sql)
try{
    $pdo=new PDO("mysql:host=localhost;dbname=testdb", "root", "123456");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}catch(PDOException $e){
    echo "Connect Error:".$e->getMessage();
    exit;
}

// SQL 
// one sql: exec() / query();
// mul sql: prepare()&execute();
//
// $pdo->exec() return int data, number;
// $pdo->query() return resource data, reusult;
// $pdo->prepare() return object data, stmt; array[][];
//
// sql query: result class;select; query(),prepar()&execute();
// sql edit : change rows :update, delete, insert; exec();prepar()&execute();
//
// error mode:
//      errmode_silent 
//      errmode_warning  
//      errmode_exception 
//
//      $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
//
// transaction processing: //事务处理
//      mul sql true;buy;
//      InnoDB; engine=innoDB;old:type=innoDB; 
//      ram edit:can rollback;
//      db  edit:commit;
//      
// create innoDB:
//      create table demo(id int,user char(30),act double)engine=innoDB;
//      set autocommit=0;
//      start transaction;
//      rollback;
//      commit;
//
try{
    // exec insert
    $sql="insert into users(name, age, sex) value('hhh', '33', 'nv')";
    $affected_rows=$pdo->exec($sql);
    echo $pdo->lastInsertId().'<br>';
    // query
    $sql="select * from users";
    $stmt=$pdo->query($sql);        // return obj, also array[][];
    foreach($stmt as $arr){
        print_r($arr);echo '<br>';
    }
    // transaction processing
    $pdo->setAttribute(PDO::ATTR_AUTOCOMMIT,0);
    $pdo->beginTransaction();
    $price=500;

    $sql="update zhanghao set price=price-{$price} where id=1";
    $affected_rows=$pdo->exec($sql);
    if(!$affcted_rows)
        throw new PDOException("1false");

    $sql="update zhanghao set price=price+{$price} where id=2";
    $affected_rows=$pdo->exec($sql);
    if(!$affcted_rows)
        throw new PDOException("2false");

    echo "busness success.";
    $pdo->commit();
}catch(PDOException $e){
    echo $e->getMessage();
    $pdo->rollback();
}

$pdo->setAttribute(PDO::ATTR_AUTOCOMMIT,1);
$pdo=null;
