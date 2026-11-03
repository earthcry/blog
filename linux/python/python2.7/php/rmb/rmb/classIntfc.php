<?php
/*      Interface
 *
 *      
 *      Abstract class & Interface
 *      same:
 *          1.have abstract method.
 *          2.can not instance object.
 *          3.define function for subclass.
 *
 *      different:
 *          1.interface all method must be abstract.
 *          2.member property must be constant.
 *          3.all method must be public.
 *          4.implements not extends(=include).
 *
 * 因为在PHP是单继承的， 如果使用抽象类，子类实现完抽象类就不能再去继承其它的类了。
 * 如果即想实现一些规范， 又想继承一个其他类。就要使用接口
 *    可以使用抽象类去实现接口中的部分方法
 *
 *    使用implements的两个目的
 *    	1. 可以实现多个接口 ，而extends词只能继承一个父类
 *    	2. 没有使用extends词，可以去继承一个类， 所以两个可以同时使用
 *
 *
 *             class Name {}
 *    abstract class Name {}
 *         interface Name {}
 *
 *   多态：  多态是面向对象的三大特性之一
 *
“多态”是面向对象设计的重要特性，它展现了动态绑
定（dynamic binding）的功能，也称为“同名异
式”（Polymorphism）。多态的功能可让软件在开发和维护
时，达到充分的延伸性（extension）。事实上，多态最直接
的定义就是让具有继承关系的不同类对象，可以对相同名称
的成员函数调用，产生不同的反应效果。
 *
 * 
 *
*/
interface Demo {
    const HOST="localhost";
    const USER="admin";        //not var member.

    function fun1();           //not word "abstract";
    function fun2();           //must is public,not protected.
}
echo Demo::USER;

interface Demo2 extends Demo {
    function fun3();
    function fun4();
}

interface Demo3 {
    function fun5();
}

class Ddd {
    function fun6(){
    
    }
} 

//must implements all func in interface.
class Test extends Ddd implements Demo2,Demo3 {    
    function fun1(){
    
    }

    function fun2(){
    
    }

    function fun3(){
    
    }

    function fun4(){
    
    }

    function fun5(){
    
    }
}
