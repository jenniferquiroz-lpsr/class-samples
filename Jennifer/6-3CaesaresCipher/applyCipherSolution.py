# applyCipher.py
# A program to encrypt/decrypt user text using Caesar's Cipher
# Author: rc.quiroz.jennifer [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters 
import string 

def createDictionary(key):
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	alphaDict = {}
	count = 0 
	for letter in upper:
		alphaDict[letter] = upper[(key + count) % 26]		
		count = count + 1
	for letter in lower: 
		alphaDict[letter] = lower[(key + count) % 26]
		count = count + 1
	return alphaDict 
	
# gets the encrypted message from the user
# arguments: none
#returns: encoded message
def getMessage(message):
	return message

# for each letter in the message, decodes and records and records the decoded letter
# arguments: encoded message and dictionary
# return: decoded message
def decodeMessage(message, dictionary):
	newMSG = ''
	for i in message:
		eachL = dictionary[i]
		newMSG = newMSG + eachL				
	return newMSG

# outputs the message to the terminal
#arguments: decoded message
#returns: none
def printMessage(decodedMessage):
	print(decodedMessage)


# execution starts here
try:

	# ask the user for key
	print("What key would you like to decode?")
	key = int(raw_input())
	
	dictionary = createDictionary(key)
	
	print("What message would you like to decode?")
	message = raw_input()

	# records message
	encodedMessage = getMessage(message)
	
	# decodes message
	decodeMessage = decodeMessage(encodedMessage, dictionary)
	print("Here's the decoding of your message:")
	printMessage(decodeMessage)

except:
	print("Sorry, this code cannot be accepted.")
