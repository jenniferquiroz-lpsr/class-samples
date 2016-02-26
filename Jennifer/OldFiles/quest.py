# welcome the user
print("Welcome to Jennifer's Quest")
# ask the user to input the name of their character
print("What is your characters name?")
name = raw_input()
# ask the user to input the amout of strength, health, and luck they want
# the input has to be an integer in between 1 and 10
print("Enter Strength (1-10)")
charactersStrength = int(raw_input())
print("Enter Health (1-10)")
charactersHealth = int(raw_input())
print("Enter Luck (1-10)")
charactersLuck = int(raw_input())
# add up all the characteristics 
totalCharacteristics = (charactersStrength + charactersHealth + charactersLuck)
# if the total of the characteristics is less than 15 create a loop until they get the right ammount of characteristics
while totalCharacteristics < 15:
	print("You have given your character to little points, set your points again.")
	print("Enter Strength (1-10)")
	charactersStrength = int(raw_input())
	print("Enter Health (1-10)")
	charactersHealth = int(raw_input())
	print("Enter Luck (1-10)")
	charactersLuck = int(raw_input())
	totalCharacteristics = (charactersStrength + charactersHealth + charactersLuck)
# if the total of the characteristics is greater than 15 print the following
if  totalCharacteristics > 15:
        print("You have given your character to many points")
        print("Default values have been assigned to " + name)
        print("Strength:5 Health:5 Luck:5")
	charactersStrength = 5
        charactersHealth = 5
        charactersLuck = 5
# now go through the process of telling them whether they won or not
print(name + ", you've come to a fork in the road. Do you want to go right or left? Enter right or left.")
userpath = raw_input()
right = "right"
left = "left"
if userpath == left:
        print("Sorry, you lost! The left path was cursed by a witch and you died.")
elif userpath == right and charactersHealth >= 6 :
	print("You Won! Your character was healthy enough to climb through the mountain")
else:
	print("Sorry, you lost. Your character wasnt healthy enough to climb the mountain")

