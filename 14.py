"""Write a function that for 2 given dictionaries find their common keys.
>>>com_d({'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90}, {'a': 25, 'l': 48, 'g': 90, 'w': 5, 'z':90})
['a']
"""
def com_d(d1, d2):
    c = []
    for i in d1:
        for k in d2:
            if (i == k):
                c.append(i)
    return c

#example
print(com_d({'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90}, {'a': 25, 'l': 48, 'g': 90, 'w': 5, 'z':90}))
