# funcPractice.py

# 1
# the argument x must be a number
# returns x to the 3rd power
def cube(x):
        myCube = x ** 3
        return myCube


# 2
# the argument x must be a number
# returns x as a string and as a percentage, converted to an integer %
# for example, if x is .252, returns "25%"
def pct_string(x):
        myPerc = (x) * 100
        y = int(myPerc)
        return str(y) + "%"


# 3
# the argument myStr must be a string
# does not return anything but prints myStr three times on separate lines
def print_thrice(myStr):
        print(myStr)
        print(myStr)
        print(myStr)
        return myStr


# 4
# the arguments x and y must be numbers
# returns the average of the two numbers as a float
# hint - you'll need to divide by 2.0
def my_avg(x, y):
        myAvg = x + y
        myTot = myAvg / 2.0
        return myTot
# DON'T TOUCH THIS CODE
# Test the function implementations
print("**************Results****************")
p = 2
q = 5
r = .25
 
# number 1
if cube(p) == 8 and cube(q) == 125:
  print("#1 passes")
else:
  print("#1 fails")
 
# number 2
if pct_string(r) == "25%":
  print("#2 passes")
else:
  print("#2 fails")
 
# number 3
print("#3 passes if the next three lines are all \"bird\"")
print_thrice("bird")
 
# number 4
if my_avg(p, q) == 3.5 and my_avg(p, 2*q) == 6:
  print("#4 passes")
else:
  print("#4 fails")
 

