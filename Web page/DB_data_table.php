
<button type="button" onclick="window.location.href='index.html'">◁</button>
<?
	include("connect.php");
	$connect = mysql_connect($mysql_sv,$mysql_id,$mysql_pw);
	$db = mysql_select_db($mysql_db,$connect);

	if($db)
	{
		$sql = "select *from ".$mysql_tb;
		$result = mysql_query($sql,$connect);
		$count = mysql_num_fields($result);
		echo "<table border align='center'>";
		echo "<th>시간</th>";
		echo "<th>거리</th>";
		echo "<th>경보</th>";
		while ($row = mysql_fetch_row($result))
		{
		if($row[2] < 70)
		{
			echo "<tr>";
			for ($i=1; $i<4; $i++)
			{
				echo "<td>";
				if ($i != 3)
					echo $row[$i];
				else if ($row[$i] == 1)
					echo "ON";
				else
					echo "OFF";
				echo "</td>";
			}
			echo "</tr>";	
			}
		}
		
echo "</table>";
	}
	else echo "DB Connect Err Error";

	mysql_close($connect);
?>
