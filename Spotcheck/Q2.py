number = int(input("Please enter your number: "))
answer = 0
print()
print("Times table for {0}:".format(number))
print()	
for count in range(12):
    answer = count*12
    print("{0:<2}* {1:<2} = {2:>3}".format(count,number,answer))
