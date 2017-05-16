import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("green")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
    for i in range(1,5): 
	brad.forward(100) 
	brad.right(90)   


	

	sudhir = turtle.Turtle()
	sudhir.shape("arrow")
	sudhir.color("blue")
	sudhir.circle(100)


	
	window.exitonclick()


draw_square()

ASK DEVESH