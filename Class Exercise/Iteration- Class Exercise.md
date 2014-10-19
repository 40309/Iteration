#Class Exercises - Iteration Statements
These tasks are designed to help you practice the knowledge and skills you have developed. There are exercises to help you revise and develop your understanding and also to challenge you further.

##Syntax
You might find it useful to refer to these examples.

```python
#prints Hello 9 times
for count in range (1,10):
    print("Hello")

#keeps prompting the user until they enter a number between 1 and 10
valid = False
while not valid:
    number = int(input("Enter a number in the range 1 to 10:"))
    if 1 <= number <= 10:
        valid = True
```

##Vocabulary
You might find it useful to refer to definitions of these terms.

|Term|Definition|
|----|----------|
|Definite iteration (`for` loop)|structure used when we know before entering the loop how often we want to repeat.|
|Iteration (`while` loop)|structure used when we do not know beforehand how often we want to repeat.|
|Boolean expression|an expression which checks whether a particular condition is `True` or `False`.|
|Rogue value|a value, which when input, is used to terminate the loop.|

##Task 1 - Improving a piece of code
Open the python file called `addition.py` and refactor the code so that it uses a more efficient and appropriate style.

```python
# program to prompt for 8 numbers and report the total to the user
num1 = int(input('Enter number 1 : ' ))
num2 = int(input('Enter number 2 : ' ))
num3 = int(input('Enter number 3 : ' ))
num4 = int(input('Enter number 4 : ' ))
num5 = int(input('Enter number 5 : ' ))
num6 = int(input('Enter number 6 : ' ))
num7 = int(input('Enter number 7 : ' ))
num8 = int(input('Enter number 8 : ' ))

total = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
print('The total is {0}'.format(total))
```

##Task 2 - Class Exercises
In this section you may choose the exercises you attempt. There are three types of exercises to consider:

1. **Revision Exercises** - choose these exercises if you are not confident in your understanding of selection statements
2. **Development Exercises** - choose these exercises if you are confident in your understanding but want some more practice
3. **Stretch and Challenge Exercises** - choose these exercises if you feel you have mastered selection and want to tackle some tougher problems

Once you feel more confident attempt some of the more difficult exercises. The more practice you get now the more comfortable you will be using selection in more complex programs later in the course.

Remember, practice makes perfect!

###Attempting These Exercises
You should do the following for each exercise you attempt:

1. Create **flowcharts** first - plan your solution on paper before attempting it
2. Create a set of **test data** - select values you will enter to test the program and know beforehand what you expect the answers to be
3. Write the **program** - write the program in Python using the pseudocode to assist you and the test data to ensure the program functions correctly

##Revision exercises
Attempt these tasks if you need to build your confidence and understanding of iteration statements.

1. Write a program that will print ‘Hello World’ 10 times. **DONE**
2. Write a program that will ask the user for a message and the number of times they want that message displayed. Then output the message that number of times. **Done**
3. Write a program that asks the user to enter how many numbers are to be averaged, then enter this number of numbers, calculating the average. The program should display the average
on the screen.**DONE**
4. Write a program that asks a user for a number between 10 and 20 inclusive. The program should give the user a message if the number input is outside this range and ask for another number until the number input is within range.**Done**
5. Write a program that calculates the average of a series of numbers. Ask the user to enter a series of numbers, entering the rogue value -1 when they have finished. Then calculate the average of those numbers.
**Incomplete**
6. Write a program that displays a conversion table for pounds to kilograms, ranging from 1 pound to 20 pounds [1 kg = 2.2 pounds]. The values should be shown in neat columns.


##Development exercises
Attempt these tasks if you are confident in your understanding but feel you need more practice

1. n factorial usually written n!, is defined to be the product of all the integers in the range 1 to n.
n! = 1 * 2 * 3 * 4 * .... * n. Write a program that calculates n! for a given positive n.
2. Write a program that asks the user to enter the number of stars per row and the number of rows to be displayed. For example, entering 5 and 3 should display:

    ```
    *****
    *****
    *****
    ```

3. Write a program which asks the user for a string and then prints out the string in reverse order. Use a loop to do this.
4. Write a program that finds the largest of a series of numbers. Ask the user to enter a series of numbers, entering the rogue value -1 when they have finished. Then report the largest value to the user.

##Stretch and challenge exercises
Attempt these tasks if you feel you have mastered selection and want to tackle tougher problems.

1.  Write a program that asks for a number and displays the squares of all the integers between 1 and this number inclusive. It should print 5 values on each line in neat columns.
2. Write a program which will convert a given denary number up to 255 into its 8-bit binary equivalent.
3. Write a program which will convert an 8-bit binary number to its denary equivalent.
4. Write a program which reports the number of words in a phrase typed in by the user. The program will need to count the number of spaces to achieve this.

    Read the section on string slicing which is about 80% down the page called [Additional Exercises 3 – FOR and WHILE LOOPS](http://www.pythonschool.net/basics/additional-exercises-3/) on the Python Summer School.

