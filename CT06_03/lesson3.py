# print("Hello from lesson 3")
# # Lesson 3 - Variables

# ## Recap 1: Pseudo Code Practice
# Write a pseudocode that calculates the average score of the 4
# students:

# Adam: 60
# Brandon: 58
# Charlie: 98
# Daniel: 79

# assign 60 to "adam"
# # assign 58 to "brandon"
# assign 98 to "charlie"
# assign 79 to "daniel"
# print "(adam+brandon+charlie+daniel)/4z" 

# --------------------------------------------------------------

# ## Task 1: Variables
# **Task 1a**:
# Create a variable named 'age' and assign your age to it.
# Then print the value of 'age'.
# age = 1000000000000
# print(age)
# **Task 1b**:
# Assign the value 10 to a variable 'x'. 
# Then reassign 20 to variable x. Print 'x'.
# x = 10
# x = 20
# print(x)
# ---------------------------------------------------------------

# ## Task 2: Simple addition calculator
# **Task 2a**:
# Create 2 variables holding 2 different numbers:

# ## Example:
# variable1 = 3
# variable2 = 5

# Print out the sum ("+") of the 2 numbers
 
# variable1 = 3
# variable2 = 5
# print(variable1 + variable2)
# # ## Example:
# # Output: 8

# **Task 2b**:
# Print out the product (‘×’), division (‘/’), and differences
# (‘-’) of the 2 numbers.

# ## Example:
# variable1 = 3
# variable2 = 5
# variable1 = 3
# variable2 = 5
# print(variable1 * variable2)
# print(variable2 - variable1)
# print(variable2 / variable1)
# Output:
# >>> 8 (addition)
# >>> 15 (multiplication)
# >>> 0.6 (division)
# >>> -2 (difference)

# ---------------------------------------------------------------

# ## Task 3: Rounding practice
# print(round(8.5))
# print(round(7.5))
# **Task 3a**:
# Round 42.56789 to two decimal places.
# print(round(42.56789, 2))
# **Task 3b**:
# Round 1267.15 to the nearest integer.
# print(round(1267.15))
# **Task 3c**:
# Round 1785.956 to the nearest hundreds.
# print(round(1785.956, -2))
# ---------------------------------------------------------------

# ## Task 4: Mathematics with variables
# For each of the following questions, create variables to hold
# the values given before finally using print(ans) to print the
# answer:

# **Task 4a**:
# Create 2 variables 'a' and 'b', assign any number to
# them and print their sum.
# a = 6789
# b = 1234
# print(a+b)
# **Task 4b**:
# Subtract 10 from 50, then multiply the result by 3.
# print((50-10) * 3)
# **Task 4c**:
# Divide 100 by 4 and print the result.
# print(100 / 4)
# **Task 4d**:
# Calculate and print the result of (3 + 4) * 5 - (10 / 2).
# print((3 + 4) * 5 - (10 / 2))
# ---------------------------------------------------------------

# ## Task 5: Order of Operations practice
# Code one Python expression to calculate and print the total cost for each task. Round the answer to 2 decimal places.

# **Task 5a**:
# - Two boxes of pineapple tarts - $15 each
# - One packet of bak kwa for - $58
# print(round(15 * 2+58, 2))
# **Task 5b**:
# A 10% service charge is applied, and a $25 off voucher is used, to the following order:
# - One seafood platter - $96
# - Three side dishes - $18 each
# - Six bowls of rice - $2 each
# print(round((1.1 * (96+3*18+6*2))-25, 2))
# **Task 5c**:
# A 10% service charge is applied then, a 9% GST is applied, to the following order:
# - Five seafood platters - $100 each
# - Eight side dishes - $20 each
# - Twenty bowls of rice - $2.50 each
#print(round(1.1*1.09*(5*100+8*20+20*2.5), 2))
# ---------------------------------------------------------------

# ## Task 6: Mathematical Function - abs 

# **Task 6a**:
# A warehouse robot's sensor records a movement of -55 meters due to an error causing it to move in the wrong direction.
# Calculate the actual distance moved.
# print(abs(-55))
# **Task 6b**:
# A smart home sensor records a temperature change of -8 degrees in a room.
# Calculate the total amount the temperature has changed.
# print(abs(-8))
# ---------------------------------------------------------------

# ## Task 7: Mathematical Function – floor & ceil

# **Task 7a**:
# A bakery has 9.8kg of ingredients to use. Each batch of bread uses 1kg of ingredients to make.
# Find the maximum number of batches that can be baked.
import math
print(math.floor(9.8))
# **Task 7b**:
# A family buys 27 oranges. Each gift bag can hold 4 oranges.
# Calculate the minimum number of bags needed to pack all the oranges.
print(math.ceil(27/4))

# Meiling cooked 130 dumplings. Each family member can eat only 25 dumplings.
# Calculate the number of people in her family consider that there are  
# dumplings left over.
print(math.floor(130/25))
# ---------------------------------------------------------------

# ## Task 8: Mathematical Function – pi

# **Task 8a**:
# An athlete runs on a circular track with a diameter of 100 meters.
# Calculate the distance of one full lap using the formula, circumference = π x diameter, and round the answer to 2 decimal places.
print(round(math.pi * 100, 2))
# **Task 8b**:
# You bought a pizza with a radius of 12cm.
print(round(math.pi * 144, 2))
# Calculate the total area of the pizza to using the formula, area = π x radius², and round the answer to 2 decimal places.
# ** : to power of something
print(12**2)

# %: mod 

# print(math.e)
# print(27**1/3)
# print(16**(1/2))
# print(16**1/2)
# print(pow(12,2))
print(8%3)

# You want to fit as many unit circle (radius = 1) as possible inside a square of side length 10
# FInd the area of one circle
# find how many circle can you fit into the square
print(100/math.pi)