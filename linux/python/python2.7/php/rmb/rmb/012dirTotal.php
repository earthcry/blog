<?php
//Frame Realize and Iteration Realize.
//Realize:computer a dir of dirTotal dir and dirTotal file;
//dirname;
//dirnum;refVar;
//filenum;
$dirname='C:\AppServ\www\phpMyAdmin';
$dirnum=0;
$filenum=0;

function dirTotal($dirname,&$dirnum,&$filenum){
    //open;
    //read dir all;if;
    $dir=opendir($dirname);
    readdir($dir);
    readdir($dir);
    while($filename=readdir($dir)){/////////////?
        $alldir=$dirname.'/'.$filename;
        if(is_dir($alldir)){
            dirTotal($alldir,&$dirnum,&$filenum);
            $dirnum++;
        }else{
            $filenum++;
        }
    }
    closedir($dir);
}
dirTotal($dirname,$dirnum,$filenum);

echo $dirnum;
echo '<br>';
echo $filenum;
echo '<br>';
