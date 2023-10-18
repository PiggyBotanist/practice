"""
Practice question from "Practice Geeks"
Written on June 06, 2022
By: Jeremy Chang

Problem: Print the Pattern:
You are given a number N. You need to print the pattern for the given value of N.
e.g: For N=2 the pattern will be:
2 2 1 1
2 1

e.g: For N=3 the pattern will be:
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1
"""
n = 0
print("Welcome to Print the Pattern!")
n = int(input("Please input the value of N: "))
i = n
while i >= 1:
    print("")
    for x in range(0, n):
        for y in range(0, i):
            print(n-x, end = ' ')
    i -= 1
