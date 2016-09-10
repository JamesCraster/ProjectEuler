import math
N =  600851475143

def findPrimes(lowLimit,upperLimit, primeSet):
    nonPrimeSet = set()
    for x in range(lowLimit,upperLimit):
        for y in range(2,x):
            if x != y and x % y == 0:
                nonPrimeSet.add(x)
                break
 
    allSet = {x for x in range(lowLimit,upperLimit)}
    for x in (allSet - nonPrimeSet):
        primeSet.add(x)

def testForFirstDivisor(n = 600851475143):
    upperBound = int(math.sqrt(n))
    
    for i in range(2,upperBound):
        while n % i == 0:
            n /= i
        if n == 1:
            return i
        if i == n:
            return i

    if(n != 1):
        
        if(testForFirstDivisor(n) == n):
            return n
        testForFirstDivisor(n)

print(testForFirstDivisor())

