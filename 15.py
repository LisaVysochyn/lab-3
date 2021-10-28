""""Create a function which reverts
a dictionary (keys become values, values become keys)
>>>{'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90}
{25: 'a', 48: 'b', 90: 'e', 5: 'd'}
"""
def r_d(d):
    d = { d[k]:k for k in d}
    return d

#example
print(r_d({'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90}))
