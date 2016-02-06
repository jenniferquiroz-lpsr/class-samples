# the followig lines open the haiku texts and reads them 
fourthHaiku = open("haiku4.txt", "r")
thirdHaiku = open("haiku3.txt", "r")

print("Hi, welcome to the Haiku Reader!")
print("Choose...")
print("(3) For a haiku about a silly person.")
print("(4) For a haiku about writing haikus.")
# the following sets userChoice as the users input
numberChoice = int(raw_input())

# the following if statements prints the haiku's that the user choose
if numberChoice == 3:
	print(thirdHaiku.read())

if numberChoice == 4:
	print(fourthHaiku.read())


fourthHaiku.close()
thirdHaiku.close()
