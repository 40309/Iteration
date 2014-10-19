
number = 0
while number < 1 or number > 20:
    number = int(input("Please enter a number between 10 and 20: "))
    if number > 20:
        print("The number that you have entered is too high")
    elif number < 10:
        print("The number that you have entered is too low")
    else:
        print("Thank you for the attempt")
