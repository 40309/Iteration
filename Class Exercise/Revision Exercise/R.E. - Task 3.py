repeat = int(input("Please enter how many numbers you have: "))
total = 0

for count  in range (repeat):
    numbers = int(input("Please enter your number: "))
    total = total + numbers

average = total/repeat

print("The average of the values you have entered is {0}.".format(average))

