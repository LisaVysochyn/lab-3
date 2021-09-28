'''Write a program to find the key of the maximum value in a dictionary.

Example: original dictionary elements:

{'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90}

Finds the keys of the maximum value of the said dictionary:

['c','e']'''

dic = {'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90}

maxKeys = []

#looking for the value of the keys
k = list(dic.keys())

#looking for the values
v = list(dic.values())

for i in range(len(v)):
    if max(v)==v[i]:
        maxKeys.append(k[i])
        
print('Keys of the maximum value:', maxKeys)
