<?php
/*
 *      类、对象
 *
 */  
//  1.思想，面向对象与面向过程，类与对象关系；
//  2.类/对象 概念/结构；
//      2.1属性与方法       如何抽象一个类?         $this
//      2.2内存中的对象,    如何实例化一个对象？如何访问存取对象成员？象数组一样？    
//      2.3构造与析构方法
//  3.封装性/魔术方法
//  4.继承性/
//      4.1继承/重载覆盖
//      4.2关键字       @static@const
//      4.3魔术方法     @__toString()@__clone()@__call()
//      4.4对象串行化   @serialize数组串行@json
//      4.41@__set_state(),eval(),var_export();
//      4.42
//      4.5自动加载     @__autoload();
//      4.6单态单例设计模式
//  5.多态
//      5.1抽象方法与抽象类
//      5.2接口
//      5.3多态
//  6.类魔术常量与函数；
//  7.命名空间
//      7.2子命名空间
//      7.3合并文件多个空间
//      7.4动态语言特征；
//      7.5别名
//
// 
// @1.
// 对象 直接代表对应物理世界的某个对象；
// 有了对象就有了物理世界与虚拟世界的对应。
//
// 面向对象，概念思想、结构、特性
// 
// ***面向过程，面向对象的思想***；
// 数组是个容器，对象是个思想；
// 语法与思想，互为表里；
// 过程，步骤；每步一个函数；以事件、过程为中心的思想,注重动作；
// 对象，类/对象；
// 对象，具体事和物，和抽象的规则、计划等；
// 对象，状态，和行为；变量和函数；
// 函数与对象：具体功能，函数来实现；所有类似/相关的功能用一个类/对象来实现；
// 面对相同的事务，从总体上划分为几个类/模块来实现；整体部分分解的思想，框架；
// 系统/元素，整体/对象的思想；
// 软件系统与现实世界结构相对应；
// 围绕现实对象结构来构造软件系统，而不是功能；
// *  数组和对象 ： 都属于php的复合类型（一个变量可以存储多个单元）
//*  对象比数组更强大， 不仅可以存储多个数据，还可以将函数存在对象
//   class is like a function, is a block, 
//   when only be called it exist in ram.

/
// @2.
// ***@概念结构
// 类/对象
// 类创建对象,多个对象；用类来实例化对象，对象应属于某一个类；
$p=new Name;
//  类相当于高级函数，实例化函数，实例化对象；
 // 类是所有相似对象共性的集中体现；还是包含所有？
 // 类是所有相关对象的共同的抽象和标准；配置单与；抽象与实现；
//  
//  对象
 // 
// @2.2
// 内存：栈堆段块；同类对象的区别只是属性的区别；
//
// 构造方法：对象创建后自动调用的方法；在内存中初始化、个性化新对象属性；__construct();
// 析构方法：对象释放前自动调用的方法；善后，关闭资源；__destruct();顺序竹简；
//
// ***@3.封装性
// 隐藏对象内部细节，控制访问(通过方法__get())；
 // public / private / protected 
 // 私有后的控制访问函数：
 // __get(); 直接访问私有成员是调用；名；
 // __set(); 直接设置私有属性时调用；名、值；
 // __isset();
 // __unset();
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
if(isset($p1->name)){echo $p1->name;}


// ***@4.继承性
 // 解决类的类的问题；猫科，虎，猫，豹；人，学生，老师，校长；
class Student extends Person {}
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
 // protected
//  重载/覆盖：父子中同名方法；子扩展父的功能行为parent::func();
//  权限：protected子权限>=父的权限private；
//  keywords:
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

//  instanceof:
echo $p instanceof Person;
//  final:
//  只能修饰类与方法，不能修饰属性；
final class Person {
    final function aaa(){}
}
//  @static:
//  1.相当于类的常量；
//  2.修饰属性和方法，不能修饰类；
class Person {
    var static $country;
    static function say(){
        echo self::$country;
    }
}
//  3.类的名字第一次出现时，被调入内存；
//  4.static members 要用class来访问：
echo Person::$name;
echo Person::say();
//  5.this-object; self-class;
//  6.释放；脚本结束；
//  7.静态方法是不能访问非静态成员；
//  8.尽量使用静态方法。不用创建对象，效率；
//  静态成员，        类来访问；
//  公开、默认的成员，对象来访问；
//  私有、保护的成员，内部来访问；
//
//  @4.6
//  单态/单例设计模式：某类只需创建一个对象；
//  团队分工开发时，避免重复创建对象的方法；
//  通过私有保护，方法控制来实现单例；由方法有控制的创建对象；
class Person {
    private function __construct(){    
    
    }
    static function getObj(){           
        $obj = new self;                // $obj 为函数内部变量,但不能内部声明，每次调用销毁；
        return $obj;
    }
}
class Person {
    private static $obj=null;           // 3.多个对象共用一个属性--对象；
    private function __construct(){     // 1.禁止外部创建对象；
    
    }
    static function getObj(){           // 2.使外部可以调用方法；
        if(is_null(self::$obj))         // 4.对象内部共有var：$obj;
            self::$obj = new self;      
        return self::$obj;
    }
    function __destruct(){
        echo "#################<br>";
    }
    function say(){
        echo "aaaaaaaaaaaaaaaa<br>";
    }
}
$a=Person::getObj();echo '<br>';
$b=Person::getObj();echo '<br>';
$a->say();echo '<br>';
$b->say();echo '<br>';


//  @const:
//  声明，常量；define("AAA", "aaa");
//  在类里声明常量：const；要求不被修改；
class Demo {
    const SEX="男";
    function say(){
        echo self::SEX;
    }
}
echo Demo::SEX;

//  魔术方法：
//  __construct(),__destruct(),__set(),__get(),__isset(),__unset();
//  __toString(): 用echo访问对象时调用，函数返回的内容；不能传参数；
class Person(){
    function __toString(){
        echo "Object base info.";
    }
}
$p=new Person();
echo $p;

// @__clone():
// 克隆对象时自动调用；
// 作用：与构造方法类似，初始化新对象；副本；
// $this 代表副本，以便给副本初始化；$that原本；
//
$p2=$p; // 不是克隆，是别名；
$p2=clone $p;

// @__call():
// 调用对象中一个不存在的方法时，被调用；
// 应用：同一函数，多个名字；
class Person{
    public $names=["aaa", "bbb", "ccc"];
    __call($func,$args){
        //echo "{$func} called is not exist."
        if(in_array($func, $this->names)){
            echo $args[0].'<br>';
        }else{
            echo "not exist";
        }
    }
}

// 对象的串行化：@serialize()
// 将对象转化成string;
// 作用：存储，传输；飞机维修；
$str=serialize($p);
file_put_contents("objstr.txt", $str);
$str=file_get_contents("objstr.txt");
$p=unserialize($str);
// __sleep():
// 对象串行化时自动调用，
// 作用，实现部分属性休眠串行化，默认全部串行；
__sleep(){
    return ["name", "age"];
}
// __wakeup():
// 反串行化时调用；
// 作用，初始化苏醒的对象；__wakeup(), __clone(), __construct();
__wakeup(){
    echo "睡了两年了";
    $this->age=12;
}
//
// 数组的串行化：@json_encode();
// 跨机器、跨语言、跨网站传输数组；
// json格式；
$arr=["name"=>"zhangsan", "age"=>19, "sex"=>"nan"];
$str=json_encode($arr);
$parr=json_decode($str); // 默认转成对象；
echo $parr->name;
$arr=json_decode($str, true);
//
// __set_state():
//
// 1.@eval()---检查并执行PHP代码；[iv l重新计算求出参数的结果]
//      把代码变成字符串可以进行匹配改查处理；
$str="echo 'abc';";
echo $str;      // echo 'abc';  --输出string内容；
eval($str);     // abc          --执行string内容；

// 2.var_export():
//  print_r(); 输出数组；
//  var_dump(); 输出变量值、类型、及相关；
//  var_export();输出值或返回string;而且是合法PHP代码；
$arr=["one"=>1, "two"=>"22222222", "three"=>333];
var_export($arr);          //echo value;
$a=var_export($arr, true); //return str;  字符串-exec->数组；
var_dump($a);              //string
eval('$b='.var_export($arr, true).';'); // 字符串-->数组；
var_dump($b);
//
eval('$b='.var_export($p, true).';');   // 字符串-->对象；
var_dump($b);

// @__set_state():
// 当var_export()输出对象时，自动调用__set_state();
// 作用：为输出的对象，自定义初始化；
// 注意：必须静态，数组参数；
public static function __set_state($args){
    $p=new Person("lisi", 30, "nv")
    $p->name=$args['name'];
    $p->age=$args['age'];
}
$p->name="lixiaosi";
$p->age=33;

// @4.41
// __invoke():
// 在对象后加（）时调用，$p();
//
// __callstatic($func, $args);
// 调用不存在静态方法时调用；
// 
// @__autoload($classname)：
// 在脚本中，类名出现时，自动调用；
function __autoload($classname){
    include strtolower($classname).'class.php';
}

//
// ***@5.多态性
////
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
// *抽象方法和抽象类
//
abstract class Person {
    abstract function say();
}
// 1.抽象类不能实例化对象，不能创建对象；
// 2.抽象类，具体类；一代家风,父类/子类；高级父类；
// 3.子类必须 全部 实现/覆盖 父类方法；
//
// 抽象方法作用：规定子类必须有这个方法；功能交给子类去实现；
//               抽类下任务，具类去实现；
//               任务/结构/标准;
// 抽象类作用：
//              是一种规范，规定具体类的结构，
// 接口：
//          1.方法都是抽象方法的抽象类；
//          2.成员属性必须是常量，不能有变量；
//          3.all public
//          4.interface 来声明；
//          5.implements Aa,Bb 来实现，extends 单继承；
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
class Demo{

}
abstract class Demo {

}
interface Demo {

}
interface func {
    const AA="nan";

    function aa();
    function bb();
    function cc();
}
interface Aa extends Bb {

}
abstract class Cc implements Aa,Bb {

}
// *多态
//  1.为程序模块扩展准备；usb设备的增加；
//
//  数组，类，接口是可以在参数里面这么限制的；
interface USB {
    const WIDTH =12;
    const HEIGHT =3;
    function load();
    function run();
    function stop();
}
class Computer {
    function useUSB (USB $usb) { //只能传USB这个类的对象；
        $usb->load();
        $usb->run();
        $usb->stop();
    }
}
class Mouse implements USB{
    function load(){
        echo "load mouse success.";
    }
    function run(){
        echo "run mouse.";
    }
    function stop(){
        echo "stop mouse.";
    }
}
class Worker {
    function work(){
        $c=new Computer;
        $m=new Mouse;
        $c->useUSB($m);
    }
}
$w=new Worker;
$w->work();
//
//  实例，图形计算器
//
// ***@类的常量与函数
//
__CLASS__;
__METHOD__;
//
//
// ***@7.命名空间
//
// 不能重复定义
// 1.常量；
// 2.函数；
// 3.类
//
namespace meizi\pl;    //前面上面不能有任何代码，除了declare(encoding="utf-8");

const AAA=1;

class Demo {
    static function one(){
        echo "11111111111<br>";
    }
}
function test(){
    echo "22222222222222<br>";
}
test();             //；当前目录；非限定名称；
meizi\pl\test();   //空间内函数；相对目录；限定名称；
\test();        //全局函数；根目录；完全限定名称；
//
// 1.同一脚本中使用多个空间，主要用于文件合并；
// 2.全局非空间代码与空间代码合并，只能使用匿名大括号形式；
// 3.大括号外，不能有任何代码；
namespace {     
    echo "这里是非命名空间代码，在合并时用";
}

//  *命名空间与动态语言特征
//  变量函数
function demo(){
    echo "1111111111111<br>";
} 
$fun=__NAMESPACE__.'demo';
$fun='meizi\pl\demo';  //  限定名称

$fun();             // 动态变化输出的，必须使用
// 变量函数、变量对象、常量；
\meizi\pl\demo();
namespace\demo();       //相当于变量；

// *别名/导入
namespace net\lampbrother\www
use net\lampbrother\www as bro, net\lampbrothe\bbs; // bro,bbs;

use \Hello;         //导入一个全局类，避免多个使用加\;
hello::one();
//
//
//
//
//
//
/*

    __class__
    __method__

    namespace
    const;
    function;
    class;
    
    namespace nudo\nu {;;;;;;}
    error;
    namespace {}



 */
namespace nudo\nu;
use nudo\nu as nd; //
use nudo\nu;       //nu

const CCC="constant";
class Classdm {
    static function classfunc(){
        echo "classfunc<br>";
    }
}
function func(){
    echo "funcccccccc<br>";
}
func();
\nudo\func();
echo CCC."<br>";
echo \nudo\Classdm::classfunc();

function demo2(){
    echo "aaaaaaaa";
}
$func='\nudo\nu\demo2'; //must use '\';
$func();

echo __NAMESPACE__.func();
echo namespace\func();

use \Hello;               // come in a global class.
Hello::one();




