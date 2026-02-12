print("Hello from lesson 7")
import time
# Lesson 7 - For Loop (Part 2)

## Recap 1: Debugging Average Score Program

### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))

# Ask the user for a word and a number n. Print the word repeated
# n times (on separate lines).

# Example:
# What word would you like to repeat? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# burger
# burger
# burger
# num = int(input("hey you! how many burgers do you want? \n                    "))
# wrd = input("hey! how what do u want to repeat")
# for poop in range(num):
#     print("burger")
# ## Task 1: For Loop: 1 to 10 using range(start, stop)
# Use a 'for' loop to print numbers from 1 to 10.
# for poop in range(11):
#     print(poop)
#     time.sleep(1)
## Task 2: Even Numbers 2-20 Loop using
##         range(start, stop, step)

# Print all even numbers between 2 and 20 using a 'for' loop and
# range().
# for cameron in range(2, 21, 1):
#     print(cameron)
## Task 3: Countdown From 10 For Loop
# Use a 'for' loop and range() to count down from 10 to 1.

# for teacher_alson in range(10, 0, -1):
#     print(teacher_alson)

# # Ask for a user's name and an integer n, then print a
# personalized greeting n times.

# Example:
# What is your name? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# Nice to meet you, burger
# Nice to meet you, burger
# # Nice to meet you, burger
# name = input("what's your name")
# poop = int(input("how many time do i need to repeat???????? \n type your answer here: \n"))
# for abcdefghijklmnopqrstuvwxyz in range(poop):
#     print("Hello! Nice to meet you, " + name + "!")
# ## Task 6: Sum of Five User Inputs

# Ask the user to input 5 numbers, one at a time, and print the
# sum of these numbers.

# Example:
# What is number #1? <<5>>
# What is number #2? <<2>>
# What is number #3? <<4>>
# What is number #4? <<1>>
# What is number #5? <<7>>

# output:
# Sum of the 5 numbers is 19
# abc = 0

# for teacher_alson in range(5):
#     num = int(input("What is #" + str(teacher_alson+1)+ " "))
#     abc += num
# print(abc)

# # task 11(torture)
# print("# \n ## \n ### \n ## \n #")

# Ask the user for a number, then print the multiplication table
# for that number from 1 to 12.

# Example:
# What number for the timestable? > << 5 >>
# output:
# 5 x 1 = 5
# 5 x 2 = 10
# ....
# ..
# 5 x 12 = 60
#task 11
# number = input("what number for times table")
# for i in range(13):
#     print(number *i)

# number = int(input("what number for times table"))
# for i in range(1, 13):
#     print(str(number) + "x" + str(i) + "=" + str(number * i))

num = int(input("whats the number? "))
for i in range(1. 6):
