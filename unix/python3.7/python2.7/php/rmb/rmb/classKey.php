<?php
/*

    keywords of object.

    instanceof
    final:
    static:unset when script finish.
    static:fast but can not access unstatic member.
    const define(key, val) in class. part constant.cstt
    self --->class;when class access members inside.
    this---->object;

    magic method
    magic method is auto called function.
    
    __toString() //when echo $obj directly.

    serial parallel
    __wakeup
    __clone
    __construct


 */
class Person {}
class Student extends Person {}
$p=new Person;
$s=new Student;
echo $p instanceof Student; //false
echo $s instanceof Student; //true
echo $s instanceof Person;  //true

final class Myclass {                  //can not extends
    protected $name;

    public final function say(){       //can not extends
    
    }
}
// when class name appear first, the static property puted into ram.
class stcMember {
    public static $counter="cn";        // subclass share one property in ram.
    const  HOST="localhost"; 

    function __construct(){
        self::$counter++;
        self::HOST;
    }

    static function getCounter(){
        return self::HOST.self::$counter;
    }
}
echo stcMember::$counter;               // class name strMember appear first
$obj1=new stcMember();
$obj2=new stcMember();
echo $obj1->country;                    // error;static property is class ,and not object.
echo stcMember::getCounter().'<br>';
echo $obj2->getCounter();
;

// __invoke()
//$obj();
//$obj->var;
//
//__call():
//when to run a func that not exist.
//many func than function is likely.
$narr=array("aaa", "bbb", "ccc");
function __call($method, $args){
    if(in_array($method, $args)){
        echo $args[0];
    }else{
        echo "no exist.";
    }
}
$p1->aaa();
$p1->bbb();
//
// static __callstatic(){}
//Person::unexistfunc();
//
// static __set_state($arr){}
//

//__clone():
//when clone a object it be called,
//it initialize cloned object as same as __construct();
$p2 = clone $p1;    //
$p2 = $p1;          //have two same values in zhan.
$p2 = &$p1;         //have one same values in zhan.
//
//__toString():
//when echo $obj directy, to run __toString();
//
class stgFun {
    private $str;
;
    function __construct($str){
        $this->str=$str;
    }

    function __toString(){
        return $this->str."<br>";
    }
}
$obj=new stgFun("hello");
echo $obj;
//
//__autoload():
//when classname appear in php,to call and pass class name.
function __autoload($className){
    include "./".$className.".class.php";
}
$p1=new Person;
Person::name;
//
//serial object and readwrite file.
//
//serialize() and __sleep();
//unserialize() and __wakeup():
//save object in ram to file or DB or net.
//to binary string.
//bad fly return to factory. come to parts.
$objString=serialize($obj);
function __sleep(){              //part property serial through magic method.
    return array($name, $age);
}
file_put_contents("file.txt", $objString);

$obj2=unserialize($objString);
function __wakeup(){             // initialize object like __construct and __clone.
    $this->age=40;               // before sleep age:30, sleep fo 10 years
}
$objString = file_get_contents("file.txt");

// array serial
//
$arr=array("name"=>"zhang", "age"=>"23", "sex"=>"nan");
$str=json_encode($arr);
$objarr=json_decode($str, true);    //false:obj, true:array.
var_dump($objarr);



















