import turtle
import random

shawn = turtle.Turtle()

count = 0

theColors = ["blue","purple","red","yellow","orange"]

while count < 100:
	shawn.color(random.choice(theColors))
	shawn.forward(80)
	shawn.right(20)
	shawn.backward(80)
	count = count - 1
shawn.exitonclick()
