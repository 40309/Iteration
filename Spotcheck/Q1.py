#Tony


number = 0
total = 0

while number != -1:
    number = int(input("Please enter your number: "))
    if number != -1:
        total = total + (number * number)

print("The total is {0}".format(total))
