<?php
	include("connect.php");

$con = mysql_connect($mysql_sv,$mysql_id,$mysql_pw);

if (!$con) {
die('Could not connect: ' . mysql_error());
}

mysql_select_db($mysql_db, $con);

$result = mysql_query("SELECT * FROM ".$mysql_tb) or die ("Error");

while($row = mysql_fetch_array($result)) {
echo $row['time'] . "/" . $row['distance']. "/" ;
}

mysql_close($con);
?>