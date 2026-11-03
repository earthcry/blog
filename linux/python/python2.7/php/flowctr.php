<?php
/*

    flow control

 1.顺序结构
 2.分支结构, 单路if，双路else，多路elseif/switch，递进分支；
             加油，立交桥上下，abc三条路线，a院门b楼3单元门201门
             范围分支else，定值分支switch；
 3.循环结构，条件循环while,记数循环for; for($i=0;count($arr)>1;$i++)
             while, do...while, for, goto ,break,continue
 4.特殊语句：break,中断该层循环; continue跳过该次循环; exit中断脚本;
            break/continue/exit(str)/die();
 5.goto:特别灵活，可以模拟分支和循环；
 */
//多路分支，只能进一个，条件可简单：
$score=72;
if($score<=60){
    echo "cha";
}else if($score<=70){
    echo "yiban";
}else if($score<=80){
    echo "liang";
}else if($score<=90){
    echo "hao";
}else if($score<=100){
    echo "you";
}else{
    echo "error";
}
//多路分支范围用elseif,定值用switch
swith (int/string){
    case value1:
    case value2:
    case value3:
        comline;
        break;
    case value4:
        comline;
        break;
    case value5:
        comline;
        break;
    default:
        comline;
        break;
}
while(exp0){
    comline;
}
do{
    comline;
}while(exp0)
for(exp1;exp2;exp4){
    comline3;
}
for($i=0,$j=0;$i<10,$j<20;$i++,$j++){
    comline;
}
for($i=0,$j=100; $i<100 || $j>0; $i++,$j--){
    echo "{$i}aaaaa,{$j}bbbbbb<br>";
}

//小九九乘法
for($i=1;$i<10;$i++){
    for($j=1;$j<=$i;$j++){
        echo $j."x".$i."=".$i*$j."&nbsp&nbsp";
    }
    echo '<br>';
}
//1.总体类似表格的形式，故按行列的方式来打印；
//2.先两个嵌套记数循环，再定变量范围；

//continue, if($i%3==0)
//break 2,一下退出2层循环；
//exit;die("...");

//goto语法
echo "1111111111<br>";
goto bz;
echo "2222222222<br>";
bz:
echo "3333333333<br>";
//分支
$a=1;$b=2;
if($a>$b){
    goto big;
}else{
    goto small;
}
big:{
    echo "big";
}
small:{
    echo "small";
}
//循环
$x=false;
$i=0;
xx:
    echo "$i 111111111<br>";
    if($i>5){
        goto mz;
    }
    $i++;
goto xx;
mz:
    echo "mz";

//打印表格
<script>
var oriColor=null;
function onRow(obj){
    oriColor=obj.bgColor;
    obj.bgColor='red';
}
function outRow(obj){
    obj.bgColor=oriColor;
}
</script>







