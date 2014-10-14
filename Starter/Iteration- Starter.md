#Starter - Iteration Statements
These tasks are designed to refresh the reading and research you have undertaken at home prior to this lesson. If you have not completed the R&R assignment then please speak to your teacher before attempting these exercises.

You have been introduced to the two types of loops that are used in Python. Refresh your knowledge of these concepts by attempting the below tasks.

##Task 1
Dry run and comment on the code snippet below:

```python
total = 0
counter = 0

while counter < 5:
    number = int(input("Please enter number {0} in the series".format(counter)))
    total = total + number
    counter = counter + 1
print("The total of the numbers you entered is {0}".format(total))
```

###Questions
1. What messages will the user see as the program runs?
*Please enter number 0 in the series* **1**
*Please enter number 1 in the series* **2**
*Please enter number 2 in the series* **3**
*Please enter number 3 in the series* **4**
*Please enter number 4 in the series* **5**
*The total of the numbers you entered is x* **15**

2. Suggest improvements
*Please enter number 0 in the series* **:**
*Make it more user friendly*
* *Starting Message, informing the user, what the program is about*
* *Finishing Message, informing the user, when the program is finished*

##Task 2
Dry run and comment on the code snippet below:

```python
import random

largest_number = 0
for count in range(20):
    random_number = random.randint(1,100)
    if random_number > largest_number:
        largest_number = random_number
    print("The largest random number generated is {0}".format(largest_number))
```

###Questions
1. What messages will the user see as the program runs?

*The largest random number generated is 70*
*The largest random number generated is 70*
*The largest random number generated is 70*
*The largest random number generated is 70*
*The largest random number generated is 70*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 90*
*The largest random number generated is 98*
*The largest random number generated is 98*

2. Suggest improvements

##Task 3
Dry run and comment on the code snippet below:

```python
import random
age = 0
while age > 16 or age < 30:
    age = int(input("Enter the student's age (16-30):"))
print("Age of {0} has been accepted by the system as valid".format(age))
```

###Questions
1. What messages will the user see as the program runs?
2. Suggest improvements

##Task 4
When you have discussed the improvements with your teacher make the changes to the programs in **tasks 1-3** and check if they now run as specified and/or more efficiently.

##Task 5
Hand trace the following algorithm written in pseudo-code. Assume that the variable **number has a value of 7**. The MOD operator calculates the remainder resulting from an integer division.

```
answer ← True
FOR count ← 2 TO (number - 1) DO
    remainder ← number MOD count
    IF remainder = 0 THEN
        answer ← False
    ENDIF
ENDFOR
```

Complete the trace table below.

|answer|count|remainder|
|:----:|:---:|:-------:|
|True|-|-|
| |2|1|
| | | |
| | | |
| | | |
| | | |

###Questions
1. What is the purpose of this algorithm?

    If you are not sure try different values for the variable number and check in each case what the value in the variable answer holds at the end of the program run.

##Task 6
Convert the above algorithm to a Python program. Enhance the program to prompt for the value of number and to show a suitable information message to the user at the end of the program run.

Now test it with the same data as given above (used in the dry run). Verify that the program produces a result which matches the last line of the trace table.
