# this function identifies if the number passed is prime or not
def isPrime(num):
	# for every number in the range use it to divide it by the number passed
	for i in range(2,num):
		a = num % i
		# if the remainder is equals to 0 return False
		# if the remainder isnt equal to zero and it has gone through evrynumber in the for 
		# statement then return True
		if a == 0:
			#print(str(num) + "Is not Prime")
			return False	
	#print(str(num) + "Is Prime")	
	return True

# this code adds the prime numbers into a txt file
# and it prints them on the terminal	
myFile = open("primes.txt", "w")
for n in range(2,10000):
	if isPrime(n):
		myFile.write(str(n) + '\n')
		print(str(n))
