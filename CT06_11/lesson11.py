"""Please uncomment code you want to test"""



"""Recap 1"""
# px = float(input("Enter the price of the item: "))

# if px <= 5:
#     print("Sounds good!")
# elif px <= 50:
#     print("Are you sure you need this?")
# elif px <= 500:
#     print("Where are you getting this money from?!")
# else:
#     print("Don't even think about it!")

"""Task 1"""
# rider1 = 125
# rider2 = 150

# if rider1 > 120 and rider2 > 120:
#     print("Both riders can go on the ride.")
# else:
#     print("One or both riders are too short.")

"""Task 2"""
# num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 7 == 0:
#     print("The number is divisible by 3 and 7!")
# else:
#     print("The number is not divisible by both 3 and 7.")
"""Task 3"""
# first_name = input("Enter your first name: ").lower()
# last_name = input("Enter your last name: ").lower

# if first_name == "james" and last_name == "leong":
#     print("YOU ARE WANTED")
# else:
#     print("You are not wanted.")
"""Task 4"""
# rider1 = 25
# rider2 = 6

# if rider1 >= 18 or rider2 >= 18:
#     print("u r allowed or else you don't")
"""Task 5"""
# age = int(input("Enter your age: "))

# if age < 12 or age > 65:
#     print("Ticket price: $15")
# else:
#     print("Ticket price: $20")
"""Task 6"""
# gender = input("enter your gender or else").upper()
# if gender == "M" or gender == "MALE":
#     print("VALID")
# else:
#     print("AEOFUWEOFEWGOFYEWGOUEPTWEYTPWEUTPWE")
    
"""Task 7"""
# try:
#     colour = input("enter a colour or else \n").upper()
#     if not colour == "green":
#         print("Ayo try again")
# except TypeError:
#     print("bruh that's not a word")

"""Task 8"""
# day = input("Enter the day of the week: ").lower()

# if day != "saturday":
#     print("It's not the weekend yet!")

"""Task 9"""
# password = input("Enter your password: ")

# if not password == "Python123":
#     print("Access Denied.")

"""Task 10"""
burger = input("do you want a burger(Y/n) ").lower()
fries = input("Do u want some fries?(Y/n) ").lower()
drink = input("DO YOU WANT A DRINK?(Y/n) ").lower()

if burger != "n" and fries == "y" and drink != "y":
    print("wont you get thirsty without a drinl???!??!??!?!?!?!?")
else:
    print("sure")