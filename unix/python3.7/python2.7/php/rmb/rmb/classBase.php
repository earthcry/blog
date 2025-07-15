<?php
/*
  class/object


    1.class property must have a word ahead : var $a;
    2.accsess property inside, add "this" ahead. because class copy times in ram. 
    3.__construct() initialize object

    function aaa(){}
    class bbb {}

    class is like a function, is a block, 
    when only be called it exist in ram.


*/

class Person {
    var $name;
    var $age;
    var $sex;

//    function Person($name="", $age=0, $sex="nan"){
    function __construct($name="", $age=0, $sex="nan"){ //构造方法,初始化对象属性；
        $this->name=$name;  //内部存值；
        $this->age=$age;
        $this->sex=$sex;
    }

    function say(){
        echo "{$this->name} speak english well.";   //内部取值；
        $this->run();                               //内部调用方法；
    }
    function run(){
        echo "{$this->name} run fast.";
    }
    function __destruct(){  //析构方法，释放资源；顺序竹筒；
        echo "{$this->name} bye <br>";
    }
}
$p1=new Person("zhangsan", "24", "nan");    //用new创建对象；
$p2=new Person("lisi", "20", "nv");

$p1->name="zhang3";             //外部改变属性（存值）；
echo $p1->name;echo '<br>';     //外部获取属性（取值）；

$p1->say();echo '<br>';         //外部使用功能（调用方法）；
$p2->run();echo '<br>';
$p1=null;                       //改变资源释放顺序；













