"""
Calculate number of distinct characters in a string using a for loop.
>>>enter a string: fff ggg eee kkk
4
"""
a = []
s = input('enter a string: ')
for i in s:
    if i not in a and i != " ":
        a.append(i)
print(len(a))
