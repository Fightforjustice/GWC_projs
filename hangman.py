word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
blanks = []
if(word.isalpha() == False)
	print("That's not a word!")
else:
	for char in word:
			blanks.append("_")
print blanks.join()
  
      
# Some useful variables
guesses = []
maxfails = 7
numfails = 0
winner = False

while (numfails < maxfails):
	guess = input("Guess a letter":)
	if (guess.isalpha() == False):
    	print("Not a letter")
  	elif (guess not in word):
    		print "Sorry; that's not one of the letters!"
    	numfails+=1
  	else:
    		for i in word:
      			if (i == guess):
        			word.remove(i)
    		if (len(word) == 0):
      			winner = True
      			break
  	guesses.append(guess)
  	print ("Your guesses: " + guesses)

if(winner == True):
  	print("You win!")
else:
  	print("Sorry, you lose. That's curtains for hangman!")
    
