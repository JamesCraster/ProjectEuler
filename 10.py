L = [True] * 2000000
L[0] = False
L[1] = False
for index,value in enumerate(L):
   if value == False:
      continue

   L[index*2::index] = [False] * len(L[index*2::index])

summation = 0
for index, value in enumerate(L):
   if value == True:
      summation += index
   
