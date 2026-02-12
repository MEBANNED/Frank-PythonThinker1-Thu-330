# print("Hello from lesson 4")

# # Lesson 4 - Strings

# ## Recap 1: Sushi Checkout

# You just had a lunch at a sushi restaurant and have to
# calculate the total amount you have spent. Different coloured
# plates costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3

# You have ordered a total of 3 red plates, 5 blue plates, and 4
# green plates.

# Calculate and print the total amount you have spent: -->

# red_cost = 1
# blue_cost = 2
# green_cost = 3
# red_qty = 3
# blue_qty = 5
# green_qty = 4
# total = red_cost * red_qty + blue_cost * blue_qty + green_cost * green_qty
# print(total)
# ---------------------------------------------------------------

# ## Task 1: Storing and printing Strings

# **Task 1a**:
# Use the input() function to ask the user for their name and
# store it in a variable. Then print that variable.
# name = input("What's your name? ")
# print("hello " + name)
# **Task 1b**:
# Ask the user for their favorite colour using input() and
# store the response in a variable. Print the variable.
# my_color = input("What's your favourite colour?")
# print(my_color)
# **Task 1c**:
# Ask the user for their age using input() and store the answer
# in a variable. Print the variable.
# my_age = input("How old are you? ")
# print(my_age)
# ---------------------------------------------------------------

# ## Task 2: Input & string concatenation

# **Task 2a**:
# Ask the user for their name using input() and store it in a
# variable. 
# Concatenate the name with "Hi, [name]!" and print the
# complete message.
# name = input("What's your name? ")
# print("hello " + name)
# **Task 2b**:
# Use input() to ask the user for their favorite hobby. Store this
# in a variable.
# Print a message saying "I enjoy [hobby]" using string
# concatenation.
# hobby = input("what's your favourite hobby?")
# print("I like " + hobby + " too")
# **Task 2c**:
# Ask the user for their dream vacation destination using input()
# and store it in a variable.
# Concatenate this variable with a phrase like "I would love to
# visit" and print the full sentence.
# drm_vctn = input("If you had a private jet, where do you want to go next summer?"
# print("I would love to go to " + drm_vctn + " too!")
# ---------------------------------------------------------------

# ## Task 3: Type conversion, math, and string concatenation

# **Task 3a**:
# 1. Ask the user for their current age using input(). Convert this
# to an integer.
# 2. Add 1 to their age and convert it back to a string.
# 3. Then print a message saying "Next year, you will be [age+1]
# years old."
# user_age = input("How old are u")
# print("Next year, you will be " + str(int(user_age)+1))
# **Task 3b**:
# 1. Use input() to ask the user for a number. Convert this number
# from a string to an integer.
# 2. Double the number and convert it back to a string.
# 3. Print "Double your number is [double the number]".
# num = input("type here a random number: \n")
# dble_num = int(num) * 2
# print("Double your number is " + str(dble_num))
# **Task 3c**:
# 1. Use input() to ask the user for the year they were born and
# convert it to an integer.
# 2. Subtract the birth year from the current year (assume the
# current year as an integer) to find their age.
# 3. Convert the age back to a string and print "You are [age]
# years old".
# user_brn = input("Type here the year you were born: \n")
# user_age = 2026 - int(user_brn)
# print("you will be turning " + str(user_age) + " years old if not yet")

# ---------------------------------------------------------------

# ## Task 4: Variable Reassignment Basics

# Assign the string "Hello" to a variable 'message'. 
# Then reassign 'message' to the integer "10" and print it.


# msg = "Hello"
# msg = 10
# print(type(msg))
# ---------------------------------------------------------------

# ## Task 5: Printing Full Name

# Create 2 variables, 'firstName' and 'lastName', assigning your
# first and last names to them. Then print them on the same line
# with a space between them.
# print("SIGN IN")
# firstname = input("First Name: \n")
# lastname = input("Last Name: \n")
# input("Password: \n")
# print("Your Full name is " + firstname + " " + lastname)
# ---------------------------------------------------------------

# ## Task 6: Age and Name Concatenation

# Assign a name to the variable "user_name"
# Assign an integer to the variable "user_age"
# Use type conversion and string concatenation to print out
# "[user_name] is [user_age] years old."
# user_name = "RandomGuy0142"
# user_age = 81234
# print("Account Locked - According to our terms of service, our users must be 1000 or younger. You - " + user_name + " - is already " + str(user_age) + " years old.")

# Q1. Red Packet Sharing at Grandma’s House
import math
# During Chinese New Year reunion dinner in Singapore, Grandma prepares $88 to give equally to 3 grandchildren in red packets.
# Each grandchild must receive the same whole-dollar amount, and no one should receive less than their fair share.
# each = math.ceil(88/3) 
# Write a program that asks for the total amount of money and number of grandchildren, 
# then displays how much each grandchild receives in one sentence.
# print("Math Test")
# print("During Chinese New Year reunion dinner in Singapore, Grandma prepares $88 to give equally to 3 grandchildren in red packets. Each person recieved " + str(each) + " each.")
# input("They recieved ")
# print(" altogether")

total_amt = int(input("How much to prepare?: "))
num_grandchildren = int(input("How many grandchildren?: "))
per_pax = math.ceil(total_amt / num_grandchildren)
print("Each grandchild receive " + str((per_pax)))

total_cost = per_pax * num_grandchildren

print(total_cost)



print("Login to MathTest")
