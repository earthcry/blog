<?php
/*
多路分支，只能进入一个，先从不能执行的顺序开始；
elseif  条件是范围；
switch  条件是点值；
    1key --- 1value;
    keys --- 1value;//去除break;

while --- 条件；
for   --- 计数；

break/continue/exit(str)/die();

goto biaoji;

while/do ... while/for/
for(a1; a2; a3){
       b1;
}
执行顺序：
a1
a2
b
a3
a2


 */
$score=200;

if($score < 60){
    echo "cha";
}else if($score < 70){
    echo "yiban";
}else if($score < 80){
    echo "hao";
}else if($score < 90){
    echo "liang";
}else if($score < 100){
    echo "you";
}else{
    echo "error";
}
switch ($a){
    case 3 :
        echo "";
        break;
    case 6 :
        echo "";
        break;
    default :
        echo "";
}

for($i=0; $i<10; $i++){}
for($i=0,$j=100; $i<100 || $j>0; $i++,$j--){
    echo "{$i}aaaaa,{$j}bbbbbb<br>";
}

echo "1111111111111";
goto biaoji;
echo "2222222222222";
biaoji:
echo "3333333333333";







