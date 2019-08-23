import random
import re
number = random.randint(1, 99)

guesses = 0
maxm = 5

while guesses < maxm:
	guess = input("Enter the guessing number between 1 to 99: ")
	if bool(re.search("^[0-9]+$", guess)):
		guess = int(guess)
		print("This is your", guess, "guess")
		if guess < number:
			print("guess is low")
		elif guess > number:
			print("guess is high")
		elif guess == number:
			print("Your guess", guess, "is correct")
			break
	else:
		print("Warning: enter numbers between 1 to 99")
	guesses += 1
	if guesses == maxm - 1:
		print("This is your last life")
	if maxm == guesses:
		print("Your are out of lifes")

		