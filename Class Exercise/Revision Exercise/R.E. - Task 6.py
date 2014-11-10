print("This programm shows you the conversion of kilogramm to pound.")
print()

answer = 0
conversion_rate = 2.2

for count in range(1,21):
    answer = conversion_rate * count
    print("{0:>2}kg | {1:<2.2f} pound".format(count, answer)) 
