'''Write a procedure which finds the Greatest Common Divisor of 2 numbers,
which is defined as the largest number which will evenly
divide two other numbers.

Examples: GCD( 5, 10 ) = 5, GCD( 21, 28 ) = 7.'''

def greatest_common_divisor(x,y):
    #list of all divisors
    divisors = []
    if x>=y:
        for i in range(x):
            if x%(i+1)==0 and y%(i+1)==0:
                divisors.append(i+1)
    elif y>x:
        for i in range(y):
            if x%(i+1)==0 and y%(i+1)==0:
                divisors.append(i+1)

    print(f'GCD({x},{y})= {divisors[-1]}')

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
greatest_common_divisor(x,y)
