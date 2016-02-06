# this imports the time  package 
import time

# the following lines opens haiku1.txt and reads it
myFirstHaiku = open('haiku1.txt', 'r')
 
print('Here is the first haiku:')
# this line prints all of haiku1.txt 
print(myFirstHaiku.read())
 
print('I will give you the second haiku line by line.') 
print('How many seconds should I wait between lines?') 
# seconds is the users input turned into an int
seconds = int(raw_input())

# this line opens and reads haiku2.txt 
mySecondHaiku = open('haiku2.txt', 'r')

# the following line prints reads the file in mySecondHaiku  
lineToPrint = mySecondHaiku.readline() 
# this line creates a while loop to print each line one by one
# it creats the while loop so he user can input the seconds they want
while lineToPrint != "":
    print(lineToPrint)
    lineToPrint = mySecondHaiku.readline()
    time.sleep(seconds)

# this closes all of the haikus used 
myFirstHaiku.close()
mySecondHaiku.close()
