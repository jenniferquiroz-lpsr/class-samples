# How many miles away do you live from Richmond State
print("How many miles away do you live from Richmond State?")
milesaway = int(raw_input())
# if you live 30 miles or less away from Richmond State you need at least a 2.00 GPA or more
# if you live more than 30 miles away from Richmond State you need at least a 2.50 GPA 
# you also need a score of 18 or more on your ACT if you live more than 30 miles away from Richmond State

if milesaway <= 30:
	print("What is your GPA?")
	gradepointaverage = float(raw_input())
	if gradepointaverage >= 2.00:
		print("Congratulations! You have been accepted to Richmond State")
else:
	print("What is your GPA?")
	gradepointaverage = float(raw_input())
	print("What is your ACT score")
	ACTscore = int(raw_input())
	if gradepointaverage >= 2.50 and ACTscore >= 18:
		print("Congratulations! You have been accepted to Richmond State")
	else: 
		print("Sorry, you have not been accepted to Richmond State")
