<?php
error_reporting( E_ALL );
ini_set('display_errors', 1);


function db_connect() 
{
    $username="kb_ster";
    $password="kb_ster";
    $database="kb_ster";
    $port=3306;
    $host="192.168.10.254";

    error_reporting(0);
    mysqli_report(MYSQLI_REPORT_OFF);
    $con = mysqli_connect($host,$username,$password,$database,$port);

    if (mysqli_connect_errno()) {
        echo('mysqli connection error: ' . mysqli_connect_error());
        return false;
    }

    /* Set the desired charset after establishing a connection */
    mysqli_set_charset($con, 'utf8mb4');
    if (mysqli_errno($con)) {
        echo('mysqli error: ' . mysqli_error($con));
        return false;
    }
    return $con;
}

?>