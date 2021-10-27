"""Write a program that asks the user to enter
the integer number greater than 1. Calculate sum of k as n goes from 1 to integer number:

>>>enter the integer number greater than 1: 3
6
"""
n = int(input("enter the integer number greater than 1: "))
print(sum([i for i in range(1, n+1)]))
