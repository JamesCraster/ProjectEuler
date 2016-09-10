f = open('Problem8input.txt','r')
N = f.read()
LN = N.split()
N = ""
for x in LN:
   N += x

product = 1
greatestProduct = 0

for x in range(0,len(N)-13):
   product = 1
   for y in range(0,13):
      product *= int(N[x+y])

   if(product > greatestProduct):
      greatestProduct = product
      
   


## answer is 23514624000...
   
