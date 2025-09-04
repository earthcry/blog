<?php
try {
    $pdo=new PDO("mysql:host=localhost;dbname=testdb", "root", "123456");
}catch(PDOException $e){
    echo $e->getMessage();
}

$sql="select * from products where id > :id1 && id < :id2";
$stmt=$pdo->prepare($sql);


function dbtab($stmt,$arr,$data){

$stmt->execute($arr);
$data=$stmt->fetchAll(PDO::FETCH_ASSOC);

echo "<table border='1' width='800'>";
foreach($data as $row){
    echo "<tr>";
    foreach($row as $col){
        echo "<td>".$col."</td>";
    }
    echo "</tr>";
}
echo "</table>";
}


$arr1=array(":id1"=>3, ":id2"=>10);
$arr2=array(":id1"=>9, ":id2"=>20);

dbtab($stmt, $arr1, $data1);
dbtab($stmt, $arr2, $data2);




$pdo=null;
