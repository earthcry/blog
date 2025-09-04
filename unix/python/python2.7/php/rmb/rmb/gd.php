<?php
//
//  GD Library
//
//  1.create a.bgimg.
//  2.draw a string on bgimg.
//  3.create b.bgimg.
//  4.copy one part from b.bgimg to a.bgimg.
//  5.sarv a.bgimg.
//
//
//  1.thumb     //  imagecopyresampled()    //same thumb 
//  2.imgcut    //  imagecopyresampled()
//  3.strmark   //  imagettftext()/imagestring()
//  4.imgmark   //  imagecopy()
//  5.rotate    //  imagerotate()
//  6.reversal  //  imagecopy()     "one colume pix by one to move"

//  1.create resource (size, color)
    $img=imagecreatetruecolor(300,300);
    $white=imagecolorallocate($img,"0xff","0xff","0xff");
    $red=imagecolorallocate($img,"255","0","0");
    $green=imagecolorallocate($img,"0","0xff","0");
    $blue=imagecolorallocate($img,"0","0","0xff");
    imagefill($img,0,0,$white);
    
//  2.draw shapes and words on created image.
    imageline($img,0,0,200,200,$blue);
    
    imagerectangle($img,50,50,150,150,$red);
    imagefilledrectangle($img,75,75,125,125,$blue);

    imageellipse($img,50,50,130,110,$red);
    imagefilledellipse($img,50,50,60,50,$red);
    
    imagearc($img,50,50,120,100,0,-90,$blue);

    imagestring($img,5,150,150,"hello world",$blue);
    imagestringup($img,5,150,150,"hello world",$blue);

    imagettftext($img,20,0,10,100,$green,"./msyh.ttf","妹子漂亮吗？");
    imagettftext($img,18,45,10,300,$blue,"./msyh.ttf","妹子漂亮吗？");
//
//  3.save and echo
    imagepng($img,"./test.png");
    //header("Content-Type:images/png");
    echo '<img id="id" class="img" src="./test.png">';
//  4.destroy resource.
    imagedestroy($img);

function thumb($imgfile,$width,$height){
    list($w,$h,$type)=getimagesize($imgfile);
    $types=array("img","gif","jpeg","png");
    $crtstr="imagecreatefrom".$types[$type];
    $srcimg=$crtstr($imgfile);

    if($h/$w <= $height/$width){        //same thumb;
        $height=$height*$h/$w;
    }else{
        $width=$width*$w/$h;
    }
    $dstimg=imagecreatetruecolor($width,$height);
    imagecopyresampled($dstimg,$srcimg,0,0,0,0,$width,$height,$w,$h);

    $savestr="image".$types[$type];
    $savestr($dstimg,"new".$imgfile);
    echo '<img id="id" class="img" src="new'.$imgfile.'">';
    imagedestroy($srcimg);
    imagedestroy($dstimg);
}
thumb("mm1.jpg",200,200);    

function imgcut($imgfile,$x,$y,$width,$height){
    list($w,$h,$type)=getimagesize($imgfile);
    $types=array("img","gif","jpeg","png");
    $crtstr="imagecreatefrom".$types[$type];
    $srcimg=$crtstr($imgfile);
    $dstimg=imagecreatetruecolor($width,$height);

    imagecopyresampled($dstimg,$srcimg,0,0,$x,$y,$width,$height,$width,$height);//on src

    $savestr="image".$types[$type];
    $savestr($dstimg,"new".$imgfile);
    echo '<img id="id" class="img" src="new'.$imgfile.'">';
    imagedestroy($srcimg);
    imagedestroy($dstimg);
}
echo '<img id="id" class="img" src="mm1.jpg">';
echo "<pre>";
    print_r(getimagesize("mm1.jpg"));
echo "</pre>";

imgcut("mm1.jpg",100,100,200,200);

function strmark($imgfile,$string){
    list($w,$h,$type)=getimagesize($imgfile);
    $types=array("img","gif","jpeg","png");
    $crtstr="imagecreatefrom".$types[$type];
    $srcimg=$crtstr($imgfile);
    
    $white=imagecolorallocate($srcimg,255,255,255);
    $green=imagecolorallocate($srcimg,0,255,0);
    $blue=imagecolorallocate($srcimg,0,0,255);

    imageline($srcimg,0,$h/2,$w,$h/2,$blue);
    imageline($srcimg,$w/2,0,$w/2,$h,$blue);

    $x=$w/2-strlen($string)*imagefontwidth(40)/2;       // size ?
    $y=$h/2+imagefontheight(40)/2;                      // size ?
    
    imagettftext($srcimg,40,0,$x,$y,$white,"msyh.ttf",$string);
    imagettftext($srcimg,40,0,$x+3,$y+3,$green,"msyh.ttf",$string);

    $save="image".$types[$type];
    $save($srcimg,"new".$imgfile);
    echo '<img id="id" class="img" src="new'.$imgfile.'">';
    imagedestroy($srcimg);
}
strmark("mm1.jpg", "hello world");

function imgmark($imgfile,$smlimg){
    list($w,$h,$type)=getimagesize($imgfile);
    list($smlw,$smlh,$smltype)=getimagesize($smlimg);
    $types=array("img","gif","jpeg","png");
    $crtstr="imagecreatefrom".$types[$type];
    $dstimg=$crtstr($imgfile);
    $srcimg=$crtstr($smlimg);
    
    $x=rand(3,$w-$smlw);
    $y=rand(3,$h-$smlh);
    imagecopy($dstimg,$srcimg,$x,$y,0,0,$smlw,$smlh);

    $save="image".$types[$type];
    $save($dstimg,"new".$imgfile);
    echo '<img id="id" class="img" src="new'.$imgfile.'">';
    imagedestroy($srcimg);
    imagedestroy($dstimg);
}
imgmark("mm1.jpg", "df.jpg");

function reversal_y($imgfile){
    list($w,$h,$type)=getimagesize($imgfile);
    $types=array("img","gif","jpeg","png");
    $crtstr="imagecreatefrom".$types[$type];
    $srcimg=$crtstr($imgfile);

    $newimg=imagecreatetruecolor($w,$h);

    for($i=0;$i<$w;$i++){
        imagecopy($newimg,$srcimg,$w-$i,0,$i,0,1,$h);
    }
    
    $save="image".$types[$type];
    $save($newimg,"new_y".$imgfile);
    echo '<img id="id" class="img" src="new_y'.$imgfile.'">';
    imagedestroy($srcimg);
}
function reversal_x($imgfile){
    list($w,$h,$type)=getimagesize($imgfile);
    $types=array("img","gif","jpeg","png");
    $crtstr="imagecreatefrom".$types[$type];
    $srcimg=$crtstr($imgfile);

    $newimg=imagecreatetruecolor($w,$h);

    for($i=0;$i<$h;$i++){
        imagecopy($newimg,$srcimg,0,$h-$i,0,$i,$w,1);
    }
    
    $save="image".$types[$type];
    $save($newimg,"new_x".$imgfile);
    echo '<img id="id" class="img" src="new_x'.$imgfile.'">';
    imagedestroy($srcimg);
}
echo '<img id="id" class="img" src="mm1.jpg">';
reversal_y("mm1.jpg");
reversal_x("mm1.jpg");


function rotate($imgfile,$angle){
    list($w,$h,$type)=getimagesize($imgfile);
    $types=array("img","gif","jpeg","png");
    $crtstr="imagecreatefrom".$types[$type];
    $srcimg=$crtstr($imgfile);
    
    $white=imagecolorallocate($srcimg,255,255,255);

    $rttimg=imagerotate($srcimg,$angle,$white);

    $save="image".$types[$type];
    $save($rttimg,"new".$imgfile);
    echo '<img id="id" class="img" src="new'.$imgfile.'">';
    imagedestroy($srcimg);
}
rotate("mm1.jpg", 30);











