word = input("Type a word for someone to guess: ")

# Converts the word to lowercasse
word = word.lower()

# Checks if only letters are present
blanks = []
if(word.isalpha() == False):
	print("That's not a word!")
elif(" " in word):
	print("Just one word, please! No spaces")
else:
	for char in word:
			blanks.append("_")
	word = word.lower()
			
s = ''.join(blanks)
print(s)
  
      
# Some useful variables
guesses = []
maxfails = 7
numfails = 0
winner = False

while (numfails < maxfails):
	guess = input("Guess a letter:")
	if (guess.isalpha() == False):
    		print("Make sure it's a letter!")
	elif (len(guess) == 0):
		print("Oops! Nothing entered.") 
	elif (len(guess) > 1):
		print("Just one letter, please!")
	elif (guess in guesses):
		print("You already guessed that.")
	else:
		if (guess not in word):
			numfails += 1
			print("Sorry; that's not one of the letters!")
		else:
    			print ("Good job!")
		word = word.replace(guess, "")
		if (len(word) == 0):
			winner = True
			break
		guesses.append(guess.lower())
		g = ", ".join(guesses)
		print("Your guesses: " + g)
		
if(winner == True):
	print("You win!")
else:
	print("Sorry, you lose. That's curtains for hangman!")
    
