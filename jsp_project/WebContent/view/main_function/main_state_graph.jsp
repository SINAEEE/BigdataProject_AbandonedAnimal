<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>Insert title here</title>
<style>
	
	*{
	-moz-box-sizing: border-box;
	box-sizing: border-box;
	
	}
	html,body{
	
		width:100%;
		height:100%;
		margin:0;
		padding:0;

	}
	.state_count_graph{
		width:100%;
		height:100%;
		position:relative;

	}
	.graph{
		width:24%;
		height:100%;
		float:left;
		position:relative;
		margin:5px 5px 5px 5px;
	
	}
	.gp1{
		width:100%;
		height:100%;
	}
</style>

</head>

<body>
	<div class="state_count_graph">
		<div class="graph" >
			<iframe class=gp1 src="../NewFile.html"></iframe>
		</div>
		<div class="graph">
			<h5 align='center'>그래프입니다</h5>
		</div>
		<div class="graph">
			<h5 align='center'>그래프입니다</h5>
		</div>
		<div class="graph">
			<h5 align='center'>그래프입니다</h5>
		</div>
	</div>
</body>
</html>