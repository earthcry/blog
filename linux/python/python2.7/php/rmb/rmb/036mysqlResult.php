<?php
//get data from result;
//print table method;
$link=mysql_connect("localhost","root","testmk");
mysql_select_db("testdb");
$sql="select name from users";
$result=mysql_query($sql);
$data0=mysql_fetch_row($result);
$data1=mysql_fetch_assoc($result);
$data2=mysql_fetch_array($result);
$data3=mysql_fetch_object($result);
print_r($data);echo "<br>";
//get values by vars;
list($id,$name,$age)=mysql_fetch_row($result);
//get every row array by while&fetch;
//get every colum from row by foreach;
while($row=mysql_fetch_assoc($result)){}
foreach($row as $col){}
//get all fieldNames by for&numFields.
$cols=mysql_num_fields($result);
$rows=mysql_num_rows($result);
for($i=0;$i<$cols;$i++){
    echo mysql_field_name($result,$i);
}
mysql_free_result($result);
mysql_close();
