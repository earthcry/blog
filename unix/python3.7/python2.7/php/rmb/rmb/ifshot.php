<?php
	$bool = false;               //声明一个boolean型变量，值为假
	$num = 10;               	 //声明一个整型的变量做计数使用，初始值为10
    
	if( $bool && ($num++ >0) ) { //”&&”前面的表达式为false，发生短路，$num++没有执行到，$num的值保持不变
		echo "条件不成立<br>";
	}
	echo $num;             		 //$num没有执行递增，输出的结果仍为$num的原值10;
     
	if( $bool & ($num++ >0) ) {  //”&”不会发生短路，两边都会执行到，$num++被执行，$num自增1
		echo "条件不成立<br>";
	}
	echo $num;              	 //$num执行了递增，输出的结果为$num递增后的值11;

	$bool = true;              	 //声明一个boolean型变量，值为真
	$num = 10;               	 //声明一个整型的变量做计数使用，初始值为10
     
	if( $bool || ($num++ >0) ) { //”||”前面的表达式为true，发生短路，$num++没有执行到，$num的值保持不变
		echo "条件成立<br>";
	}
	echo $num;             		//$num没有执行递增，输出的结果仍为$num的原值10;
 
	if( $bool | ($num++ >0) ) { //”|”不会发生短路，两边都会执行到，$num++被执行，$num自增1
		echo "条件成立<br>";
	}
	echo $num;      			//$num执行了递增，输出的结果为$num递增后的值11;
    //
    //
    //
	//如果$num是整型就执行后面的运算，不是就不执行后面的表达式，and同使用&&一样
	is_int($num) and $num += 10;	
