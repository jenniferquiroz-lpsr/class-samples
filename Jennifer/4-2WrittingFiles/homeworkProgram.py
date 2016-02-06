print("Welcome to the Haiku generator!") 
print("Provide the first line of your haiku:") 
firstLine = raw_input() 
print("Provide the second line of your haiku:") 
secondLine = raw_input()
print("Provide the third line of your haiku:") 
thirdLine = raw_input() 
print("What file would you like to write your haiku to?")
FileName = raw_input()

userHaiku = [firstLine, secondLine, thirdLine]

myFile = open(FileName, "a")

for line in userHaiku:
	myFile.write(line + "\n") 	

print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")

myFile.close()

