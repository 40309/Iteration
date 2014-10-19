repeat = int(input("Please enter how many numbers you have: "))
total = 0

for count  in range (repeat):
    number = int(input("Please enter your number: "))
    total = total + number

average = total/repeat

print("The mean of the values you have entered is {0}.".format(average))

