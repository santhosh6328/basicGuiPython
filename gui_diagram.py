import turtle

def draw_square():
	for i in range(4):
		brad.forward(100)
		brad.right(90)
	brad.right(10)
	
	
window = turtle.Screen()
window.bgcolor("red")
	
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(.1)
for i in range(36):
	draw_square()
	

