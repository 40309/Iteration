print("Once you have finished entering all your values please enter -1, to get your answer.")

counter = 0
total = 0
number = 0

while number != -1:
    number = int(input("Please enter your number: "))
    if number != -1:
        total = total + number
        counter = counter + 1
    else:
        average = total/counter
        print()
        print("The answer is {0}.".format(average))
        print()
        print("Thank you for using this programm.")
