#importing the time module
import time
import random

tries = 5
guesses = []

#welcoming the user


words = ['india', 'pakistan', 'scotland', 'west indies', 'bangalesh', 'myanmar', ]

rand = random.randint(0, len(words)-1)


print("You have 5 tries to find the country name")
time.sleep(3)
print("Generating the word...")
time.sleep(3)
print("Start guessing...")
while tries > 0:
    dashes = len(words[rand])
    for x in range(0, len(words[rand])):
        if words[rand][x] in guesses:
            print(words[rand][x], end=" ")
            dashes -= 1
        else:
            print("_", end=" ")
    if dashes == 0:
        time.sleep(0.5)
        print(" ")
        print("You won")
        break
    guess = input("Guess the letter: ")
    if guess not in words[rand]:
        tries = tries - 1
        if tries == 0:
            print("You lose")
        else:
            print("You have", tries, "tries")
    else:
        if guess not in guesses:
            guesses.append(guess)
        else:
            tries = tries - 1
            print("You already gueessed that letter, try the letter that's not gueessed")
            print("You have", tries, "tries")
            

