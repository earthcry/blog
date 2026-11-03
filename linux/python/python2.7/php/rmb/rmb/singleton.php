<?php
/*
    design pattern

    1.singleton
    2.prototype
    3.builder
    4.factoryMethod
    5.abstractFactory

    singleton
    is for one class only can be build one object.
    same as "objects" share one real object in ram.
    when the second object try be constructed, private __construct can notice error. 

    logic:
    1.can not be construct.--->private--> function--> notice error.
    2.only constrct one.--> inside build--> 
    3.one object can be many called.--> static



 */
class Person {
    static $obj=null;
    private function __construct(){
        echo "start........<br>";
    }
    static function getobj(){
        if(self::$obj==null){self::$obj=new self;}
        return self::$obj;
    }
    function say(){
    
    }
    function __destruct(){
        echo "end...........<br>";
    }
}

$p= Person::getobj();
$p= Person::getobj();
$p= Person::getobj();



















