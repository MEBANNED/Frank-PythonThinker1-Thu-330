# # Lesson 6 - Debugging

# ## Recap 1: Class Average Calculator

# You have been tasked to create a programme that calculates the
# average marks of a class.

# Your programme will have to ask the
# user for the total number of students, followed by the marks of
# each student one at a time.

# Use only variables, math operators that you have learnt, as
# well as a 'for' loop.
# amt = int(input("Sup! \n how many students are in your class?"))
# sum = 0
# for i in range(1, amt+1):
#     score = int(input("score:\n"))
#     sum = sum+score
# print(sum / amt)


# ---------------------------------------------------------------

# ## Task 1: Syntax Errors
# Fix the errors in the following:

# **Task 1a**:
# for i in range(3):
#     print("Hello, World!")

# **Task 1b**:
# for i in range(5):
#   print(i)

# **Task 1c**:
# print("Hello, World!")

# **Task 1d**:
if_ = 5
# **Task 1e**:
# print("hello, world")
# ---------------------------------------------------------------

# ## Task 2: Name Errors
# Fix the errors in the following:

# **Task 2a**:
# print("age")

# **Task 2b**:
# name = "Alice"
# print(name)

# **Task 2c**: 

# x = 5
# print(x)

# **Task 2d**:
# print("Hello, World!")

# ---------------------------------------------------------------

# ## Task 3: Type Errors
# Fix the errors in the following:

# **Task 3a**:
# age = 25
# print (age + 1)

# **Task 3b**:
# number = 10
# print(number - int("5"))

# **Task 3c**:
# print("Repeat" * int("3"))

# **Task 3d**:
# year = str(2023)
# print("The year is " + year)

# **Task 3e**:
# x = int("10")
# y = x / 2

# **Task 3f**:
# end = int("5")
# for i in range(1, end+1):
#     print(i)

# Q1.
# This code is supposed to find the sum of numbers from 1 to 5.

# total = 0
# for i in range(1, 5):
#     total += i
# print(total)

# i = 1, total = total + 1 = 1
# i = 2, total = total + 2 = 3
# i = 3, total = total + 3 = 6
# i = 4, total = total + 4 = 10
 
# What is wrong?
# A. The loop stops too early
# B. total should start from 1
# C. += is incorrect
# D. print is in the wrong place

# ANS: a

# Q2.
# This code is supposed to add all numbers from 1 to 5.

# for i in range(1, 6):
#     total = 0
#     total = total + i
# print(total)

# What is the main problem?
# A. i should start from 0
# B. range(1, 6) is incorrect
# C. total is reset every loop
# D. print should be inside the loop

# ANS: c

# Q3.
# This code is supposed to add all numbers from 0 to 4 into total.

# total = 0
# for i in range(5):
#     i += total
# print(total)

# Why does total stay 0?
# A. total is never updated
# B. the loop does not run
# C. range(5) is wrong
# D. i cannot change

# ANS: a

# Q4.
# This code is supposed to find the sum of odd numbers from 1 to 9.

# total = 0
# for i in range(1, 10, 2):
#     total += 2
# print(total)

# What is the mistake?
# A. The wrong value is added
# B. The range is incorrect
# C. total should start from 1
# D. The step size is wrong

# i = 1, total += 2 = 2
# i = 3, total += 2 = 4
# i = 5, total += 2 = 6 

# i = 1, total += 1 = 1
# i = 3, total += 3 = 4
# i = 5, total += 5 = 9 

# ANS: c

# Q5.
# This code is supposed to find the sum of numbers from 1 to 5.

# total = 0
# for i in range(1, 6):
#     total += 1
# print(total)

# What is the code actually doing?
# A. Counting how many times the loop runs
# B. Adding numbers from 1 to 5
# C. Adding only the last number
# D. Nothing

# ANS: b

# Q6.
# This code is supposed to find the sum of numbers from 1 to 5.

# total = 0
# for i in range(1, 6):
#     total = i
# print(total)

# Why is the answer wrong?
# A. total is overwritten each loop
# B. range(1, 6) is incorrect
# C. i should start from 0
# D. print should be inside the loop

# ANS: a

# This code is supposed to print the sum of numbers from 10 to 1
# (10 + 9 + 8 + ... + 1 = 55).

# total = 0
# for i in range(10, 0 -1):
#     total += i
# print(total)


# This code is supposed to print the sum of multiples of 3 from 3 to 30 (165).

# total = 0
# for i in range(3, 31, 3):
#     total += i
# print(total)

# This code is supposed to print:
# • the sum of numbers from 1 to 5 (15)
# • the sum of numbers from 6 to 10 (40)
# 15 40

# total_1 = 0
# total_2= 0

# for i in range(1, 6):
#     total_2 += i

# for i in range(6, 11):
#     total_1 += i

# print(total_2, total_1)

# This code is supposed to print the sum of numbers from 1 to n.
# If n = 6, it should print 21.

# n = 6
# total = 0
# for i in range(1, n + 1):
#     total += i
# print(total)

# This code is supposed to print the sum of even numbers from 2 to 10 (30).

# total = 0
# for i in range(2, 11, 2):
#     total += i
# print(total)

# This code is supposed to print the sum of numbers from 3 to 7 (25).

# total = 0
# for i in range(3, 8):
#     total = total + i
# print(total)

# This code is supposed to print  sum of even numbers from 2 to 20 (110).
# the
total = 0
for i in range(2, 21, 2):
    total += i
print(total)