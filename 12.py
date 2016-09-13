import math
triangle = lambda n:n * (n-1)/2



def primesUpTo(n):
   L = [True] * n
   L[0] = False
   L[1] = False
   returnList = []
   for index, value in enumerate(L):
      if value == True:
         L[index * 2::index] = [False] * (((len(L)-1)//index)-1)
         returnList.append(index)
   return returnList

def addPrime(primeList, upperLimit):
   for x in range(primeList[-1] + 1, upperLimit+1):
      continueFlag = 0
      for y in primeList:
         if x % y == 0:
            continueFlag = 1
            break
      if continueFlag == 1:
         continue
      
      primeList.append(x)
   return primeList

def numberOfDivisorsFromRepeats(primeFactorRepeatList):
   number = 1
   for x in primeFactorRepeatList:
      number *= (x+1)

   return number

def generateDivisorRepeats(primeList,n):
   divisorRepeatList = []
   if(n%2 == 0):
      n /= 2
      
   for x in primeList:
      
      if n % x == 0:
     
         divisorRepeatList.append(1)
         y = n
         y /= x
         while y % x == 0:
            y /= x
            divisorRepeatList[-1] += 1
      

   return divisorRepeatList
         
   

def numberOfDivisors(primeList, n):
   primeList = addPrime(primeList,n)
   return numberOfDivisorsFromRepeats(generateDivisorRepeats(primeList,n))



primesList = [2]
n = 1
a = 0
b = 0

while a * b < 500:
   b = a
   a = numberOfDivisors(primesList,n+1)
   n+=1

print(triangle(n))


   

   
