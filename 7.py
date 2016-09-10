import copy

def eratosthenes(n, limit = 125000):
   primes = [True] * limit
 
   primes[0], primes[1] = [False] * 2
   count = 0
   for ind, val in enumerate(primes):
      if val is True:
         primes[ind*2::ind] = [False] *  len(primes[ind*2::ind])
         count += 1
      if count == n:
         return ind
      
   return False
         

def fast_nth_prime(n, limit=125000):
   if limit % 2 != 0: limit += 1
   primes = [True] * limit
   primes[0],primes[1] = [None] * 2
   count = 0 
   for ind,val in enumerate(primes):
      if val is True:
           primes[ind*2::ind] = [False] * len(primes[ind*2::ind])
           count += 1
      if count == n: return ind

   return False
 

prime = fast_nth_prime(10001)

  
      
