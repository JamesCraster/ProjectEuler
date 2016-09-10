f = open('11.txt','r')
##L will be the master list

L = f.read()
B = ""
for x in range(0,len(L[:])):
   if L[x] == '\n':
      B += ' '
   else:
      B += L[x]
      
L = B.split(' ')

B = []

for x in range(0,len(L[:])):
   B.append(int(L[x]))

L = B

B = []

row = 0
column = 0
for x in range(0,400,20):
   B.append(L[x:x+20])

L = B

product = 1

for x in range(0,len(L)):
   for y in range(0,len(L[x])):
      if(y + 3 < len(L[x])):
         if(y * (y+1)*(y +2)* (y +3) > product):
            product = y * (y+1)*(y +2)* (y +3)

for x in range(0,len(L)):
   for y in range(0,len(L[x])):
      if(x + 3 < len(L)):
         if(L[x][y] * L[x+1][y] * L[x+2][y] * L[x+3][y] > product):
            product = L[x][y] * L[x+1][y] * L[x+2][y] * L[x+3][y]

for x in range(0,len(L)):
   for y in range(0,len(L[x])):
      if(x + 3 < len(L) and y + 3 < len(L[x]) ):
         if(L[x][y] * L[x+1][y+1] * L[x+2][y+2] * L[x+3][y+3] > product):
            product = L[x][y] * L[x+1][y+1] * L[x+2][y+2] * L[x+3][y+3]

for x in range(0,len(L)):
   for y in range(0,len(L[x])):
      if(x + 3 < len(L) and y - 3 > 0):
         if(L[x][y] * L[x+1][y-1] * L[x+2][y-2] * L[x+3][y-3] > product):
            product = L[x][y] * L[x+1][y-1] * L[x+2][y-2] * L[x+3][y-3]
            
            
            
            
         
   


   


