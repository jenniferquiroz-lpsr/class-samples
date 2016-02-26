# import the turtle package
import turtle

# create the a rhombus shape with angels of 60 and 120
# start the function at an angle so you can keep the whole cube straight up and not tilted
# you will be using this function throughout the whole code  
def drawRhombus(myTurtle):
        myTurtle.right(30)
        count = 0
        while count < 2:
                myTurtle.left(60)
                myTurtle.forward(40)
                myTurtle.left(120)
                myTurtle.forward(40)
                count = count + 1

# make the first rhombus and make it dark blue so we can start the 3D effect
# also fill the shape with the color dark blue
# use the previous function in this function to create the rhombus
def addRhombusColor(myTurtle):
        myTurtle.color("dark blue")
        myTurtle.fillcolor("dark blue")
        myTurtle.begin_fill()
        drawRhombus(myTurtle)
        myTurtle.end_fill()

# now we have to create one side of the cube
# we have to make it at an angle so it connects with the first rhombus
# now we have to make the new rhombus in a light blue color so we can continue with the 3D effect 
# we also have to fill in the shape with the color light blue
# use the previous function in this function so we can continue embeding the functions with in functions
# to make one whole def function
def drawOneSide(myTurtle):
        addRhombusColor(myTurtle)
        myTurtle.left(150)
        myTurtle.color("light blue")
        myTurtle.fillcolor("light blue")
        myTurtle.begin_fill()
        drawRhombus(myTurtle)
        myTurtle.end_fill()

# use the previous function in this function so we can continue embeding the functions with in functions
# to make one whole def function
# make this rhombus a medium blue color to continue with the 3D effect
# also make sure to fill in the shape with the same medium blue color
# make this rhombus with an angle to attach this rhombus to the previous rhombus
def drawSecondSide(myTurtle):
        drawOneSide(myTurtle)
        myTurtle.left(150)
        myTurtle.color("medium blue")
        myTurtle.fillcolor("medium blue")
        myTurtle.begin_fill()
        drawRhombus(myTurtle)
        myTurtle.end_fill()

# i added this function to tie everything together into one 
# this function makes the cube 
def drawCube(myTurtle):
        drawSecondSide(myTurtle)

# this function repositions the arrow or turtle so we can be able to draw another cube
# right next to it
def repositionCube(myTurtle):
        myTurtle.right(60)
        myTurtle.forward(40)
        myTurtle.left(60)
        myTurtle.penup()
        myTurtle.forward(40)
        myTurtle.right(210)
        myTurtle.pendown()

# this functions makes one row i used a while loop to do so
# this function also uses previous functions to complete the first row
# i used drawCube() and repositionCube()
def draw1stRow(myTurtle):
    count = 0
    while count < 2:
      drawCube(myTurtle)
      repositionCube(myTurtle)
      drawCube(myTurtle)
      repositionCube(myTurtle)
      drawCube(myTurtle)
      repositionCube(myTurtle)
      count = count + 1

# this function also uses previous functions to make 2 rows
# this function makes the turtle go back to the start (0,0) so it can be able to draw a new row
def draw2ndRow(myTurtle):
        draw1stRow(myTurtle)
        myTurtle.penup()
        myTurtle.goto(0,0)
        myTurtle.right(90)
        myTurtle.forward(60)
        myTurtle.left(90)
        myTurtle.backward(35)
        myTurtle.pendown()
        draw1stRow(myTurtle)

# this function also uses previous functions
# it also repositions the turtle or arrow so it can draw a 3rd row attached to the previous rows
def draw3rdRow(myTurtle):        
        draw2ndRow(myTurtle)
        myTurtle.penup()
        myTurtle.goto(0,0)
        myTurtle.right(90)
        myTurtle.forward(120)
        myTurtle.left(90)
        myTurtle.backward(70)
        myTurtle.pendown()
        draw1stRow(myTurtle)
        
# this function uses previous functions as well 
# this function adds the final row 
# it repositions the arrow so it can draw the 4th row attached to the previous rows
def draw4thRow(myTurtle):
        draw3rdRow(myTurtle)
        myTurtle.penup()
        myTurtle.goto(0,0)
        myTurtle.right(90)
        myTurtle.forward(180)
        myTurtle.left(90)
        myTurtle.backward(105)
        myTurtle.pendown()
        draw1stRow(myTurtle)
        
# these last 3 functions tie everything up
# I name my turtle shawn and I tell shawn to draw the whole pattern
# i used exitonclick so it can stay on the page until you click it to exit
shawn = turtle.Turtle()
draw4thRow(shawn)
turtle.exitonclick()
