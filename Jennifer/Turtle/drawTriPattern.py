import turtle

def drawTriangle(myTurtle):
	count = 0
	while count < 3:
		myTurtle.forward(10)
		myTurtle.right(120)
		count = count + 1

def drawMultipleTriangles(myTurtle):
	count = 0 
	while count < 4:
		myTurtle.penup()
		myTurtle.forward(20)
		myTurtle.pendown()
		drawTriangle(myTurtle)
		count = count + 1

def drawRowsofTri(myTurtle):
	count = 0
        while count < 3:
                drawMultipleTriangles(myTurtle)
                myTurtle.penup()
                myTurtle.goto(0,0)
                myTurtle.pendown()
                myTurtle.left(30)
                count = count + 1
        myTurtle.penup()
        myTurtle.goto(0,0)
        myTurtle.pendown()
        myTurtle.right(260)
        number = 0
        while number < 3:
                drawMultipleTriangles(myTurtle)
                myTurtle.penup()
                myTurtle.goto(0,0)
                myTurtle.pendown()
                myTurtle.left(30)
                number = number + 1

shawn = turtle.Turtle()

drawRowsofTri(shawn)

turtle.exitonclick()
