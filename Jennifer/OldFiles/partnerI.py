# set doubleIt as a function
def doubleIt(myNum):
# doubleIt is a function that multiplies a number by 2
  myResult = myNum * 2
# return will make the function doubleIt actually work
  return myResult
# it used the function doubleIt to multiply 3 by 2 
print(doubleIt(3))
# it uses the function doubleIt to multiply 5 by 2
print(doubleIt(5))

print("Enter a number.")
# num is set to the users input
num = int(raw_input())
# this prints the statement plus the string of the inputs number times 2 
print("Ok, here you go: " + str(doubleIt(num)))


