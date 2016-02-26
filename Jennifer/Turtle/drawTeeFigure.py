import turtle

def drawTee(myTurtle):
	myTurtle.forward(200)
	myTurtle.backward(50)
	myTurtle.right(90)
	myTurtle.forward(50)
	myTurtle.backward(100)
	myTurtle.forward(50)
	myTurtle.left(90)
	myTurtle.backward(150)
	myTurtle.right(90)
def drawFourTees(myTurtle):
	count = 0
	while count < 4:
		drawTee(shawn)
		count = count + 1	

shawn = turtle.Turtle()

drawFourTees(shawn)

# make your turtle down here and pass it to the appropriate places

turtle.exitonclick()
