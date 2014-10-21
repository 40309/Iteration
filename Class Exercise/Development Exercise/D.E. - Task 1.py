#Tony K.
#21/10/2014
#Iteration- D.E. Task 1

n = int(input(" Please enter your integer: "))
answer = 1
n = n + 1
print()
for count in range(1,n):
    answer = answer * count

print("The answer is {0}.".format(answer))
