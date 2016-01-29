# teamManager.py

# steps A and B
#this creates a class
class Player(object):
	# this makes the init function include name, age, and goals
	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals
	# this makes the data print 	
	def printStats(self):
		print("Name:" + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.goals))

# this creats a list for myPlayers
myPlayers = []
# this sets userChoice to 1 but this is later changed in the while loop
userChoice = 1

# this creates a loop for the user
while userChoice != "0":
	# this allows the user to chose a number
	print("Enter the number of your choice:")
	print("(1) Make Player")
	print("(2) List Player")
	print("(0) Exit and delete players")
	userChoice = raw_input()
	
	# if the user chooses 1, let them input their information
	if userChoice == "1":
		print("Add players name:")
		userName = raw_input()
		print("Add players age:")
		userAge = raw_input()
		print("Add players number of goals:")
		userGoals = raw_input()
		
		# this puts in the users data into the list 
		myPlayers.append(Player(userName, userAge, userGoals))

	# if the user choose 2, it will print all the information that they inputed 
	elif userChoice == "2":
		for x in myPlayers:
			print(" ")
			x.printStats()
			print(" ")

# when the user put in 0, this message will appear
print("Okay then, bye")
