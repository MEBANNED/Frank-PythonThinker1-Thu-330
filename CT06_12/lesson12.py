"""recap 1"""
# num = input("Enter a number: ")

# if num % 3 == 0 and num % 5 == 0:
#     print(f'{num} is divisible by both 3 and 5')
# else:
#     print(f'{num} is not divisible by both 3 and 5')

"""Task 1a"""
# visitors = 0
# while visitors < 50:
#     visitors += 1
#     print(visitors)

"""Task 1b"""
# visitors = 18
# max_visitors = 30
# while visitors < max_visitors:
#     visitors += 1
#     print(visitors)

"""Task 1c"""
# visitors = 4
# max_visitors = 25
# while visitors < max_visitors:
#     visitors += 1
#     print(visitors)

# """Task 2"""
# visitors = 0
# while visitors < 50:
#     visitors += 1
#     print(visitors)
#     if visitors == 30:
#         break

"""task 3"""

# order = ""
# while True:
#     new_order = input("Enter your oder or else!!!!! ")
#     if new_order == "end":
#         break
#     order += ", " + new_order
# print(order)

"""task 4a"""
# while num != 0:
#     print(num)
#     num -= 1

#     # if num ==5:
#     #   break
# else:
#     print("sad new year")

"""Task 5"""
ans = 0
import random

while True:
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operations = random.randint(1, 3)
    if operations == 1:
        ans = num1 + num2
        operation_sign = "+"
    elif operations == 2:
        ans = num1 - num2
        operation_sign = "-"
    else:
        ans = num1 * num2
        operation_sign = "*"
    user_ans = int(input(f"What is {num1} {operation_sign} {num2}? "))
    if user_ans == ans:
        print("That's correct!")
        break
    else:
        print("Wrong! Try again")