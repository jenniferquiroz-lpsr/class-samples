# open a file for writing
# second argument:
# r is for reading
# r+ is for reading and writting
# w is for writting but be careful it starts writting from the begining
# a is append - writting from the end 
myFile = open("numlist.txt", "w")

# create a list to write to my file
nums = range(1,500)

# write each item to the file
for n in nums:
	myFile.write(str(n) + "\n") 

# close file
myFile.close()


