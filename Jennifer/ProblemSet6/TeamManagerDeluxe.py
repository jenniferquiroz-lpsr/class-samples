#welcomes the user to the program`
print("Welcome to Team Manager Deluxe!")

# creates the class Player
class Player(object):
	
	# makes objects, such as information of the player
	def __init__(self, name, age, goals, jerseyNumber, position):
                self.name = name
                self.age = age
                self.goals = goals
                self.jerseyNumber = jerseyNumber
                self.position = position
 
	# this creates a function that neatly prints the information of the player
        def printStats(self):
                print(" ")
		print("Name: " + self.name)
                print("Age: " + str(self.age))
                print("Goals: " + str(self.goals))
                print("Jersey Number: " + str(self.jerseyNumber))
                print("Position: " + self.position)
		print(" ")		

# takes the playerList and the user's desired filename writes each Player to file
def saveTeam(playerList, filename):
	# open the file
    	file = open(filename, "a")	 
    	# write to the file
	for i in playerList:
		file.write(i.name + " " + str(i.age) + " " + str(i.goals) + " " + str(i.jerseyNumber) + " " + i.position + "\n")
    	# close the file
    	file.close()
   
# takes a filename for a file of players returns a list of Players
def loadTeam(filename):
	# create empty list
	list = []
	# open the file
        file = open(filename, "r")
        # read each line and create Player from it (use a loop)
        ltr = file.readline()
        # split each line into a list of the variables read each next line
	while ltr != "":
		stringSplitter = ltr.split()	
		list.append(Player(stringSplitter[0], stringSplitter[1], stringSplitter[2], stringSplitter[3], stringSplitter[4]))
		#print(stringSplitter)
		ltr = file.readline()
	# close the file
        file.close()
	# return the completed list
   	return list
    
# instructions 
print("Do you want to start with a new team or existing team?")
print("Enter the letter of your choice and press enter")
print("(A) Start with a new team")
print("(B) Open a file with existing team")
AorB = raw_input()

# if the users choice is a B 
# open the file that they want to open 	
# and print all the players in the file
if  AorB == "B" or AorB == "b":
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension")
        filename = raw_input()
        playerList = loadTeam(filename)
	print("Here are all the players...")
		
		
# if A just print a space to save time and space
# because the instructions for both A and B 
# are going to be listed below 
elif AorB == "A" or AorB == "a":
	print(" ")
	playerList = []
# this sets the userchouce to 1 but is later changed in the while loop
userChoice = 1

# this creates a loop for the instructions
while userChoice != "0":
	print("What do you want to do? Enter the number of your choice and press Enter.") 
	print("(1) Add a player") 	
	print("(2) Print all players")  
	print("(3) Save your player list to a file") 
	print("(0) Leave the program (save first to avoid losing your data!)")
	userChoice = raw_input()
	
        # if the user chooses 1, let them input their information
        if userChoice == "1":
                print("Add players name:")
                userName = raw_input()
                print("Add players age:")
                userAge = raw_input()
                print("Add players number of goals:")
                userGoals = raw_input()
		print("Add players Jersey Number:")
		userJerseyNumber = raw_input()
		print("Add players position")
		usersPosition = raw_input()
		 
                # this puts in the users data into the list
                playerList.append(Player(userName, userAge, userGoals, userJerseyNumber, usersPosition))

	# if the user choose 2, it will print all the information that they inputed
        elif userChoice == "2":
		# this creates a loop to print everything in seperate lines from myPlayers
                for x in playerList:
                        print(" ")
			# this calls the def function that we make earlier
                        x.printStats()
                        print(" ")

	# this saves the players list to a file
	elif userChoice == "3":
		print("Enter the name of the file you want to add your players to, make sure to add your tmd or txt extension")
		newFile = raw_input()
		#print(playerList)
		saveTeam(playerList, newFile)

# when the user put in 0, this message will appear
print("Thanks for using the app! Bye!")
