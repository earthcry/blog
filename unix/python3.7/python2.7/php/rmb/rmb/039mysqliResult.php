<?php
$mysqli=@new mysqli("localhost","root","testmk","testdb");
if(mysqli_connect_errno()){
    echo "Error: ".mysqli_connect_error();
    $mysqli=null;
    exit;
}
$sql="select * from users";
$result=$mysqli->query($sql);
if(!$result){
    echo "SQL error ".$mysqli->errno." : ".$mysqli->error;;
    exit;
}
echo '<table border=1>';

echo '<tr>';
while($field=$result->fetch_field()){
    echo '<th>'.$field->orgname.'</th>';
}
echo '</tr>';

$result->data_seek(3);
while($row=$result->fetch_assoc()){
    echo '<tr>';
    foreach($row as $col){
        echo '<td>'.$col.'</td>';
    }
    echo '</tr>';
};
echo '</table>';
echo $result->num_rows.'<br>';
echo $result->field_count.'<br>';
$result->free();
$mysqli->close();
