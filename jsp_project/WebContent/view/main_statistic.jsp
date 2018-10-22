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
		position:absolute;
	
	}
	
	#frame{
		
		width:100%;
		height:100%;
		margin:0;
		position:relative;

	}
	
	#top_graph{
		width:100%;
		height:21.5%;
		margin:0px 0px 7px 0px;
		padding:0;
		position:relative;
	
	}
	
	#graph_1{
	
		width:20%;
		height:100%;
		float:left;
		position:relative;
		margin: 3px 3px 3px 3px;
		border:3px solid #FF0000;
		border-radius:5px;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3); 
			}
	
	#panel1{
		width:100%;
		height:18%;
		position:relative;
		margin:0;
		padding:0;
		background-color: #FF0000;

	}
	
	#panel_head1{
		
		width:32px;
		height:100%;
		border:1px solid #FF0000;
		background-image:url(../css/image_files/analytics.svg);
		background-repeat: no-repeat;
		background-color: #FF0000;
		bordor: 1px solid black;
		
	}
	
	#graph_2{
	
		width:20%;
		height:100%;
		float:left;
		position:relative;
		margin: 3px 3px 3px 0px;
		border:2px solid #FFFF00;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3); 
			}
	
	#panel2{
		width:100%;
		height:18%;
		float:left;
		position:relative;
		margin:0;
		padding:0;
		background-color: #FFFF00;
	}
	#panel_head2{
		
		width:32px;
		height:100%;
		border:1px solid #FFFF00;
		background-image:url(../css/image_files/analytics.svg);
		background-repeat: no-repeat;
		background-color: #FFFF00;
		
	}
	
	#graph_3{
	
		width:20%;
		height:100%;
		float:left;
		position:relative;
		margin: 3px 3px 3px 0px;
		border:3px solid #5cb85c;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3); 
			
		}
			
	#panel3{
	
		width:100%;
		height:18%;
		float:left;
		position:relative;
		margin:0;
		padding:0;
		background-color: #5cb85c;
		}
	
	#panel_head3{
		
		width:32px;
		height:100%;
		border:1px solid #5cb85c;
		background-image:url(../css/image_files/analytics.svg);
		background-repeat: no-repeat;
		background-color: #5cb85c;
		
		}
	
	#graph_4{
	
		width:20%;
		height:100%;
		float:left;
		position:relative;
		margin: 3px 0px 3px 0px;
		border:3px solid #5cb85c;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3); 
			
		}
		
	
	#panel4{
	
		width:100%;
		height:18%;
		float:left;
		position:relative;
		margin:0;
		padding:0;
		background-color: #5cb85c;
	}
	#panel_head4{
		
		width:32px;
		height:100%;
		border:1px solid #5cb85c;
		background-image:url(../css/image_files/analytics.svg);
		background-repeat: no-repeat;
		background-color: #5cb85c;
		
	}
	
	#graph_5{
	
		width:19%;
		height:100%;
		float:left;
		border:3px solid #5cb85c;
		position:relative;
		margin: 3px 0px 3px 3px;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3); 
			}
	
	#panel5{
		width:100%;
		height:18%;
		float:left;
		position:relative;
		margin:0;
		padding:0;
		background-color: #5cb85c;
	}
	#panel_head5{
		
		width:32px;
		height:100%;
		border:1px solid #5cb85c;
		background-image:url(../css/image_files/analytics.svg);
		background-repeat: no-repeat;
		background-color: #5cb85c;
		
	}

	
	#bottom_graph{
		width:100%;
		height:76%;
		position:relative;
		
	}
	
		
	#geograph{
	
		width:80.5%;
		height:100%;
		float:left;
		position:relative;
		margin: 0px 3px 0px 3px;
		padding: 0px;
		background-color:white;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3);

	}
	#panel6{
		width:100%;
		height:5%;
		float:left;
		position:relative;
		margin:0;
		padding:0;
		background-color: #5cb85c;
		
	}
	
	#panel_head6{
		
		width:32px;
		height:100%;
		background-image:url(../css/image_files/analytics.svg);
		background-repeat: no-repeat;
		background-color: #5cb85c;
		
	}
	
	#news{
		width:19%;
		height:100%;
		float:left;
		position:relative;
		margin: 0px 0px 0px 0px;
		background-color:white;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3);

	
	
	}
	#panel7{
		width:100%;
		height:5%;
		float:left;
		position:relative;
		margin:0;
		padding:0;
		background-color: #5cb85c;
		
	}
	#panel_head7{
		
		width:32px;
		height:100%;
		border:1px solid #5cb85c;
		background-image:url(../css/image_files/analytics.svg);
		background-repeat: no-repeat;
		background-color: #5cb85c;
		box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3);
		
	}
	
	.graphs{

		position:relative;
		height: 82%;
	}
	
	.frame_wrap{
		width:100%;
		height:100%;
		position:relative;
	
	
	}
	



		.frames{
		width:100%;
		height:100%;
		position: relative;
		margin:0;
		padding:0;
		border:0;
		background-color:white;
		overflow:hidden;
	}

	
		
	i{
		color:white;
		font-size: 30px;
		margin:0px 0px 0px 10px;
		
	}
	
	
	


</style>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">

</head>
<script src="/js/BWL1420.js?ver=2"></script>
<body>
	<div id= 'frame'>
		<div id=top_graph>
			<div id= 'graph_1'>
				<div id=panel1>
					<div id=panel_head1>
						<i class="fas fa-chart-bar "></i>
					</div>
				</div>
				<div class='graphs' >
					<div class=frame_wrap>
						<iframe  class='frames' src=NewFile.html></iframe>
					</div>
				</div>
			</div>
			
			<div id= 'graph_2'>
				<div id=panel2>
					<div id=panel_head2>
						<i class="fas fa-chart-bar "></i>
					</div>
					<div class="graph_title">
					</div>
				</div>
				<div class='graphs' >
					<div class=frame_wrap>
						<iframe  class='frames' src=NewFile.html></iframe>
					</div>
				</div>
			</div>
			
			<div id= 'graph_3'>
				<div id=panel3>
					<div id=panel_head3>
						<i class="fas fa-chart-bar "></i>
					</div>
				</div>
				<div class='graphs' >
					<div class=frame_wrap>
						<iframe  class='frames' src=NewFile.html></iframe>
					</div>
				</div>
			</div>
			
			<div id= 'graph_4'>
				<div id=panel4>
					<div id=panel_head4>
						<i class="fas fa-chart-bar "></i>
					</div>
				</div>
				<div class='graphs' >
					<div class=frame_wrap>
						<iframe  class='frames' src=NewFile.html></iframe>
					</div>
				</div>
			</div>
				
			<div id='graph_5'>
				<div id='panel5'>
					<div id=panel_head5>
						<i class="fas fa-chart-bar "></i>
					</div>
				</div>
				<div class='graphs' >
					<div class=frame_wrap>
						<iframe  class='frames' src=NewFile.html></iframe>
					</div>
				</div>
			</div>
		</div>
		
		<div id='bottom_graph'>
	
			<div id= 'geograph'>
				<div id=panel6>
					<div id=panel_head6>
						<i class="fas fa-chart-bar "></i>
					</div>
				</div>
				<div class='graphs' >
					<div class=frame_wrap>
						<iframe  class='frames' src=NewFile.html></iframe>
					</div>
				</div>
			</div>
			<div id= 'news'>
				<div id=panel7>
					<div id=panel_head7>
						<i class="fas fa-chart-bar "></i>
					</div>
				</div>
				<div class='graphs' >
					<div class=frame_wrap>
						<iframe  class='frames' src=NewFile.html></iframe>
					</div>
				</div>
			</div>
		</div>
	</div>	
			
			



</body>
</html>