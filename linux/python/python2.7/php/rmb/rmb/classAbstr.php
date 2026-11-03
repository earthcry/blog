<?php
//
//1.abstract method have not {}, have ";" and "abstract", & in class.
//2.abstract class is class of that have one or more abstract method,
//  and have a "abstract" ahead.
//3.abstract class can not instance object. 
//4.subclass must inheritance all abstract method, or is abstract class also.
//5.abstract class define function, subclass come to realize.
//
abstract class AbstrClass {
    abstract function aaa();   //no {};
    abstract function bbb();   //no {};
    function ccc(){

    }
}

class Subclass extends AbstrClass {
    function aaa(){
        echo "extends abstract,and add new function.";
    }
    function bbb(){
        echo "extends abstract,and update extends.";
    }
}
class Subclass2 extends AbstrClass {
    function aaa(){
        echo "I am subclass2, realize another";
    }
    function bbb(){
        echo "extends abstract2,and update extends.";
    }
}
$obj=new Subclass();
$obj->aaa();
