#Tony K.
#20/10/2014
#Revision Exercise 5

print("This program calculates the average of the values entered") # user friendly
print()
repeat = int(input("How many values do you have? ")) #asks user how often the loop to be repeated
total = 0
print()

for count in range(repeat):
    number = int(input("Please enter your number: "))
    print()
    if number > 0:
        
    total = total + number

print()



if total % 2 == 0:
    print("Your value is even")
else:
    print("Your value is odd")

print()
