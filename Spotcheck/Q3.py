import random
number = random.randint(1,100)

guessed = False
userGuess = 0
noOfTurns = 0

while guessed == False:
    noOfTurns = noOfTurns + 1
    userGuess = int(input("Please eneter your guess for the number: "))
    if userGuess == number:
        guessed = True
    elif userGuess > number:
        print("The number you guessed is too high")
    else:
        print("The number of guessed is too low")
print()

print("You took {0} turns to guess the number.".format(noOfTurns))
print("The number was: {0}".format(number))
