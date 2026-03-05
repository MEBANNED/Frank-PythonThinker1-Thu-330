# # print("Hello from lesson 8")

# # # ===============================
# # # PART B — FOR LOOPS
# # # ===============================

# # # Q21
# # for i in range(3):
# #     print(i)

# # # A) 1 2 3
# # # B) 0 1 2
# # # C) 0 1 2 3
# # # D) 1 2
# # ans: __________________A_______✅

# # # Q22
# # for i in range(2, 8, 2):
# #     print(i)

# # # A) 2 times
# # # B) 3 times
# # # C) 4 times
# # # D) 5 times
# #b✅

# # # Q23
# # total = 0
# # for i in range(1, 4):
# #     total = total + i
# # print(total)

# # # A) 6
# # # B) 10
# # # C) 4
# # # D) 3
# # ans: ____________a____________✅

# # # Q24
# # for i in range(5, 1, -1):
# #     print(i)

# # # A) 5 4 3 2
# # # B) 5 4 3 2 1
# # # C) 4 3 2
# # # D) 5 4 3

# a ✅
# # # Q25
# # s = ""
# # for i in range(3):
# #     s += "A"
# # print(s)

# # # A) A
# # # B) AA
# # # C) AAA
# # # D) Error
# a

# # # Q26
# # for i in range(1, 6, 2):
# #     print(i)

# # # A) 1 3 5
# # # B) 1 2 3 4 5
# # # C) 2 4 6
# # # D) 1 3
# a✅

# # # Q27
# # total = 1
# # for i in range(1, 4):
# #     total *= i
# # print(total)

# # i = 1, total = 1  * 1
# # i = 2, total = 1 * 2
# # i = 3, total = 2 * 3 = 6

# # # A) 6
# # # B) 24
# # # C) 4
# # # D) 3
# a

# # # Q28
# # for ch in "cat":
# #     print(ch)

# # # A) cat
# # # B) c 
# #a 
# # t
# # # C) c
# # # D) Error
# b

# # # Q29
# # count = 0
# # for i in range(4):
# #     count += 2
# # print(count)

# # # A) 6
# # # B) 8
# # # C) 4
# # # D) 2
# b
# # i = 0, 0 + 2 = 2
# # i = 1, 2 + 2 = 4
# # i = 2, 4 + 2 = 6
# # i = 3, 6 + 2 = 8


# # # Q30
# # for i in range(3):
# #     print("Hi" + str(i))

# # # A) Hi
# # # B) Hi0 Hi1 Hi2
# # # C) Hi012
# # # D) Error
# b

# # # Q31
# # x = 0
# # for i in range(1, 5):
# #     x += 1
# # print(x)
# i = 1, 0 + 1 = 1
# i = 2, 1 + 1 = 2
# i = 3, 2 + 1 = 3
# i = 4, 3 + 1 = 4

# # # A) 4
# # # B) 5
# # # C) 3
# # # D) 1
# a

# # Q32
# for i in range(4, 0, -2):
#     print(i)

# # A) 4 2
# # B) 4 2 0
# # C) 3 1
# # D) 4
b

# # Q33
# s = ""
# for i in range(1, 4):
#     s += str(i)
# print(s)

# # A) 123
# # B) 6
# # C) 321
# # D) Error
a

# # Q34
# for i in range(10, 5, -1):
#     print(i)

# # A) 4 times
# # B) 5 times
# # C) 6 times
# # D) 3 times
b

# # Q35
# for i in range(0, 5):
#     if i % 2 == 0:
#         print(i)

# # A) 0 2 4
# # B) 1 3 5
# # C) 2 4
# # D) 0 1 2 3 4


# # Q36
# x = 5
# for i in range(3):
#     x += i
# print(x)

# # A) 8
# # B) 9
# # C) 11
# # D) 6


# # Q37
# for i in range(1, 5):
#     print(i * 2)

# # A) 2 4 6 8
# # B) 1 2 3 4
# # C) 2 4 6
# # D) 8


# # Q38
# s = "A"
# for i in range(2):
#     s += s
# print(s)

# # A) AA
# # B) AAAA
# # C) AAA
# # D) Error


# # Q39
# total = 0
# for i in range(2, 6):
#     total += i
# print(total)

# # A) 14
# # B) 12
# # C) 10
# # D) 8


# # Q40
# for i in range(1, 4):
#     print(str(i) + "!")

# # A) 1! 2! 3!
# # B) 123!
# # C) 6!
# # D) Error