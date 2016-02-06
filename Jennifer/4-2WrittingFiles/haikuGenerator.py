# the following lines welcome the user and set certain values to the users input
print("Welcome to the Haiku generator!") 
print("Provide the first line of your haiku:") 
firstLine = raw_input() 
print("Provide the second line of your haiku:") 
secondLine = raw_input()
print("Provide the third line of your haiku:") 
thirdLine = raw_input() 
print("What file would you like to write your haiku to?")
FileName = raw_input()

# this makes a list of the users haikus in order from which they entered
userHaiku = [firstLine, secondLine, thirdLine]

# this makes the file with the name the user chose and it appends everything they wrote into the file
myFile = open(FileName, "a")

# this line prints each stanza in seperate lines 
for line in userHaiku:
	myFile.write(line + "\n") 	

# this gives the user instructions to find the file they made
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")

# this closes the file that was made
myFile.close()

