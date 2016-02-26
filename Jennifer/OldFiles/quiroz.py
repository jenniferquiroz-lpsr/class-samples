import random
# set your number to a random number between 1 and 1000
myNum = random.randint(1,1001)
#print(myNum)
# ask the user to enter a number
print("I'm thinking of a number between 1 and 1000. Enter your guess!")
userNum = int(raw_input())
while userNum != myNum:
	print("No")
	if userNum > myNum:
		print("Too High! Guess Again!")
		userNum = int(raw_input())
	if userNum < myNum:
		print("Too Low! Guess Again!")
		userNum = int(raw_input())
	if userNum == myNum:
		print("You guessed it right! You win!")
