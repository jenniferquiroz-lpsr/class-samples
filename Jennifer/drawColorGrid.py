import turtle 

def drawRedSquare(myTurtle):
        myTurtle.color("red")
        count = 0 
        while count < 4:
                myTurtle.forward(20)
                myTurtle.right(90)
                count = count + 1

def drawBlueSquare(myTurtle):
	myTurtle.color("blue")
	myTurtle.penup()
	myTurtle.forward(20)
	myTurtle.pendown()
	count = 0
	while count < 4:
		myTurtle.forward(20)
		myTurtle.right(90)
		count = count + 1

def drawGreenSquare(myTurtle):
	myTurtle.color("green")
	myTurtle.penup()
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.pendown()
	count = 0 
	while count < 4:
		myTurtle.forward(20)
		myTurtle.right(90)
		count = count + 1

def drawYellowSquare(myTurtle):
	myTurtle.color("yellow")
	myTurtle.penup()
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.pendown()
	count = 0
	while count < 4:
		myTurtle.forward(20)
		myTurtle.right(90)
		count = count + 1	
def drawColorfulSquare(myTurtle):
	drawRedSquare(myTurtle)
	drawBlueSquare(myTurtle)
	drawGreenSquare(myTurtle)
	drawYellowSquare(myTurtle)

def drawFinalPattern(myTurtle):
	count = 0
	while count < 5:
		drawColorfulSquare(shawn)
		myTurtle.right(90)
		myTurtle.penup()
		myTurtle.forward(5)
		myTurtle.right(90)
		myTurtle.pendown()	
		count = count + 1

shawn = turtle.Turtle()

shawn.speed(3)

drawFinalPattern(shawn)

turtle.exitonclick()

