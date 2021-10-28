"""
Write a function to calculate number e (base of natural logarithms 2.718281828459045...)
"""
import math 
e = 0
for i in range(100):
              e = e + (1/math.factorial(i))
print(e)
