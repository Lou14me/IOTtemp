<?php
$con=mysqli_connect("localhost","root","raspberry","raspberryDB"); 
if (mysqli_connect_errno()){
  echo "Failed to connect to MySQL".mysqli_connect_error();
}

$now1 = date('Ymdhis');
$id = $_GET['id'];
$temp = $_GET['temp'];
mysqli_query($con,"INSERT INTO temp(datetime,temp,userid) VALUES ($now1,$temp,$id)");

mysqli_close($con);
  echo "powenko.com get it".",date time = ".$now.", temp = ".$temp."id = ".$id;
?>
