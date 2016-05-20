usersChoice = 1
# empty dictionary
phoneBook = { }

# go through the loop 
while usersChoice != "0":
	# menu
	print("Welcome to Contacts!")
	print("What would you like to do?")
	print("(1) Add a phone number.")
	print("(2) Print the full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.")
	print("(4) Delete a contact")
	print("(0) Exit the Contacts app.")
	usersChoice = raw_input()

	# this lets the user input their contact info
	if usersChoice == "1":
		print("Whats the name of your contact?")
		name = raw_input()
		print("Whats the phone number of your contact?")
		number = raw_input()
		phoneBook[name] = number		

	# print the phone numbers
	elif usersChoice == "2":
		print(phoneBook)

	# this lets the user find a contact
	elif usersChoice == "3":
		print("Whose number would you like?")
		contactName = raw_input()
		print(phoneBook[contactName])

	# delete a contact
	elif usersChoice == "4":
		print("What Contact do you want to delete?")
		deleted = raw_input()
		del phoneBook[deleted]

# you leave the app
print("Thanks for using, Bye!")
