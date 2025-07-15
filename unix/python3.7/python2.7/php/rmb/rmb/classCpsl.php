<?php
/*
  class/object


    encapsulation cpsl
    封装，即限制访问；
    封装，权限化 对象成员的访问；prtc
    private/protected/public



*/

class Person {
    private $name;
    private $age;
    private $sex;

//    function Person($name="", $age=0, $sex="nan"){
    function __construct($name="", $age=0, $sex="nan"){ //构造方法,初始化对象属性；
        $this->name=$name;
        $this->age=$age;
        $this->sex=setpro($sex);
    }
    function setpro($sex){
        if($sex=="nan" or $sex=="nv"){
            $this->sex=$sex;
        }else{
            return;
        }
    }
    function getpro($age){
        if($this->age < 20){
            return $this->age;
        }else if($this->age < 30){
            return $this->age-5;
        }else if($this->age < 40){
            return $this->age-10;
        }else{
            return 29;
        }
    }
    function __get($pro){               //访问私有属性时调用；
        return $this->$pro;
    }
    function __set($proname,$value){    //通用的 访问属性方法
        if($proname=="age" && ($value>100 || $value <0)){
            return;
        }
        $this->$pro=$value;
    }
    function __isset($pro){             //外部使用isset()访问时自动调用
        if($pro=="age"){return false;}
        return isset($this->$pro);
    }
    function __unset($pro){
        return unset($this->$pro);
    }

    function say(){
        echo "{$this->name} speak english well.";
    }
    function run(){
        $this->left();
        $this->right();
        $this->left();
        $this->right();
    }
    private function left(){
        echo "left<br>";
    }
    private function right(){
        echo "right<br>";
    }
    function __destruct(){  //析构方法，释放资源；顺序竹筒；
        echo "{$this->name} bye <br>";
    }
}
$p1=new Person("zhangsan", "24", "nan");

if(isset($p1->name)){echo $p1->name;}


















