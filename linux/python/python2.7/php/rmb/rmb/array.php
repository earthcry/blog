<?php
//
//  array:php array not need order, and not need associate.
//  php array is a order picture data structure.
//  index array and associate arrary.
//  php array key : [] or {}; $arr[] or $arr{}
//  $arr[str] $arr['one'] $arr[one] //the secend is contant.
//  $arr['8']---$arr[8]
//  $arr['08']---$arr['08'] //8 jinzhi, not a shi jinzhi.
//  $arr['2.7']---$arr['2']
//  $arr[null]----$arr['']
//  $arr[true]----$arr[1]
//  $arr[false]---$arr[0]
//  array keyup start 0 then up from max number.
//  array_values(),rebuild index. 
//  
//  array bianli:
//  for/foreach/list,each,while/offset
//  for/list ----index array & lianxu array.
//
//  $_SERVER;
//  $arr=!empty($_POST) ? $_POST : $_GET;
//  $_REQUEST,same name,no safe.
//
//
//
//
//
//
//
/*
for($i=0; $i<10; $i++){
    $arr[]=$i*$i;
}
echo "<pre>";
    print_r($arr);
echo "</pre>";

$arr=array(3,2,6);
$arr=[4,2,9];//php5.4
echo "<pre>";
    print_r($arr);
echo "</pre>";
function demo(){
    return array("one", "two", "three");
}
echo demo()[1];
 */


//select last;
function sellast($m, $n){
    for($i=0;$i<$m;$i++){
        $arr1[]=$i;
    } 
    delele($m, $n, $arr1);
    return $arr1;

}
function delele($mm, $nn, &$arr){
    $i=0;
    while(count($arr)>1){
        if($i=0){
            $flen=count($arr);
        }
        if($i%$nn==0){
            echo $arr[$i].'<br>';
            unset($arr[$i]);
        }
        $i++;
        if($i>$flen){
            $i=1;
            $arr=array_values($arr);
        }
    }
}
echo "<pre>";
    print_r(sellast(10,3));
echo "</pre>";

// for eacharray : array elenum and keynum;
$arr=[1,3,5];
for($i=0;$i<count($arr);$i++){
    echo $arr[$i];
}

list($x, ,$z) = array("aa", "bb", "cc");
echo $x.'<br>';echo $z.'<br>';
list($name, $pro)=explode("_", "aaa_bbb");
echo $name;echo $pro;echo '<br>';















