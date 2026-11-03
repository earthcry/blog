<?php
//注释，数据库数据的查询显示；
$link=mysql_connect("localhost","root","123456") or die("connect error.");
mysql_select_db("testdb") or die("select db error.");
function disptable($tabname){
    //$sql="select * from {$tabname}";
    $sql="desc {$tabname}";
$result=mysql_query($sql);
echo '<table border="1">';
echo '<caption><h1>'.$tabname.'</h1></caption>';

echo '<tr>';
for($i=0;$i<mysql_num_fields($result);$i++){
    echo '<td>'.mysql_field_name($result,$i).'</td>';
}
echo '</tr>';

while($row=mysql_fetch_assoc($result)){
    echo '<tr>';
    foreach($row as $col){
        echo '<td>'.$col.'</td>';
    }
    echo '</tr>';
}
echo '</table>';
echo '<br>';
mysql_free_result($result);
}
disptable('users');
disptable('products');
mysql_close();
