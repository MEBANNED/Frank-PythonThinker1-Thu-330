import time
print("Hello from lesson 5")

# # Lesson 5 - Introduction to For Loop and range()

# ## Recap 1: Automated Birthday Invitation

# You run a small business that creates personalized digital
# birthday invitation cards. To automate the process, you decide
# to write a Python program. 

# This program should ask the user for:
# 1. birthday person's name
# 2. the age that they are turning that year
# 3. personal message from the sender

# Finally, the program prints out a personalized invitation
# message.

# ### Sample output:
# "Happy <Age>th birthday <Name>! <Message>"

# ---------------------------------------------------------------
# print("Welcome")
# name = input("Please type the your friend's name here: \n")
# age = input("Please type your friend's upcoming age here: \n")
# mssg = input("Please type a personalized message here: \n")
# print("Here's your birthday card!")
# print("Happy " + age + "th birthday " + name + "!" )
# print(mssg)

# ## Task 1: Repeated Sentence Loop

# Print the sentence "I like chicken rice." 100 times using the
# 'for' loop
# for i in range(100):
#     print("i don't like chickn rice")
# ---------------------------------------------------------------

# ## Task 2: Sentence Repetition Loop with Order of Code
# ## Sequence

# Using the 'for' loop, print the following sentences sequence
# 100 times:
# "I like cake."
# "Give me more"
# for i in range(100):
#     print("i lik cake")
#     print("give me more")

# ---------------------------------------------------------------

# ## Task 3: range(stop)

# Using the 'for' loop, print the numbers from 0 - 59

# Question:
# How many numbers are printed? 

# ---------------------------------------------------------------

# ## Task 4: range(start, stop)

# **Task 4a**:
# Print numbers from 1 to 5 using a 'for' loop.
# for j in range(1, 6):
#     print(j)
# **Task 4b**:
# Print numbers from 51 to 100 using a 'for' loop.
# for counter in range(51, 101):
#     print(counter)
# **Task 4c**:
# Print numbers from 18 to 29 using a 'for' loop.
# for i in range(18, 30):
#     print(i)
# **Task 4d**:
# Print numbers from 36 to -5 using a 'for' loop.
# for i in range(36, -6, -1):
#     print(i)


# ---------------------------------------------------------------

# ## Task 5: range(start, stop, step)

# **Task 5a**:
# Use a 'for' loop to print numbers from 2 to 24 in multiples of 2.
# for i in range(2, 25, 2):
#     print(i)
# # **Task 5b**:
# # Use a 'for' loop to print numbers from 8 to 96 in multiples of 8.
# for i in range(1, 97, 8):
#     print(i)
# # **Task 5c**:
# # Use a 'for' loop to print numbers from 5 to 1 in descending order.
# for i in range(5, 0, -1):
#     print(i)
# # **Task 5d**:
# # Use a 'for' loop to print all odd numbers between 7 to -7 in descending order.
# for i in range(7, -8, -2):
#     print(i)

# # **Task 5e**:
# # Use a 'for' loop to print all numbers that are multiples of 25 between 100 to -70 in descending order.
# for i in range(100, -71, -25):
#     print(i)

# # **Task 5f**:
# # Use a 'for' loop to print all numbers that are multiples of 3 between -24 to -70 in descending order.
# for i in range(-24, -72, -3):
#     print(i)
# ---------------------------------------------------------------

# ## Task 6: Countdown timer

# **Task 6a**:
# Imagine you are the race official and to start the race, you
# must say the following:

#     Ready!
#     3
#     2
#     1

# Using a 'for' loop, recreate the above sequence.
# print("Ready")
# for i in range(3, 0, -1):
#     print(i)
# # **Task 6b**:
# # Create a countdown timer that counts from 10 to 1.
# # When the timer hits 1, print "Boo!"
# for i in range(10, 1, -1):
#     print(i)
#     time.sleep(1)
# print("boo")
# ---------------------------------------------------------------

# ## Task 7: User-Defined Range Counter

# Using input(), ask the user for 2 numbers and store them in the
# variables:
# 1. start
# 2. stop
# start = int(input("start: \n"))
# stop = int(input("stop: \n"))
# # Write a 'for' loop to count from **start** to **stop**
# for i in range(start, stop + 1):
#     print(i)
#     time.sleep(1)

# Note:
# What happens if the user inputs a higher start number than stop?
# Modify your code to be able to handle that scenario.

# ---------------------------------------------------------------

# ## Task 8: Accumulative Sum in Loop

# 1. Create a variable 'num' and assign the integer "0" to it
# 2. Create a 'for' loop that repeats 10 times
# 3. Add the sum of 'num' and the loop's parameter and print out
#    the value.
# 4. Observe what happens.

# Example:
# 1st iteration
#     num = num + i
#     print(num)

# 2nd iteration
#     num = num + i
#     print(num)

# ...

# 10th iteration
#     num = num + i
#     print(num)
# num = 0
# for i in range(0, 10):
#     num = num + i
#     print(num)
# Output:
#     0
#     1
#     3
#     6
#     10
#     15
#     21
#     28
#     36
#     45

# ## Task 9: Name Cheer

# Your school's Sports Day is coming up and you are coding a
# program to cheer your schoolmates up.

# Your program needs to:
# 1. Using input(), ask the user for their namee e.g. <Dave>
# 2. Print a cheer as shown below:
   
#     ### Example:
#     What is your name? [Input: "Dave"]
#     Give me a D!
#     Give me a a!
#     Give me a v!
#     Give me a e!
#     What do we have?
#     Dave is the best!
# name = input("Name: \n")
# input("password \n")
# for char in name:
#     print("give me a " + char)
#     time.sleep(1)
# print("what do we have?")
# time.sleep(1)
# print(name + " is the best!")
# Note:
#     Notice how "Give me a..." is repeated!
#     Which function should you be using?

# ---------------------------------------------------------------


# Write a program that calculates the following value for a given n:

# 1×1 + 2×2 + 3×3 + ... + n×n
# sum = 0
# n = int(input("Choose a random number from 0 to infinity: \n"))
# for loop

# for i in range(n+1):
#     sum = sum+i**2
# print(sum)
sum = 0
# 3 + 11 + 19 + 27 + ... + 83
for i in range(3, 84, 8):
    sum = sum + i
    print(sum)