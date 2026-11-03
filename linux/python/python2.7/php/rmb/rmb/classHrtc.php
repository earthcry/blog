<?php
/*
  class/object


    encapsulation cpsl
    inheritance hrtc
    polymorphism plmph

    1.when two classes have same property, get out and put in a new class.
    2.if want to extend a exist class, do not change it, 
      but maybe inheritance it by a new class. 

class add function with inheritance
inheritance of class is add property and update method.
inheritance class name by "extends" and class method by "parent".


*/
class Person {
    protected $name;

    function __construct($name=""){
        $this->name=$name;
    }
    
    function say(){
        echo "My name is {$this->name}.";
    }
}

class Student extends Person {
    private $school;

    function __construct($name="", $school=""){
        parent::__construct($name);
        $this->school=$school;
    }
    
    function say(){
        parent::say();
        echo "and study in {$this->school}.<br>";
    }
}
$stu=new Student("zhangsan", "edu");
$stu->say();
