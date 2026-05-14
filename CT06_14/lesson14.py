# import random 

# rolls = []
# for i in range (5):
#     rolls.append(random.randint(1,6))
# print(rolls)
# total = 0
# for i in range(len(rolls)):
#     total += rolls[i]

# print(f"sum : {total}")

"""Task 1"""
# fruits = ["Apples", "Oranges", "leaves", "Green apples"]
# cost = [80000000, 20000000, 92000000000000, 2]
# for teacher_alson in range(len(fruits)):
#     print(f"{fruits[teacher_alson]} costs ${cost[teacher_alson]}")
"""Task 2"""
"""    2a"""
items = ["Apple", "Milk", "Bread", "Egg", "Chocolate"]
stock = [15, 0, 8, 25, 3]
for teacher_alson in range(5):
    if stock[teacher_alson] >= 10:
        status = "well stocked" 
    elif stock[teacher_alson] < 10 and stock[teacher_alson] != 0:
        status = "Low Stock"
    elif stock[teacher_alson] == 0:
        status = "Out of Stock"

    print(f"Item: {items[teacher_alson]} | Stock: {stock[teacher_alson]} | Status: {status}")

"""   2b"""
# ask = input("THIS IS TOTALLY NOT A HOMEMADE CATALOGUE I CREATED 2 SECOSNDS AGO, FIND STOCK AND STUFF: \n")

# if ask in items:
#     item_index = items.index(ask) #this returns the index number of whatever you ask
#     print(f"We have {stock[item_index]} {ask}(s) remaining.")
# else:
#     print(f"HOMEMADE CATALOGUE ERROR: 404 THIS IS NOT THE PAGE YOU ARE LOOKING FOR, YOU ARE EITHER GOOFING AROUND OR IF IT'S LEGIT, {ask} DOES NOT EXSIST")

"""Task 4"""

import random
move = ["scissors", "paper", "stone"]

playerScore = 0
computerScore = 0

while playerScore <3 and computerScore < 3:
    playerMove = input ("HOMEMADE AI SCISSOR PAPER STONE THING: CHOOSE YOUR MOVE:\n")
    computerMove = random.choice(move)
    print(f"Computer chooses {computerMove}")
    if playerMove == computerMove:
        print('HOMEMADE AI SCISSOR PAPER STONE THING SAYS: "It\'s a draw"')
    elif (playerMove == "scissors" and computerMove == "paper") or (playerMove == "stone" and computerMove == "scissors") or (playerMove == "paper" and computerMove == "stone"):
        print("HOMEMADE SCISSOR PAPER STONE THING: You won this round")
        playerScore = playerScore + 1
    else:
        print("HOMEMADE SCISSOR PAPER STONE THING: Whoops, You lost this round")
        computerScore += 1

print(f"{computerScore}-{playerScore}, computer score - your score")

