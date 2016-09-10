
def collatz(n):
   if n % 2 == 0:
      return int(n/2)

   return int(3*n + 1)
      
counter = 0
savedCount = 0
savedX = 0
a = 0

for x in range(2,1000000):
   a = x
   counter = 0
   while a != 1:
      a = collatz(a)
      counter += 1
   if counter > savedCount:
      savedCount = counter
      savedX = x

print(savedCount)
print(savedX)

#answer is 837799
