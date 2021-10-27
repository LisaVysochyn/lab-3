"""Write a program that asks the user to enter integer number. Then check if the number is prime.
>>>Введіть число: 3
Число є простим
>>>Введіть число: 4
Число не є простим
"""
a = int(input("Введіть число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k + 1
if (k <= 0):
    print("Число є простим")
else:
    print("Число не є простим")
