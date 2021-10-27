"""Calculate N! (factorial)
>>>enter an ineger: 5
120
"""
n = int(input("enter an ineger: "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)
