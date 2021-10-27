"""
The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each number thereafter is the sum of the two preceding numbers. Write a program that asks the user how many Fibonacci numbers to print and then prints that many.

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
>>> Введіть скільки чисел Фібоначчі Ви хочете отримати: 8
[1, 1, 2, 3, 5, 8, 13, 21]

"""

n = int(input("Введіть скільки чисел Фібоначчі Ви хочете отримати: "))
if n == 0:
    f = []
elif n == 1:
    f = [1]
elif n >= 2:
    f = [1, 1]
    while len(f) != n:
        f.append(f[-1] + f[-2])
print(f)
