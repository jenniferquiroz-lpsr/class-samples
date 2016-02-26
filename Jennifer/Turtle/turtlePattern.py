import turtle

def makeSquare(myTurtle, side):
        myNum = 0
        while myNum <= 4:
          myTurtle.forward(100)
          myTurtle.left(90)
          myNum = myNum + 1

# make our turtle
squeak = turtle.Turtle()

# squeak makes squares centered at the same point
# but going in a slightly rotated position with each loop
# and with a slightly smaller side length each time
length = 100
while length > 0:
        makeSquare(squeak, length)
# rotate and make the sides shorter
        squeak.right(10)
        length = length - 5
# wait to exit until I've clicked
turtle.exitonclick()
