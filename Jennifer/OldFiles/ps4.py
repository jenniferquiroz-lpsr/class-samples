# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors
 
# bring in the packages of functions we need
import random
import turtle
 
# -------- functions start here ----------------

# create a function that makes a triangle whenever its being asked to
def regular_triangle(myTurtle, x, y, side):
        # make the turtle go to a random area on the platform but 
        # put the pen up so it wont randomly draw on the platfrom
        # when the turtle gets there make sure to put the pen down
        # so it can draw the shape 
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        # make a loop 
        # create a variable that equals to 0 so the loop can terminate
        side_count = 0
        while side_count < 3:
                # to give the triangle its shape follow these instructions:
                myTurtle.forward(side)
                # 360/3 = 120
                myTurtle.right(120)
                # add one each time so the loop can terminate
                side_count = side_count + 1
# create a function that makes a square whenever its being asked to
def regular_square(myTurtle, x, y, side):
        # make the turtle go to a random area on the platform but 
        # put the pen up so it wont randomly draw on the platform 
        # when the turtle gets there make sure to put the pen down
        # so it can draw the shape 
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        # make a loop 
        # create a variable that equals to 0 so the loop can terminate
        side_count = 0
        # since a square has 4 sides make the loop stop once side_count 
        # reaches 4
        while side_count < 4:
          # to give the square its shape follow these instructions:
          myTurtle.forward(side)
          # 360/4 = 90
          myTurtle.right(90)
          # make side_count increase by 1 each time so the loop can
          # eventually terminate 
          side_count = side_count + 1
# create a function that creates a pentagon whenever its being asked to
def regular_pentagon(myTurtle, x, y, side):
        # make the turtle go to a random area on the platform but 
        # put the pen up so it wont randomly draw on the platform 
        # when the turtle gets there make sure to put the pen down
        # so it can draw the shape 
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        # make a loop 
        # create a variable that equals to 0 so the loop can terminate
        side_count = 0
        # since a pentagon has 5 sides make the loop stop when it 
        # reaches the number 5 
        while side_count < 5:
          # to make a pentagon follow the instructions :
          myTurtle.forward(side)
          # 360/5 = 72
          myTurtle.right(72)
          # make side_count increase by 1 so the loop can eventually
          # terminate 
          side_count = side_count + 1
# create a function that creates a hexagon           
def regular_hexagon(myTurtle, x, y, side):
        # make the turtle go to a random area on the platform but 
        # put the pen up so it wont draw on your shape 
        # when the turtle gets there make sure to put the pen down
        # so it can draw the shape 
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        # make a loop 
        # create a variable that equals to 0 so the loop can terminate
        side_count = 0
        # since a hexagon has 6 sides make the loop stop when it reaches
        # the number 6
        while side_count < 6:
          # follow the instructions to make the shape:
          myTurtle.forward(side)
          # 360/6 = 60
          myTurtle.right(60)
          # make side_count increase by 1 so the loop can eventually
          # terminate 
          side_count = side_count + 1
# create a function that creates an octagon  
def regular_octagon(myTurtle, x, y, side):
        # make the turtle go to a random area on the platform but 
        # put the pen up so it wont draw on your shape 
        # when the turtle gets there make sure to put the pen down
        # so it can draw the shape 
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        # make a loop 
        # create a variable that equals to 0 so the loop can terminate
        side_count = 0
        # since an octagon has 8 sides make the loop stop when it
        # reaches the number 8
        while side_count < 8:
          # to make the shape follow these instructions:
          myTurtle.forward(side)
          # 360/8 = 45
          myTurtle.right(45)
          # make side_count increase by 1 so the loop can eventually
          # terminate 
          side_count = side_count + 1
# create a function that makes an octagon 
def circle(myTurtle, x, y, radius):
        # make the turtle go to a random area on the platform but 
        # put the pen up so it wont draw on your shape 
        # when the turtle gets there make sure to put the pen down
        # so it can draw the shape 
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        # with this function theres a special function to make a circle
        # so just use .circle(radius)
        myTurtle.circle(radius)
 
# -------- execution starts here ----------------
# welcome the user 
print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")
# create a list of colors 
myColors = ['blue','red','green','orange','yellow','pink','purple']
# make a turtle called squirt
squirt = turtle.Turtle()
# create a loop that makes the user type in a shape
# and if they dont make them go into a loop until they do
# if they type in "exit" end the game
shape = ""
while shape != "exit":
        print("Enter a shape - your choices are triangle, square, pentagon, hexagon, octagon, and circle.")
        print("If you're done making shapes, just type 'exit'.")
        # let squirt get a random color each time he draws a shape
        squirt.color(random.choice(myColors))
        # this will allows the user to type in the shape they want
        shape = raw_input()
        # this lets the turtle go to a random place in the platform
        # and random size 
        randx = random.randint(-200,200)
        randy = random.randint(-200,200)
        randside = random.randint(5,100)
        
        # all the following elif and if statements allow the 
        # computer to know what to do when the user types in the shape
        # they want drawn 
        # and when it draws the shape it gives it a random
        # place and size to draw it with 
        # if the shape is a triangle follow these instructions
        if shape == 'triangle':
                regular_triangle(squirt, randx, randy, randside)
        # if the shape is a square follow these instructions
        elif shape == 'square':
                regular_square(squirt, randx, randy, randside)
        # if the shape is a pentagon follow these instructions
        elif shape == 'pentagon':
                regular_pentagon(squirt, randx, randy, randside)
        # if the shape is a hexagon follow these instructions
        elif shape == 'hexagon':
                regular_hexagon(squirt, randx, randy, randside)
        # if the shape is an octagon follow these instructions
        elif shape == 'octagon':
                regular_octagon(squirt, randx, randy, randside)
        # if the shape is a circle follow these instructions
        elif shape == 'circle':
                circle(squirt, randx, randy, randside)
