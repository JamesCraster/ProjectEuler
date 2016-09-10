import math

def factorSum(n):
    n = float(n)
    summation = 0
    for x in range(1,int(math.sqrt(n))):
        if n % x == 0:
            summation += x

            if n/x != x and x != 1:
                summation += n/x
                
    return summation
summation = 0
x = 0
while x < 10000:
    if factorSum(factorSum(x)) == x and factorSum(x) != x:
        summation += x
        print(x)
    x+= 1



