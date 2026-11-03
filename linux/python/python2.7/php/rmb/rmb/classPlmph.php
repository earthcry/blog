<?php 
//
//      Polymorphism
//      
//change differrent classobj,the same fun come to different result.
//
interface USB {
    const WIDTH = 12;
    const HEIGHT= 3;

    function load();
    function run();
    function unload();
}
class Computer {                       // only pass USB object.
    function autoLink(USB $usbdev){    // array, class, interface
        $usbdev->load();               // usbdev is a object.
        $usbdev->run();
        $usbdev->unload();
    }
}
class Mouse implements USB {
    function load(){
        echo "load mouse success.<br>";
    }
    function run(){
        echo "mouse is running.<br>";
    }
    function unload(){
        echo "mouse is unloaded.<br>";
    }
}
class Keyboard implements USB {
    function load(){
        echo "load keyboard success.<br>";
    }
    function run(){
        echo "keyboard is running.<br>";
    }
    function unload(){
        echo "keyboard is unloaded.<br>";
    }
    
}
class Worker {
    function plugin(){
        $c=new Computer();
        $m=new Mouse();
        $c->autoLink($m);
        $k=new Keyboard();
        $c->linkUSBDev($k);
    }
}

$u=new Worker();
$u->plugin();

































