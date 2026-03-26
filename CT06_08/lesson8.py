"""
# Lesson 8 - Importing Libraries, Boolean & Conditions

## Recap 1: Product of 5 numbers

Write a program to calculate the product (multiplication) of 5
numbers.

1. Using a for loop, ask the user for 5 numbers one at a time.
2. Calculate the multiplication for these 5 numbers and print
   it out.
"""
# total = 1
# for i in range(1, 6):
#     number = input("what is number " + str(i) + "?")
#     total = total * number
# print("total: " + str(total))
"""
---------------------------------------------------------------

## Task 1: 'time' library

**Task 1a**:
Import the 'time' library and make use of the 'time.sleep()'
function to create a 10 seconds countdown timer that counts
to 1, printing the number of seconds remaining every second.
"""
# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
"""
**Task 1b**:
Modify your code from Task 1a to include an 'input()' function
asking the user for the number to countdown from, before
counting down every second from the number given by the user.

---------------------------------------------------------------

## Task 2: 'random' library

**Task 2a**:
Import the 'random' library and create a program that randomly
output a number between 1 to 6
"""
# import random
# ran = random.randint(1, 6)
"""
**Task 2b**:
Using the 'random' library, create 20 numbers between 0 and
9999 randomly.
"""

"""
---------------------------------------------------------------

## Task 3: Print Boolean Value & Condition

**Task 3a**:
Assign a boolean value to a variable and print it.

**Task 3b**:
Create 2 variables both holding the "True" boolean.
Print out the result of comparing the 2 variables using
the "==" operator.

**Task 3c**:
Now, assign 1 variable the "True" boolean, and assign another
variable the "False" boolean.

Print out the result of comparing the 2 variables using
the "==" operator.

---------------------------------------------------------------

## Task 4: Random Number Guessing Game

Create a simple program to guess a random number:​
- Create a variable called ‘random_num’ and assign a random integerbetween 1 to 10.​
- Ask the user for an input 'guess'​

Your program will check if ‘guess’ is equal to 'random_num'.​

The output should be one of the following:​
- If the answer is correct – output "Correct!" ​
- If the answer is wrong – output "Wrong!​
"""
# import random
# random_num = random.randint(1, 10)
# guess = int(input("Type a number below in between 1 and 10: \n"))
# if  guess == random_num:
#    print("Correct!")
# else:
#    print('wrong buddy')
"""
## Task 5: Math Question Generator

Create a simple program that generate 2 numbers
between 1 and 50 that the user must add together.​

Ask the user to input the answer.​

The output should be one of the following:​
- If the answer is correct – output "Correct!"​
- If the answer is wrong – output "Wrong!​
"""
# import random
# rand1 = random.randint(1, 50)
# rand2 = random.randint(1, 50)
# ans = rand1 + rand2
# usr_ans = int(input("what is " + str(rand1 + " + " + str(rand2) + )))
"""
## Task 6: Random Multiplication Quiz

Create a program that generates a certain number of
random multiplication questions.​
1. Ask the user to input how many questions should be asked.​
2. Multiply 2 random numbers between 1 and10 and save the 'answer'.​
3. Ask the user to input their answer, 'user_answer'.​
4. Check if 'user_answer' is equal to 'answer'.

The output should be one of the following:​
- If the answer is correct – output "Correct!" ​
- If the answer is wrong – output "Wrong!​
"""
# amt_of_questions = int(input("how many questions should i ask?"))
# for i in range(amt_of_questions):
#    import random
#    rand1 = random.randint(1, 50)
#    rand2 = random.randint(1, 50)
#    ans = rand1 + rand2
#    usr_ans = int(input("what is " + str(rand1) + " + " + str(rand2) + str(rand1)))
"""
## Task 7: Even or Odd Checker

Write a program that asks the user to enter a number. The
program then tells the user whether the number is even
(True) or odd (False).

Your program needs to:
1. Ask user for an integer input.
2. Check if there is any remainder when user input is divided
   by 2 (using '%').
3. Print 'True' if number is even, otherwise print 'False'.
"""
# num = int(input("gimme a number"))
# if num % 2 == 1:
#    print("odd number")
# else:
#    print("even number") 
"""
## Task 8: Multiple Check Program

Create a program where the user enters 2 numbers. The
program then checks if the first number is a multiple of
the second number.

Your program needs to:
1. Get user to input 2 numbers.
2. Check if there is any remainder when number #1 is divided
   by number #2
3. Print 'True' if number #1 is a multiple of number #2,
   otherwise print 'False'.
"""

