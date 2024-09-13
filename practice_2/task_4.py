# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
d = input("Please enter 4-digit number ")
if (not d.isdigit()) or len(d) != 4 :
    print(f"{d} is not a 4-digit number")
    exit()

print(sum([int(c) for c in d]))