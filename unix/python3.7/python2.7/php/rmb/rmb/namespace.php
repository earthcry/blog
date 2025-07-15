<?php
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




