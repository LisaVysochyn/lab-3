"""
Write a function which asks the user to enter a text and returns 3 numbers like unix wc utility:

- number of characters,
- number of words,
- number of lines.

>>>print(unix("mom, dad\n i love you"))
chararers: 20
words: 5
lines: 1
"""
def unix(s):
    nc = len(s)#how many chararers
    nw = len(s.split())#how many words
    nl = s.count('\n')#how many lines
    return f"chararers: {nc}\nwords: {nw}\nlines: {nl}"

