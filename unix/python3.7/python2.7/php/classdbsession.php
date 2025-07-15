<?php
// 
//  class custom session save db.
//
class DBSession {
    public static $pdo;
    public static $ctime;
    public static $maxlifetime;
    public static $uip;
    public static $uagent;

    // start and init
    public static function start(PDO $pdo){
        self::$pdo=$pdo;
        self::$ctime=time();
        self::$maxlifetime=int_get("session.gc_maxlifetime");
        self::$uip="192.168.1.111";
        self::$uagent=!empty($_SERVER['HTTP_USER_AGENT'])?$_SERVER['HTTP_USER_AGENT']:"";

        // reg function,let PHP work self.
        session_set_save_handler(
            array(__CLASS__,"open"),
            array(__CLASS__,"close"),
            array(__CLASS__,"read"),
            array(__CLASS__,"write"),
            array(__CLASS__,"destroy"),
            array(__CLASS__,"gc"),
        );
        session_start();
    }
    // session_start();
    public static function open($path,$name){
        return true;
    }
    public static function close(){
        return true;
    }
    // echo $_SESSION['username']
    public static function read($sid){
        $sql="select * from session where sid=?";
        $stmt=self::$pdo->prepare($sql);
        $stmt->execute(array($sid));
        $result=$stmt->fetch(PDO::FETCH_ASSOC);
        // if no session ,
        if(!$result){
            return "";
        }
        // if over time, destroy session
        if($result['utime']+self::$maxlifetime < self::$ctime){
            self::destroy($sid);
            return "";
        }
        // if ip and agent changed, destroy session
        if($result['uip']!=self::$uip || $result['uagent']!=self::$uagent){
            self::destroy($sid);
            return "";
        }

        return $return['sdata'];
    }
    // $_SESSION['username']="meizi"
    public static function write($sid,$data){

        // fetch exist data by sid
        $sql="select * from session where sid=?";
        $stmt=self::$pdo->prepare($sql);
        $stmt->execute(array($sid));
        $result=$stmt->fetch(PDO::FETCH_ASSOC);

        // if got, update or not insert.
        if($result){
            // only update when data not same.
            if($result['sdata']!=$data || $result['utime']+30 < self::$ctime){
                $sql="update session set sdata=?,utime=? where sid=?";
                $stmt=self::$pdo->prepare($sql);
                $stmt->execute(array($data,self::$ctime,$sid));
            }

        // if not, insert.
        }else{
            if(!empty($data)){
                $sql="insert into session(sid,sdata,utime,uip,uagent) values(?,?,?,?,?)";
                $stmt=self::$pdo->prepare($sql);
                $stmt->execute(array($sid,$data,self::$ctime,self::$uip,self::$uagent));
            }
        }
    }
    // session_destroy()
    public static function destroy($sid){
        $sql="delete from session where sid=?";
        $stmt=self::$pdo->prepare($sql);
        return $stmt->execute(array($sid));
    }
    // recycle
    public static function gc($maxlifetime){
        // utime + self::$maxlifetime < ctime
        $sql="delete from session where utime < ?";
        $stmt=self::$pdo->prepare($sql);
        return $stmt->execute(array(self::$ctime-self::$maxlifetime));
    }
}

DBSession::start($pdo);












