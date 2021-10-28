'''John has 300 at the start, he saves 100 per month,
and 500 every 6 months.
Write a function returning his savings after N months.
(N is an input from the user)'''

def savings(n):
    
    s = 300 + n*100 + (n//6)*500
    print(f'Savings: {s}')

n = int(input('Enter the number of months: '))
savings(n)
