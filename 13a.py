"""A simple way of encrypting a message is to
rearrange its characters. One way to rearrange
the characters is to pick out the characters at even indices,
put them first in the encrypted string, and follow them by the
odd characters. For example, the string message would be
encryptedas msaeesgbecause the even characters are m, s, a, e (at indices 0, 2, 4, and
6)and the odd characters are e, s, g (at indices 1, 3, and 5).

Write a function that asks the user for a string and uses this method to encrypt the string

>>>"I like tea"
I lkie tae

Write a function that decrypts a string that was encrypted with this method

>>>I lkie tae
"I like tea"
"""
def encryp(text):
    t = text.split()
    l = [(list(i)[::2] + list(i)[1::2]) for i in t]
    for i in l:
        for k in i:
            print(k, end="")
        print(" ", end='')

#exaple
encryp("I like tea")
encryp("I lkie tae")
