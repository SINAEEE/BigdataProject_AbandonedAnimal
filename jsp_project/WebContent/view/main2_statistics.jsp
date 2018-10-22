<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<%
response.setHeader("Cache-Control","no-cache");
response.setHeader("Pragma","no-cache");
response.setDateHeader("Expires",0);
%>

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
	
	.wrap {
		width:100%;
		height:100%;
		position:absolute;
		margin: 0;
		padding: 0;

		
	}
	#top_graph{
		width:100%;
		height:30%;
		position:relative;
	
	}
	
	
	
	
	#title1{
		width:100%;
		height:10%;
		
	
	}
	

	#graph_area1{
		width:100%;
		height:90%;
		position:relative;
		margin:0;
		padding:0;
	
	}
	
	#bottom_graph{
		width:100%;
		height:70%;
		position:relative;
	
		
	}

	#menu_wrap{
		width:60%;
		height:20%;
		position:relative;
		margin:auto; 
		padding: 0px 0px 0px 0px;

	}
		
	#graph_area2{
		width:100%;
		height:80%;
		position:relative;
		margin:0;
		padding:0;

		}
	.area2_menu{
		background-image:url(../css/image_files/GreenCircle.png);
		background-repeat: no-repeat;
		background-size:contain;
		background-position: center;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3); 
		border-radius:5px;
		border: 1px solid black;
		width:20%;
		height:80%;
		float:left;
		position:relative;
		margin:1% 2.5% 0% 2.5% ;
		padding: 0;
	
	
	}
		
		.iframe{
		width:99%;
		height:99%;
		position:relative;
		margin:0% 0.5% 0% 0.5%;
		background-color:white;
		border-radius: 10px;
		border: 0;

		
		}
	


</style>
</head>
	<body>
		<div class="wrap">
			<div id=top_graph>
				<div id="title1" align="center" >
					
				</div>
				
				<div id="graph_area1">
					<iframe class="iframe" src="./main2_function/main2_all_year_statistics.jsp"></iframe>		  
				</div>
			</div>
			
			<div id=bottom_graph>
				
							<div id="menu_wrap">	
									
										<div class="area2_menu">
											
										
										 </div>
										
										<div class="area2_menu">
											
											
										  </div>
										
										<div class="area2_menu">
											
									
										</div>
										
										<div class="area2_menu">
										
										</div>
										
									</div>
							
							<div id="graph_area2">
									<iframe class='iframe' name='iframe2' src="./main2_function/main2_detail_statistics.jsp" ><a >asdf</a></iframe>
							</div>		
				</div>
			</div>
						 
			

		
		
		
	</body>
</html>