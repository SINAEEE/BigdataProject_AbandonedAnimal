<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html charset=EUC-KR">
<title>대한민국 유기동물 보고서</title>

<!-- css 메뉴스타일 -->



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
		background-color:#E4EBF7;
	
		}
	
	.frame_area{
		width:100%;
		height:100%;
		margin: 0;
		padding: 0;
		background-color:#E4EBF7;
		
		
	}
	
	.top{
		width:100%;
		height:10%;
		position:relative;
		margin:0;
		padding:-5px -5px -5px -5px;
		background-color:black;
		color:white;


	}
	.menu_graph_wrap{
		width:100%;
		height:90%;
		position:relative;
		margin:auto;
		margin: 0px 0px 0px 0px;

		
	}
	.menubar{
		width:10%;
		height:100%;
		position:absolute;
		float:left;
		background-color:#1B2133;

	}
	
	.main_graph_area{
		width:90%;
		height:100%;
		position:relative;
		margin:0;
		float:right;
		
	}
	
	#iframes{
		
		width:100%;
		height:100%;
		position:relative;
		margin:0;
		border:0;

	}




</style>

<!-- 스크립트 -->

<script src="/js/BWL1420.js?ver=3"></script>
<link rel="stylesheet" type="text/css" href="../css/menubar.css">

</head>


	<body>
		<div class='frame_area'>
		
			
			<!-- header 부분 -->			
			<div class='top'>
				<br><h5 align='center'> 유기동물 보고서</h5>
			</div>
			<!-- header end-->
			
			<!-- menu -->
		
			<div class='menu_graph_wrap'>
			
					<div class="menubar">	
						<ul class="sidenav">
							<li>
								<a href="main_statistic.jsp" target="display">Dashboard
								<span> 2018년 현재의 유기동물의 안락사, 자연사, 입양, 유기동물의 수 통계를 한눈에 볼 수 있는 페이지입니다. </span>
								</a>
							</li>
							<li>
								<a href="main2_statistics.jsp" target="display">Statistic analysis
								<span>Blandit turpis patria euismod at iaceo appellatio, demoveo esse. Tation utrum utrum abigo demoveo immitto aliquam sino aliquip. </span>
								</a>
							</li>
							<li>
								<a href="#">Machine Learning
								<span>Blandit turpis patria euismod at iaceo appellatio, demoveo esse. Tation utrum utrum abigo demoveo immitto aliquam sino aliquip. </span>
								</a>
							</li>
							
						</ul>
					</div> 
					<div class="main_graph_area">
							<iframe id='iframes' name='display' src='main_statistic.jsp'></iframe>	
					</div>
					
					
			</div>
		
		</div>
	</body>
	
</html>