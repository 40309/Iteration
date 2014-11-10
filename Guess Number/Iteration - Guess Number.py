#Tony K.
#10/11/2014
#Iteration - Guess Number

def main():
 
    import random

    random_number = random.randrange(1,100)
    guess_number = 0
    count = 0

    while 1:
        guess_number = int(input("Please enter your value, between 1 and 100: "))
        print()
        if guess_number == random_number:
            count = count + 1
            print("Well done! You entered the correct number. You have had {0} tries.".format(count))
        elif guess_number < random_number:
            count = count + 1
            print("Your number is too low, try a higher number.")
        elif guess_number > random_number:
            count = count +1
            print("Your number is too high, try a lower number.")
        else:
            print("Your number is invalid, please enter number between 1-100.")
