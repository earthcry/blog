<?PHP
/*
 *  1.php.ini
 *      file_uploads=on
 *      upload_max_filesize=200M // <ram
 *      post_max_size=250M
 *      upload_tmp_dir=c://upload;
 *  2.html
 *      method="post"
 *      type="file"
 *      enctype="multipart/form-data"
 *      hidden.MAX_FILE_SIZE.20000000;
 *  3.handle
 *      a. $_FILES["pic"]["error"]
 *
 *      b. $_FILES["pic"]["size"]
 *
 *      c. $_FILES["pic"]["type"]
 *
 *      d. rename upload file.
 *
 */
echo "<pre>";
    print_r($_POST);
    print_r($_FILES);
echo "</pre>";

//  array[key][value]
//  $_FILES['userfile']['name']
//  $_FILES[attachname][attachproperty]; 
//
//
//  handle errors;
if($_FILES["pic"]["error"] > 0){
     switch($_FILES["pic"]["error"]){
         case 1:
             echo "file size is out php.ini.";
             break;
         case 2:
             echo "file size is out hidden form.";
             break;
         case 3:
             echo "only some parts of file uploaded.";
             break;
         case 4:
             echo "file was not uploaded.";
             break;
         default:
             echo "unknow error.";
     } 
     exit;
}

//  limit size;
 $maxsize=20000000;
 if($_FILES["pic"]["size"] > $maxsize){
     echo "file uploaded is small than {$maxsize}";
     exit;
 }

 // limit type;
 $extns=array("png", "gif", "jpg", "jpeg");
 list($dl, $xl)=explode("/", $_FILES["pic"]["type"]);
 if($dl!="image"){
     echo "only picture can be uploaded.";
     exit;
 }else{
     $arr=explode(".", $_FILES["pic"]["name"]);
     $extn=$arr[count($arr)-1];
     if(!in_array($extn, $extns)){
         echo "only file extenssions of png/gif/jpg/jpeg can be uploaded.";
         exit;
     }
 }

 // rename;
 $filepath="./uploads/";
 $randname=date("Y").date("m").date("d").date("H").date("i").date("s").rand(100,999).'.'.$extn;
 if(is_uploaded_file($_FILES["pic"]["tmp_name"])){
     if(move_uploaded_file($_FILES["pic"]["tmp_name"], $filepath.$randname)){
         echo "upload success.";
     }else{
         echo "upload failed.";
     }
 }else{
     echo "not a upload file.";
 }


