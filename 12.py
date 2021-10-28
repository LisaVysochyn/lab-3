"""
Write a program that generates the 26-line block of letters partially shown below. Use a loop containing one or two print statements.

abcdefghijklmnopqrstuvwxyz

bcdefghijklmnopqrstuvwxyza

cdefghijklmnopqrstuvwxyzab

...

yzabcdefghijklmnopqrstuvwx

zabcdefghijklmnopqrstuvwxy
"""

l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x in range(len(l)):
    for y in range(len(l)):
        print(l[x-y],end='')
    print('\n')
