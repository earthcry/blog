<?php
$mysqli=@new mysqli("localhost","root","testmk","testdb");
if(mysqli_connect_errno()){
    echo "Error: ".mysqli_connect_error();
    $mysqli=null;
    exit;
}
$sql="insert into users(name,age,sex) values('ddd','23','nv')";
$result=$mysqli->query($sql);
if(!$result){
    echo "SQL error ".$mysqli->errno." : ".$mysqli->error;;
    exit;
}
if($mysqli->affected_rows>0){
    echo "affected rows";
}
echo "last autoup ID : ".$mysqli->insert_id;
$mysqli->close();
